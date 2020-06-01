import copy
import math
from eval import *
from getplays import *

#choix de depth = 3 a faire choisir plus tard
def minimax(depth, player_id,maximizing_player, board, alpha, beta):
  #condition de sortie 1: arrivé a une feuille
  if(depth == 3):
    #print("profondeur max atteinte")
    #print(evalboard(board,player_id))
    return evalboard(board,player_id)
  
  #conditions de sortie 2: partie terminé
  if(evalboard(board,player_id) == float("inf") or evalboard(board,player_id)== float("-inf") ):
      #print(evalboard(board,player_id))
      return evalboard(board,player_id)
  
  
  
  
  best = 0
  if(maximizing_player):
    plays = get_plays(player_id,board)
    #print("maximise")
    best = -10000
    for play in plays:
        value= minimax(depth+1,player_id,not(maximizing_player),play,alpha,beta)
        if value>best:
            best = value
        if best>=alpha:
            alpha = best
        if alpha>= beta:
            break
  
  else:
    plays = get_plays(1-player_id,board)
    #print("minimise")
    best = 10000
    for play in plays:
        value= minimax(depth+1,player_id,not(maximizing_player),play,alpha,beta)
        if value<best:
            best = value
        if best<=beta:
            beta = best
        if alpha>= beta:
            break
  #print(best)
  return best


# Board = [[[] for i in range (3)] for j in range(3)]
# for j in range(3):
#     Board[0][j] = [1,1]
#     Board[1][j] = []
#     Board[2][j] = [0,0]

# #print(len(Board[1][1]))
# #print(not(Board[1][1])) 
# best = minimax(0,0,0,Board,float("-inf"),float("+inf"))
# print(best)