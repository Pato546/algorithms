#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(list_: list, item: int or str) -> int:
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = list_[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

my_list = ['Ababio', 'Patrick']

print(binary_search(my_list, 'Patrick'))










