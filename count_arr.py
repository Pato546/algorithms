#!/usr/bin/env python3

def count_arr(arr:list) -> int:
    
    if len(arr) == 0:
        return 0

    return 1 + count_arr(arr[1:])
