# Number of nodes and adjacency list representation of the graph
network = {
    '0': ['9', '1'],
    '1': ['0', '8'],
    '9': ['0', '8'],
    '8': ['7'],
    '7': ['8', '3', '6', '11', '10'],
    '3': ['7', '2', '4', '5'],
    '6': ['7', '5'],
    '11': ['7', '10'],
    '10': ['7', '11'],
    '2': ['3'],
    '4': ['3'],
    '5': ['3', '6'],
    '12': []
}

def depth_first_search(network, current_node, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = set()

    visited_nodes.add(current_node)
    print(current_node, end=" ")

    for connected_node in network[current_node]:
        if connected_node not in visited_nodes:
            depth_first_search(network, connected_node, visited_nodes)

# Run DFS starting from node '0'
starting_point = '0'
depth_first_search(network, starting_point)

