def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Add the current board configuration to solutions
        solutions.append(["".join("Q" if cell else "." for cell in r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 1
            # Recur to the next row
            solve_n_queens_util(board, row + 1, n, solutions)
            # Backtrack
            board[row][col] = 0
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for _ in range(n)]
        solutions = []
        solve_n_queens_util(board, 0, n, solutions)
        return solutions

