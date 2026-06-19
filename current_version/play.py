""" run this module to play othello!
    Date: 17/6/26
    Author: Zachary Thirkell
"""

from pairings import *

def main():
    """ play a game! """
    print("modes available := two player (2), one_player (1), or zero_player (0)")
    mode = input("Select mode: ")
    if mode == '2':
        two_player_game()
    elif mode == '1':
        c = input("Choose colour: ")
        print("bots available := 'Randall', 'Graham', 'Edgar'")
        bot = input("Choose bot: ")
        if bot == 'Randall' and c == 'black':
            play_Randall_black()
        elif bot == 'Randall' and c == 'white':
            play_Randall_white()
        elif bot == 'Graham' and c == 'black':
            play_Graham_black()
        elif bot == 'Graham' and c == 'white':
            play_Graham_white()
        elif bot == 'Edgar' and c == 'black':
            play_Edgar_black()
        elif bot == 'Edgar' and c == 'white':
            play_Edgar_white()
        else:
            raise ValueError("bots must be capitalised and colours must be 'white' or 'black'")
    else:
        print("bots available := 'Randall', 'Graham', 'Edgar'")
        bot_b = input("Choose first bot: ")
        bot_w = input("Choose second bot: ")
        if bot_b == 'Randall' and bot_w == 'Graham':
            Randall_vs_Graham()
        elif bot_b == 'Graham' and bot_w == 'Randall':
            Graham_vs_Randall()
        elif bot_b == 'Edgar' and bot_w == 'Randall':
            Edgar_vs_Randall()
        elif bot_b == 'Randall' and bot_w == 'Edgar':
            Randall_vs_Edgar()
        elif bot_b == 'Graham' and bot_w == 'Edgar':
            Graham_vs_Edgar()
        elif bot_b == 'Edgar' and bot_w == 'Graham':
            Edgar_vs_Graham()
        else:
            raise ValueError("bots must be capitalised and colours must be 'white' or 'black'")            
    
if __name__ == "__main__":
    main()