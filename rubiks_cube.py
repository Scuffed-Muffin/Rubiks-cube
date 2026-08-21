import numpy as np

cube = np.array([
    [["W","W","W"],["W","W","W"],["W","W","W"]],  # Top
    [["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]],  # Bottom
    [["R","R","R"],["R","R","R"],["R","R","R"]],  # Front
    [["O","O","O"],["O","O","O"],["O","O","O"]],  # Back
    [["G","G","G"],["G","G","G"],["G","G","G"]],  # Right
    [["B","B","B"],["B","B","B"],["B","B","B"]],  # Left
])

def rotate_row_right(num):
    cube1 = cube.copy()
    if num == 0 or num == 2:
        cube[num,0,0] = cube1[num,0,2]
        cube[num,0,1] = cube1[num,1,2]
        cube[num,0,2] = cube1[num,2,2]
        cube[num,1,0] = cube1[num,0,1]
        cube[num,1,2] = cube1[num,2,1]
        cube[num,2,0] = cube1[num,0,0]
        cube[num,2,1] = cube1[num,1,0]
        cube[num,2,2] = cube1[num,2,0]
    for i in range(3):
        cube[2,num,i] = cube1[4,num,i]
        cube[5,num,i] = cube1[2,num,i]
        cube[3,num,i] = cube1[5,num,i]
        cube[4,num,i] = cube1[3,num,i]

    return(cube)
def rotate_row_left(num):
    cube1 = cube.copy()
    if num == 0 or num == 2:
        cube[num,0,2] = cube1[num,0,0]
        cube[num,1,2] = cube1[num,0,1]
        cube[num,2,2] = cube1[num,0,2]
        cube[num,0,1] = cube1[num,1,0]
        cube[num,2,1] = cube1[num,1,2]
        cube[num,0,0] = cube1[num,2,0]
        cube[num,1,0] = cube1[num,2,1]
        cube[num,2,0] = cube1[num,2,2]
    for i in range(3):
        cube[4,num,i] = cube1[2,num,i]
        cube[2,num,i] = cube1[5,num,i]
        cube[5,num,i] = cube1[3,num,i]
        cube[3,num,i] = cube1[4,num,i]

def rotate_column_down(num):
