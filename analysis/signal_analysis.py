import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # So the noise doesnt change from one execution to the next

# 1. and 2. Generation of noisy signal and plot
N = 1000 # array size
sample_rate = 10000 # Sample rate in Hz

t = np.arange(N) / sample_rate # Time array, sample_rate transforms it in seconds

frequency = 1000 # Frequency in Hz

signal = np.sin(2 * np.pi * frequency * t) # Generate sine wave

noise = np.random.normal(0, 0.5, N) # Generate noise 

raw_signal = signal + noise # Combine signal and noise

# Fourier Transform to find the frequency
fft_raw_signal = np.fft.fft(raw_signal)
frequencies = np.fft.fftfreq(N, 1/sample_rate) # Storing the frequencies
power = np.abs(fft_raw_signal)

# olotting the raw signal
plt.plot(frequencies, power)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.show()

window = 11 # Size of the moving average window. Odd number so we can have a symmetric window around each point
smoothed_power = np.zeros_like(power) # Arrat to store the smoothed power values. Currently filled with zeros

half_window = window // 2 # Whole number division to find the half window size


for i in range(len(power)):
    start = max(0, i - half_window) 
    end = min(len(power), i + half_window + 1) 
    smoothed_power[i] = np.mean(power[start:end])


mask_negative_frequencies = frequencies >= 0

plt.plot(frequencies[mask_negative_frequencies], power[mask_negative_frequencies], label='Raw Power', color='blue')
plt.plot(frequencies[mask_negative_frequencies], smoothed_power[mask_negative_frequencies], label='Smoothed Power', color='red')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.show()


peak_index = 0
peak_power_value = smoothed_power[0]

for i in range(len(smoothed_power)):
    if(smoothed_power[i] > peak_power_value):
        peak_power_value = smoothed_power[i]
        peak_index = i 

print(f"Peak frequency index: {peak_index}") # The peak frequency index
print(f"Peak frequency: {frequencies[mask_negative_frequencies][peak_index]} Hz") # The peak freaquency walue


