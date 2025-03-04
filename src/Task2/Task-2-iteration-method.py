
def find_start_end_nodes(graph):
    all_nodes = set(graph.keys())
    incoming_edges = set()
    outgoing_edges = set(graph.keys())

    for neighbors in graph.values():
        for node, _ in neighbors:
            incoming_edges.add(node)
            all_nodes.add(node)

    start_nodes = list(all_nodes - incoming_edges)
    end_nodes = list(all_nodes - outgoing_edges)

    return start_nodes[0] if start_nodes else None, end_nodes[0] if end_nodes else None


def all_paths(graph, start, end, path=[], total_cost=0):
    path = path + [start]
    if start == end:
        return [(path, total_cost)]
    if start not in graph:
        return []

    paths = []
    for node, cost in graph[start]:
        if node not in path:
            paths.extend(all_paths(graph, node, end, path, total_cost + cost))
    return paths


def find_min_paths(paths):
    if not paths:
        return []
    min_distance = min(paths, key=lambda x: x[1])[1]
    min_paths = [p for p in paths if p[1] == min_distance]
    return min_distance, min_paths



graph = {
    '1': [('2', 6), ('3', 3), ('4', 2), ('5', 8)],
    '2': [('6', 5), ('8', 9)],
    '3': [('6', 2), ('7', 8), ('8', 5)],
    '4': [('7', 4), ('8', 7)],
    '5': [('6', 5), ('7', 1), ('8', 6)],
    '6': [('10', 5), ('11', 9), ('12', 6), ('14', 8)],
    '7': [('9', 7), ('12', 1), ('13', 10)],
    '8': [('10', 3), ('11', 5), ('12', 2), ('13', 3), ('14', 3)],
    '9': [('15', 5), ('16', 6)],
    '10': [('15', 4), ('16', 3)],
    '11': [('15', 2), ('17', 6)],
    '12': [('15', 8), ('16', 4)],
    '13': [('16', 8), ('17', 9)],
    '14': [('16', 6), ('17', 2)],
    '15': [('18', 6), ('19', 2)],
    '16': [('18', 3), ('19', 1)],
    '17': [('18', 3), ('19', 4)],
    '18': [('0', 5)],
    '19': [('0', 3)],
}


start, end = find_start_end_nodes(graph)
print(f"Start: {start}")
print(f"End: {end}")

if start and end:
    paths = all_paths(graph, start, end)
    min_distance, min_paths = find_min_paths(paths)
    print(f"Shortest path: {min_distance}")
    for path, cost in min_paths:
        print(f"Path: {' -> '.join(path)}, Distance: {cost}")
else:
    print("The graph doesn't have start and end nodes.")



