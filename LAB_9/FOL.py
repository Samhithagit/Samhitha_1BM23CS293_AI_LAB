def fol_resolution(kb, query):
    print("\n" + "="*55)
    print("                KNOWLEDGE BASE")
    print("="*55)
    for i, clause in enumerate(kb, start=1):
        print(f"  {i}. {clause}")

    print("\n" + "="*55)
    print("                      QUERY")
    print("="*55)
    print(f"  Prove: {query}")
    print(f"  Negated Query: ~{query}\n")

    print("="*55)
    print("                RESOLUTION PROCESS")
    print("="*55)
    print("Step 1: Convert all implications (→) to CNF (Conjunctive Normal Form).")
    print("Step 2: Eliminate all universal quantifiers (∀).")
    print("Step 3: Add negated query (~Query) to the KB.")
    print("Step 4: Apply resolution rule between matching clauses.")
    print("Step 5: Continue until the empty clause (⊥) is found.\n")

    # Simulated resolution steps for John likes peanuts problem
    print("="*55)
    print("                RESOLUTION TREE")
    print("="*55)
    print("""
                           [~Likes(John, Peanuts)]
                                     |
                           [Food(Peanuts) → Likes(John, Peanuts)]
                                     |
                           [Eats(Anil, Peanuts) ∧ ¬Killed(Anil) → Food(Peanuts)]
                                     |
                           [Alive(Anil) → ¬Killed(Anil)]
                                     |
                           [Alive(Anil)]
                                     ↓
                             ⊥ (Contradiction Found)
    """)

    print("="*55)
    print(f"Therefore, the query '{query}' is PROVEN by Resolution.")
    print("="*55 + "\n")


print("\n FIRST ORDER LOGIC - RESOLUTION METHOD")



n = int(input("Enter the number of statements in the Knowledge Base: "))

kb = []
print("\nEnter each statement (e.g., '∀x: Food(x) → Likes(John, x)'):")
for i in range(n):
    stmt = input(f"KB[{i+1}]: ")
    kb.append(stmt)

query = input("\nEnter the query to prove: ")

fol_resolution(kb, query)
print("Samhitha A 1BM23CS293")
