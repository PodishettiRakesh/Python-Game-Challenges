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

def toggle_light(grid,row,col):
    #code snippet to toggel adjacent lights along with diagonal lights also
    # for i in range(max(0,row-1),min(5,row+2)):
    #     for j in range(max(0,col-1),min(5,col+2)):
    #         if grid[i][j]==1:
    #             grid[i][j]=0
    #         else:
    #             grid[i][j]=1
    # return grid

    # Top light
    if row>0: 
        if grid[row-1][col]==0:
            grid[row-1][col]=1
        else:
            grid[row-1][col]=0
    # Bottom light
    if row<4:
        if grid[row+1][col]==0:
            grid[row+1][col]=1
        else:
            grid[row+1][col]=0
    # left light
    if col>0:
        if grid[row][col-1]==0:
            grid[row][col-1]=1
        else:
            grid[row][col-1]=0

    # right light
    if col<4:
        if grid[row][col+1]==0:
            grid[row][col+1]=1
        else:
            grid[row][col+1]=0

    if grid[row][col]==0:
            grid[row][col]=1
    else:
        grid[row][col]=0
    return grid
        
        

# grid=initialize_grid()
# print(grid)
# print_grid(grid)
# row=2
# col=3
# grid=toggle_light(grid,row,col)
# print("===========")
# print_grid(grid)

def check_win(grid):
    for i in grid:
        for j in i:
            if j!=0:
                return False
    return True
# print(check_win(initialize_grid()))

def play_game():
    print("welcome to the lights Out game")
    grid=initialize_grid()
    while True:
        print_grid(grid)
        choice=input("enter Y to choose light to off or else exit: ")
        choice=choice.lower()
        if choice=="Y":
            break
        else:
            choose=get_user()
            row=choose[0]
            col=choose[1]
            grid=toggle_light(grid,row,col)
play_game()
