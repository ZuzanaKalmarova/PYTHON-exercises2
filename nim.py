"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    
    # Insert your code here
    sim_num = dict()
    sim_win = dict()
    for trial in range(TRIALS):
        num = num_items
        init_val = random.randrange(MAX_REMOVE)+1
        num -= init_val
        while True:
            play_move = random.randrange(MAX_REMOVE) + 1
            num -= play_move
            if num <= 0:
                win = 0
                break
            comp_move = random.randrange (MAX_REMOVE) + 1
            num -= comp_move
            if num <= 0:
                win = 1
                break
        sim_num[init_val] = sim_num.get(init_val,0) + 1
        sim_win[init_val] = sim_win.get(init_val,0) + win
    fract_won = dict()
    for key in sim_num:
        fract_won[key] = float(sim_win[key])/float(sim_num[key])
    temp_list = list()
    for key,val in fract_won.items():
        temp_list.append((val,key))
    temp_list.sort(reverse=True)
    
    return temp_list[0][1]


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

#play_game(21)
print evaluate_position(21)

        
    
                 
    