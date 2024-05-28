#!/usr/bin/python3
'''This module for task 3'''

import json


def to_json_string(my_obj):
    '''Return the JSON representation of a string object.'''
    jsonStr = json.dumps(my_obj)
    return jsonStr
