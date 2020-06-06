# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:22:06 2020

@author: vlt
"""
import tkinter as tk
from PIL import ImageTk,Image
import main
import tkinter.simpledialog as sd
import sys
    




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
    
def getUserInput(msg):
    userInput = sd.askstring('User Input',msg)
    return userInput

def pogoGame(t):
    t.insert(tk.END,"Voulez vous jouer?")
    
start()
