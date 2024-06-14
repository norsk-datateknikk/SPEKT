import requests
import time

ip = "http://localhost"  # Replace this with the IP of the PC running the REST server
# If testing on the same PC as the server, use localhost.
port = "8080"  # The server is always running on PORT :8080

# --------- SET MODE -------------------------------------------

url = f"{ip}:{port}/api/setMode"
# Available modes: GPSEmulator, ToneDetect, Sweep
data = {"mode": "GPSEmulator"}

response = requests.put(url, files=data, timeout=120)
print("Response:", response.json())

# --------- GET POSITION ---------------------------------------

url = f"{ip}:{port}/api/gpsEmulator/position"

response = requests.get(url, timeout=120)
print("Response:", response.json())

# --------- SET POSITION ---------------------------------------

url = f"{ip}:{port}/api/gpsEmulator/position"
# This example's location data is using the following units:
# latitude (Degrees), longitude (Degrees), height (Meters)
data = {"latitude": "35.6895", "longitude": "139.6917", "height": "10"}

response = requests.put(url, files=data, timeout=120)
print("Response:", response.json())

# --------- GET GAIN ------------------------------------------

url = f"{ip}:{port}/api/gpsEmulator/gain"

response = requests.get(url, timeout=120)
print("Response:", response.json())

# --------- SET GAIN ------------------------------------------

url = f"{ip}:{port}/api/gpsEmulator/gain"
data = {"gain": "4"}  # Gain level

response = requests.put(url, files=data, timeout=120)
print("Response:", response.json())

# --------- GET PLAYBACK DURATION ------------------------------

url = f"{ip}:{port}/api/gpsEmulator/playbackDuration"

response = requests.get(url, timeout=120)
print("Response:", response.json())

# --------- SET PLAYBACK DURATION ------------------------------

url = f"{ip}:{port}/api/gpsEmulator/playbackDuration"
data = {"duration": "10"}  # Duration in seconds

response = requests.put(url, files=data, timeout=120)
print("Response:", response.json())

# --------- PREPARE PLAYBACK -----------------------------------

url = f"{ip}:{port}/api/gpsEmulator/preparePlayback"

response = requests.put(url, timeout=120)
print("Response:", response.json())

time.sleep(10)  # Wait for prepare playback to finish before sending new request

# --------- START PLAYBACK -------------------------------------

url = f"{ip}:{port}/api/gpsEmulator/startPlayback"

response = requests.put(url, timeout=120)
print("Response:", response.json())
