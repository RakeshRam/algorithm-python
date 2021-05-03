# Dijkstra’s Shortest Path Algorithm
# Requirements
#  DAG
#  Positive edges

from pprint import pprint
from math import inf


# MyRef: https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=1195s
def dijkstras(start, graph):
    if start not in graph:
        return "NA"

    dist = {g: inf for g in graph}   # Initialize all nodes with infinity
    dist[start] = 0                  # Starting Node
    # Priority Queue with tuple(distance, node)
    pq = [(0, start)]
    while pq:
        cur_dis, cur_node = pq.pop(0)   # Get first element in queue

        if cur_dis > dist[cur_node]:    # Check if current distance gt mapped distance
            continue                    # Skip

        for n, d in graph[cur_node].items():  # Get neighboring nodes and distance
            distance = cur_dis + d            # current node distance + neighbor distance
            if distance < dist[n]:    # Check if distance lt mapped distance
                dist[n] = distance    # Update mapped distance
                pq.append((distance, n))   # Add to PQ

    return dist


graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 1, 'G': 3}, 'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3, 'A': 1, 'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}
# {'A': 0, 'B': 4, 'C': 4, 'D': 1, 'E': 2, 'F': 5, 'G': 5, 'H': 3, 'I': 5}
pprint(dijkstras("A", graph))

graph2 = {'a': {'b': 7, 'c': 9, 'f': 14},
          'b': {'a': 7, 'c': 10, 'd': 15},
          'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
          'd': {'b': 15, 'c': 11, 'e': 6},
          'e': {'d': 6, 'f': 9},
          'f': {'a': 14, 'c': 2, 'e': 9}}
# {'a': 11, 'b': 12, 'c': 2, 'd': 13, 'e': 9, 'f': 0}
pprint(dijkstras("f", graph2))

graph3 = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
# {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
pprint(dijkstras("X", graph3))

graph4 = {'s': {'a': 2, 'b': 1},
          'a': {'s': 3, 'b': 4, 'c': 8},
          'b': {'s': 4, 'a': 2, 'd': 2},
          'c': {'a': 2, 'd': 7, 't': 4},
          'd': {'b': 1, 'c': 11, 't': 5},
          't': {'c': 3, 'd': 5}}
# {'a': 2, 'b': 1, 'c': 10, 'd': 3, 's': 0, 't': 8}
pprint(dijkstras("s", graph4))

graph5 = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}
# {'B': 0, 'D': 1, 'E': 2, 'G': 2, 'C': 3, 'A': 4, 'F': 4}
pprint(dijkstras("B", graph5))
