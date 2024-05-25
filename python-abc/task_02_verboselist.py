#!/usr/bin/env python3

class VerboseList(list):

    """A custom list class that prints a notification
    message every time an item"""

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=None):
        if index is not None:
            item = super().pop(index)
        else:
            item = super().pop()
        print(f"Popped {item} from the list.")
