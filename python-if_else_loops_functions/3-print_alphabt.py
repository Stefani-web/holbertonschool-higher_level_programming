#!/usr/bin/python3
for index in range(97, 123): # Loop over ASCII values for lowercase letters (97 to 122)
    # Check if the character is not 'q' and not 'e'
    if chr(index) != 'q' and chr(index) != 'e':
        print(chr(index), end='')
