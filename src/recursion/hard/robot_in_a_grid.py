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

    isAtOrigin = (row == 0) and (col == 0)
    
    if(isAtOrigin or getPath(grid, row, col-1, path)) or getPath(grid, row-1, col, path):
        point = row,col
        path.append(point)

        return True

    return False

print(callGetPath(3,3)) #[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
print(callGetPath(2,2)) #[(0, 0), (1, 0), (1, 1)]
print(callGetPath(4,3)) #[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]



# Solution With Memoization

def callGetPathMemo(rows, cols):
    assert rows and cols > 0
    grid = [[False for i in range(cols)] for j in range(rows)]
    path = [];
    failedPoints =  set()

    if(getPathMemo(grid, len(grid)-1, len(grid[0])-1, path, failedPoints)):
        return path

    return None


def getPathMemo(grid, row, col, path, failedPoints):
    if( row < 0 or col < 0 or (grid[row][col] == True)):
        return False

    p = row, col

    if p in failedPoints:
        return False

    isAtOrigin = (row == 0) and (col == 0)
    
    if(isAtOrigin or getPathMemo(grid, row, col-1, path, failedPoints)) or getPathMemo(grid, row-1, col, path, failedPoints):
        point = row,col
        path.append(point)

        return True

    failedPoints.add(p) #Cache results
    return False



print("\n\nRunning with Memoization \n\n")
print(callGetPathMemo(4,4)) #[(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
print(callGetPathMemo(3,8)) #[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]