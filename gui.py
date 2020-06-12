# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:22:06 2020
@author: vlt
"""
import tkinter as tk
from PIL import ImageTk,Image
import sys
import tkinter.simpledialog as sd
from main import *
from getplays import *
import time
global Board  

def start(board):
    global Board 
    Board = board
    root = tk.Tk() 
    root.title('Jeu du pogo')
    icon = tk.PhotoImage(file='dice.png')
    root.call('wm', 'iconphoto', root._w, icon)
    canvas = tk.Canvas(root, width=245, height=245)
    backgroundImage = ImageTk.PhotoImage(Image.open("pogo.png"))
    canvas.create_image(125,125, image = backgroundImage)
    
    playButton = tk.Button(root, text="Jouer", padx=10, command=lambda: [f() for f in [root.destroy(), game_window(root)]])
    play_button_window = canvas.create_window(75, 200, window=playButton,)
    
    quitButton = tk.Button(root, text="Quitter", padx=10, command=lambda: [f() for f in [root.destroy()]])
    quit_button_window = canvas.create_window(175, 200, window=quitButton)
    
    canvas.pack()
    root.mainloop()

def game_window(root):
    game = tk.Tk()
    game.title('Jeu du pogo')
    S = tk.Scrollbar(game)
    T = tk.Text(game, height=35, width=50)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    pogoGame(T, game)
    
    game.mainloop()
    
def getUserInput(msg):
    userInput = sd.askstring('User Input',msg)
    return userInput

def getUserInt(msg):
    userInput = sd.askinteger('User Input',msg)
    return userInput

def print_guiboard(text,board):
    lens = [[len(x) for x in y]for y in board]
    max = np.amax(lens)
    char = 0
    
    text.insert(tk.INSERT,"  ",tk.END)
    t = (max+max-1+2)*3
    cpt = 0
    for i in range(t):
        if i == int(t/6) or i == int(3*t/6) or i == int(5*t/6):
            text.insert(tk.INSERT,cpt,tk.END)
            cpt+=1  
        else:
            text.insert(tk.INSERT," ",tk.END)
    
    for i in range(3):
        text.insert(tk.INSERT,"\n ")
        text.insert(tk.INSERT,str(char)+" ",tk.END)
        char+=1
        for j in range (3):
            l = len(board[i][j])
            if l == 0:
                text.insert(tk.INSERT,"[",tk.END)
                for m in range(max-1):
                    text.insert(tk.INSERT,"  ",tk.END)
                text.insert(tk.INSERT," ]",tk.END)
            else :
                if l == max:       
                    for k in range(l):
                        if k == 0:
                            text.insert(tk.INSERT,"[",tk.END)
                        text.insert(tk.INSERT,str(board[i][j][k]),tk.END)
                        if k==l-1:
                            text.insert(tk.INSERT,"]",tk.END)
                        else:
                            text.insert(tk.INSERT," ",tk.END)
                else:
                    for k in range(l):
                        if k == 0:
                            text.insert(tk.INSERT,"[",tk.END)
                        text.insert(tk.INSERT,str(board[i][j][k])+" ",tk.END)
                    for n in range(0,max-l-1,1):
                        text.insert(tk.INSERT,"  ",tk.END)
                    text.insert(tk.INSERT," ]",tk.END)
        text.insert(tk.INSERT," ")
        text.insert(tk.INSERT,"\n")

       
def player_move_gui(id,t):
    global Board
    plays = get_plays(id,Board)
    t.insert(tk.INSERT,"Quelle pile voulez-vous changer ?")
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

def pl_pc_gui(t,game):
    global Board
    for j in range(3):
        Board[0][j] = [1,1]
        Board[1][j] = []
        Board[2][j] = [0,0]
        
    t.insert(tk.INSERT,"Vous êtes le joueur 0 \n")
    t.insert(tk.INSERT,"------------------------ \n")
    print_guiboard(t, Board)
    t.insert(tk.INSERT,"------------------------ \n")
    curr_player = 0
    i=0
    while(1):
        if(curr_player==0):
            t.insert(tk.INSERT, "Tour "+str(i)+" \n")
            player_move_gui(curr_player, t)
            print_guiboard(t,Board)
            t.insert(tk.INSERT,"------------------------ \n")
        else:
            t.insert(tk.INSERT, "Tour 1 \n")
            Board = best_move(curr_player, Board)
            print_guiboard(t,Board)
        
        if(evalboard(Board,curr_player) == float("inf") or evalboard(Board,curr_player) == float("-inf")):
           t.insert(tk.INSERT, "Player "+curr_player+" won !")
           break
        curr_player=1-curr_player
        i+=1
        
def pc_v_pc_gui(t):
    global Board
    for j in range(3):
        Board[0][j] = [1,1]
        Board[1][j] = []
        Board[2][j] = [0,0]
    curr_player = 0
    print_guiboard(t,Board)
    t.insert(tk.INSERT,"\n Player 0 starts \n")
    i=0
    while(1):
        t.insert(tk.INSERT,"\n Tour "+str(i)+" : \n \n")
        Board = best_move(curr_player,Board)
        print_guiboard(t,Board)
        t.insert(tk.INSERT,"------------------------ \n")
        if(evalboard(Board,curr_player) == float("inf") or evalboard(Board,curr_player)== float("-inf")):
            t.insert(tk.INSERT,"\n player "+(str(curr_player)+" won !"))
            break;
        curr_player= 1-curr_player
        i+=1

def pogoGame(t, game):
    t.insert(tk.INSERT, "Choisir une option \n 1 -> Joueur vs PC \n 2 -> PC vs PC \n 3 -> Quitter \n")
    
    input1 = getUserInt("Que choissisez-vous ?") 
    inputBool = False
    while(inputBool == False):
        if(input1 == 1):
            t.insert(tk.INSERT, "Lancement Joueur vs PC en cours... \n")
            pl_pc_gui(t)
            break
        elif(input1 == 2):
            t.insert(tk.INSERT, "Lancement PC vs PC en cours... \n")
            pc_v_pc_gui(t)
            break
        elif(input1 == 3):
            game.destroy()
            break
        input1 = getUserInt("Que choissisez-vous ?") 

         

                
