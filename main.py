import copy
import math
import minimax
import eval

global Board

def evalBoard(board,joueur): #var joueur entre 0 et 1
  eval = 0
  nbTas = 0
  # LOOP SUR BOARD: #
  # +1 pour chaque Tas avec "var joueur" en derniere position#
  # -1 pour chaque Tas avec "var nonjoueur en derniere position#
  # +inf si eval = nbTas && eval>0 #
  # -inf si |eval| = nbTas && eval<0 #

  # positive infinity
  p_inf = float("inf")
  # negative infinity
  n_inf = float("-inf")

  math.isinf(float("-inf")) #OUTPUT:True
  math.isinf(float("inf"))  #OUTPUT:True

  return eval

def coupPossible(board):
  # EXEMPLE UTILISATION #
  Board_Copy = copy.deepcopy(board)
  Board_Copy[0][0] = [0,0]
  Board_Copy2 = copy.deepcopy(board)
  listCoups = []
  listCoups.append(Board_Copy)
  listCoups.append(Board_Copy2)
  print(listCoups)
  print(listCoups[0])
  print(listCoups[1])
  return listCoups

def best_move(player):
  #plays[] = get_plays(board,player)
  # best = -100000
  # best_board =[]
  #for i in (0,plays.length,1)
  # val = minmax(0,player,false,plays[i],float("-inf"),float("+inf"))
  # if best<val:
  # best = val
  # best_board = plays[i]
  print("best move")
  #global_board = best_board

#PC vs PC game
def pc_v_pc():
    print("pc v pc")
    global Board
    pc1 = false
    pc2 = true
    curr_player = 0
    #while(!math.isinf(eval(board,curr_player))):
    # plays = get_plays(Board, curr_player)
    # for play in plays
    # minimax(play,...)
    # curr_player = !curr_player

def player_move(id):
    print("id")
        
#PLAYER vs PC game
def pl_v_pc():
    print("pl v pc")
    

def main():
   # INIT PLATEAU DEBUT#
  global Board
  Board = [[0 for x in range(3)] for y in range(3)] 


   # LANCE LE MENU CONSOLE#
  while(1):
      playing = input("Voulez vous jouer ? (O/N)  ")
      if(playing != "O"):
          print("Arret du jeu")
          return
      else:
          for j in range(3):
              Board[0][j] = [1,1]
              Board[1][j] = []
              Board[2][j] = [0,0]
          print("Choisir une option")
          print("1 -> Joueur vs PC")
          print("2 -> PC vs PC")
          print("3 -> Quitter")
          mode = input("-> ")
          if(mode == "1"):
              print("Lancement: Joueur vs PC")
          elif (mode== "2"):
              print("Lancement: PC vs PC")
          else:
              return
     
  
  # /!\ CREATION DE COPY DE PLATEAU #
  #Board_Copy = copy.deepcopy(Board)
  #Board_Copy[0][0] = [0,0]
  #Board_Copy[0][0].append(1) # fonction de array utilisable
  #print(Board_Copy)
  #print(Board)

  #coupPossible(Board)

if __name__ == "__main__":
    main()
