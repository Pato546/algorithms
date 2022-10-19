import pytest

from src.search.linear_search import LinearSearch


collection = [4, 3, 6, 5]


@pytest.mark.parametrize(
    "collection, item, idx",
    [(collection, 4, 0), (collection, 3, 1), (collection, 9, -1)],
)
def test_linear_search(collection, item, idx):
    ls = LinearSearch(collection)
    assert ls.search(item) == idx
