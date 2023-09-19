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

2. Navigate to the `root` directory:
	```bat
	cd root
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
            "A1": 1.4343301666752584,
            "A2": 2.942247018293831,
            "A3": 1.7646446676322307,
            "A4": 1.7647452812345685,
            "A5": 2.042899553420991,
            "B1": 376.4866125360412,
            "B2": 0.0,
            "B3": 0.15944134726045894,
            "B4": 2.3506923547341207,
            "B5": 2.5599921316075185,
            "weightedSum": "39.15056050569002065456561433"
        },
        "Shanta": {
            "A1": 0.5877982793537057,
            "A2": 1.9323578626248397,
            "A3": 1.0967147563190252,
            "A4": 1.0969961924704923,
            "A5": 1.3968489728572893,
            "B1": 359.9484607165907,
            "B2": 0.0,
            "B3": 0.4630242637086237,
            "B4": 1.5678432577807475,
            "B5": 1.8294748845138409,
            "weightedSum": "36.99195191862193010612091629"
        },
        "Shringar": {
            "A1": 0.3196046027226819,
            "A2": 0.618494027329678,
            "A3": 0.2639381179780499,
            "A4": 0.26394669324245484,
            "A5": 0.4173470575564007,
            "B1": 352.3490717577444,
            "B2": 0.0,
            "B3": 1.4736777112400485,
            "B4": 0.5162667443751316,
            "B5": 0.6670335300076445,
            "weightedSum": "35.68893802421965213916499461"
        },
        "Veera": {
            "A1": 0.0004937470230943188,
            "A2": 0.29147378135282315,
            "A3": 0.02340424724350487,
            "A4": 0.02341583559810685,
            "A5": 0.06445787329655918,
            "B1": 332.25444690129444,
            "B2": 0.0,
            "B3": 2.479730146348764,
            "B4": 0.1280079278658161,
            "B5": 0.1802704867076569,
            "weightedSum": "33.54457009467307874642833838"
        }
    }
}