# -*- coding: utf-8 -*-
"""
Created in 2020

@author: Hadrien, Valentin, Stéphane
"""

import copy
global Board

def endStack(stack):
    """
    Parameters
    ----------
    stack : stack you want the value from

    Returns
    -------
    last value of the stack

    """
    if not (stack):
        return -1
    else:
        if (len(stack)==0):
            return stack[0]
        else:
            return stack[len(stack)-1]

def move(original_stack,target_stack,a,b,piece):
    """
    Parameters
    ----------
    original_stack : stack
    target_stack : stack
    a : ligne index
    b : column index
    piece : number of pieces to move

    Returns
    -------
    Succes or failure

    """
    if not (original_stack):
        print("source is empty")
    elif (original_stack):
        if(piece == 1):
            if(len(original_stack) == 0):
                target_stack.append(Board[a][b])
                original_stack.pop()    
            else:
                target_stack.append(original_stack[len(original_stack)-1])
                original_stack.pop()
        elif(piece == 2):
            for i in range(len(original_stack)-2,len(original_stack),1):
                target_stack.append(original_stack[i])#add to target stack
            for i in range(len(original_stack)-2,len(original_stack),1):
                original_stack.pop()#removes from original stack
        elif(piece == 3):
            for i in range(len(original_stack)-3,len(original_stack),1):
                target_stack.append(original_stack[i])
            for i in range (len(original_stack)-3,len(original_stack),1):
                original_stack.pop()
    return 0

def get_plays(player,board):
    """
    Parameters
    ----------
    player : player id
    board : 3D array representing the board on a certain turn

    Returns
    -------
    plays : array of boards with all possible plays to make for the given player

    """
    global Board
    Board = board
    plays = []

    for i in range(3) :
        for j in range(3):        
            if(endStack(Board[i][j]) == player):#if the top 
                t = len(Board[i][j])
                if t>3:
                    t=3
                for k in range(1,t+1):
                    for n in range(0,k):
                        tmp = k-n
                        ###############################################                        
                        play = copy.deepcopy(Board)
                        try:
                            move(play[i][j],play[i+n][j+tmp],i,j,k)
                            plays.append(play)
                        except:
                            pass
                        ###############################################
                        play = copy.deepcopy(Board)
                        try:
                            if(i-n>=0 and j-tmp>=0):
                                move(play[i][j],play[i-n][j-tmp],i,j,k)
                                plays.append(play)
                        except:
                            pass
                        ###############################################
                        play = copy.deepcopy(Board)
                        try:
                            if(j-n>=0):
                                move(play[i][j],play[i+tmp][j-n],i,j,k)
                                plays.append(play)
                        except:
                            pass
                        ###############################################
                        play = copy.deepcopy(Board)
                        try:
                            if(i-tmp>=0):
                                move(play[i][j],play[i-tmp][j+n],i,j,k)
                                plays.append(play)
                        except:
                            pass
                            
                        ################################################
                        ## CAS EXCEPTIONEL DES MOUVEMENTS DE 3        ##
                        ################################################
                        if(t==3 and k==1 and n==0):
                            play = copy.deepcopy(Board)
                            try:
                                move(play[i][j],play[i+n][j+tmp],i,j,3)
                                plays.append(play)
                            except:
                                pass
                            ###############################################
                            play = copy.deepcopy(Board)
                            try:
                                if(i-n>=0 and j-tmp>=0):
                                    move(play[i][j],play[i-n][j-tmp],i,j,3)
                                    plays.append(play)
                            except:
                                pass
                            ###############################################
                            play = copy.deepcopy(Board)
                            try:
                                if(j-n>=0):
                                    move(play[i][j],play[i+tmp][j-n],i,j,3)
                                    plays.append(play)
                            except:
                                pass
                            ###############################################
                            play = copy.deepcopy(Board)
                            try:
                                if(i-tmp>=0):
                                    move(play[i][j],play[i-tmp][j+n],i,j,3)
                                    plays.append(play)
                            except:
                                pass
    return plays
