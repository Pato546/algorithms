#!/usr/bin/env python3

routes = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

graph = {
    'i': ['j', 'k'],
    'j': ['i', 'k'],
    'k': ['i', 'm', 'l', 'j'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

def bfs(routes, src, dst):

    items = []
    items += graph[src]

    while items:
        node = items.pop(0)
        if node == dst:
            return True
        items += graph[node]

    else:
        return False

def dfs(routes, src, dst):

    items = []
    items += graph[src]

    while items:
        node = items.pop()
        if node == dst:
            return True 
        items += graph[node]

    else:
        return False

def u_dfs(graph, src, dst):
    items = []
    items += graph[src]
    searched = []

    while items:
        node = items.pop()
        if node == dst:
            return True
        if node not in searched:
            items += graph[node]
            searched.append(node)

    return False

if __name__ == '__main__':

    print(u_dfs(graph, 'm', 'l'))
