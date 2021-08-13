#!/usr/bin/env python3

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depth_first_search(graph, source):
    items = []
    items += graph[source]

    print(source)

    while items:
        node = items.pop()
        print(node)
        items += graph[node]

    else:
        print('done traversing')

if __name__ == '__main__':

    depth_first_search(graph, 'f')
