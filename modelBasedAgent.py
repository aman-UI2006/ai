
grid = [
    ['S', 0, 1, 0],
    [0,   0, 1, 0],
    [1,   0, 0, 0],
    [0,   1, 1, 'G']
]

# Internal state representation
position = (0, 0)
visited = set()

def agent(position):
    visited.add(position)

    if grid[position[0]][position[1]] == 'G':
        print("Goal reached!")
        return True

    row, col = position

    # Possible movements: Down, Right, Up, Left
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if (0 <= r < len(grid) and
            0 <= c < len(grid[0]) and
            grid[r][c] != 1 and
            (r, c) not in visited):

            print("Moving to:", (r, c))

            if agent((r, c)):
                return True

    return False

if not agent(position):
    print("No path found!")
