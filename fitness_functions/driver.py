import json
from audio_features import AudioFeatures
import sys

# Define the audio file path
audio_file = 'aaramb.wav'
directory = ""

num_arguments = len(sys.argv)

if num_arguments > 1:
    audio_file = sys.argv[1]
# Create an instance of the AudioFeatures class
audio_features = AudioFeatures(directory = directory, filename = audio_file)

if __name__ == "__main__":
    # Call all the functions and store the results
    results = {
        "A1": float(audio_features.A1()),
        "A2": float(audio_features.A2()),
        "A3": float(audio_features.A3()),
        "A4": float(audio_features.A4()),
        "A5": float(audio_features.A5()),
        "B1": float(audio_features.B1()),
        "B2": float(audio_features.B2()),
        "B3": float(audio_features.B3()),
        "B4": float(audio_features.B4()),
        "B5": float(audio_features.B5())
    }

    # Print the results
    for feature, value in results.items():
        print(f"{feature}:", value)

    # Save the results to a JSON file
    output_filename = f"{audio_file.replace('.wav', '')}_10_features.json"
    with open(output_filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    
    print(f"Results saved to {output_filename}")
