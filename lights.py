import random
def initialize_grid():
    grid=[]
    for i in range(5):
        row=[]
        for j in range(5):
            x=random.choice([1,0])
            row.append(x) 
        grid.append(row)   
    return grid

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j,end="  ")
        print()
# print_grid(initialize_grid())

def get_user():
    while True:
        try:
            row=int(input("please enter your row: "))
            if 0<=row<=4:
                while True:
                    try:
                        col=int(input("please enter your col position: "))
                        if 0<=col<=4:
                            return row,col
                        else:
                            print("Invalid col position")
                    except:
                        print("enter valid light positions")
                
            else:
                print("Invalid row position")
        except ValueError:
            print("enter valid light positions")
