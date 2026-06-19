""" an object and functions that store and modify the state of an othello game
    Date: 17/6/26
    Author: Zachary Thirkell
"""

import copy

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
        return (black_sum, white_sum)
    
    def finish_print(self, black_code='u', white_code='u'):
        score = self.score(self.board)
        if score[0] > score[1]:
            if black_code == 'G':
                print("Graham wins!")
            elif black_code == 'R':
                print("Randall wins!")
            elif black_code == 'E':
                print("Edgar wins!")
            elif black_code == 'U':
                print("Black wins!")
            else:
                print("You win!")
        elif score[1] > score[0]:
            if white_code == 'G':
                print("Graham wins!")
            elif white_code == 'R':
                print("Randall wins!")
            elif white_code == 'E':
                print("Edgar wins!")
            elif white_code == 'U':
                print("Black wins!")
            else:
                print("You win!")
        else:
            print("Tie!")
        print(f"Score: Black={score[0]}, White={score[1]}")
        
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
    
    def __str__(self):
        """ game representation """
        s = '   - - - - - - - -  \n'
        for i in range(len(self.board)):
            s += f'{8 - i}| '
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    s += ' '
                else:
                    s += str(self.board[i][j])
                s += ' '
            s += '|\n'
        s += '   - - - - - - - -  \n'
        s += '   a b c d e f g h  '
        return s    
        
def white_move(O, position, coordinate, human=True):
    """ coordinate given in algebraic notation """
    if coordinate[0] not in 'abcdefgh' or coordinate[1] not in '12345678':
        return O.error('key error')
    
    if not O.turn:
        return O.error('white turn error')
    
    current_position = copy.deepcopy(position)
    x = 8 - int(coordinate[1])
    y = O.LTON[coordinate[0]]
    if current_position[x][y] != None:
        return O.error('coordinate error', human)
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
        return O.error('flank error', human)
    
    return current_position
    
def black_move(O, position, coordinate, human=True):
    """ coordinate given in algebraic notation """
    if len(coordinate) != 2:
        return O.error('key error')
    
    if coordinate[0] not in 'abcdefgh' or coordinate[1] not in '12345678':
        return O.error('key error')
    
    if O.turn:
        return O.error('black turn error')
    
    current_position = copy.deepcopy(position)
    x = 8 - int(coordinate[1])
    y = O.LTON[coordinate[0]]
    if current_position[x][y] != None:
        return O.error('coordinate error', human)
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
        return O.error('flank error', human)
    
    return current_position