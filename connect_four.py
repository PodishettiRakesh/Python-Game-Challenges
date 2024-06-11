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