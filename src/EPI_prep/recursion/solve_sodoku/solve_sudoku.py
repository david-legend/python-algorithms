from itertools import product
class Solution(object):

    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.search(board)
    
    def search(self, board):
        if self.is_valid_state(board):
            return True # found solution
        
        # find the next empty spot and take a guess
        for row_idx, row in enumerate(board):
            for col_idx, elm in enumerate(row):
                if elm == self.EMPTY:
                    # find candidates to construct the next state
                    for candidate in self.get_candidates(board, row_idx, col_idx):
                        board[row_idx][col_idx] = candidate
                        # recurse on the modified board
                        is_solved = self.search(board)
                        if is_solved:
                            return True
                        else:
                            # undo the wrong guess and start anew
                            board[row_idx][col_idx] = self.EMPTY
                    # exhausted all candidates
                    # but none solves the problem
                    return False
        # no empty spot
        return True
                            
    def is_valid_state(self, board):
        # check if it is a valid solution
        # validate all the rows
        for row in self.get_rows(board):
            if not set(row) == self.DIGITS:
                return False
        # validate columns
        for col in self.get_cols(board):
            if not set(col) == self.DIGITS:
                return False
        # validate sub-boxes
        for grid in self.get_grids(board):
            if not set(grid) == self.DIGITS:
                return False
        return True

    def get_candidates(self, board, row, col):
        used_digits = set()
        # remove digits used by the same row
        used_digits.update(self.get_kth_row(board, row))
        # remove digits used by the same column
        used_digits.update(self.get_kth_col(board, col))
        # remove digits used by the 3x3 sub-box
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= set([self.EMPTY])
        candidates = self.DIGITS - used_digits
        return candidates

    
    # helper functions for retrieving rows, cols, and grids
    def get_kth_row(self, board, k):
        return board[k]

    def get_rows(self, board):
        for i in range(self.SHAPE):
            yield board[i]
    
    def get_kth_col(self, board, k):
        return [
            board[row][k] for row in range(self.SHAPE)
        ]

    def get_cols(self, board):
        for col in range(self.SHAPE):
            ret = [
                    board[row][col] for row in range(self.SHAPE)
            ]
            yield ret

    def get_grid_at_row_col(self, board, row, col):
        row = row // self.GRID * self.GRID
        col = col // self.GRID * self.GRID
        return [
            board[r][c] for r, c in 
            product(range(row, row + self.GRID), range(col, col + self.GRID))
        ]

    def get_grids(self, board):
        for row in range(0, self.SHAPE, self.GRID):
            for col in range(0, self.SHAPE, self.GRID):
                grid = [
                    board[r][c] for r, c in 
                    product(range(row, row + self.GRID), range(col, col + self.GRID))
                ]
                yield grid

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
solution.solveSudoku(board)

print(board)
# Expected Output
[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]