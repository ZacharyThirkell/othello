""" Othello game
    Author: Zachary Thirkell
    Date: 16/4/26
    Version: 1.0
"""

# edit summary
# 16/4/26 game created
# 5/6/26 game logic and two player fully implemented
# 6/6/26 automated two player gameplay and saved scoresheets fully implemented,
# 'Randall' random algorithm implemented
# 7/6/26 'Graham' algorithm implemented, ran twenty trials of Randall vs Graham

# improvements
# allow Randall and Graham to play with the black pieces
# add other 'bot' functions with different algorithms

import copy
import random


class Othello:
    
    LTON = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    START = [[None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, 0, 1, None, None, None],
             [None, None, None, 1, 0, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None]
             ]
    
    def __init__(self):
        self.board = self.START
        self.turn = False
        self.scoresheet = []
    
    def pass_turn(self):
        self.turn = not self.turn
        
    def is_complete(self, complete_flag):
        if complete_flag:
            return True
        else:
            board_full = True
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == None:
                        board_full = False
            return board_full
    
    def score(self, current_position):
        white_sum = 0
        black_sum = 0
        for i in range(len(current_position)):
            for j in range(len(current_position[i])):
                if current_position[i][j] == 0:
                    black_sum += 1
                if current_position[i][j] == 1:
                    white_sum += 1
        return (white_sum, black_sum)
    
    def save(self, bot_code='u'):
        """ saves the scorecard to the specified txt file """
        filepath = "Othello Saved.txt"
        tx = f'u  {bot_code} \n'
        for s in self.scoresheet[:-1]:
            tx += f'{s[0]:2} {s[1]}\n'
        if self.scoresheet[-1][1] == None:
            tx += f'{self.scoresheet[-1][0]}'
        else:
            tx += f'{self.scoresheet[-1][0]:2} {self.scoresheet[-1][1]}\n'
        tx += f'{self.score(self.board)[1]}-{self.score(self.board)[0]}'
        with open(filepath, "w") as infile:
            infile.write(tx)
    
    def finish_print(self, bot_code='u'):
        score = self.score(self.board)
        if score[0] > score[1]:
            if bot_code == 'G':
                print("Graham wins!")
            elif bot_code == 'R':
                print("Randall wins!")
            else:
                print("White wins!")
        elif score[1] > score[0]:
            if bot_code == 'u':
                print("Black wins!")
            else:
                print("You win!")
        else:
            print("Tie!")
        print(f"Score: White={score[0]}, Black={score[1]}")
        
    def error(self, code, human=True):
        """ error print function """
        
        if code == 'key error' and human:
            print("ERROR: Invalid coordinate!")
        
        if code == 'white turn error' and human:
            print("ERROR: It's not white's turn!")
            
        if code == 'black turn error' and human:
            print("ERROR: It's not black's turn!")
            
        if code == 'coordinate error' and human:
            print("ERROR: Coordinate is already occupied!")
            
        if code == 'flank error' and human:
            print("ERROR: Nothing to flank here!")
            
        return 'ERROR'
        
    def white_move(self, coordinate, human=True):
        """ coordinate given in algebraic notation """
        if coordinate[0] not in 'abcdefgh' or coordinate[1] not in '12345678':
            return self.error('key error')
        
        if not self.turn:
            return self.error('white turn error')
        
        current_position = copy.deepcopy(self.board)
        x = 8 - int(coordinate[1])
        y = self.LTON[coordinate[0]]
        if current_position[x][y] != None:
            return self.error('coordinate error', human)
        current_position[x][y] = 1
        flank_check = False
        
        # scan South
        if x <= 5:
            # search for another white counter
            next_white_counter = None
            u = x + 1
            while u < 7 and next_white_counter == None:
                u += 1
                if current_position[u][y] == 1:
                    next_white_counter = u
            # if there is one, check if all squares in between are filled with black
            if next_white_counter != None:
                all_black = True
                for i in range(x + 1, next_white_counter):
                    if current_position[i][y] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    # if they are all black, change them to white
                    for i in range(x + 1, next_white_counter):
                        current_position[i][y] = 1
        
        # scan North
        if x >= 2:
            next_white_counter = None
            u = x - 1
            while u > 0 and next_white_counter == None:
                u -= 1
                if current_position[u][y] == 1:
                    next_white_counter = u
            if next_white_counter != None:
                all_black = True
                for i in range(x - 1, next_white_counter, -1):
                    if current_position[i][y] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(x - 1, next_white_counter, -1):
                        current_position[i][y] = 1
                        
        # scan East
        if y <= 5:
            next_white_counter = None
            v = y + 1
            while v < 7 and next_white_counter == None:
                v += 1
                if current_position[x][v] == 1:
                    next_white_counter = v
            if next_white_counter != None:
                all_black = True
                for i in range(y + 1, next_white_counter):
                    if current_position[x][i] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(y + 1, next_white_counter):
                        current_position[x][i] = 1
                        
        # scan West
        if y >= 2:
            next_white_counter = None
            v = y - 1
            while v > 0 and next_white_counter == None:
                v -= 1
                if current_position[x][v] == 1:
                    next_white_counter = v
            if next_white_counter != None:
                all_black = True
                for i in range(y - 1, next_white_counter, -1):
                    if current_position[x][i] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(y - 1, next_white_counter, -1):
                        current_position[x][i] = 1
        
        # scan South-East
        if x <= 5 and y <= 5:
            next_white_counter = None
            u = x + 1
            v = y + 1
            while u < 7 and v < 7 and next_white_counter == None:
                u += 1
                v += 1                
                if current_position[u][v] == 1:
                    next_white_counter = u
            if next_white_counter != None:
                all_black = True
                for i in range(x + 1, next_white_counter):
                    if current_position[i][y + i - x] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(x + 1, next_white_counter):
                        current_position[i][y + i - x] = 1
        
        # scan South-West
        if x <= 5 and y >= 2:
            next_white_counter = None
            u = x + 1
            v = y - 1
            while u < 7 and v > 0 and next_white_counter == None:
                u += 1
                v -= 1                
                if current_position[u][v] == 1:
                    next_white_counter = u
            if next_white_counter != None:
                all_black = True
                for i in range(x + 1, next_white_counter):
                    if current_position[i][y - i + x] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(x + 1, next_white_counter):
                        current_position[i][y - i + x] = 1
        
        # scan North-East
        if x >= 2 and y <= 5:
            next_white_counter = None
            u = x - 1
            v = y + 1
            while u > 0 and v < 7 and next_white_counter == None:
                u -= 1
                v += 1
                if current_position[u][v] == 1:
                    next_white_counter = u
            if next_white_counter != None:
                all_black = True
                for i in range(x - 1, next_white_counter, -1):
                    if current_position[i][y - i + x] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(x - 1, next_white_counter, -1):
                        current_position[i][y - i + x] = 1
                        
        # scan North-West
        if x >= 2 and y >= 2:
            next_white_counter = None
            u = x - 1
            v = y - 1
            while u > 0 and v > 0 and next_white_counter == None:
                u -= 1
                v -= 1
                if current_position[u][v] == 1:
                    next_white_counter = u
            if next_white_counter != None:
                all_black = True
                for i in range(x - 1, next_white_counter, -1):
                    if current_position[i][y + i - x] in [None, 1]:
                        all_black = False
                if all_black:
                    flank_check = True
                    for i in range(x - 1, next_white_counter, -1):
                        current_position[i][y + i - x] = 1          
                        
        # raise an error if we haven't flanked anything, and undo the move
        if not flank_check:
            return self.error('flank error', human)
        
        return current_position
        
    def black_move(self, coordinate, human=True):
        """ coordinate given in algebraic notation """
        if len(coordinate) != 2:
            return self.error('key error')
        
        if coordinate[0] not in 'abcdefgh' or coordinate[1] not in '12345678':
            return self.error('key error')
        
        if self.turn:
            return self.error('black turn error')
        
        current_position = copy.deepcopy(self.board)
        x = 8 - int(coordinate[1])
        y = self.LTON[coordinate[0]]
        if current_position[x][y] != None:
            return self.error('coordinate error', human)
        current_position[x][y] = 0
        flank_check = False
        
        # scan South
        if x <= 5:
            # search for another black counter
            next_black_counter = None
            u = x + 1
            while u < 7 and next_black_counter == None:
                u += 1
                if current_position[u][y] == 0:
                    next_black_counter = u
            # if there is one, check if all squares in between are filled with white
            if next_black_counter != None:
                all_white = True
                for i in range(x + 1, next_black_counter):
                    if current_position[i][y] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    # if they are all white, change them to black
                    for i in range(x + 1, next_black_counter):
                        current_position[i][y] = 0
        
        # scan North
        if x >= 2:
            next_black_counter = None
            u = x - 1
            while u > 0 and next_black_counter == None:
                u -= 1
                if current_position[u][y] == 0:
                    next_black_counter = u
            if next_black_counter != None:
                all_white = True
                for i in range(x - 1, next_black_counter, -1):
                    if current_position[i][y] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(x - 1, next_black_counter, -1):
                        current_position[i][y] = 0
                        
        # scan East
        if y <= 5:
            next_black_counter = None
            v = y + 1
            while v < 7 and next_black_counter == None:
                v += 1
                if current_position[x][v] == 0:
                    next_black_counter = v
            if next_black_counter != None:
                all_white = True
                for i in range(y + 1, next_black_counter):
                    if current_position[x][i] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(y + 1, next_black_counter):
                        current_position[x][i] = 0
                        
        # scan West
        if y >= 2:
            next_black_counter = None
            v = y - 1
            while v > 0 and next_black_counter == None:
                v -= 1
                if current_position[x][v] == 0:
                    next_black_counter = v
            if next_black_counter != None:
                all_white = True
                for i in range(y - 1, next_black_counter, -1):
                    if current_position[x][i] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(y - 1, next_black_counter, -1):
                        current_position[x][i] = 0
        
        # scan South-East
        if x <= 5 and y <= 5:
            next_black_counter = None
            u = x + 1
            v = y + 1
            while u < 7 and v < 7 and next_black_counter == None:
                u += 1
                v += 1                
                if current_position[u][v] == 0:
                    next_black_counter = u
            if next_black_counter != None:
                all_white = True
                for i in range(x + 1, next_black_counter):
                    if current_position[i][y + i - x] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(x + 1, next_black_counter):
                        current_position[i][y + i - x] = 0
        
        # scan South-West
        if x <= 5 and y >= 2:
            next_black_counter = None
            u = x + 1
            v = y - 1
            while u < 7 and v > 0 and next_black_counter == None:
                u += 1
                v -= 1                
                if current_position[u][v] == 0:
                    next_black_counter = u
            if next_black_counter != None:
                all_white = True
                for i in range(x + 1, next_black_counter):
                    if current_position[i][y - i + x] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(x + 1, next_black_counter):
                        current_position[i][y - i + x] = 0
        
        # scan North-East
        if x >= 2 and y <= 5:
            next_black_counter = None
            u = x - 1
            v = y + 1
            while u > 0 and v < 7 and next_black_counter == None:
                u -= 1
                v += 1
                if current_position[u][v] == 0:
                    next_black_counter = u
            if next_black_counter != None:
                all_white = True
                for i in range(x - 1, next_black_counter, -1):
                    if current_position[i][y - i + x] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(x - 1, next_black_counter, -1):
                        current_position[i][y - i + x] = 0
                        
        # scan North-West
        if x >= 2 and y >= 2:
            next_black_counter = None
            u = x - 1
            v = y - 1
            while u > 0 and v > 0 and next_black_counter == None:
                u -= 1
                v -= 1
                if current_position[u][v] == 0:
                    next_black_counter = u
            if next_black_counter != None:
                all_white = True
                for i in range(x - 1, next_black_counter, -1):
                    if current_position[i][y + i - x] in [None, 0]:
                        all_white = False
                if all_white:
                    flank_check = True
                    for i in range(x - 1, next_black_counter, -1):
                        current_position[i][y + i - x] = 0         
                        
        # raise an error if we haven't flanked anything, and undo the move
        if not flank_check:
            return self.error('flank error', human)
        
        return current_position       
        
    def __str__(self):
        """ game representation """
        s = ' -------- \n'
        for i in range(len(self.board)):
            s += '|'
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    s += ' '
                else:
                    s += str(self.board[i][j])
            s += '|\n'
        s += ' -------- '
        return s
    
