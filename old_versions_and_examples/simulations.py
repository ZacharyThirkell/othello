""" simulate many matches between Randall and Graham to determine the stronger
    algorithm when facing each other
    this module is not part of the main othello library
    Date: 17/6/26
    Author: Zachary Thirkell
"""

import random
import matplotlib.pyplot as plt
from controls import *

def Randall_vs_Graham_raw():
    """ simulate a game Othello between Randall and Graham """
    O = Othello()
    n_passes = 2
    complete_flag = False
    while not O.is_complete(complete_flag):
        candidate_moves = []
        for a in 'abcdefgh':
            for b in '12345678':
                s = a + b
                candidate_position = black_move(O, O.board, s, False)
                if candidate_position != 'ERROR':
                    candidate_moves.append((candidate_position, s))
        if candidate_moves != []:
            O.board, move_choice = random.choice(candidate_moves)
            n_passes = 2
        else:
            move_choice = 'p'
            n_passes -= 1
        O.pass_turn()
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            candidate_moves = []
            for a in 'abcdefgh':
                for b in '12345678':
                    s = a + b
                    candidate_position = white_move(O, O.board, s, False)
                    if candidate_position != 'ERROR':
                        candidate_moves.append((candidate_position, s))
            if candidate_moves != []:
                max_so_far = [candidate_moves[0]]
                for candidate_position, s in candidate_moves[1:]:
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
            if n_passes == 0:
                complete_flag = True
    return O.score(O.board)[0]

def main():
    """ plot the result of 100 games between Randall and Graham """
    black_scores = []
    n = 100
    for i in range(n):
        black_scores.append(Randall_vs_Graham_raw())
    
    axes = plt.axes()
    axes.hist(black_scores, bins=64, color='skyblue', edgecolor='black')
    axes.set_title(f'Randall vs Graham results - {n} trials')
    axes.set_xlabel("Randall's score")
    axes.set_ylabel('Frequency')
    plt.show()
    
if __name__ == "__main__":
    main()