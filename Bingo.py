import random
def generateBoard():
    numbers=random.sample(range(10,100),25)
    board=[[numbers.pop() for _ in range(5)]for _ in range(5)]
    return board


def display_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=" ")
        print()
board=generateBoard()
display_board(board)

def mark_number(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = "x"
    return board
