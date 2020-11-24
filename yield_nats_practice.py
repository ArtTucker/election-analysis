import numpy as np

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

def possible(y,x,n):
    global grid
    for i in range(0,9) :
        if grid[y][x] == 0:
            for n in range(1,10):
                if possible(y,x,n):
                    grid[y][x] = n
                    solve()
                    grid[y][x]
            return
    print(np.matrix(grid))
    input("More?")