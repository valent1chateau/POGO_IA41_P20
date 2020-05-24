# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:01:17 2020

@author: vlt
"""

#import minimax
import copy
from main import print_board
global Board

def finPile(pile):
    if not (pile):
        return False
    else:
        if (len(pile)==0):
            return pile[0]
        else:
            return pile[len(pile)-1]

def move(pileOrigine,pileCible,a,b,nbPions):
    if not (pileOrigine):
        print("source is empty")
    elif (pileOrigine):
        if(nbPions == 1):
            if(len(pileOrigine) == 0):
                pileCible.append(Board[a][b])
                pileOrigine.pop()    
            else:
                pileCible.append(pileOrigine[len(pileOrigine)-1])
                pileOrigine.pop()
        elif(nbPions == 2):
            for i in range(len(pileOrigine)-1,len(pileOrigine)-3,-1):
                pileCible.append(pileOrigine[i])
            for i in range(len(pileOrigine)-1,len(pileOrigine)-3,-1):
                pileOrigine.pop()
        elif(nbPions == 3):
            for i in range(len(pileOrigine)-1,len(pileOrigine)-4,-1):
                pileCible.append(pileOrigine[i])
            for i in range (len(pileOrigine)-1,len(pileOrigine)-4,-1):
                pileOrigine.pop()
    return 0

def get_plays(player):
    plays = []
    play = copy.deepcopy(Board)
    for i in range(3):
        for j in range(3):
            if(finPile(Board[i][j]) == player):
                for n in range(1,3,1):
                    if(i != 0):
                        move(play[i][j],play[i-1][j],i,j,n)
                        plays.append(play)
                        play = copy.deepcopy(Board)
                    if(i != 2):
                        move(play[i][j],play[i+1][j],i,j,n)
                        plays.append(play) 
                        play = copy.deepcopy(Board)
                    if(j != 0):
                        move(play[i][j],play[i][j-1],i,j,n)
                        plays.append(play)
                        play = copy.deepcopy(Board)
                    if(j != 2):
                        move(play[i][j],play[i][j+1],i,j,n)
                        plays.append(play)
                        play = copy.deepcopy(Board)
    return plays


Board = [[[] for i in range (3)] for j in range(3)]
for j in range(3):
    Board[0][j] = [1,1]
    Board[1][j] = []
    Board[2][j] = [0,0]
"""
print("Joueur 0 :\n")
j0 = get_plays(0)
for i in range (0,len(j0)-1):
    print_board(j0[i])
    print("\n")
    
"""   
print("Joueur 1 :\n")
j1 = get_plays(1)
for i in range (0,len(j1)-1):
    print_board(j1[i])
    print("\n")

#print("Taille J0 :",len(j0),"\nTaille J1 :",len(j1))

print("Taille J1 :",len(j1))