from collections import defaultdict

def solveSudoku(board):
    BOARD_SIZE = 9
    rows = defaultdict(set)
    cols = defaultdict(set)
    box = defaultdict(set)
    unfilled = []
    
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            val = board[r][c]
            if val != '.':
                rows[r].add(val)
                cols[c].add(val)
                box[(r//3, c//3)].add(val)
            else:
                unfilled.append((r,c))
    
    def dfs():
        if len(unfilled) == 0:
            return True
        
        r, c = unfilled[-1]
        box_idx = (r // 3, c//3)
        
        for i in range(1, BOARD_SIZE+1):
            val = str(i)
            if val in rows[r] or val in cols[c] or val in box[box_idx]:
                continue
            
            rows[r].add(val)
            cols[c].add(val)
            box[box_idx].add(val)
            board[r][c] = val
            unfilled.pop()
            
            if dfs():
                return True
            
            rows[r].remove(val)
            cols[c].remove(val)
            box[box_idx].remove(val)
            board[r][c] = '.'
            unfilled.append((r,c))
        
        return False
    
    dfs()



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)

print(board)