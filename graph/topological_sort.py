# Topological Sort(Or Ordering) of a Graph
# https://en.wikipedia.org/wiki/Topological_sorting
# !Important not possible if the graph is not a DAG
# My Ref:
#     https://www.youtube.com/watch?v=eL-KzMXSXXI
#     https://www.youtube.com/watch?v=HyVI8-nHgEg


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


graph = {"B": {"A"}, "C": {"A"}, "D": {"B", "C"},
         "E": {"D", "B"}}     # -> ['A', 'B', 'C', 'D', 'E']
print(topological_sort(graph, 5))

# -> [0,1]
graph2 = {1: {0}}
print(topological_sort(graph2, 2))

# -> [0,2,1,3]
graph3 = {1: {0}, 2: {0}, 3: {1, 2}}
print(topological_sort(graph3, 4))

graph4 = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5],
          4: [6], 5: [6]}         # -> [6,5,4,3, 1,2, 0]
print(topological_sort(graph4, 7))
