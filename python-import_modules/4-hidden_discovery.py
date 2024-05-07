#!/usr/bin/python3
import sys

# Initialize the sum
total_sum = 0

# Iterate over arguments and sum up their integer values
for arg in sys.argv[1:]:
    total_sum += int(arg)

# Print the total sum
print(total_sum)
