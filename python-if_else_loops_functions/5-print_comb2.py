#!/usr/bin/python3
print("{:02d}".format(0), end=', ')
for i in range(1, 100):
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')
