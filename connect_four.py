def generate_grid(row,col):
    grid=[]
    for i in range(row):
        rows=[]
        for j in range(col):
            rows.append("_")
        
        grid.append(rows)
    return grid
# print(generate_grid(6,7))

def display_grid(grid):
    for i in grid:
        for j in i:
            print(j,end=" ")
        print()
# display_grid(generate_grid(6,7))

def get_user_input():
    while True:
        try:
            col_num=int(input("enter your col number to drop the disc: "))
            if col_num>col-1 or col_num<0:
                print("col position out of grid")
            else:
                return col_num
        except ValueError:
            print("Error in selecting column to drop disc! try again")
# print(get_user_input())
row=6
col=7
def drop_disc(grid,col_num,disc):
    i=0
    while i<row:
        if grid[i][col_num]=="_" and i!=5:
            if grid[i+1][col_num]!="_":
                grid[i][col_num]=disc
                break
            i+=1
        else:
            grid[i][col_num]=disc
            break
    return grid
# grid=generate_grid(row,col)
# display_grid(grid)
# print("---------------")
# grid1=drop_disc(grid,1,"x")
# display_grid(grid1)
# grid2=drop_disc(grid1,1,"x")
# print("---------------")
# display_grid(grid2)
# grid3=drop_disc(grid2,4,"F")
# print("---------------")
# display_grid(grid3)
def right_connect(grid,i,j,disc):
    # print("-------------------cdcj")
    # print(i,j)
    if j+1<len(grid[0]) and j+2<len(grid[0]) and j+3<len(grid[0]):
        if grid[i][j]==disc and grid[i][j+1]==disc  and grid[i][j+2]==disc and grid[i][j+3]==disc :
            print(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3])
            print("yes")
            return True
        else:
            return False
    else:
        return False
def vertical_connect(grid,disc):
    for i in range(len(grid)-3):
        for j in range(len(grid[i])):
            if grid[i][j]==disc and grid[i+1][j]==disc and grid[i+2][j]==disc and grid[i+3][j]==disc:
                return True
    return False

def diagonal_connect(grid,i,j,disc):
    if i+3<len(grid) and j-3>=0:
        if grid[i][j]==disc and grid[i+1][j-1]==disc and grid[i+2][j-2]==disc and grid[i+3][j-3]==disc:
            return True
    if i+3<len(grid) and j+3<len(grid[0]):
        if grid[i][j]==disc and grid[i+1][j+1]==disc and grid[i+2][j+2]==disc and grid[i+3][j+3]==disc:
            return True
        
    return False
    


def checkwin(grid,disc):
    for i in range(len(grid)):
        # print(len(grid),"len grid")
        for j in range(len(grid[i])):
            # print(len(grid[i]),"grid[i]")
            if right_connect(grid,i,j,disc):
                # print(i,j,"i,,j")
                return True
            elif diagonal_connect(grid,i,j,disc):
                return True
    if vertical_connect(grid,disc):
        return True  
    
    return False   

def draw(grid):
    for i in grid:
        for j in i:
            if j=="_":
                return False
    return True

def main():
    print('welcome to the connect four game')
    grid=generate_grid(6,7)
    current_player=0
    desk=["x","y"]
    
    while True:
        print("connect your desk as straight four in any direction to win the game")
        display_grid(grid)
        print(f"player{current_player+1}'s turn: ")
        col=get_user_input()
        disc=desk[current_player]
        grid=drop_disc(grid,col,disc)
        if checkwin(grid,disc):
            display_grid(grid)
            print(f"the player{current_player+1} is winner")
            break
        if draw(grid):
            print("DRAW")
            break
        else:
            current_player=1-current_player  
main()