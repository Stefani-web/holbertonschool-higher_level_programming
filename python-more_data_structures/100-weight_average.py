#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_products = 0
    sum_weights = 0

    for score, weight in my_list:
        # Cal the product of the score and wght and add it to the sum of prodct
        sum_products += score * weight
        # Add the weight to the sum of weights
        sum_weights += weight

    # Calculate the weighted average
    weighted_avg = sum_products / sum_weights

    return weighted_avg
