#!/usr/bin/python3
def uppercase(str):
    for index in range(len(str)):
        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            numb = 32
        else:
            numb = 0
        print("{:c}".format(ord(str[index]) - numb), end='')
    print()
