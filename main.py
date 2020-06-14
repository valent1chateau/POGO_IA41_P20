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