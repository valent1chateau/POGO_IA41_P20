import copy
import math
from minimax import *
import numpy as np
from eval import *
from getplays import *
from gui import *
global Board

def print_board(board):

    lens = [[len(x) for x in y]for y in board]
    max = np.amax(lens)
    char = 0
    
    print("  ",end='')
    t = (max+max-1+2)*3
    cpt = 0
    for i in range(t):
        if i == int(t/6) or i == int(3*t/6) or i == int(5*t/6):
            print(cpt,end='')
            cpt+=1  
        else:
            print(" ",end='')
    print()
    
    for i in range(3):
        print(str(char)+" ",end='')
        char+=1
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
  global Board
  plays = get_plays(player,Board)
  best = float("-inf")
  best_board =[]
  for i in range(len(plays)):
      val = minimax(0,player,0,plays[i],float("-inf"),float("+inf"))
      #print(val)
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
    
def player_move(id):
    global Board
    plays = get_plays(id,Board)
    print("Quelle pile vous voulez changer")
    ligne_s = int(input("Ligne-> "))
    col_s = int(input("Colonne-> "))
    nbPions = int(input("Nombre de Pions que vous voulez deplacer-> "))
    print("Ou vous voulez mettre ceci?")
    ligne_d = int(input("Ligne destination-> "))
    col_d = int(input("Colonne destination-> "))
    
    
    play = copy.deepcopy(Board)
    try:
        move(play[ligne_s][col_s],play[ligne_d][col_d],ligne_s,col_s,nbPions)
    except:
        print("mauvaises valeurs")
        
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
            Board = best_move(curr_player)
            print_board(Board)
        
        if(evalboard(Board,curr_player) == float("inf") or evalboard(Board,curr_player)== float("-inf")):
            print("player:",end='')
            print(curr_player,end='')
            print(" won!",end='')
            break;
        curr_player= 1-curr_player

def main():
    
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