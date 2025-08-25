def print_board(board):
    for row in board:
        display_row = [("''" if cell == ' ' else cell) for cell in row]
        print("[ " + ", ".join(display_row) + " ]")

def check_winner(board, player):
    for i in range(3):
        if all(s == player for s in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    moves = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn. (Enter row & col between 0-2)")

        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if row in range(3) and col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = current_player
                        moves += 1
                        break
                    else:
                        print("That spot is already taken. Try again.")
                else:
                    print("Row and column must be between 0 and 2. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            print(f"Cost of path: {moves}")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            print(f"Cost of path: {moves}")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
print("Samhitha A 1BM23CS293")

