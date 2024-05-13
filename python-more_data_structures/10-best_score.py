

def best_score(a_dictionary):
    # Initialize variables to store the maximum score and corresponding key
    max_score = None
    max_key = None

    # Iterate through the dictionary to find the key with the maximum value
    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            max_key = key

    return max_key
