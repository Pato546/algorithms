#!/usr/bin/env python3

from collections import deque
from depth_first_search import depth_first_search

graph = {
    'You': ['Alice', 'Bob', 'Claire'],
    'Alice': ['Peggy'],
    'Peggy': [],
    'Bob': ['Anuj', 'Peggy'],
    'Anuj': [],
    'Claire': ['Thom', 'Jonny'],
    'Jonny': [],
    'Thom': [],
}

'''
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
'''
def breadth_first_search(graph, source):
    items = []
    items += graph[source]
    print(source)

    while items:
        node = items.pop(0)
        print(node)
        items += graph[node]

if __name__ == '__main__':

    depth_first_search(graph, 'You')
    print('')
    breadth_first_search(graph, 'You')

