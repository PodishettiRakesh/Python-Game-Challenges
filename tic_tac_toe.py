def initialize_board(n):
    board=[[" " for _ in range(n)]for _ in range(n)]
    return board
# initialize_board(3)

def display_board(board):
    """Display the current state of the tic-tac-toe board."""
    for row in board:
        # print(row)
        print('|'.join(row))
        print('-' * 5)
# board=initialize_board(3)
# display_board(board)

def makeMove(board,player,row,col):
    if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == ' ':
        board[row][col]=player
        return board
# board=initialize_board(3)
# display_board(board)
# board1=makeMove(board,"x",1,2)
# print("----------")
# display_board(board1)

def switch_player(current_player):
    if current_player=="x":
        return "o"
    else:
        return 'x'
    
def checkWin(board):
    """Check if there is a winner on the board."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def playTicTacToe():
    board=initialize_board(3)

    current_player="x"
    print("welcome to the tic_tac_toe game")

    while True:
        display_board(board)
        print(f"player{current_player}'s turn ")
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        if makeMove(board, current_player, row, col):
            if checkWin(board):
                display_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break
            current_player=switch_player(current_player)
        else:
            print("invalid move try again")

playTicTacToe()