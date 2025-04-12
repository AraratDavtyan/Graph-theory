graph_data = {
    "A": [("B", 3), ("C", 6)],
    "B": [("C", 4), ("D", 4), ("E", 11)],
    "C": [("D", 8), ("G", 11)],
    "D": [("E", -4), ("F", 5), ("G", 2)],
    "E": [("H", 9)],
    "F": [("H", 1)],
    "G": [("H", 2)],
    "H": [],
}


def topological_sort(graph):
    incoming = {node: 0 for node in graph}

    for edges in graph.values():
        for target, _ in edges:
            incoming[target] += 1

    queue = [node for node in incoming if incoming[node] == 0]
    order = []

    while queue:
        current = queue.pop(0)
        order.append(current)

        for neighbor, _ in graph[current]:
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                queue.append(neighbor)

    return order


def find_longest_paths(graph, start):
    topo = topological_sort(graph)
    distance = {node: float('-inf') for node in graph}
    distance[start] = 0

    for node in topo:
        if distance[node] == float('-inf'):
            continue
        for neighbor, weight in graph[node]:
            distance[neighbor] = max(distance[neighbor], distance[node] + weight)

    return distance


longest = find_longest_paths(graph_data, "A")

print("Longest path distances starting from 'A':")
for node, dist in longest.items():
    print(f"From 'A' to {node}: {dist if dist != float('-inf') else 'Unreachable'}")
