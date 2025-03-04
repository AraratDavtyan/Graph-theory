from collections import defaultdict, deque

def find_shortest_paths_with_weights(graph, start, end):
    # Create a queue for BFS
    queue = deque()
    queue.append((start, [start], 0))  # Start with the start node, its path, and distance

    # Dictionary to store the shortest distances from start to each node
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0

    # Dictionary to store the shortest paths to each node
    paths = defaultdict(list)
    paths[start].append([start])

    # Perform BFS
    while queue:
        node, path, distance = queue.popleft()

        if node == end:
            continue  # Skip further exploration if end node is reached

        for neighbor, edge_weight in graph.get(node, []):
            new_distance = distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                new_path = path + [neighbor]
                paths[neighbor] = [new_path]
                queue.append((neighbor, new_path, new_distance))
            elif new_distance == distances[neighbor]:
                new_path = path + [neighbor]
                paths[neighbor].append(new_path)
                queue.append((neighbor, new_path, new_distance))  # Include the path with equal distance

    return paths[end], distances[end]



graph_with_weights = {
    1: [(2, 6), (3, 3), (4, 2), (5, 8)],
    2: [(6, 5), (8, 9)],
    3: [(6, 2), (7, 8), (8, 5)],
    4: [(7, 4), (8, 7)],
    5: [(6, 5), (7, 1), (8, 6)],
    6: [(10, 5), (11, 9), (12, 6), (14, 8)],
    7: [(9, 7), (12, 1), (13, 10)],
    8: [(10, 3), (11, 5), (12, 2), (13, 3), (14, 3)],
    9: [(15, 5), (16, 6)],
    10: [(15, 4), (16, 3)],
    11: [(15, 2), (17, 6)],
    12: [(15, 8), (16, 4)],
    13: [(16, 8), (17, 9)],
    14: [(16, 6), (17, 2)],
    15: [(18, 6), (19, 2)],
    16: [(18, 3), (19, 1)],
    17: [(18, 3), (19, 4)],
    18: [(0, 5)],
    19: [(0, 3)],
}

# Find the shortest paths and distance from node 1 to node 0
shortest_paths, shortest_distance = find_shortest_paths_with_weights(graph_with_weights, 1, 0)
print("Shortest path:", shortest_paths)
print("Shortest distance:", shortest_distance)




