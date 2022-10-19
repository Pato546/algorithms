"""Binary search algorithm implementation.

The module contains the following classes:

- `BinarySearch` - Implements the binary search algorithm.
"""

from typing import Sequence


class BinarySearch:
    """Binary search algorithm implementation.

    The binary search algorithm has been implemented using two different
    approaches i.e The iterative approach and the recursive approach.The
    algorithm requires the collection of items to be sorted.

    Examples:
        >>> binary = BinarySearch([1, 2, 3, 4])
        >>> binary.search(4)
        3
        >>> binary.search(2)
        1
        >>> binary.search(5)
        -1
        >>> binary.search_recursive(4)
        3
        >>> binary.search_recursive(2)
        1
        >>> binary.search_recursive(5)
        -1

    Attributes:
        collection: collection of sorted items needed to be search through
               for a particular item

    methods exported by this package:

    - `search`: searches and returns the index or -1 depending on whether
                the item was found or not.
    """

    def __init__(self, collection: Sequence):
        """
        Args:
            collection (Sequence): collection to search.
        """
        self.collection = collection

    def search(self, item) -> int:
        """Searches for the item in the Sequence provided

        This method uses the iterative approach of searching for
        the item.

        Args:
            item: the object to search for.

        Returns:
            int: The index of the item if found in the collection
                 or -1 if not found.
        """

        low = 0
        high = len(self.collection) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self.collection[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search_recursive(self, item, low=0, high=None) -> int:
        """Searches for the item in the Sequence provided

        This method uses the recursive approach of searching for
        the item.

        Args:
            item: the object to search for.

        Returns:
            int: The index of the item if found in the collection or -1
                if not found.
        """

        high = len(self.collection) - 1
        mid = (low + high) // 2

        if low > high:
            return -1

        if self.collection[mid] == item:
            return mid

        return (
            self.search_recursive(item, low=mid + 1, high=high)
            if self.collection[mid] < item
            else self.search_recursive(item, low=low, high=mid - 1)
        )
