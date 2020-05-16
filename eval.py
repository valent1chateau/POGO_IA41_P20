def evalboard(board,n):
    eval=0
    nbTas=0
    #a,b=np.shape(board)
    for i in range(3):
        for j in range(3):
            l=len(board[i][j]-1)
            if l!=0:    
                if board[i][j][l]==n:
                    eval+=1
                else:
                    eval-=1
                nbTas+=1
    if eval == nbTas:
        eval= float("inf")
    elif -eval == nbTas:
        eval=float("-inf")
    
    return eval