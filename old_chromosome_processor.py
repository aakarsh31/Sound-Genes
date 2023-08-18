import numpy as np
import random

import numpy as np
import wave
def decode(chromosome, filename):

    frames_per_sec = 44100
    frame_duration = 0.2  # seconds
    num_bins = 50
    waves_per_bin = 20
    sample_width = 2  # in bytes (16-bit)

    num_frames = len(chromosome)
    num_samples = int(frames_per_sec * frame_duration * num_frames)

    # Initialize an array to hold the waveform samples
    waveform = np.zeros(num_samples, dtype=np.int16)

    for frame_idx, frame in enumerate(chromosome):
        for bin_idx, bin_waves in enumerate(frame):
            amplitude = bin_waves[0]
            phase = bin_waves[1]
            frequency = bin_waves[2]
            bin_samples = generate_bin_samples(amplitude, phase, frequency, frame_duration, frames_per_sec, waves_per_bin)
            segment_start = frame_idx * int(frame_duration * frames_per_sec)
            segment_end = (frame_idx + 1) * int(frame_duration * frames_per_sec)
            waveform[segment_start:segment_end] += bin_samples

    write_wave(filename, waveform)
    print("Decoding completed!")

def generate_bin_samples(amplitude, phase, frequency, duration, frames_per_sec, waves_per_bin):
    t = np.linspace(0, duration, int(duration * frames_per_sec), endpoint=False)
    frequency = np.full_like(t, frequency)  # Reshape frequency to match t
    waveform = amplitude * np.sin(2 * np.pi * frequency * t + np.deg2rad(phase))
    return (waveform * 32767).astype(np.int16)


def write_wave(filename, waveform):
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono audio
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(44100)
        wav_file.writeframes(waveform.tobytes())




def generate_chromosome():
    num_bins = 50
    waves_per_bin = 20
    num_frames = 300
    min_frequency = 20.0    
    max_frequency = 20020.0
    frequency_Range = max_frequency - min_frequency
    current_frequency = min_frequency
    frequency_difference = frequency_Range/1000
    chromosome = []

    for frame_idx in range(num_frames):
        frame = []
        current_frequency = min_frequency
        for bin_idx in range(num_bins):
            bin_waves = []
            amplitude = random.uniform(-1.0, 1.0)
            phase = random.uniform(0.0, 360.0)
            for wave_idx in range(waves_per_bin):
                bin_waves.append(amplitude)
                bin_waves.append(phase)
                bin_waves.append(current_frequency)
                current_frequency+=frequency_difference

            frame.append(bin_waves)

        chromosome.append(frame)

    return chromosome

print(np.array(generate_chromosome()).shape)
print(len(generate_chromosome()[0][0]))

decode(generate_chromosome(), "bro2.wav")


