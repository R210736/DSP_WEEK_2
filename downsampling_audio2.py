import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load audio file
fs, audio = wavfile.read('audio_file.wav')

# Define downsampling factor
downsampling_factor = 2

# Downsample audio signal
fs_downsampled = fs // downsampling_factor
audio_downsampled = audio[::downsampling_factor]

# Plot original and downsampled audio signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(audio)
plt.title('Original Audio Signal')
plt.xlabel('Time Index')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(audio_downsampled)
plt.title('Downsampled Audio Signal')
plt.xlabel('Time Index')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Plot frequency spectra
freq = np.fft.fftfreq(len(audio), d=1/fs)
freq_downsampled = np.fft.fftfreq(len(audio_downsampled), d=1/fs_downsampled)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(freq, np.abs(np.fft.fft(audio)))
plt.title('Original Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.stem(freq_downsampled, np.abs(np.fft.fft(audio_downsampled)))
plt.title('Downsampled Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Save downsampled audio file
wavfile.write('downsampled_audio.wav', fs_downsampled, audio_downsampled)
