from copy import deepcopy 
import random 
from driver import computeFitnessValues
from chromosome_processor import decode
import os
import json

Gl= 50
# Bins per frame
# Gene Length
# This is the number of frequency Bins in a single Time Frame

Wpb= 20
# Waves per bin
# This is the number of waves in a single Bi

A = 1000

minFrequency = 200
# minimum frequency per frame

maxFrequency = 17000


# Function to generate a random chromosome based on specified parameters
def generate_chromosome(A, Cl=300, Gl=50):
# Cl = Number of frames
# Gl = Number of bins per frame
# A = Amplitude Range

# Random Chromosome Generator
# Creates a random chromosome with the permissible boundary values

    L=[]

    for i in range(Cl):
        L.append([])
        
        for j in range(Gl):
            L[i].append([random.uniform(0,A), random.uniform(0,360)])
    
    return L


def fitnessFunction(Inp):
    """
    Calculate fitness value for a given chromosome.
    
    Args:
        chromosome (list): The chromosome to calculate fitness for.
        index (int): Population number of the chromosome.
        generation (int): Generation number.
        rasaNumber (int, optional): The rasa number to consider (default is 1 which represents Karuna).

    Returns:
        float: The fitness value.
    """

    chromosome=Inp[0]
    index=Inp[1]
    generation=Inp[2]
    rasaNumber=Inp[3]

    rasas = ['Karuna', 'Shanta', 'Shringar', 'Veera']
    chromosome_copy = deepcopy(chromosome)

    decode(chromosome_copy, index=index,bins_per_frame=Gl, waves_per_bin=Wpb, generation = generation, minFrequency=minFrequency, maxFrequency=maxFrequency)

    values = computeFitnessValues(rasaNumber=rasaNumber, audioFile=f"gen{generation}-{index}.wav", generation=generation, populationNumber=index)
    fitnessValues = {}
    for i in range(len(rasas)):
        fitnessValue = float(values["fitnessValues"][rasas[i]]["weightedSum"])
        fitnessValues[rasas[i]] = fitnessValue

    return fitnessValues, values['featureValues']

if __name__ == "__main__":

    audioOutputPath = 'audio_output'
    featuresOutputPath = 'features_output'
    graphsPath = 'graphs'
    if not os.path.exists(audioOutputPath):
        os.makedirs(audioOutputPath)
    else:
        pass
    if not os.path.exists(featuresOutputPath):
        os.makedirs(featuresOutputPath)
    else:
        pass
    if not os.path.exists(graphsPath):
        os.makedirs(graphsPath)
    else:
        pass


    Amps = [0.1, 10, 100, 1000]

    results = {}
    for A in Amps:
        x=generate_chromosome(A=A)
        testInputAll=[x,0,0,5]
        fitnessValues, featureValues=fitnessFunction(testInputAll)
        results[A] = {"featureValues":featureValues, "fitnessValues":fitnessValues}
        print(f"{A} Amplitude: \nFeature Values: {featureValues}\nFitness Values: {fitnessValues}\n")

        with open("FFtesting.json", 'w') as json_file:
                json.dump(results, json_file, indent=4, default=str)




 

