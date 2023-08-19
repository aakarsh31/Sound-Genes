import numpy as np
import random
import wave
import sys

def decode(chromosome, output_dir, frames_per_sec=44100, frame_duration=0.2): # Configuration parameters
    
    sample_width = 2  # in bytes (16-bit)
    
    num_frames = len(chromosome)
    num_samples = int(frames_per_sec * frame_duration * num_frames)

    # Initialize an array to hold the waveform samples
    waveform = np.zeros(num_samples, dtype=np.int16)

    # Iterate over frames in the chromosome
    for frame_idx, frame in enumerate(chromosome):
        # Iterate over bins in the frame
        for bin_idx, bin in enumerate(frame):
            # Iterate over waves in the bin
            for wave in bin:
                # Extract wave parameters
                amplitude = wave[0]
                phase = wave[1]
                frequency = wave[2]
                
                # Generate bin samples
                bin_samples = generate_bin_samples(amplitude, phase, frequency, frame_duration, frames_per_sec)
                
                # Calculate segment indices for the current bin
                segment_start = frame_idx * int(frame_duration * frames_per_sec)
                segment_end = (frame_idx + 1) * int(frame_duration * frames_per_sec)
                
                # Add bin samples to the waveform
                waveform[segment_start:segment_end] += bin_samples

    # Write the waveform to a WAV file
    write_wave(output_dir, waveform)
    print("Decoding completed!")

def generate_bin_samples(amplitude, phase, frequency, duration, frames_per_sec):
    # Generate time array
    t = np.linspace(0, duration, int(duration * frames_per_sec), endpoint=False)
    
    # Reshape frequency to match t
    frequency = np.full_like(t, frequency)
    
    # Generate waveform samples
    waveform = amplitude * np.sin(2 * np.pi * frequency * t + np.deg2rad(phase))
    
    '''This operation scales the waveform samples up or down to fit within the range of 16-bit signed integers
    , which is the format typically used in audio files (WAV format).'''

    return (waveform * 32767).astype(np.int16) 
        
def write_wave(output_dir, waveform):
    # Write waveform samples to a WAV file
    with wave.open(output_dir, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono audio
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(44100)
        wav_file.writeframes(waveform.tobytes())

def generate_full_chromosome_old():
    # Generate a full chromosome with multiple bins and waves per bin
    num_bins = 50
    waves_per_bin = 20
    num_frames = 300
    min_frequency = 20.0    
    max_frequency = 20020.0
    frequency_Range = max_frequency - min_frequency
    current_frequency = min_frequency
    frequency_difference = frequency_Range / 1000
    chromosome = []

    for frame_idx in range(num_frames):
        frame = []
        current_frequency = min_frequency
        for bin_idx in range(num_bins):
            bin = []
            amplitude = random.uniform(-1.0, 1.0)
            phase = random.uniform(0.0, 360.0)
            for wave_idx in range(waves_per_bin):
                bin.append([amplitude, phase, current_frequency])
                current_frequency += frequency_difference
            frame.append(bin)
        chromosome.append(frame)
    return chromosome

def generate_chromosome(frames = 300, bins=50, amplitude_range=1):
    # Generate a chromosome with single waves per bin
    chromosome = []

    for _ in range(frames):
        frame = []
        for _ in range(bins):
            bin = []
            amplitude = random.uniform(-amplitude_range,amplitude_range)
            phase = random.uniform(0.0, 360.0)
            bin.append([amplitude, phase])
            frame.append(bin)

        chromosome.append(frame)

    return chromosome

def enlarge_chromosome(chromosome, waves_per_bin=20, min_frequency=20.0, max_frequency=20020.0):
    # Enlarge the chromosome by adding more waves to each bin

    frequency_Range = max_frequency - min_frequency
    current_frequency = min_frequency
    frequency_difference = frequency_Range / 1000

    for frame in chromosome:
        for bin in frame:
            bin[0].append(current_frequency)
            for _ in range(waves_per_bin-1):
                bin.append([bin[0][0], bin[0][1], current_frequency])
                current_frequency += frequency_difference

    return chromosome

def generate_full_chromosome(frames = 300, bins=50, amplitude_range=1, waves_per_bin=20, min_frequency=20.0, max_frequency=20020.0):
    return enlarge_chromosome(generate_chromosome(frames=frames, bins=bins, amplitude_range=amplitude_range), waves_per_bin=waves_per_bin, min_frequency=min_frequency, max_frequency=max_frequency)


# example usage (driver code)

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
        audio_file_name = "sample_output.wav"
    
    chromosome = generate_full_chromosome()
    decode(chromosome, audio_file_name + ".wav")



