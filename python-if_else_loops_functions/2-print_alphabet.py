#!/usr/bin/python3
for i in range(97, 123): # Loop over ASCII values for lowercase letters (97 to 122) and print each character
    print("{:s}".format(chr(i)), end="")   # Convert ASCII value to character and print without newline
