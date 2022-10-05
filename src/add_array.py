#!/usr/bin/env python3

def sum_arr(arr:list) -> int:

    if len(arr) == 0:
        return 0

    return arr[0] + sum_arr(arr[1:])
