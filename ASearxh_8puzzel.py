
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def h(state):
    # Count misplaced tiles
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

pq = [(h(start), 0, start, [])]
visited = set()

while pq:
    f, g, state, path = heapq.heappop(pq)

    if state in visited:
        continue
    visited.add(state)

    if state == goal:
        for step in path + [state]:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
        break

    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                new_g = g + 1
                new_f = new_g + h(new_state)
                heapq.heappush(
                    pq, (new_f, new_g, new_state, path + [state])
                )
else:
    print("No solution found!")
