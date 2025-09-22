import random, math

def cost(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def neighbor(state):
    n = len(state)
    new_state = state[:]
    col = random.randint(0, n-1)
    row = random.randint(0, n-1)
    new_state[col] = row
    return new_state

def simulated_annealing(n=8, T=1000, cooling=0.99):
    current = [random.randint(0, n-1) for _ in range(n)]
   
    while T > 1e-6:
        next_state = neighbor(current)
        deltaE = cost(current) - cost(next_state)

   
        if deltaE > 0:
            current = next_state
        else:
         
            if random.random() < math.exp(deltaE / T):
                current = next_state
   
        T *= cooling

     
        if cost(current) == 0:
            break

    return current


solution = simulated_annealing(8)
print("The best position found is:", solution)
print("The number of queens that are not attacking each other is:", 8 if cost(solution) == 0 else 8 - cost(solution))
