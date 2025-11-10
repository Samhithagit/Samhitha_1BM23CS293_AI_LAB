from queue import PriorityQueue

graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('E', 3), ('F', 1)],
    'E': [('H', 5)],
    'F': [('I', 2), ('G', 3)],
    'C': [],
    'D': [],
    'H': [],
    'I': [],
    'G': []
}

H = {
    'S': 13,
    'A': 12,
    'B': 4,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'H': 4,
    'I': 9,
    'G': 0
}

def greedy_best_first_search(start, goal):
    pq = PriorityQueue()
    pq.put((H[start], start))
    visited = set()
    parent = {}

    while not pq.empty():
        h, node = pq.get()
        if node in visited:
            continue
        visited.add(node)

      
        if node == goal:
          
            path = []
            while node:
                path.append(node)
                node = parent.get(node)
            path.reverse()

           
            total_cost = 0
            for i in range(len(path) - 1):
                for neighbor, cost in graph[path[i]]:
                    if neighbor == path[i + 1]:
                        total_cost += cost
                        break

            print(f"\nPath found: {' -> '.join(path)}")
            print(f"Total path cost: {total_cost}")
            return path, total_cost

        
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                pq.put((H[neighbor], neighbor))

    print("Goal not reachable.")
    return None, None


path, cost = greedy_best_first_search('S', 'G')
