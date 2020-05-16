# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:01:17 2020

@author: vlt
"""

import minimax
#import main
import copy

global Board

def finPile(pile):
    return pile[len(pile)-1]

def move(pileOrigine,pileCible,nbPions):
    if(nbPions == 1):
        pileCible.append(pileOrigine[len(pileOrigine)-1])
        pileOrigine.pop()
    elif (nbPions == 2):
        for i in range(len(pileOrigine)-1,1,-1):
            pileCible.append(pileOrigine[i])
        for i in range(2):
            pileOrigine.pop()
    else: #nbPions == 3
        for i in range(len(pileOrigine)-1,0,-1):
            pileCible.append(pileOrigine[i])
        for i in range (3):
            pileOrigine.pop()
    return 0

def get_plays(Board, player):
    plays = []
    play = copy.deepcopy(Board)
    for i in range(3) :
        for j in range(3):
            if(finPile(Board[i][j],i) == player):
                if(i != 0):
                    move(play[i][j],play[i-1][j],1)
                    plays.append(play)
                    play = copy.deepcopy(Board)
                if(i != 2):
                    move(play[i][j],play[i+1][j],1)
                    plays.append(play) 
                    play = copy.deepcopy(Board)
                if(j != 0):
                    move(play[i][j],play[i][j-1],1)
                    plays.append(play)
                    play = copy.deepcopy(Board)
                if(j != 2):
                    move(play[i][j],play[i][j+1],1)
                    plays.append(play)
                    play = copy.deepcopy(Board)
    return plays

                        
                

Board = [[[] for i in range (3)] for j in range(3)]
Board[0][1] = [0,0,1,0]
print(Board[0],'\n')
move(Board[0][1],Board[0][2],3)
print(Board[0])