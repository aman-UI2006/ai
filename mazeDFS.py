
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

visited = set()

def dfs(row, col):
    if row < 0 or col < 0 or row >= 4 or col >= 4:
        return False

    if maze[row][col] == 1 or (row, col) in visited:
        return False

    if (row, col) == (3, 3):
        print("Goal reached!")
        return True

    visited.add((row, col))
    print("Visiting:", (row, col))

    if (dfs(row + 1, col) or
        dfs(row - 1, col) or
        dfs(row, col + 1) or
        dfs(row, col - 1)):
        return True

    return False

if not dfs(0, 0):
    print("No path found")

