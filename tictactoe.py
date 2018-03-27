"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board,player):
    """
    One trial play for Tic tac toe with
    random moves on both sides
    """
    winner = None
    current_player = player
    while winner == None:
        empty_squares = board.get_empty_squares()
        pos = random.choice(empty_squares)
        board.move(pos[0],pos[1],current_player)
        winner = board.check_win()
        current_player = provided.switch_player(current_player)
    #print board
    
def mc_update_scores(scores, board, player):
    """
    Scoring the board for the trial plays,
    getting back the score for each square after all the trials
    """
    winner = board.check_win()
    if player == winner:
        scorep = SCORE_CURRENT
        scoreo = - SCORE_OTHER
    else:
        scorep = -SCORE_CURRENT
        scoreo = SCORE_OTHER
    #print winner
    #print player
    if winner == provided.DRAW:
        scores = scores
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row,col) == provided.EMPTY:
                    scores[row][col] += 0
                elif board.square(row,col) == player:
                    scores[row][col] += scorep
                else:
                    scores[row][col] += scoreo

    #print scores

def get_best_move(board, scores):
    """
    getting the best move based on a score
    of the available - empty squares
    """
    empty_squares = board.get_empty_squares()
    max_value = None
    choice_list = []
    for row, col in empty_squares:
        if max_value == None:
            max_value = scores[row][col]
        elif max_value < scores[row][col]:
            max_value = scores[row][col]
        #print max_value
    for row, col in empty_squares:
        if max_value == scores[row][col]:
            choice_list.append((row,col))
        #print choice_list, len(choice_list)
    choice = random.choice(choice_list)
    return choice
    
def mc_move(board, player, trials):
    """
    Running the number of trials given in the arguments,
    getting the aggregate score for all trials,
    chosing the move with the highest score on the actual board
    """
    scores = [[ 0 for dummycol in range(board.get_dim())]
              for dummyrow in range(board.get_dim())]
    for dummynum in range(trials):
        #print scores
        tboard = board.clone()
        #print tboard
        mc_trial(tboard,player)
        #print tboard
        mc_update_scores(scores,tboard,player)
        #print tboard
        #print scores
    move = get_best_move(board,scores)
    return move

    


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
#board = provided.TTTBoard(3)
#board.move(1,2,provided.PLAYERX)
#board.move(1,1,provided.PLAYERO)
#board.move(0,2,provided.PLAYERX)
#mc_trial(board,provided.PLAYERX)
#scores = [[0,1,-1],[1,0,0],[-1,0,1]]
#mc_update_scores(scores, board, provided.PLAYERX)
#get_best_move(board, scores)
#mc_move(board, provided.PLAYERX,1)
#print mc_move(board,provided.PLAYERX,700)