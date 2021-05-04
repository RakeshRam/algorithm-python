# Prim's Minimum Spanning Tree
# Requirment: All nodes must be connected
# Greedy Algo
# MyRef: https://www.youtube.com/watch?v=jsmMtJpPnhU&t=694s

import heapq
from pprint import pprint


def addEdges(node, pq, visited, graph):
    """
    Add neighboring nodes, distance & parent node
    """
    visited.add(node)  # Add node to visited tracker
    for n, c in graph[node].items():
        if n not in visited:
            heapq.heappush(pq, (c, n, node))


def prims_algo(start, graph):
    visited = set()  # Visited node tracker
    mst = 0          # MST count
    map = {}         # MST direction map
    pq = []          # Priority Queue with tuple(distance, node, parent_node)
    addEdges(start, pq, visited, graph)   # Add neighbors
    heapq.heapify(pq)

    while pq:
        cost, cur_node, parent_node = heapq.heappop(
            pq)  # Get lowest count node !Important
        if cur_node not in visited:     # Check if node is visited
            mst += cost                 # Increment count
            map.setdefault(parent_node, []).append(
                cur_node)  # Update direction map
            addEdges(cur_node, pq, visited, graph)            # Add neighbors

    pprint(map)
    return mst


graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1}
}
print(prims_algo("A", graph))  # 7


graph1 = {'A': {'B': 1, 'C': 2, 'D': 1, 'E': 1, 'F': 2, 'G': 1},
          'B': {'A': 1, 'C': 2, 'G': 2},
          'C': {'A': 2, 'B': 2, 'D': 1},
          'D': {'A': 1, 'C': 1, 'E': 2},
          'E': {'A': 1, 'D': 2, 'F': 2},
          'F': {'A': 2, 'E': 2, 'G': 1},
          'G': {'A': 1, 'C': 2, 'F': 1}}
print(prims_algo("A", graph1))  # 6

graph2 = {'A': {'B': 4, 'C': 1, 'D': 5},
          'B': {'A': 4, 'D': 2, 'E': 3, 'F': 3},
          'C': {'A': 1, 'D': 2, 'E': 8},
          'D': {'A': 5, 'B': 2, 'C': 2, 'E': 1},
          'E': {'B': 3, 'C': 8, 'D': 1, 'F': 3},
          'F': {'B': 3, 'E': 3}}
print(prims_algo("A", graph2))  # 9
