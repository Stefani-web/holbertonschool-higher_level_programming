#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1 # Subtract 1 to exclude the script name

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s):", num_args, "argument" if num_args == 1 else "arguments", ":")

    # Print each argument
    for i in range(num_args):
        print(i + 1, ":", sys.argv[i + 1])
