def vacuum_agent():
    A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
    B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
    loc = input("Enter location (A or B): ").upper()

    state = {'A': A, 'B': B}
    cost = 0

    if state['A'] == 0 and state['B'] == 0:
        print("Turning vacuum off")
        print("Cost:", cost)
        print(state)
        return

    if loc == 'A':
        if state['A'] == 0 and state['B'] == 1:
            print("A is clean")
            print("Moving vacuum right")
            print("Cleaned B.")
            state['B'] = 0; cost += 1
            print(f"Is B clean now? (0 if clean, 1 if dirty): {state['B']}")
            print(f"Is A dirty? (0 if clean, 1 if dirty): {state['A']}")
            print("B is clean")
            print("Moving vacuum left")

        elif state['A'] == 1 and state['B'] == 0:  # <-- Case 3
            print("Cleaned A.")
            state['A'] = 0; cost += 1
            print(f"Is A clean now? (0 if clean, 1 if dirty): {state['A']}")
            print(f"Is B dirty? (0 if clean, 1 if dirty): {state['B']}")
            print("A is clean")
            print("Moving vacuum right")

        elif state['A'] == 1 and state['B'] == 1:
            print("Cleaned A.")
            state['A'] = 0; cost += 1
            print("Moving vacuum right")
            print("Cleaned B.")
            state['B'] = 0; cost += 1
            print(f"Is B clean now? (0 if clean, 1 if dirty): {state['B']}")
            print(f"Is A dirty? (0 if clean, 1 if dirty): {state['A']}")
            print("B is clean")
            print("Moving vacuum left")

    elif loc == 'B':
        if state['B'] == 0 and state['A'] == 1:
            print("B is clean")
            print("Moving vacuum left")
            print("Cleaned A.")
            state['A'] = 0; cost += 1
            print(f"Is A clean now? (0 if clean, 1 if dirty): {state['A']}")
            print(f"Is B dirty? (0 if clean, 1 if dirty): {state['B']}")
            print("A is clean")
            print("Moving vacuum right")

        elif state['B'] == 1 and state['A'] == 0:
            print("Cleaned B.")
            state['B'] = 0; cost += 1
            print(f"Is B clean now? (0 if clean, 1 if dirty): {state['B']}")
            print(f"Is A dirty? (0 if clean, 1 if dirty): {state['A']}")
            print("B is clean")
            print("Moving vacuum left")

        elif state['B'] == 1 and state['A'] == 1:
            print("Cleaned B.")
            state['B'] = 0; cost += 1
            print("Moving vacuum left")
            print("Cleaned A.")
            state['A'] = 0; cost += 1
            print(f"Is A clean now? (0 if clean, 1 if dirty): {state['A']}")
            print(f"Is B dirty? (0 if clean, 1 if dirty): {state['B']}")
            print("A is clean")
            print("Moving vacuum right")

    print("Cost:", cost)
    print(state)


vacuum_agent()


print("Samhitha A 1BM23CS293")
