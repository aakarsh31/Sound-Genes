import numpy as np
import random
import numpy as np
import wave
import time
import sys

def decode(chromosome, filename):
    start = time.time()
    frame_duration = 0.2  # seconds
    frames_per_sec = 44100
    num_bins = 50
    waves_per_bin = 20
    sample_width = 2  # in bytes (16-bit)

    num_frames = len(chromosome)
    num_samples = int(frames_per_sec * frame_duration * num_frames)

    # Initialize an array to hold the waveform samples
    waveform = np.zeros(num_samples, dtype=np.int16)
    k = 0
    for frame_idx, frame in enumerate(chromosome):
        if frame_idx % 33:
            print(f"{frame_idx}/300")
        for bin_idx, bin_waves in enumerate(frame):
            for i in range(0, len(bin_waves), 3):
                # print(111111111111111111111111111111111111)
                # print(bin_waves[i], bin_waves[i+1], bin_waves[i+2])
                # print(1111111111111111)
                amplitude = 0.0
                phase = bin_waves[i+1]
                frequency = bin_waves[i+2]
                if i == 57:
                    if bin_idx in range(0,2):
                        # print(k)
                        k+=1
                        amplitude = bin_waves[0]
                        # print(bin_waves[0])
                # # print(i)
                bin_samples = generate_bin_samples(amplitude, phase, frequency, frame_duration, frames_per_sec, waves_per_bin)
                segment_start = frame_idx * int(frame_duration * frames_per_sec)
                segment_end = (frame_idx + 1) * int(frame_duration * frames_per_sec)
                waveform[segment_start:segment_end] += bin_samples

    write_wave(filename, waveform)
    print("Decoding completed!")
    print("The Decoding Execution Time is :", (time.time()-start), "s")

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
        # print(bin_waves)
        chromosome.append(frame)

    return chromosome

# print(np.array(generate_chromosome()).shape)
# print(len(generate_chromosome()[0][0]))

# decode(generate_chromosome(), "cata.wav")



if __name__ == "__main__":
    chromosome = []
    audio_file_name = ""

    num_arguments = len(sys.argv)

    if num_arguments == 2:
        audio_file_name = sys.argv[1]
    elif num_arguments == 3:
        chromosome = sys.argv[1]
        audio_file_name = sys.argv[2]
    elif num_arguments == 1:
        audio_file_name = "sample_output"

    chromosome = generate_chromosome()

    if len(audio_file_name) < 4 or audio_file_name[-4] != ".wav":
        audio_file_name += ".wav"
    decode(chromosome, audio_file_name)