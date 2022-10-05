#!/usr/bin/env python3

def min_(arr:list) ->int:
    ''' This function returns the index of the smallest item'''
    m = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < m:
            m = arr[i]
            index = i
    return index

def max_(arr:list) ->int:
    ''' This function returns the index of the largest item'''
    m = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] > m:
            m = arr[i]
            index = i
    return index

