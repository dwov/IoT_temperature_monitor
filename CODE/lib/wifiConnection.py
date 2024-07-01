import network
import time
import keys

# Constants
WIFI_POWER_SAVE_MODE = 0xa11140  # Set power-saving off
RETRY_INTERVAL = 1  # seconds

def connect():
    wlan = network.WLAN(network.STA_IF)                 # Put modem on Station mode
    if not wlan.isconnected():                          # Check if already connected
        print('connecting to network...')
        wlan.active(True)                               # Activate network interface
        wlan.config(pm = WIFI_POWER_SAVE_MODE)          # Set power-saving off
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)    # Your WiFi Credential

        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            time.sleep(RETRY_INTERVAL)
        
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip

def disconnect():
    wlan = network.WLAN(network.STA_IF)  # Put modem on Station mode
    if wlan.isconnected():
        wlan.disconnect()
        print('Disconnected from network...')
    else:
        print('Not connected to any network.')
    wlan.active(False)  # Deactivate network interface
    wlan = None  # Cleanup
