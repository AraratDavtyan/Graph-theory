import numpy as np

def topological_sort(network):
    nodes = list(network.keys())
    in_degree_count = np.zeros(len(nodes), dtype=int)

    # Count in-degrees
    for node in network:
        for connected_node in network[node]:
            in_degree_count[nodes.index(connected_node)] += 1

    # Collect nodes with zero in-degree
    zero_in_degree_queue = [nodes[i] for i in range(len(nodes)) if in_degree_count[i] == 0]

    sorted_order = []

    while zero_in_degree_queue:
        current_node = zero_in_degree_queue.pop(0)
        sorted_order.append(current_node)

        for connected_node in network[current_node]:
            idx = nodes.index(connected_node)
            in_degree_count[idx] -= 1
            if in_degree_count[idx] == 0:
                zero_in_degree_queue.append(connected_node)

    if len(sorted_order) != len(network):
        return None  # Graph has a cycle

    return sorted_order


network = {
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

print(topological_sort(network))
