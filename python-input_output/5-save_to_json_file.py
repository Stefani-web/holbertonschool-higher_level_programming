#!/usr/bin/python3

'''This module for task 5'''

import json


def save_to_json_file(my_obj, filename):
    '''Write an object to a text file using JSON representation'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
