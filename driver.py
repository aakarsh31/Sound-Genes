# Import the AudioFeatures class
from audio_features import AudioFeatures

# Define the audio file path
audio_file = 'veera.mp3'

# Create an instance of the AudioFeatures class
audio_features = AudioFeatures(audio_file)


if __name__ == "__main__":
	# Call all the functions and store the results
	result_A1 = audio_features.A1()
	result_A2 = audio_features.A2()
	result_A3 = audio_features.A3()
	result_A4 = audio_features.A4()
	result_A5 = audio_features.A5()
	result_B1 = audio_features.B1()
	result_B2 = audio_features.B2()
	result_B3 = audio_features.B3()
	result_B4 = audio_features.B4()
	result_B5 = audio_features.B5()
	# result_feature_Entropy = audio_features.feature_Entropy()

	# Print the results
	print("A1:", result_A1)
	print("A2:", result_A2)
	print("A3:", result_A3)
	print("A4:", result_A4)
	print("A5:", result_A5)
	print("B1:", result_B1)
	print("B2:", result_B2)
	print("B3:", result_B3)
	print("B4:", result_B4)
	print("B5:", result_B5)
	# print("Feature Entropy:", result_feature_Entropy)
