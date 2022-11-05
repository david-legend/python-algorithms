# Time O(V+E) 
def search_maze(maze, start, dest):
    WHITE, BLACK = range(2)
    def search_maze_helper(curr):
        nonlocal path
        row, col = curr

        if not (0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == WHITE):
            return False
        
        path.append(curr)
        maze[row][col] = BLACK
        if curr == dest:
            return True
        
        result = search_maze_helper([row - 1, col]) or search_maze_helper([row + 1, col]) \
            or search_maze_helper([row, col + 1]) or search_maze_helper([row, col - 1])  
        if result:
            return True

        del path[-1]
        return False
    path = []
    search_maze_helper(start)
    return path





# print(search_maze(
#     [
#         [0,1,0],
#         [1,1,0],
#         [0,0,0],
#     ],
#     [2,0],
#     [0,2]
# ))

# print(search_maze(
#     [
#         [0,1],
#         [0,0]
#     ],
#     [0,0],
#     [1,1]
# ))

print(search_maze(
    [
        [0,1,0],
        [0,1,0],
        [0,0,0],
    ],
    [2,0],
    [0,2]
))