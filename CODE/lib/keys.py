import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor

# Wireless network configuration
WIFI_SSID = 'YOUR_SSID'
WIFI_PASS = 'YOUR_PASS'

# MQTT server configuration
MQTT_SERVER = "MQTT_LOCAL_NETWORK_SERVER_IP"
MQTT_PORT = 1883
MQTT_USER = "USER"
MQTT_KEY = "KEY"
MQTT_CLIENT_ID = "id-1234"  # Client ID must start with 'id-'

# MQTT feeds
MQTT_TEMPERATURE_FEED = "devices/temperature-mcp"
MQTT_TEMPERATURE_FEED1 = "devices/temperature-dht"
MQTT_HUMIDITY_FEED = "devices/humidity-dht"
MQTT_LIGHTLEVEL_FEED = "devices/light-level"
MQTT_BOARD_LIGHT_FEED = "devices/board-light"
