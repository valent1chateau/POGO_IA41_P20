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
    
def start():
    root = tk.Tk()   
    root.title('Jeu du pogo')
    icon = tk.PhotoImage(file='dice.png')
    root.call('wm', 'iconphoto', root._w, icon)
    canvas = tk.Canvas(root, width=245, height=245)
    canvas.pack()
    backgroundImage = ImageTk.PhotoImage(Image.open("pogo.png"))
    canvas.create_image(125,125, image = backgroundImage)
    playButton = tk.Button(root, text="Jouer", padx=10, command=lambda: [f() for f in [root.destroy(), game(root)]])
    play_button_window = canvas.create_window(75, 200, window=playButton,)
    quitButton = tk.Button(root, text="Quitter", command=root.destroy, padx=10)
    quit_button_window = canvas.create_window(175, 200, window=quitButton)
    root.mainloop()
    
def game(root):
    game = tk.Tk()
    game.title('Jeu du pogo')
    canvas = tk.Canvas(game, width=400, height=400)
    canvas.pack()
    textField = tk.Text(canvas, width=120, height=40)
    canvas.create_window((0, 0), window=textField, anchor='nw')
    pogoGame(textField)
    
    game.mainloop()
    root.destroy()
    
def getUserInput(msg):
    userInput = sd.askstring('User Input',msg)
    return userInput

def getUserInt(msg):
    userInput = sd.askinteger('User Input',msg)
    return userInput

def pogoGame(t):
    t.insert(tk.INSERT,"Voulez vous jouer? \n")
    if (getUserInput("Voulez vous jouer ? O/N") != "O"):
        t.insert(tk.INSERT, "Arrêt du jeu \n")
        game.destroy()
    else :
        t.insert(tk.INSERT, "Choisir une option \n 1 -> Joueur vs PC \n 2 -> PC vs PC \n 3 -> Quitter \n")
    if (getUserInt("Que choissisez-vous ?") == 1):
        t.insert(tk.INSERT, "Lancement Joueur vs PC en cours...")
        
    elif(getUserInt("Que choissisez-vous ?") == 2):
        t.insert(tk.INSERT, "Lancement PC vs PC en cours...")
    else:
        game.destroy
        
start()
