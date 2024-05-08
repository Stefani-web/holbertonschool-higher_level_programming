#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Get the number of arguments
    num_args = len(argv)

    # Print the number of arguments
    if num_args - 1 == 0:
        print("{} arguments.\n".format(num_args - 1), end="")
    elif num_args - 1 == 1:
        print("{} argument:\n".format(num_args - 1), end="")
    else:
        print("{} arguments:\n".format(num_args - 1), end="")

    # Print each argument
    if num_args != 0:
        for index in range(1, num_args):
            print("{}: {}".format(index, argv[index]))
