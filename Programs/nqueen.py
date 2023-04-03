def nqueen(board,tq,row):
    if(tq == 0):
        display(board)
        return
    for col in range(len(board)):
        if(isitsafe(board,row,col)):
            board[row][col] = True
            nqueen(board,tq-1,row+1)
            board[row][col] = False


def isitsafe(board,row,col):
    #UPPER SIDE
    r =row
    while(r > 0):
        if(board[r][col] == True):
            return False
        r= r-1
    #LEFT Diagonal
    r = row
    c =col
    while(c > 0):
        if(board[r][c] == True) :
            return False
        c=c-1
        r = r-1
    #RIGHT Diagonal
    r = row
    c = col
    while(r > 0 and c < len(board)):
        if(board[r][c] == True):
            return False
        r=r-1
        c= c+1
    return True
    
    
def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()        
tq = 4            
board = [[False for i in range(tq)] for j in range(tq)]
nqueen(board,tq,0)