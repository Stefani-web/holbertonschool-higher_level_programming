#!/usr/bin/python3

'''This module is serialization'''

import json


def serialize_and_save_to_file(data, filename):

    '''Serialize a Python dictionary to a JSON file and save it.
    Args: data (dict): A Python dictionary with data.
    filename (str): The filename of the output JSON file.
    If the output file already exists, it will be replaced.
    '''

    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Data serialized and saved to {filename}")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")


def load_and_deserialize(filename):

    '''Load and deserialize data from a specified JSON file.

    Args:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: A Python dictionary with the deserialized JSON data from the file.
    '''

    try:
        with open(filename, 'r') as json_file:
            loaded_data = json.load(json_file)
        return loaded_data
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return None
