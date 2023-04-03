def two_queens(board, tq, qpsf, ans):
    if tq == qpsf:
        print(ans)
        return
    
    for i in range(len(board)):
        if board[i]:
            board[i] = False
            two_queens(board, tq, qpsf+1, ans+f"A{i+1}")
            board[i] = True

board = [True]*8
two_queens(board, 2, 0, "")
'''
In this code, board is a list of boolean values representing the availability of each column on the chessboard. tq is the target number of queens to be placed (2 in this case), qpsf is the number of queens placed so far, and ans is the string representing the positions of the queens placed.

The two_queens function is a recursive function that tries to place two queens on the board. If the target number of queens has been reached, it prints the solution and returns. Otherwise, it loops through each available column, places a queen in that column, and recursively tries to place the remaining queens. When the recursive call returns, it removes the queen from the board to backtrack and try another position.

The board[4] line is unnecessary and has been removed from the code. The example usage at the end of the code creates a board with all columns available and calls the two_queens function with the board, the target number of queens, the number of queens placed so far, and an empty string representing the positions of the queens placed
'''