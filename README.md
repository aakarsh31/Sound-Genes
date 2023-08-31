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
            "A1": 1.007926428105154e-216,
            "A2": 0.0,
            "A3": 0.0,
            "A4": 0.07136738676533654,
            "A5": 0.03540579509976832,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 7.965308281109304e-35,
            "B4": 0.02970490566232599,
            "B5": 0.015199189310386774,
            "weightedSum": "0.01516772768378176290225576772"
        },
        "Shanta": {
            "A1": 0.0,
            "A2": 0.0,
            "A3": 3.105293884278763e-202,
            "A4": 0.302468141094954,
            "A5": 0.10137543405224186,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 8.413282257594547e-86,
            "B4": 0.181042117825626,
            "B5": 0.04989471991558238,
            "weightedSum": "0.06347804128884042765157643068"
        },
        "Shringar": {
            "A1": 0.0,
            "A2": 0.0,
            "A3": 4.078053448903015e-14,
            "A4": 0.9074938031625237,
            "A5": 0.9031055509346169,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 1.739872913908333e-75,
            "B4": 0.827073848939163,
            "B5": 0.849685417236637,
            "weightedSum": "0.3487358620272981608820735707"
        },
        "Veera": {
            "A1": 0.9567246507759632,
            "A2": 0.0,
            "A3": 0.05677496157925463,
            "A4": 0.9919184411017616,
            "A5": 0.9851225786315673,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 1.0005724566213508e-132,
            "B4": 0.9566103330580354,
            "B5": 0.9589459520793028,
            "weightedSum": "0.4906096917225885279184411769"
        }
    }
}