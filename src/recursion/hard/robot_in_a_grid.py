#Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
#The robot can only move in two directions, right and down, but certain cells are "off limits" 
#such that the robot cannot step on them. Design an algorithm to find a path for the 
#robot from the top left to the bottom right.

def uniquePaths(r, c):
    matrix = [[0 for y in range(c)] for x in range(r)]

    for i in range(r):
        matrix[i][0] = 1
    
    for i in range(c):
        matrix[0][i] = 1

    for i in range(1, r):
        for j in range(1,c):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] 

    print(matrix)
    return matrix[r-1][c-1];
    



print(uniquePaths(3,7)) #28
print(uniquePaths(3,2)) #3
print(uniquePaths(7,3)) #28
print(uniquePaths(3,3)) #6