# Sound Genes

Software for the research project named "Generating Rasa based Indian classical music using genetic algorithm".
More specifically, this repository contains programs to decode chromosomes to Wav files, the necessary fitness function to make this project possible and the customized genetic algorithm for the same.

## Dependencies Installation

1. Install Java: Make sure you have Java installed on your system. You can download and install the latest version of Java from the [official website](https://www.java.com/en/download/).

2. Make sure you have [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed

3. Then run the following command to install all the python based dependencies

	```bat
	pip install -r requirements.txt
	```

## Fitness Functions Usage

1. Place your sample audio file in the test_data folder

2. Navigate to the `fitness_functions` directory:
	```bat
	cd fitness_functions
	```

3. Run the Python driver script with the desired audio file:
	```bat
    python driver.py aaramb.wav
	```
4. Utilize the main() function from the `driver.py` file to obtain the fitness values.
    ```bat
    parameters:
        rasaNumber:
            Index of the Rasa:
                1 : Karuna
                2 : Shanta
                3 : Shringar
                4 : Veera
                5 : All Rasas

        audioFile:
            audio file name
            example: aaramb.wav
    ```
	
Replace aaramb.wav with the name of your audio file that you want to process. Make sure you have the necessary dependencies installed and configured before running the script.

## Chromosome Processor Usage

1. Run the chromosome_processor script with an argument of output audio filename to generate a random chromosome and convert it to a wav file:
	```bat
	python chromosome_processor.py output.wav
	```

## Sample Fitness Function Output of a Veera Rasa Based Song:

```json
{
    "featureValues": {
        "A1": "14.06",
        "A2": "0.1224",
        "A3": "22.54",
        "A4": "352.2",
        "A5": "371.8",
        "B1": "134.5",
        "B2": "371.8",
        "B3": "6.176",
        "B4": "382.5",
        "B5": "400.8"
    },
    "fitnessValues": {
        "Karuna": {
            "A1": 24.98825485211512,
            "A2": 84.81153910986474,
            "A3": 52.452985312986755,
            "A4": 45.16991167466113,
            "A5": 62.76833476569898,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 4.7392966978203255,
            "B4": 60.16764411652675,
            "B5": 78.65606649392738,
            "weightedSum": "41.37540330236012077055348115"
        },
        "Shanta": {
            "A1": 34.70402034481276,
            "A2": 41.03697400310057,
            "A3": 30.21598582359505,
            "A4": 23.96852971643465,
            "A5": 42.96127242831291,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 12.756949341283889,
            "B4": 34.25617880240763,
            "B5": 56.26704850817493,
            "weightedSum": "27.61669589681224057468566495"
        },
        "Shringar": {
            "A1": 18.574844443874557,
            "A2": 25.573423473654675,
            "A3": 3.821007500597925,
            "A4": 3.3497367535085014,
            "A5": 4.955143156261227,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 21.334294687137604,
            "B4": 6.551920264668792,
            "B5": 7.919659600732833,
            "weightedSum": "9.208002988043611814372890082"
        },
        "Veera": {
            "A1": 0.00437258413398673,
            "A2": 11.004358716880821,
            "A3": 0.3470746642123026,
            "A4": 0.28846699363146283,
            "A5": 0.7468164816450708,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 36.77330438901285,
            "B4": 1.5769696519149885,
            "B5": 2.088635006743907,
            "weightedSum": "5.282999848817539228801312625"
        }
    }
}