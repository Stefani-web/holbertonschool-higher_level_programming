#!/usr/bin/python3
"""a class MyList that inherits"""


class MyList(list):
    """Class inheriting from the list"""

    def print_sorted(self):

        """Displays the list sorted in ascending order"""

        sorted_list = sorted(self)
        print(sorted_list)
