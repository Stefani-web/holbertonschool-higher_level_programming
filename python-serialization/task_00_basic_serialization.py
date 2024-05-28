#!/usr/bin/python3

'''This module is serialization'''

import json


def serialize_and_save_to_file(data, filename):

    '''Serialize a Python dictionary to a JSON file and save it.
    Args: data (dict): A Python dictionary with data.
    filename (str): The filename of the output JSON file.
    If the output file already exists, it will be replaced.
    '''

    with open(filename, "w") as my_file:
        json.dump(data, my_file)


def load_and_deserialize(filename):

    '''Load and deserialize data from a specified JSON file.

    Args:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: A Python dictionary with the deserialized JSON data from the file.
    '''

    with open(filename, "r") as my_file:
        return json.load(my_file)
