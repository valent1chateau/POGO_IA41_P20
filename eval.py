# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Hadrien, Valentin, Stéphane
"""
def evalboard(board,n):
    """
    Evaluates the board for player n. Higher the evaluation the better the board is for the player

    Parameters
    ----------
    board : 3D array representing the board
    n : player id (0 or 1)

    Returns
    -------
    INT
        evaluation

    """
    
    ev=0
    nbUnder=0
    nbStack=0
    for i in range(3):
        for j in range(3):
            l=len(board[i][j])-1
            if l>=0:    
                if board[i][j][l]==n:
                    ev+=1
                    for k in range(l-1):#counts the number of enemi pieces under player stack
                        if(board[i][j][k]!=n):
                            nbUnder+=1
                else:
                    for k in range(l-1):#counts the number of player pieces under enemi stack
                        if(board[i][j][k]==n):
                            nbUnder-=1
                nbStack +=1
                
    if ev/nbStack == 1:
        ev= float("inf")
        return ev
    elif ev/nbStack == 0:
        ev=float("-inf")
        return ev
    
    return nbUnder
