#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Try to execute the function with the arguments provided
        result = fct(*args)
        # Returns the result of the function
        return result
    except Exception as error_execution:
        # On error, print an error message to stderr
        print("Exception:", error_execution, file=sys.stderr)
        # Returns None to indicate that an error has occurred
        return None
