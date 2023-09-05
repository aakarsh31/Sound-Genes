import json
from audio_features import AudioFeatures
import sys
import math
import csv
import pandas as pd
from decimal import Decimal, localcontext



# normal distribution function
def g(x, mean, variance):
    return math.exp(-((x - mean)**2) / (2 * variance))

# to add weights to the fitness values
def addWeights(fitnessValues, weights):
    weightesFitnessvalues = []
    for feature, fitnessValue in fitnessValues.items():
        weightesFitnessvalues.append(Decimal(weights[feature]) * Decimal(fitnessValue))
    fitnessValues["weightedSum"] = sum(weightesFitnessvalues)

    return fitnessValues

def main(rasaNumber, audioFile="aaramb.wav"):

    directory = ""

    # num_arguments = len(sys.argv)

    # if num_arguments > 1:
    #     audio_file = sys.argv[1]
    # Create an instance of the AudioFeatures class
    audio_features = AudioFeatures(directory = directory, filename = audioFile)

    # mean
    meanDf = pd.read_csv("mean.csv") 

    # sd
    varDf = pd.read_csv("sd.csv") 

    rasas = ['Karuna', 'Shanta', 'Shringar', 'Veera']

    weights = {
                "A1": 0.1,
                "A2": 0.1,
                "A3": 0.1,
                "A4": 0.1,
                "A5": 0.1,
                "B1": 0.1,
                "B2": 0.1,
                "B3": 0.1,
                "B4": 0.1,
                "B5": 0.1
            }
    rasa = rasas[0]
    # Call all the functions and store the results
    results = {
        "featureValues":{
            "A1": Decimal(audio_features.A1()),
            "A2": Decimal(audio_features.A2()),
            "A3": Decimal(audio_features.A3()),
            "A4": Decimal(audio_features.A4()),
            "A5": Decimal(audio_features.A5()),
            "B1": Decimal(audio_features.B1()),
            "B2": Decimal(audio_features.B2()),
            "B3": Decimal(audio_features.B3()),
            "B4": Decimal(audio_features.B4()),
            "B5": Decimal(audio_features.B5())
        },
    }

    fitnessValues = {}

    # to calculate fitness values from the feature values according to each rasa
    for i in range(len(rasas)):
        if rasaNumber == i+1 or rasaNumber==5:
            rasaValues = {}
            for feature, value in results["featureValues"].items():
                index = int(feature[1])
                mean = Decimal(meanDf.iloc[index][f"{rasas[i]} Peak Point"])
                variance = Decimal(5 * varDf.iloc[index][f"{rasas[i]} SigmaSq in Normal Distbn. "])
                fitnessValue = g(value, mean, variance)
                if fitnessValue != 0:
                    rasaValues[feature] = -1 * math.log(fitnessValue)
                else:
                    rasaValues[feature] = 0.0

            rasaValues = addWeights(rasaValues, weights)
            fitnessValues[rasas[i]] = rasaValues

    results["fitnessValues"] = fitnessValues


    # Save the results to a JSON file
    output_filename = f"{audioFile.replace('.wav', '')}_10_features.json"
    with open(output_filename, 'w') as json_file:
        json.dump(results, json_file, indent=4, default=str)
    
    print(f"Results saved to {output_filename}")
    
    return results


results = main(5)