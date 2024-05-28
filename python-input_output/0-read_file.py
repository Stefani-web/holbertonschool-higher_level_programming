#!/usr/bin/python3
'''read file'''


def read_file(filename=""):

    '''Reads a UTF-8 encoded text file and prints its contents to stdout.
    Args: filename (str, optional): The name of the file to read.
    If not provided, the function will attempt to read from stdin.'''

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
