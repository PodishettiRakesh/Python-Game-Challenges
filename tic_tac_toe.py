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
    