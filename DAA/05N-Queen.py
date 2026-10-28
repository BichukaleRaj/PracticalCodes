import time 
 
def is_safe(board, row, col, n): 
    # Check column 
    for i in range(row): 
        if board[i][col] == 1: 
            return False 
 
    # Check upper-left diagonal 
    i, j = row - 1, col - 1 
    while i >= 0 and j >= 0: 
        if board[i][j] == 1: 
            return False 
        i -= 1 
        j -= 1 
 
    # Check upper-right diagonal 
    i, j = row - 1, col + 1 
    while i >= 0 and j < n: 
        if board[i][j] == 1: 
            return False 
        i -= 1 
        j += 1 
 
    return True 
 
 
def solve(board, row, n): 
    if row == n: 
        return True 
 
    for col in range(n): 
        if is_safe(board, row, col, n): 
            board[row][col] = 1 
 
            if solve(board, row + 1, n): 
                return True 
 
            board[row][col] = 0 
 
    return False 
 
 
n = int(input("Enter N (4 to 20): ")) 
 
if n < 4 or n > 20: 
    print("Enter N between 4 and 20") 
else: 
    board = [[0] * n for i in range(n)] 
 
    # Place first queen at row 1, column 1 
    board[0][0] = 1 
 
    start = time.perf_counter() 
    solved = solve(board, 1, n) 
    end = time.perf_counter() 
 
    print("N-Queens execution time:", end - start, "seconds") 
 
    if solved: 
        print("N-Queens Solution:") 
        for row in board: 
            print(*row) 
    else: 
        print("No solution with first queen at (1, 1)")