import requests
import time

import matplotlib.pyplot as plt
import numpy as np

ip = "http://localhost"
port = "8080"

# --------- SET MODE -------------------------------------------

# Set mode to ToneDetect:
url = f"{ip}:{port}/api/setMode"
# Available modes: GPSEmulator, ToneDetect, Sweep
data = {"mode": "ToneDetect"}

response = requests.put(url, files=data)
print("Response:", response.json())

# --------- GET GAIN VALUE -------------------------------------

# Get current gain value
url = f"{ip}:{port}/api/toneDetector/gain"

response = requests.get(url)
print("Response:", response.json())

# --------- SET GAIN VALUE -------------------------------------

# Set new gain value
url = f"{ip}:{port}/api/toneDetector/gain"
data = {"gain": 0}

response = requests.put(url, files=data)
print("Response:", response.json())

# --------- GET FREQUENCY RANGE -------------------------------------

# Get the frequency range
url = f"{ip}:{port}/api/toneDetector/frequencyRange"
response = requests.get(url)
print("Response:", response.json())

# --------- SET FREQUENCY RANGE -------------------------------------

# Set the frequency range
url = f"{ip}:{port}/api/toneDetector/frequencyRange"
data = {"startFrequency": "2400e6", "stopFrequency": "2485e6"}

response = requests.put(url, files=data)
print("Response:", response.json())

# --------- START TONE DETECT -------------------------------------

# Start the tone detection run
url = f"{ip}:{port}/api/toneDetector/start"
response = requests.put(url)
print("Response:", response.json())
time.sleep(20)  # Wait for detections to occur


# --------- Read OUT DETECTED TONES ----------------------------------

# Get the results from tone detection
url = f"{ip}:{port}/api/toneDetector/results"

tone_response = requests.get(url, timeout=10)
# print("Response:", tone_response.json())

# --------- RESTART TONE DETECT -------------------------------------

# Restart the tone detection
url = f"{ip}:{port}/api/toneDetector/restart"

response = requests.put(url, timeout=20)
print("Response:", response.json())

# --------- PLOT DETECTED TONES -------------------------------------

# Extracting frequency and power values
frequencies_Hz = [item["frequency_Hz"] for item in tone_response.json()["data"]]
power_dBm = [item["power_dBm"] for item in tone_response.json()["data"]]

# Creating the plot
plt.figure(figsize=(10, 6))

# Plotting the lines
plt.plot(frequencies_Hz, power_dBm, color="blue", marker="o", linestyle="-")

# Manually drawing red lines below the lowest points
lowest_power_index = np.argmin(power_dBm)
lowest_freq_Hz = frequencies_Hz[lowest_power_index]
plt.hlines(
    y=lowest_power_index,
    xmin=lowest_freq_Hz - 0.5,
    xmax=lowest_freq_Hz + 0.5,
    colors="red",
    linestyles="dashed",
)

plt.title("Tone Response")
plt.xlabel("Frequency [MHz]")
plt.ylabel("Power [dBm]")
plt.grid(True)

# Save the plot to a file
plt.savefig("detected_tones.png")

# Optionally, display the plot if needed
plt.show()
