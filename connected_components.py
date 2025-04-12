graph = {
    0: [1],
    1: [2, 4, 6],
    2: [3],
    3: [2, 4, 5],
    4: [5],
    5: [4],
    6: [0, 2],
    7: []
}

num_nodes = len(graph) 
component_count = 0
component_ids = [-1] * num_nodes
visited = [False] * num_nodes

for node in range(num_nodes):
    if not visited[node]:
        component_count += 1
        stack = [node]

        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                component_ids[current] = component_count
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

print("Number of connected components:", component_count)
print("Component assignments:", component_ids)
