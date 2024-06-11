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