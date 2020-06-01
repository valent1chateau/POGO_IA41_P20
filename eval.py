# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Hadrien, Valentin, Stéphane
"""
def evalboard(board,n):
    # NOMBRE DE TAS
    # NOMBRE DE TAS DU JOUEUR
    # NOMBRE DE TAS DU JOUEUR ADVERSE
    # NOMBRE DE PIONS ADVERSE SOUS LES TAS DU JOUEUR
    
    ev=0
    nbSous=0
    nbTas=0
    for i in range(3):
        for j in range(3):
            l=len(board[i][j])-1
            if l>=0:    
                if board[i][j][l]==n:
                    ev+=1
                    for k in range(l-1):
                        if(board[i][j][k]!=n):
                            nbSous+=1
                else:
                    for k in range(l-1):
                        if(board[i][j][k]==n):
                            nbSous-=1
                nbTas +=1
                
    if ev/nbTas == 1:
        ev= float("inf")
        return ev
    elif ev/nbTas == 0:
        ev=float("-inf")
        return ev
    
    return nbSous
