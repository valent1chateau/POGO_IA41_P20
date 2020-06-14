# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Hadrien, Valentin, Stéphane
"""

import copy
import math
from eval import *
from getplays import *


def minimax(depth, player_id,maximizing_player, board, alpha, beta):
    """
    minmax algorithm

    Parameters
    ----------
    depth : current depth
    player_id : player id (0 or 1)
    maximizing_player : true or false
    board : current board of the node
    alpha : local maximum
    beta : local minimum

    Returns
    -------
    the best evaluation

    """
    #exit condition 1: arrived at leaf node
    if(depth == 3): # maximum depth before computer takes too long
        return evalboard(board,player_id)
  
    #exit condition 2: evaluation says game is over
    if(evalboard(board,player_id) == float("inf") or evalboard(board,player_id)== float("-inf") ):
        return evalboard(board,player_id)
  
  
    best = 0
    #MAXIMISATION
    if(maximizing_player):
        plays = get_plays(player_id,board)
        best = -10000
        for play in plays:
            value= minimax(depth+1,player_id,not(maximizing_player),play,alpha,beta)
            if value>best:
                best = value
            if best>=alpha:
                alpha = best
            if alpha>= beta:
                break
    #MINIMISATION
    else:
      plays = get_plays(1-player_id,board)
      best = 10000
      for play in plays:
          value= minimax(depth+1,player_id,not(maximizing_player),play,alpha,beta)
          if value<best:
              best = value
          if best<=beta:
              beta = best
          if alpha>= beta:
              break
    return best
