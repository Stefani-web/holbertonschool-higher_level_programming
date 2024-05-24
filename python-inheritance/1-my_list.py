#!/usr/bin/python3
"""A class MyList that inherits"""


class MyList(list):
    """Class inheriting from the list"""

    def print_sorted(self):
        """
        prints list in ascending sort
        """
        sort_list = super().copy()
        sort_list.sort()
        print(sort_list)
