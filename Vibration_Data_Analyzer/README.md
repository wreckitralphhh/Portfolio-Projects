# Vibration Data Analyzer
# Typical Vibration Data Workflow
## 1. Load your data
* Usually time-series acceleration from accelerometers (CSV, TDMS, MAT, binary, etc.)
## 2. Pre-process
* Detrend, filter, convert units, windowing, segmenting
## 3. Convert to frequency domain
* Fast Fourier Transform (FFT), PSD (Power Spectral Density), STFT for time-varying vibration
## 4. Analyze key metrics
* RMS acceleration, dominant frequencies, peak levels (G-rms), frequency response, etc.
## 5. Visualize
* Time history, FFT, spectrograms