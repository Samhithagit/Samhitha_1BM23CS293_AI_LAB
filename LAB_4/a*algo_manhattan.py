import heapq

def manhattan(state, goal):
    dist = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            j = goal.index(state[i])
            x2, y2 = divmod(j, 3)
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    x, y = divmod(i, 3)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            j = nx*3 + ny
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(tuple(new_state))
    return neighbors


def a_star(start, goal):
    open_heap = [(manhattan(start, goal), 0, start, [])]
    visited = set()
    while open_heap:
        f, g, state, path = heapq.heappop(open_heap)
        if state == goal:
            return path + [state], g
        if state in visited: continue
        visited.add(state)
        for nb in get_neighbors(state):
            if nb not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(nb, goal)
                heapq.heappush(open_heap, (new_f, new_g, nb, path + [state]))
    return None, -1


print("Enter initial state (9 numbers, 0 for blank):")
start = tuple(map(int, input().split()))
print("Enter goal state (9 numbers, 0 for blank):")
goal = tuple(map(int, input().split()))

path, cost = a_star(start, goal)

if path:
    print("\nSolution found in", cost, "moves\n")
    for step, p in enumerate(path):
        print("Step", step, " g=", step, " h=", manhattan(p, goal), " f=", step + manhattan(p, goal))
        for i in range(0, 9, 3):
            print(p[i:i+3])
        print()
else:
    print("No solution found")
print("Samhitha A 1BM23CS293")
