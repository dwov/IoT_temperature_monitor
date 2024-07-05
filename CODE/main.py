#===================================================================#
# __author__ = "David Permlid"                                      #
# __version__ = "1.0.0"                                             #
#===================================================================#

import time                         # List of needed libraries
from mqtt import MQTTClient
import machine
import micropython
import dht
from machine import Pin
import keys
import wifiConnection


# Constants
PUBLISH_INTERVAL = 10000                    # milliseconds
RECONNECT_INTERVAL = 300000                 # milliseconds (5 minutes)

# Global Variables
last_reconnect_ticks = 0
last_random_sent_ticks = 0

# Hardware Initialization
led = Pin("LED", Pin.OUT)                   # On-board led pin initialization for Raspberry Pi Pico W
light_sensor = machine.ADC(27)
temp_sensor = machine.ADC(26)
dht_sensor = dht.DHT11(machine.Pin(18))


# Callback Function to respond to messages from MQTT
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        led.on()                 # ... then LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        led.off()                # ... then LED off
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.

def read_sensors():
    global last_random_sent_ticks

    if ((time.ticks_ms() - last_random_sent_ticks) < PUBLISH_INTERVAL):
        return; # Too soon since last one sent.

    light_level = round((light_sensor.read_u16() / 65535) * 100, 2)   # Read light sensor and convert to percentage
    temp_voltage = temp_sensor.read_u16() * (3.3 / 65535)           # Read temperature sensor voltage and convert with scale factor
    temp_celsius = (temp_voltage - 0.5) * 100                       # Convert voltage to temperature in Celsius
    dht_sensor.measure()
    temp_dht = dht_sensor.temperature()
    humidity_dht = dht_sensor.humidity()

    print(f"Publishing sensor data: Temp: {temp_celsius}, Humidity: {humidity_dht}, DHT Temp: {temp_dht}, Light Level: {light_level} ...")
    try:
        client.publish(topic=keys.MQTT_TEMPERATURE_FEED, msg=str(temp_celsius))
        client.publish(topic=keys.MQTT_HUMIDITY_FEED, msg=str(humidity_dht))
        client.publish(topic=keys.MQTT_TEMPERATURE_FEED1, msg=str(temp_dht))
        client.publish(topic=keys.MQTT_LIGHTLEVEL_FEED, msg=str(light_level))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_random_sent_ticks = time.ticks_ms()
    
    return light_level, temp_celsius, temp_dht, humidity_dht


# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.MQTT_CLIENT_ID, keys.MQTT_SERVER, keys.MQTT_PORT, keys.MQTT_USER, keys.MQTT_KEY)

client.set_callback(sub_cb)
while True:
    try:
        client.connect()
        print("Connected to MQTT server successfully")
        break
    except Exception as e:
        print("Failed to connect to MQTT server, {}".format(e))
        time.sleep(10)
client.subscribe(keys.MQTT_BOARD_LIGHT_FEED)
print("Connected to %s, subscribed to %s topic" % (keys.MQTT_SERVER, keys.MQTT_BOARD_LIGHT_FEED))


try:
    while 1:              # Repeat this loop forever
        if ((time.ticks_ms() - last_reconnect_ticks) > RECONNECT_INTERVAL): # Ensure we are connected to WiFi and reconnect MQTT
            wifiConnection.connect()
            client.disconnect()
            time.sleep(1)
            client.connect()
            client.subscribe(keys.MQTT_BOARD_LIGHT_FEED)
            last_reconnect_ticks = time.ticks_ms()
        
        client.check_msg()
        read_sensors()
except Exception as e:  # If an exception is thrown, print the error and reset the Pico to try and reconnect.
    print("An error occurred, {}".format(e))
    wifiConnection.disconnect()
    time.sleep(20)   # Wait 20 seconds before resetting
    machine.reset()  # Restart the Pico
finally:                  # If an exception is thrown disconnect from MQTT and WiFi
    client.disconnect()
    wifiConnection.disconnect()
    print("Disconnected from MQTT(NODE RED).")