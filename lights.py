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