def two_player_game():
    """ run a two player game of Othello in the python shell """
    print("Welcome to two player Othello!")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    
    while not O.is_complete(complete_flag):
        error_free = False
        while not error_free:
            b = input("Black to move: ")
            if b != 'p':
                current_position = O.black_move(b)
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
        O.scoresheet.append((b, None))
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            error_free = False
            while not error_free:
                w = input("White to move: ")
                if w != 'p':
                    current_position = O.white_move(w)
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
            O.scoresheet[-1] = (O.scoresheet[-1][0], w)
            if n_passes == 0:
                complete_flag = True
    
    O.save()            
    O.finish_print()
    
    
def play_Randall():
    """ run a game of Othello vs Randall in the python shell """
    print("Randall welcomes you to a game of Othello! You play with the black pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    
    while not O.is_complete(complete_flag):
        error_free = False
        while not error_free:
            b = input("Your turn: ")
            if b != 'p':
                current_position = O.black_move(b)
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
        O.scoresheet.append((b, None))
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            print("Randall is thinking...")
            candidate_moves = []
            for a in 'abcdefgh':
                for b in '12345678':
                    s = a + b
                    candidate_position = O.white_move(s, False)
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
            O.scoresheet[-1] = (O.scoresheet[-1][0], move_choice)
            if n_passes == 0:
                complete_flag = True
                
    O.save('R')            
    O.finish_print('R')    
    
    
def play_Graham():
    """ run a game of Othello vs Graham in the python shell """
    print("Graham welcomes you to a game of Othello! You play with the black pieces.")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    
    while not O.is_complete(complete_flag):
        error_free = False
        while not error_free:
            b = input("Your turn: ")
            if b != 'p':
                current_position = O.black_move(b)
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
        O.scoresheet.append((b, None))
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            print("Graham is thinking...")
            candidate_moves = []
            for a in 'abcdefgh':
                for b in '12345678':
                    s = a + b
                    candidate_position = O.white_move(s, False)
                    if candidate_position != 'ERROR':
                        candidate_moves.append((candidate_position, s))
            if candidate_moves != []:
                max_so_far = [candidate_moves[0]]
                for candidate_position, s in candidate_moves[1:]:
                    if O.score(candidate_position)[0] > O.score(max_so_far[0][0])[0]:
                        max_so_far = [(candidate_position, s)]
                    elif O.score(candidate_position)[0] == O.score(max_so_far[0][0])[0]:
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
            O.scoresheet[-1] = (O.scoresheet[-1][0], move_choice)
            if n_passes == 0:
                complete_flag = True
                
    O.save('G')            
    O.finish_print('G')    


def Randall_vs_Graham():
    """ run a game of Othello between Randall and Graham in the python shell """
    print("Othello - Randall vs Graham")
    O = Othello()
    print(O)
    print()
    n_passes = 2
    complete_flag = False
    
    while not O.is_complete(complete_flag):
        print("Randall is thinking...")
        candidate_moves = []
        for a in 'abcdefgh':
            for b in '12345678':
                s = a + b
                candidate_position = O.black_move(s, False)
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
        if n_passes == 0:
            complete_flag = True
        if not O.is_complete(complete_flag):
            print("Graham is thinking...")
            candidate_moves = []
            for a in 'abcdefgh':
                for b in '12345678':
                    s = a + b
                    candidate_position = O.white_move(s, False)
                    if candidate_position != 'ERROR':
                        candidate_moves.append((candidate_position, s))
            if candidate_moves != []:
                max_so_far = [candidate_moves[0]]
                for candidate_position, s in candidate_moves[1:]:
                    if O.score(candidate_position)[0] > O.score(max_so_far[0][0])[0]:
                        max_so_far = [(candidate_position, s)]
                    elif O.score(candidate_position)[0] == O.score(max_so_far[0][0])[0]:
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
            if n_passes == 0:
                complete_flag = True
                           
    O.finish_print('G')    

def main():
    play_Graham()
    

if __name__ == '__main__':
    main()