def find_source_and_target(edges):
    start_node, end_node = None, None

    for u, v, _ in edges:
        if u not in [x[1] for x in edges]:
            start_node = u
        if v not in [x[0] for x in edges]:
            end_node = v

    return start_node, end_node


def bellman_ford_shortest_path(edges, start_node, end_node):
    vertex_set = set()
    for u, v, _ in edges:
        vertex_set.add(u)
        vertex_set.add(v)
    num_vertices = len(vertex_set)

    INF = float('inf')
    distance = [INF] * num_vertices
    previous_node = [None] * num_vertices
    distance[start_node] = 0

    # Bellman-Ford Algorithm
    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                previous_node[v] = u

    #Shortest path
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = previous_node[current]
    path.reverse()

    total_distance = distance[end_node]

    print(f"Shortest path from {start_node} to {end_node}:")
    for i in range(len(path) - 1):
        edge_length = distance[path[i + 1]] - distance[path[i]]
        print(f"{path[i]} → {path[i + 1]} (length: {edge_length})", end=" ")

    print(f"\nTotal path length: {total_distance}")


#Example graph edges: [from, to, weight]
edges_list = [
    [0, 1, 4],
    [0, 2, 2],
    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 3],
    [2, 1, 1],
    [2, 3, 4],
    [2, 4, 5],
    [3, 4, 1],
    [4, 5, 2]
]

start_node, end_node = find_source_and_target(edges_list)
bellman_ford_shortest_path(edges_list, start_node, end_node)
