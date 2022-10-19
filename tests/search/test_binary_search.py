import pytest

from src.search.binary_search import BinarySearch


collection = [1, 2, 3, 4]


@pytest.mark.parametrize(
    "collection, item, idx",
    [(collection, 3, 2), (collection, 4, 3), (collection, 5, -1)],
)
def test_binary_search(collection, item, idx):
    bs = BinarySearch(collection)
    assert bs.search(item) == idx
    assert bs.search_recursive(item) == idx
