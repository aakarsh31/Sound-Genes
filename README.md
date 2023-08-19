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

1. Navigate to the `fitness_functions` directory:
	```bat
	cd fitness_functions
	```


2. Run the Python driver script with the desired audio file:
	```bat
    python driver.py aaramb.wav
	```
	
Replace aaramb.wav with the name of your audio file that you want to process. Make sure you have the necessary dependencies installed and configured before running the script.

## Chromosome Processor Usage

1. Run the chromosome_processor script with an argument of output audio filename:
	```bat
	python chromosome_processor.py output.wav
	```