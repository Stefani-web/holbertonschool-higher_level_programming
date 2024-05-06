#!/usr/bin/python3
for i in range(97, 123): # Loop over ASCII values for lowercase letters (97 to 122)
    if (i != 101) and (i != 113): # Check if the character is not 'e' (ASCII 101) and not 'q' (ASCII 113)
        print("{:s}".format(chr(i)), end="")
