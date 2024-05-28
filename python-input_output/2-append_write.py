#!/usr/bin/python3

'''This module for task 2'''


def append_write(filename="", text=""):
    '''Append text to a file'''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
