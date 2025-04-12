graph = {
    '0': ['2', '6', '3'],
    '1': ['4'],
    '2': ['6'],
    '3': ['1', '4'],
    '4': ['5', '8'],
    '5': [],
    '6': ['7', '11'],
    '7': ['4', '12'],
    '8': [],
    '9': ['2', '10'],
    '10': ['6'],
    '11': ['12'],
    '12': ['8'],
    '13': [],
}


def topological_sort(graph):
    in_degree_count = {node: 0 for node in graph}

    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree_count[neighbor] += 1

    nodes_with_no_incoming = [node for node in in_degree_count if in_degree_count[node] == 0]
    sorted_nodes = []

    while nodes_with_no_incoming:
        current_node = nodes_with_no_incoming.pop(0)
        sorted_nodes.append(current_node)

        for adjacent in graph[current_node]:
            in_degree_count[adjacent] -= 1
            if in_degree_count[adjacent] == 0:
                nodes_with_no_incoming.append(adjacent)

    return sorted_nodes if len(sorted_nodes) == len(graph) else None


sorted_order = topological_sort(graph)

print("Topological Order:" if sorted_order else "There is a circular dependency.")
print(sorted_order if sorted_order else "")
