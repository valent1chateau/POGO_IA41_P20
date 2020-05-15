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
    pileInter = []
    if(nbPions == 1):
        pileCible.append(pileOrigine[len(pileOrigine)-1])
        pileOrigine.pop()
    elif (nbPions == 2):
        pileCible.append(pileOrigine[len(pileOrigine)-1])
        pileInter.append(pileOrigine[len(pileOrigine)-2])
        for i in range(2):
            pileOrigine.pop()
        pileCible.extend(pileInter)
    else:
        pileCible.append(pileOrigine[len(pileOrigine)-1])
        pileInter.append(pileOrigine[len(pileOrigine)-2])
        pileInter.append(pileOrigine[len(pileOrigine)-3])
        for i in range (3):
            pileOrigine.pop()
        pileCible.extend(pileInter)
    return 0

def get_plays(Board, player):
    plays = []
    play = copy.deepcopy(Board)
    for i in range(3) :
        for j in range(3):
            if(finPile(Board[i][j],i) == player):
                

                        
                

Board = [[[] for i in range (3)] for j in range(3)]
Board[0][1] = [0,0,1,0]
print(Board[0],'\n')
move(Board[0][1],Board[0][2],3)
print(Board[0])
