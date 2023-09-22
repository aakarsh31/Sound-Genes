import json
import xml.etree.ElementTree as ET
import subprocess
import os

def extract_features(settings="final_settings.xml", directory="", filename="aaramb.wav", output_filename=None):

    output_folder = "features_output"
    # If no output filename is provided, use the original filename without .wav extension
    if output_filename is None:
        output_filename = filename.replace(".wav", "")
    
    # Create the full audio file path
    audio_filepath = os.path.join(directory, filename)
    
    # Construct the Java command to run jAudio feature extraction
    java_command = [
        'java',
        '-Xmx1024M',
        '-jar',
        'jAudio.jar',  # jAudio Executable filename
        '-s',
        settings,  # jAudio settings file
        output_filename,  # Features Output FileName
        "../audio_output/" + audio_filepath  # Audio Filename
    ]
    
    try:
        # Run the Java command and set the current working directory to 'jAudio'
        subprocess.run(java_command, check=True, cwd="jAudio")
    except subprocess.CalledProcessError as e:
        print("Error executing Java command:", e)
    else:
        pass
        # print("Java command executed successfully")

        # Load XML file
        current_path = os.getcwd()
        xml_file = os.path.join(current_path, 'jAudio', f'{output_filename}FV.xml')
        # print("Current path:", current_path)
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Create a dictionary to store the extracted data
        data = {'data_set_id': root.find('./data_set/data_set_id').text}

        # Iterate through feature elements and extract data
        features = root.findall('./data_set/feature')
        for feature in features:
            feature_name = feature.find('name').text
            values = [v.text for v in feature.findall('v')]
            if len(values) == 1:
                data[feature_name] = values[0]
            else:
                data[feature_name] = values

        # Store the extracted data in a JSON file
        json_file = f'{output_folder}/{output_filename}_all_features.json'
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        # print(f"Data extracted and saved to {json_file}")

        return data
    return None
