""" a function bank for all the possible othello matchups
    Date: 17/6/26
    Author: Zachary Thirkell
"""

from controls import Othello
from algorithms import *

def two_player_game():
    """ run a two player game of Othello in the python shell """
    print("Welcome to two player Othello!")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = human(O, 'black', n_passes, True)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = human(O, 'white', n_passes, True)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('U', 'U')
    
def play_Randall_black():
    """ run a game of Othello vs Randall in the python shell with the black 
    pieces 
    """
    print("Randall welcomes you to a game of Othello! You are playing with the black pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = human(O, 'black', n_passes, False)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Randall(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('u', 'R')

def play_Randall_white():
    """ run a game of Othello vs Randall in the python shell with the white 
    pieces 
    """
    print("Randall welcomes you to a game of Othello! You are playing with the white pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Randall(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = human(O, 'white', n_passes, False)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('R', 'u')

def play_Graham_black():
    """ run a game of Othello vs Graham in the python shell with the black 
    pieces
    """
    print("Graham welcomes you to a game of Othello! You are playing with the black pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = human(O, 'black', n_passes, False)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Graham(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('u', 'G')

def play_Graham_white():
    """ run a game of Othello vs Graham in the python shell with the white
    pieces
    """
    print("Graham welcomes you to a game of Othello! You are playing with the white pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Graham(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = human(O, 'white', n_passes, False)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('G', 'u')

def play_Edgar_black():
    """ run a game of Othello vs Edgar in the python shell with the black
    pieces
    """
    print("Edgar welcomes you to a game of Othello! You are playing with the black pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = human(O, 'black', n_passes, False)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Edgar(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('u', 'E')
    
def play_Edgar_white():
    """ run a game of Othello vs Edgar in the python shell with the white
    pieces
    """
    print("Edgar welcomes you to a game of Othello! You are playing with the white pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Edgar(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = human(O, 'white', n_passes, False)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('E', 'u')

def Randall_vs_Graham():
    """ run a game of Othello between Randall and Graham in the python shell """
    print("Othello - Randall vs Graham")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Randall(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Graham(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True                           
    O.finish_print('R', 'G')
    
def Graham_vs_Randall():
    """ run a game of Othello between Graham and Randall in the python shell """
    print("Othello - Graham vs Randall")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Graham(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Randall(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True                           
    O.finish_print('G', 'R')

def Randall_vs_Edgar():
    """ run a game of Othello between Randall and Edgar in the python shell """
    print("Othello - Randall vs Edgar")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Randall(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Edgar(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('R', 'E')

def Edgar_vs_Randall():
    """ run a game of Othello between Edgar and Randall in the python shell """
    print("Othello - Edgar vs Randall")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Edgar(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Randall(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('E', 'R')

def Graham_vs_Edgar():
    """ run a game of Othello between Graham and Edgar in the python shell """
    print("Othello - Graham vs Edgar")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Graham(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Edgar(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('G', 'E')

def Edgar_vs_Graham():
    """ run a game of Othello between Edgar and Graham in the python shell """
    print("Othello - Edgar vs Graham")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        n_passes = Edgar(O, 'black', n_passes)
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            n_passes = Graham(O, 'white', n_passes)
            if n_passes == 0:
                complete_flag = True
    O.finish_print('E', 'G')