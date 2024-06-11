def generate_grid(row,col):
    grid=[]
    for i in range(row):
        rows=[]
        for j in range(col):
            rows.append("_")
        
        grid.append(rows)
    return grid
# print(generate_grid(6,7))

