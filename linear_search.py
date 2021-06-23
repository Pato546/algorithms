#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def linear_search(list_: list, item: int or str) -> int:

    for index in range(len(list_)):
        
        if list_[index] == item:
            return index

    return -1
