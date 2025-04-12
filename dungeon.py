from collections import deque

dungeon_map = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '.', 'E', '.', '#', '.']
]

rows, cols = len(dungeon_map), len(dungeon_map[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False for _ in range(cols)] for _ in range(rows)]
previous = [[None for _ in range(cols)] for _ in range(rows)]

start_pos = None
end_pos = None

# Locate start and end points
for r in range(rows):
    for c in range(cols):
        if dungeon_map[r][c] == 'S':
            start_pos = (r, c)
        elif dungeon_map[r][c] == 'E':
            end_pos = (r, c)

def bfs_shortest_path():
    queue = deque([start_pos])
    visited[start_pos[0]][start_pos[1]] = True
    steps = 0
    found_exit = False

    while queue and not found_exit:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            if (row, col) == end_pos:
                found_exit = True
                break

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    not visited[new_row][new_col] and
                    dungeon_map[new_row][new_col] != '#'
                ):
                    visited[new_row][new_col] = True
                    previous[new_row][new_col] = (row, col)
                    queue.append((new_row, new_col))

        steps += 1

    return steps if found_exit else -1

def get_path():
    path = []
    current = end_pos
    while current != start_pos:
        path.append(current)
        current = previous[current[0]][current[1]]
    path.append(start_pos)
    return path[::-1]

result = bfs_shortest_path()

if result == -1:
    print("Escape is not possible!")
else:
    print(f"Escape is possible! It will take {result-1} steps.")
    path = get_path()
    print("Shortest path to escape:", path)
