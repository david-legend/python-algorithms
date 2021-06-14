#Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
#The robot can only move in two directions, right and down, but certain cells are "off limits" 
#such that the robot cannot step on them. Design an algorithm to find a path for the 
#robot from the top left to the bottom right.

def callGetPath(rows, cols):
    assert rows and cols > 0
    grid = [[False for i in range(cols)] for j in range(rows)]
    path = [];

    if( getPath(grid, len(grid)-1, len(grid[0])-1, path) ):
        return path

    return None
   


def getPath(grid, row, col, path):
    if( row < 0 or col < 0 or (grid[row][col] == True)):
        return False

    print("row: ", row, " col: ", col, "\n")
    isAtOrigin = (row == 0) and (col == 0)
    
    if(isAtOrigin or getPath(grid, row, col-1, path)) or getPath(grid, row-1, col, path):
        point = row,col
        path.append(point)

        return True

    return False

print(callGetPath(3,3)) #[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
print(callGetPath(2,2)) #[(0, 0), (1, 0), (1, 1)]
print(callGetPath(4,3)) #[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]




# TODO:: Add robot in a grid with memoization