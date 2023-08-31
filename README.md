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

## Sample Fitness Function Output

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
            "A1": 5.1714082224028503e-20,
            "A2": 0.9967487572869576,
            "A3": 4.481061417839407e-50,
            "A4": 1.0,
            "A5": 1.0,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 3.476904958439876e-05,
            "B4": 1.0,
            "B5": 1.0,
            "weightedSum": "0.4996783526336542230246889775"
        },
        "Shanta": {
            "A1": 1.6806723548042655e-07,
            "A2": 0.9978634499662695,
            "A3": 1.634847951314908e-31,
            "A4": 1.0,
            "A5": 1.0,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 1.0050196364249697e-13,
            "B4": 1.0,
            "B5": 1.0,
            "weightedSum": "0.4997863618033605782133917063"
        },
        "Shringar": {
            "A1": 0.0002039691907196878,
            "A2": 0.9993156897693886,
            "A3": 1.211896034138856e-07,
            "A4": 1.0,
            "A5": 1.0,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 2.410311400691143e-39,
            "B4": 1.0,
            "B5": 1.0,
            "weightedSum": "0.4999519780149711939063894759"
        },
        "Veera": {
            "A1": 0.9848099465109225,
            "A2": 0.9996774492466621,
            "A3": 0.2410275745808868,
            "A4": 1.0,
            "A5": 1.0,
            "B1": 0.0,
            "B2": 0.0,
            "B3": 3.37789377052089e-66,
            "B4": 1.0,
            "B5": 1.0,
            "weightedSum": "0.6225514970338471744421836047"
        }
    }
}