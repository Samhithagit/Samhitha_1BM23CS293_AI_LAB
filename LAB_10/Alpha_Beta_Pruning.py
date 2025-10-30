moves = 0  

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    global moves
    moves += 1

   
    if depth == 3:
        print(f"Visited leaf node {values[nodeIndex]} at depth {depth}")
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2): 
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f" Pruned at depth {depth} (MAX node)")
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f" Pruned at depth {depth} (MIN node)")
                break
        return best



print("Alpha–Beta Pruning Implementation (With Move Count)")



values = [10, 9, 14, 18, 5, 4, 50, 3]

print("Leaf node values:", values)

alpha = float('-inf')
beta = float('inf')

print("\nApplying Alpha–Beta Pruning...\n")

optimal_value = alphabeta(0, 0, True, values, alpha, beta)

print("\n----------------------------------------------")
print(f" Optimal value for the root node: {optimal_value}")
print(f" Total number of moves (nodes evaluated): {moves}")
print("----------------------------------------------")
print("Samhitha A 1BM23CS293")
