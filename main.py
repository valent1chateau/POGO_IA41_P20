# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Hadrien, Valentin, Stéphane
"""

import copy
import math
from minimax import *
import numpy as np
from eval import *
from getplays import *
from gui import *
global Board
import tkinter as tk
import tkinter.simpledialog as sd       
        
def best_move(player, board):
    """
    Does a maximisation of minmax to remember the board and starts the minmax algorithm 

    Parameters
    ----------
    player : player id
    board : 3D array representing the current board

    Returns
    -------
    best_board : returns the new board after making the best move

    """
    plays = get_plays(player, board)
    best = float("-inf")
    best_board =[]
    for i in range(len(plays)):
        val = minimax(0,player,0,plays[i],float("-inf"),float("+inf"))
        if best<=val:
            best = val
            best_board = plays[i]
    return best_board

#PC vs PC game
def pc_v_pc():
    global Board
    curr_player = 0
    print_board(Board)
    print("player 0 starts")
    print("")
    while(1):
        print("")
        print("Tour ",end='')
        print(curr_player)
        print("")
        Board = best_move(curr_player)
        print_board(Board)
        if(evalboard(Board,curr_player) == float("inf") or evalboard(Board,curr_player)== float("-inf")):
            print("player:",end='')
            print(curr_player,end='')
            print(" won!",end='')
            break;
        curr_player= 1-curr_player
        

    
def player_move(t,id, Board):
    plays = get_plays(id,Board)
    t.insert(tk.INSERT,"\n Quelle pile voulez-vous changer ?")
    ligne_s = getUserInt("Rentrez la ligne de la pile à déplacer :")
    col_s = getUserInt("Rentrez la colonne de la pile à déplacer :")
    nbPions = getUserInt("Rentrez le nombre de pions à déplacer :")
    ligne_d = getUserInt("Ligne destination :")
    col_d = getUserInt("Colonne destination :")
    
    play = copy.deepcopy(Board)
    try:
        move(play[ligne_s][col_s],play[ligne_d][col_d],ligne_s,col_s,nbPions)
    except:
        t.insert(tk.INSERT,"\n Mauvaises valeurs \n")
        
    is_in = 0
    for p in plays:
        cpt =0
        for i in range(3):
            for j in range(3):
                if(p[i][j]==play[i][j]):
                    cpt+=1  
        if(cpt==9):
            is_in=1
            break
        
    Board = play
    #print(is_in)
       
#PLAYER vs PC game
def pl_v_pc():
    global Board   
    print("Vous êtes le joueur 0")
    print_board(Board)
    curr_player = 1
    while(1):
        if(curr_player ==0):
            print("Tour 0")
            player_move(curr_player)
            print_board(Board)
        else:
            print("Tour 1")
            Board = best_move(curr_player, Board)
            print_board(Board)
        
        if(evalboard(Board,curr_player) == float("inf") or evalboard(Board,curr_player)== float("-inf")):
            print("player:",end='')
            print(curr_player,end='')
            print(" won!",end='')
            break;
        curr_player= 1-curr_player

        
def main():
    """
    Initialize the board

    Returns
    -------
    int
        success

    """
   # INIT PLATEAU DEBUT#
    global Board

    Board = [[[] for x in range(3)] for y in range(3)] 

    for j in range(3):
        Board[0][j] = [1,1]
        Board[1][j] = []
        Board[2][j] = [0,0]
    return 0

if __name__ == "__main__":
    main()
    start(Board)