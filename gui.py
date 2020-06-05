# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:22:06 2020

@author: vlt
"""
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()   
root.title('Jeu du pogo')
icon = tk.PhotoImage(file='dice.png')
root.call('wm', 'iconphoto', root._w, icon)

canvas = tk.Canvas(root, width=245, height=245)
canvas.pack()

backgroundImage = ImageTk.PhotoImage(Image.open("pogo.png"))
canvas.create_image(125,125, image = backgroundImage)

playButton = tk.Button(root, text="Jouer", padx=10)
play_button_window = canvas.create_window(75, 200, window=playButton)

quitButton = tk.Button(root, text="Quitter", command=root.destroy, padx=10)
quit_button_window = canvas.create_window(175, 200, window=quitButton)


root.mainloop()