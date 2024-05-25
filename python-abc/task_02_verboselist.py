class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        num_items = len(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        try:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        except ValueError:
            print(f"{item} not found in the list. Cannot remove.")

    def pop(self, index=None):
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
