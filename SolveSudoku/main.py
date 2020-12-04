grid = [
    [5,0,8,0,0,7,9,0,0],
    [0,4,0,0,0,0,6,0,0],
    [0,0,0,8,0,3,2,4,0],
    [6,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,2,0],
    [0,0,9,0,7,0,0,0,0],
    [0,2,0,0,0,0,0,5,4],
    [0,5,0,4,0,9,0,0,0],
    [4,0,0,0,0,0,0,1,0]
]

def solve(sdk):
    
    find = find_blank(sdk)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid_grid(sdk, i, (row, col)):
            sdk[row][col] = i

            if solve(sdk):
                return True

            sdk[row][col] = 0
    return False


#identifies if board is valid prior to solving

def valid_grid(sdk, num, pos):
    for i in range(len(sdk[0])):
        if sdk[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(sdk)):
        if sdk[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if sdk[i][j] == num and (i, j) != pos:
                    return False
    return True            



def print_grid(sdk):

#prints readable sudoku grid instead of list

    for i in range(len(sdk)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
    
        for j in range(len(sdk[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sdk[i][j])
            else:
                print(str(sdk[i][j]) + " ", end="")


#identifies black spaces

def find_blank(sdk):
    for i in range(len(sdk)):
        for j in range(len(sdk[0])):
            if sdk[i][j] == 0:
                return (i, j)

    return None

print_grid(grid)
solve(grid)
print('=============================')
print_grid(grid)