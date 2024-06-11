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
            if col_num>7 or col_num<1:
                print("col position out of grid")
            else:
                return col_num
        except ValueError:
            print("Error in selecting column to drop disc! try again")
# print(get_user_input())