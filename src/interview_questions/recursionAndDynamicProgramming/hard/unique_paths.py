# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


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