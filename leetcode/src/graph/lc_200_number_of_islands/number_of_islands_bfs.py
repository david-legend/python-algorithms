from collections import deque

def number_of_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                island_count += 1
                bfs(r, c, grid, visited)
    return island_count

def bfs(row, col, grid, visited):
    visited.add((row, col))
    queue = deque([(row, col)])
    row_length, col_length = len(grid), len(grid[0])
    while queue:
        r, c = queue.popleft()
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        
        for dr, dc in directions:
            row_pos = r + dr
            col_pos = c + dc
            if 0 <= row_pos < row_length and 0 <= col_pos < col_length and \
                      grid[row_pos][col_pos] == '1' and (row_pos, col_pos) not in visited:
                    queue.append((row_pos, col_pos))
                    visited.add((row_pos, col_pos))



grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(number_of_islands(grid1)) #1
print(number_of_islands(grid2)) #3