import librosa
import numpy as np
import math

class AudioFeatures:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.audio, self.sr = librosa.load(audio_file)

    def A1(self):
        # Calculate the spectral centroids for the audio time series.
        spectral_centroids = librosa.feature.spectral_centroid(y=self.audio, sr=self.sr)

        # Calculate the mean spectral centroid of all frames.
        mean_spectral_centroid = np.mean(spectral_centroids)

        # Calculate the standard deviation of the spectral centroids.
        sc_std = math.sqrt(((spectral_centroids - mean_spectral_centroid) ** 2).mean())

        return sc_std

    def A2(self):
        # Function A2: Derivative of Spectral Rolloff Point Overall Standard Deviation
        spectral_rolloff = librosa.feature.spectral_rolloff(y=self.audio, sr=self.sr)
        spectral_rolloff_derivative = np.diff(spectral_rolloff)
        return np.std(spectral_rolloff_derivative)

    def A3(self):
        # Function A3: Derivative of Zero Crossings Overall Standard Deviation
        zero_crossings = librosa.feature.zero_crossing_rate(y=self.audio)
        zero_crossings_derivative = np.diff(zero_crossings)
        return np.std(zero_crossings_derivative)

    def A4(self):
        # Function A4: Derivative of Strongest Frequency Via Zero Crossings Overall Standard Deviation
        zero_crossing_rate = librosa.feature.zero_crossing_rate(self.audio)
        freq_via_zero_crossings = librosa.fft_frequencies(sr=self.sr)
        
        # Find the frame with the highest zero crossing rate
        frame_index = np.argmax(zero_crossing_rate)
        
        # Get the frequencies corresponding to all frames
        freqs_frames = freq_via_zero_crossings
        
        # Calculate the derivative of the frequencies
        freqs_derivative = np.diff(freqs_frames)
        
        # Calculate the standard deviation of the derivative
        return np.std(freqs_derivative)

    def A5(self):
        # Function A5: Strongest Frequency Via Spectral Centroid
        spectral_centroids = librosa.feature.spectral_centroid(y=self.audio, sr=self.sr)
        freq_bins = librosa.core.fft_frequencies(sr=self.sr)
        min_shape = min(freq_bins.shape[0], spectral_centroids.shape[1])
        freq_bins = freq_bins[:min_shape]
        freq_via_spectral_centroid = freq_bins[np.argmax(spectral_centroids[:, :min_shape])]
        
        return freq_via_spectral_centroid

    def B1(self):
        # Function B1: Standard Deviation of Zero Crossings Overall Standard Deviation
        zero_crossings = librosa.feature.zero_crossing_rate(y=self.audio)
        return np.std(zero_crossings)

    def B2(self):
        # Function B2: Strongest Frequency Via FFT Maximum Overall Standard Deviation
        fft_max = np.abs(librosa.stft(self.audio)).flatten()
        freq_via_fft_max = librosa.fft_frequencies(sr=self.sr)
        
        # Find the index of the frame with the highest FFT maximum
        frame_index = np.argmax(fft_max)
        
        # Ensure the frame index is within the valid range
        if frame_index >= len(freq_via_fft_max):
            frame_index = len(freq_via_fft_max) - 1
        
        # Get the frequency corresponding to the frame index
        freq_frame = freq_via_fft_max[frame_index]
        
        # Calculate the standard deviation of the frequency
        return np.std(freq_frame)




    def B3(self):
        # Function B3: Running Mean of Spectral Centroid
        spectral_centroids = librosa.feature.spectral_centroid(y=self.audio, sr=self.sr)
        
        # Calculate the running mean using a simple moving average with a window of 3
        running_mean = np.convolve(spectral_centroids[0], np.ones(3), mode='same') / 3.0
        
        return running_mean



    def B4(self):
        # Function B4: Strongest Frequency Via FFT Maximum Overall Standard Deviation
        stft = librosa.stft(y=self.audio)
        magnitudes = np.abs(stft)
        freq_bins = librosa.fft_frequencies(sr=self.sr)
        freq_via_fft_max = freq_bins[np.argmax(magnitudes, axis=0)]
        std_freq_via_fft_max = np.std(freq_via_fft_max)
        
        return std_freq_via_fft_max


    def B5(self):
        # Function B5: Strongest Frequency Via FFT Maximum Overall Standard Deviation
        stft = librosa.stft(y=self.audio)
        magnitudes = np.abs(stft)
        freq_bins = librosa.fft_frequencies(sr=self.sr)
        freq_via_fft_max = freq_bins[np.argmax(magnitudes, axis=0)]
        std_freq_via_fft_max = np.std(freq_via_fft_max)
        
        return std_freq_via_fft_max


    def feature_Entropy(self):
        # Function feature_Entropy: Feature entropy
        feature = librosa.feature.rms(y=self.audio)
        hist, _ = np.histogram(feature, bins=10, density=True)
        entropy = -np.sum(hist * np.log2(hist + 1e-6))
        return entropy
