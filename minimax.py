import copy
import math

#choix de depth = 3 a faire choisir plus tard
def minimax(depth, player_id,maximizing_player, board, alpha, beta):
  #condition de sortie 1: arrivé a une feuille
  if(depth == 3):
    print("profondeur max atteinte")
    #return eval(board,player)
  
  #conditions de sortie 2: partie terminé
  #if( eval(board,player)== +inf || eval(board,player)== -inf ):

  #plays[] = get_plays(board,!player)
  best = 0
  if(maximizing_player):
    print("maximise")
    best = -10000
    #for play in plays
    # value= minimax(depth+1,!maximizing_player,play,alpha,beta)
    # if value>best:
    # best = value
    # if best>=alpha:
    # alpha = best
    # if alpha>= beta:
    # break
  else:
    print("minimise")
    best = 10000
    #for play in plays
    # value= minimax(depth+1,!maximizing_player,play,alpha,beta)
    # if value<best:
    #  best = value
    # if best<=beta:
    #  beta = best
    # if alpha>= beta:
    #  break

  return best
