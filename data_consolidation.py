import os
import json
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split

def parse_xml_file(xml_file):
    """
    Parse an XML file to extract image and bounding box data.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list: A list of dictionaries containing image and bounding box data.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []

    for image in root.findall('image'):
        image_id = image.get('id')
        image_name = image.get('name')
        image_width = image.get('width')
        image_height = image.get('height')
        
        for box in image.findall('box'):
            label = box.get('label')
            xtl = box.get('xtl')
            ytl = box.get('ytl')
            xbr = box.get('xbr')
            ybr = box.get('ybr')
            
            observation = {
                "image_id": image_id,
                "image_name": image_name,
                "image_width": image_width,
                "image_height": image_height,
                "xtl": xtl,
                "ytl": ytl,
                "xbr": xbr,
                "ybr": ybr
            }
            
            data.append([observation, label])
    
    return data

def consolidate_data(input_folder, output_folder, test_percentage, training_percentage, output_prefix):
    """
    Consolidate data from XML files, split into training and test sets, and save as JSON.

    Args:
        input_folder (str): Path to the input folder containing XML files.
        output_folder (str): Path to the output folder for JSON files.
        test_percentage (float): Percentage of data to be used for testing.
        training_percentage (float): Percentage of data to be used for training.
        output_prefix (str): Prefix for the output JSON file names.

    Raises:
        Exception: If there is an error during the data consolidation process.
    """
    all_data = []

    # Iterate through each XML file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xml'):
            file_path = os.path.join(input_folder, file_name)
            file_data = parse_xml_file(file_path)
            all_data.extend(file_data)
    
    # Split the data into training and test sets
    train_data, test_data = train_test_split(all_data, test_size=test_percentage/100, train_size=training_percentage/100)

    # Define the output file paths
    train_file_path = os.path.join(output_folder, f"{output_prefix}_Train.json")
    test_file_path = os.path.join(output_folder, f"{output_prefix}_Test.json")

    # Save the training data as a JSON file
    with open(train_file_path, 'w') as train_file:
        json.dump(train_data, train_file, indent=4)

    # Save the test data as a JSON file
    with open(test_file_path, 'w') as test_file:
        json.dump(test_data, test_file, indent=4)
