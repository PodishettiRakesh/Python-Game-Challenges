import random
def grid(row,col):
    board=[]
    letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']
    for _ in range(row):
        row=[]
        for _ in range(col):
            row.append(random.choice(letter))
        board.append(row)
    print(board)
    return board
# grid(6,6)


def readfile(filename):
    with open(filename,"r") as file:
        data=file.read()
        words=data.split("\n")    
    return words
# print(readfile("words_puzzle.txt"))
