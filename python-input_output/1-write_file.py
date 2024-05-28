#!/usr/bin/python3
'''Write File'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str, optional): The name of the file to write. Defaults to an empty string.
        text (str, optional): The string to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    '''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
