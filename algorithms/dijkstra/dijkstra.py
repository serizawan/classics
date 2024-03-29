from collections import defaultdict
import heapq
import math


# Implementation without Heap Queue
def compute_dijkstra_shortest_paths_naive(graph, start_node):
    visited = {}
    unvisited = {node: math.inf for node in graph.keys()}
    unvisited[start_node] = 0
    current_distance = 0
    node = start_node
    while unvisited:
        for neighbour, distance in graph[node]:
            node_distance = current_distance + distance
            if neighbour not in visited and node_distance < unvisited[neighbour]:
                unvisited[neighbour] = node_distance
        visited[node] = current_distance
        unvisited.pop(node)
        candidates = [(n, d) for n, d in unvisited.items() if d != math.inf]
        node, current_distance = min(candidates, key=lambda x: x[1]) if candidates else (None, None)
    return visited


# Implementation with Heap Queue
def compute_dijkstra_shortest_paths(graph, start_node):
    visited = defaultdict(lambda: math.inf)
    unvisited = defaultdict(lambda: math.inf)
    unvisited[start_node] = 0
    heap = [(0, start_node)]
    while heap:
        current_distance, node = heapq.heappop(heap)
        if node not in visited:
            for neighbour, distance in graph[node]:
                node_distance = current_distance + distance
                if neighbour not in visited and node_distance < unvisited[neighbour]:
                    unvisited[neighbour] = node_distance
                    heapq.heappush(heap, (node_distance, neighbour))
            visited[node] = current_distance
            unvisited.pop(node)
    return visited


if __name__ == "__main__":
    graph = {
        "A": [("B", 3), ("C", 1)],
        "B": [("D", 2), ("E", 3)],
        "C": [("D", 3)],
        "D": [("E", 1), ("A", 2)],
        "E": [],
    }
    assert (compute_dijkstra_shortest_paths_naive(graph, "A") == {"A": 0, "C": 1, "B": 3, "D": 4, "E": 5})
    assert(compute_dijkstra_shortest_paths(graph, "A") == {"A": 0, "C": 1, "B": 3, "D": 4, "E": 5})
