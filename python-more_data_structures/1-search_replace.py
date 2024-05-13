#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Utiliser une compréhension de liste pour créer la nouvelle liste avec les remplacements
    new_list = [replace if item == search else item for item in my_list]
    return new_list
