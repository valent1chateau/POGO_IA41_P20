import copy
import math
import minimax
import numpy as np
import eval
import getplays



global Board


#math.isinf(float("-inf")) #OUTPUT:True
#math.isinf(float("inf"))  #OUTPUT:True


def print_board(board):

    lens = [[len(x) for x in y]for y in board]
    max = np.amax(lens)
    char = "A"
    asc = ord(char[0])
    
    print("  ",end='')
    t = (max+max-1+2)*3
    cpt = 1
    for i in range(t):
        if i == int(t/6) or i == int(3*t/6) or i == int(5*t/6):
            print(cpt,end='')
            cpt+=1  
        else:
            print(" ",end='')
    print()
    
    for i in range(3):
        print(chr(asc+i)+" ",end='')
        for j in range (3):
            l = len(board[i][j])
            if l == 0:
                print("[",end='')
                for m in range(max-1):
                    print("  ",end='')
                print(" ]",end='')
            else :
                if l == max:       
                    for k in range(l):
                        if k == 0:
                            print("[",end='')
                        print(str(board[i][j][k]),end='')
                        if k==l-1:
                            print("]",end='')
                        else:
                            print(" ",end='')
                else:
                    for k in range(l):
                        if k == 0:
                            print("[",end='')
                        print(str(board[i][j][k])+" ",end='')
                    for n in range(0,max-l-1,1):
                        print("  ",end='')
                    print(" ]",end='')
        print("")
        
        
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
    pc1 = 0
    pc2 = 1
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
              print_board(Board)
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
