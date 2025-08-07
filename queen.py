N = 8  # Size of the chessboard (8x8)

def printSolution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def isSafe(board, row, col):
    # Check this row on the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solveNQueensUtil(board, col):
    # Step 2: If all queens are placed
    if col >= N:
        return True

    # Step 3: Try all rows in the current column
    for row in range(N):
        if isSafe(board, row, col):
            # Step 3a: Place queen
            board[row][col] = 1

            # Step 3b: Recur to place rest
            if solveNQueensUtil(board, col + 1):
                return True

            # Step 3c: Backtrack
            board[row][col] = 0

    # Step 4: If queen can't be placed in any row in this column
    return False

def solveNQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQueensUtil(board, 0):
        print("Solution does not exist.")
        return

    print("One of the solutions to the 8 Queens problem:")
    printSolution(board)

# Run the program
solveNQueens()