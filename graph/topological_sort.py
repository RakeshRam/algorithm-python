# Topological Sort(Or Ordering) of a Graph
# https://en.wikipedia.org/wiki/Topological_sorting
# !Important not possible if the graph is not a DAG
# My Ref:
#     https://www.youtube.com/watch?v=eL-KzMXSXXI
#     https://www.youtube.com/watch?v=HyVI8-nHgEg
from collections import defaultdict


def __topological_sort(v, visited, result, graph):
    if not visited[v]:                                     # Check if visited node
        # Set node visited to true
        visited[v] = True
        for n in graph.get(v, []):                         # Get neighbours of node
            # Recursively get parent node
            __topological_sort(n, visited, result, graph)
        result.append(v)                                   # Append Node


def topological_sort(graph, n):
    # Node visited dict -> {"A": False, "B": False....}
    visited = {i: False for i in set(
        list(graph.keys()) + [m for j in graph.values() for m in j])}
    result = []
    for v in visited:  # Iterate each unique node
        # Recursively get parent node
        __topological_sort(v, visited, result, graph)
    return result

# My Ref: https://www.youtube.com/watch?v=cIBFEhD77b4
def khan_algo(graph):
    in_degree = defaultdict(int)
    # Get count of outbound connects
    for i in set(list(graph.keys()) + [m for j in graph.values() for m in j]):
        in_degree[i] += len(graph.get(i, []))

    # Get reverse node connection
    out_connection = {}
    for k, v in graph.items():
        for i in v:
            out_connection.setdefault(i, []).append(k)

    queue = []
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)

    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for n in out_connection.get(node, []):
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)
    return order


graph = {"B": {"A"}, "C": {"A"}, "D": {"B", "C"},
         "E": {"D", "B"}}     # -> ['A', 'B', 'C', 'D', 'E']
print(topological_sort(graph, 5))
print(khan_algo(graph))


graph2 = {1: {0}}  # -> [0,1]
print(topological_sort(graph2, 2))
print(khan_algo(graph2))


graph3 = {1: {0}, 2: {0}, 3: {1, 2}}  # -> [0,2,1,3]
print(topological_sort(graph3, 4))
print(khan_algo(graph3))


graph4 = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5],
          4: [6], 5: [6]}         # -> [6,5,4,3, 1,2, 0]
print(topological_sort(graph4, 7))
print(khan_algo(graph4))
