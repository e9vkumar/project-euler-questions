import pandas as pd


def min_path_sum(inp):
    grid = [[0]*80 for i in range(80)]
    sum = 0
    for i in range(79,-1,-1):
        sum += inp[79][i]
        grid[79][i] = sum
    
    sum = 0
    for j in range(79,-1,-1):
        sum += inp[j][79]
        # print(sum,inp[j][4])
        grid[j][79] = sum
    
    for i in range(78,-1,-1):
        for j in range(78,-1,-1):
            grid[i][j] = min(grid[i+1][j],grid[i][j+1]) + inp[i][j]

    return grid[0][0]

# inp = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

with open('data/matrix.txt','r') as inp:
    inp = inp.readlines()
    inp = [[int(ele) for ele in lst.split(',')] for lst in inp]
    print(min_path_sum(inp))
