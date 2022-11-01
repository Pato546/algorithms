"""Bubble Sort Algorithm"""


def bubble_sort(arr: list):
    """Sorts an array using the bubble sort algorithm

    Examples:
        >>> bubble_sort([9, 7, 8, 5, 6, 3, 4, 1, 2])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Args:
        arr: list to be sorted
    """

    arr_len = len(arr)
    swap = True

    while swap:
        swap = False
        for i in range(arr_len - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

    return arr


if __name__ == "__main__":
    print(bubble_sort([9, 7, 8, 5, 6, 3, 4, 1, 2, 2]))
