""" logic for othello algorithms (random, greedy, edge-weighted) and 
    human-controlled moves
    Date: 17/6/26
    Author: Zachary Thirkell
"""

from controls import white_move
from controls import black_move
import random

def human(O, colour, n_passes, u_flag):
    """ function that controls a human move """
    error_free = False
    while not error_free:
        if not u_flag:
            b = input("Your turn: ")
        else:
            if colour == 'black':
                b = input("Black to move: ")
            else:
                b = input("White to move: ")
        if b == 'q':
            n_passes = None
            break
        elif b != 'p':
            if colour == 'black':
                current_position = black_move(O, O.board, b)
            else:
                current_position = white_move(O, O.board, b)
            if current_position != 'ERROR':
                O.board = current_position
                O.pass_turn()
                error_free = True
            n_passes = 2
        else:
            error_free = True
            O.pass_turn()
            n_passes -= 1
        print(O)
        print()
    return n_passes

def Randall(O, colour, n_passes):
    """ function that controls Randall's moves """
    print("Randall is thinking...")
    candidate_moves = []
    for a in 'abcdefgh':
        for b in '12345678':
            s = a + b
            if colour == 'black':
                candidate_position = black_move(O, O.board, s, False)
            else:
                candidate_position = white_move(O, O.board, s, False)
            if candidate_position != 'ERROR':
                candidate_moves.append((candidate_position, s))
    if candidate_moves != []:
        O.board, move_choice = random.choice(candidate_moves)
        n_passes = 2
    else:
        move_choice = 'p'
        n_passes -= 1
    O.pass_turn()
    print(O)
    print(f"Randall plays {move_choice}")
    print()
    return n_passes

def Graham(O, colour, n_passes):
    """ function that controls Graham's moves """
    print("Graham is thinking...")
    candidate_moves = []
    for a in 'abcdefgh':
        for b in '12345678':
            s = a + b
            if colour == 'black':
                candidate_position = black_move(O, O.board, s, False)
            else:
                candidate_position = white_move(O, O.board, s, False)
            if candidate_position != 'ERROR':
                candidate_moves.append((candidate_position, s))
    if candidate_moves != []:
        max_so_far = [candidate_moves[0]]
        for candidate_position, s in candidate_moves[1:]:
            if colour == 'black':
                if O.score(candidate_position)[0] > O.score(max_so_far[0][0])[0]:
                    max_so_far = [(candidate_position, s)]
                elif O.score(candidate_position)[0] == O.score(max_so_far[0][0])[0]:
                    max_so_far.append((candidate_position, s))                 
            else:
                if O.score(candidate_position)[1] > O.score(max_so_far[0][0])[1]:
                    max_so_far = [(candidate_position, s)]
                elif O.score(candidate_position)[1] == O.score(max_so_far[0][0])[1]:
                    max_so_far.append((candidate_position, s))                    
        O.board, move_choice = random.choice(max_so_far)
        n_passes = 2
    else:
        move_choice = 'p'
        n_passes -= 1
    O.pass_turn()
    print(O)
    print(f"Graham plays {move_choice}")
    print()
    return n_passes

class EdgarSortKey:
    MOVE_PRIORITY = [['a1', 'a8', 'h1', 'h8'],
                     ['c1', 'a3', 'a6', 'c8', 'f1', 'h3', 'h6', 'f8'],
                     ['d1', 'a4', 'a5', 'd8', 'e1', 'h4', 'h5', 'e8'],
                     ['c3', 'c6', 'f3', 'f6'],
                     ['d3', 'c4', 'c5', 'd6', 'e3', 'f4', 'f5', 'e6'],
                     ['c2', 'b3', 'b6', 'c7', 'f2', 'g3', 'g6', 'f7'],
                     ['d2', 'b4', 'b5', 'd7', 'e2', 'g4', 'g5', 'e7'],
                     ['d4', 'd5', 'e4', 'e5'],
                     ['b1', 'a2', 'a7', 'b8', 'g1', 'h2', 'h7', 'g8'],
                     ['b2', 'b7', 'g2', 'g7']
                     ]
    
    def __init__(self, move):
        """ Initialise a priority value """
        s = 10
        for l in self.MOVE_PRIORITY:
            if move in l:
                self.priority = s
            else:
                s -= 1
        
    def __gt__(self, other):
        """ allow > comparison with other values """
        return self.priority > other.priority
    
    def __eq__(self, other):
        """ allow == comparison with other values """
        return self.priority == other.priority

def Edgar(O, colour, n_passes):
    """ function that controls Edgar's moves """
    print("Edgar is thinking...")
    candidate_moves = []
    for a in 'abcdefgh':
        for b in '12345678':
            s = a + b
            if colour == 'black':
                candidate_position = black_move(O, O.board, s, False)
            else:
                candidate_position = white_move(O, O.board, s, False)
            if candidate_position != 'ERROR':
                esk = EdgarSortKey(s)
                candidate_moves.append((candidate_position, esk, s))
    if candidate_moves != []:
        max_so_far = [candidate_moves[0]]
        for candidate_position, esk, s in candidate_moves[1:]:
            if esk.priority > max_so_far[0][1].priority:
                max_so_far = [(candidate_position, esk, s)]
            elif esk.priority == max_so_far[0][1].priority:
                max_so_far.append((candidate_position, esk, s))
        O.board, esk, move_choice = random.choice(max_so_far)
        n_passes = 2
    else:
        move_choice = 'p'
        n_passes -= 1
    O.pass_turn()
    print(O)
    print(f"Edgar plays {move_choice}")
    print()
    return n_passes