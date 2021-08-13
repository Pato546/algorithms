#!/usr/bin/env python3
from find_min_max import min_, max_

def is_empty(func):
    
    def wrapper(*args, **kwargs):
        
        for arg in args:
            if len(arg) == 0:
                return [] 
        return func(*args, **kwargs)
    
    return wrapper


@is_empty
def selection_sort(arr:list, reverse=False) -> list or str:
    #if len(arr) == 0:
        #return 'cannot sort an empty list'

    sorted_array = []

    if not reverse:
        for i in range(len(arr)):
            sorted_array.append(arr.pop(min_(arr)))

        return sorted_array

    else:
        for i in range(len(arr)):
            sorted_array.append(arr.pop(max_(arr)))

        return sorted_array

