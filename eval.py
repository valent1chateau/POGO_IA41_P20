import numpy as np

def evalboard(board,n):
    eval=0
    nbTabs=0
    a,b=np.shape(board)
    for i in range b:
        for j in range a:
            if board[i][j][0]==n:
                eval+=1
            else:
                eval-=1
        nbTabs+=1
    if eval == nbTabs:
        eval= float("inf")
    elif -eval == nbTabs:
        eval=float("-inf")
    
    return eval