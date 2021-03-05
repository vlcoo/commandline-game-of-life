import time, sys, random

try:
    RES = int(sys.argv[1])
except:
    RES = 5

SPEED = 0.3
iteration = 0


def zero_grid():
    grid = [[0 for i in range(RES)] for i in range(RES)]
    return grid


def rand_grid():
    grid = [[random.choice([0, 1]) for i in range(RES)] for i in range(RES)]
    return grid


def input_grid():
    print("Type in cells (0 for dead, 1 for alive), pressing [ENTER] after each row. Leaving cell or row empty means it'll be 0. Grid size is {r} by {r}.".format(r = RES))
    grid = zero_grid()
    for i in range(RES):
        row = [int(char) for char in input("."*RES + "\r")]
        for j in range(len(row)):
            if row[j] == 1: grid[i][j] = 1
    return grid


def print_grid(grid, i):
    print(" Iteration {}".format(i))
    for row in grid:
        print("|", end="")
        for val in row:
            print("()" if bool(val) else "  ", end="")
        print("|")
    print("|" + "__"*RES + "|", end="\n\n")


def calc_neighbourhood(grid, pos_i, pos_j):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if grid[pos_i + i][pos_j + j] == 1: sum += 1
            except:
                continue
    if grid[pos_i][pos_j] == 1: sum -= 1
    return sum
    

def next_iteration(grid):
    global iteration
    next_grid = []
    for row in grid:
        next_row = []
        for val in row:
            next_row.append(val)
        next_grid.append(next_row)
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            n = calc_neighbourhood(grid, i, j)
            if value == 1:
                if n < 2 or n > 3:
                    next_grid[i][j] = 0
            elif value == 0:
                if n == 3:
                    next_grid[i][j] = 1
    iteration += 1
    return next_grid


try:
    if sys.argv[2] == "random":
        grid = rand_grid()
except:
    grid = input_grid()

while 1:
    print_grid(grid, iteration)
    grid = next_iteration(grid)
    time.sleep(SPEED)
