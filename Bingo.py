import random
def generateBoard():
    numbers=random.sample(range(10,100),25)
    # print(board)
    board=[[numbers.pop() for _ in range(5)]for _ in range(5)]
    # print(board)
    return board
# generateBoard()

def display_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end=" ")
        print()
board=generateBoard()
display_board(board)


