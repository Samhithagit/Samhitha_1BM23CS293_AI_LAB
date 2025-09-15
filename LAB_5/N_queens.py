import random

def heuristic(board):
    """Count number of attacking pairs of queens."""
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def get_neighbors(board):
    """Generate neighbors by swapping the row positions of any two queens."""
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            new_board = list(board)
            # Swap queens in columns i and j
            new_board[i], new_board[j] = new_board[j], new_board[i]
            neighbors.append(new_board)
    return neighbors

def hill_climbing(board, max_sideways=100):
    steps = 0
    sideways_moves = 0
    current_heur = heuristic(board)
    path = [board[:]]

    while True:
        if current_heur == 0:
            return board, steps, path

        neighbors = get_neighbors(board)
        neighbor_heuristics = [(neighbor, heuristic(neighbor)) for neighbor in neighbors]

        best_heur = min(h for _, h in neighbor_heuristics)
        best_neighbors = [nb for nb, h in neighbor_heuristics if h == best_heur]

        if best_heur > current_heur:
            # No improvement, reached local minimum
            return None, steps, path

        next_board = random.choice(best_neighbors)

        if best_heur < current_heur:
            sideways_moves = 0
        elif best_heur == current_heur:
            sideways_moves += 1
            if sideways_moves > max_sideways:
                return None, steps, path

        board = next_board
        current_heur = best_heur
        path.append(board[:])
        steps += 1

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[col] == row else ". "
        print(line)
    print()

def main():
    n = int(input("Enter the number of queens (N): "))
    print(f"Enter the initial board positions (row for each queen in column 0 to {n-1}):")
    print(f"Rows should be between 0 and {n-1}, space separated.")
    board_input = input()

    try:
        board = list(map(int, board_input.strip().split()))
    except ValueError:
        print("Invalid input format.")
        return

    if len(board) != n or any(r < 0 or r >= n for r in board):
        print("Invalid board input.")
        return

    solution, cost, path = hill_climbing(board)

    if solution:
        print("\nSolution found!\n")
    else:
        print("\nNo solution found (stuck in local minimum).\n")

    print(f"Cost (steps taken): {cost}\n")
    print("Steps to reach solution:")

    for step_num, state in enumerate(path):
        print(f"Step {step_num}: heuristic = {heuristic(state)}")
        print_board(state)

    print("Samhitha A 1BM23CS293")

if __name__ == "__main__":
    main()
