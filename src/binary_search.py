from typing import Sequence


class BinarySearch:
    """Binary search algorithm implementation.

    Examples:
        >>> BinarySearch([1, 2, 3, 4]).search(2)
        1
        >>> BinarySearch([1, 2, 3, 4]).search(5)
        -1

    Attributes:
        items: collection of items needed to be search through
               for a particular item

    methods exported by this package:

    - `search`: searches and returns the index or -1 of the item
                being searched for in the `Sequence`
    """

    def __init__(self, items: Sequence):
        """
        Parameters:
            items: collection to search
        """
        self.items = items

    def search(self, item) -> int:
        """Searches for the item in the collection provided

        Args:
            item: the object to search for.

        Returns:
            int: The index of the item if found in the collection
                 or -1 if not found.
        """

        low = 0
        high = len(self.items) - 1

        while low <= high:
            mid = round((low + high) / 2)
            guess = self.items[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == "__main__":
    s = BinarySearch([1, 2, 3, 4])
    print(s.search(5))
