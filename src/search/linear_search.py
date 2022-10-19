from typing import Iterable


class LinearSearch:
    """Linear search algorithm implementation.

    Examples:
        >>> linear = LinearSearch([4, 3, 2, 8])
        >>> linear.search(8)
        3
        >>> linear.search(3)
        1
        >>> linear.search(9)
        -1

    Attributes:
        collection: collection of items needed to be searched for a particular
                    item or object.

    methods exported by this package:

    - `search`: searches and returns the index or -1 depending on whether the
                item was found or not.
    """

    def __init__(self, collection: Iterable):
        """
        Args:
            collection (Iterable): collection to search.
        """
        self.collection = collection

    def search(self, item) -> int:
        """Searches for the item in the collection provided (`collection`)

        Args:
            item: The object to search for.

        Returns:
            int: The index of the item if found in the collection or -1 if not found.
        """

        for idx, val in enumerate(self.collection):
            if val == item:
                return idx

        return -1
