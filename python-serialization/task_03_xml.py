#!/usr/bin/python3

'''Serializing and Deserializing with XML'''

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    '''
    Serialize a Python dictionary into XML and save it to the given filename.

    Args:
    dictionary (dict): The dictionary to be serialized.
    filename (str): The name of the output XML file.

    Example:
        my_dict = {'name': 'John', 'age': 28, 'city': 'New York'}
        serialize_to_xml(my_dict, 'data.xml')
    '''

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    '''
    Deserialize an XML file and return a Python dictionary.

    Args:
    filename (str): The name of the input XML file.

    Returns:
    dict: The deserialized dictionary.

    Example:
    loaded_dict = deserialize_from_xml('data.xml')
    print(loaded_dict)
    '''

    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_dict = {}
    for child in root:
        deserialized_dict[child.tag] = child.text

    return deserialized_dict
