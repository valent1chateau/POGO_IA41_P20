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
    canvas = tk.Canvas(game, width=400, height=400)
    canvas.pack()
    textField = tk.Text(canvas, width=120, height=40)
    canvas.create_window((0, 0), window=textField, anchor='nw')
    pogoGame(textField, game)
    
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

def pl_pc(t,game, Board):
    t.insert(tk.INSERT,"Vous êtes le joueur 0 \n")
    print_guiboard(t, Board)

def pogoGame(t, game):
    t.insert(tk.INSERT,"Voulez vous jouer? \n")
    if(getUserInput("Voulez vous jouer ? O/N") != "O"):
        game.destroy()
    else:
        t.insert(tk.INSERT, "Choisir une option \n 1 -> Joueur vs PC \n 2 -> PC vs PC \n 3 -> Quitter \n")
    
    input1 = getUserInt("Que choissisez-vous ?") 
    inputBool = False
    while(inputBool == False):
        if(input1 == 1):
            t.insert(tk.INSERT, "Lancement Joueur vs PC en cours... \n")
            pl_pc(t, game, Board)
            break
        elif(input1 == 2):
            t.insert(tk.INSERT, "Lancement PC vs PC en cours... \n")
            break
        elif(input1 == 3):
            game.destroy()
            break
        input1 = getUserInt("Que choissisez-vous ?") 

         

                
