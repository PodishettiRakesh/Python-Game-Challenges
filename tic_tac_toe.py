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