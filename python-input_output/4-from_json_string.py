#!/usr/bin/python3

'''This module for task 4'''

import json


def from_json_string(my_str):
    ''' Return the Python object representation of a JSONString '''
    jsonObj = json.loads(my_str)
    return jsonObj
