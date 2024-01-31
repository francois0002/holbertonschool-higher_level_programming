#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    for key, value in a_dictionary.items():
        if value is max(a_dictionary.values()):
            return key
