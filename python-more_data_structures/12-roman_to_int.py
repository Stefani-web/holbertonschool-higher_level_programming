#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5,
                      'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    prev_value = 0

    for numb in roman_string[::-1]:  # Rev string to iterate from right to left
        current_value = roman_numerals[numb]
        if prev_value > current_value:
            int_value -= current_value
        else:
            int_value += current_value
        prev_value = current_value

    return int_value
