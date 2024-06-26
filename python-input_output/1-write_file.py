#!/usr/bin/python3
'''A file-writing function.'''


def write_file(filename="", text=""):
    '''Write a string to a UTF8 text file.'''
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
