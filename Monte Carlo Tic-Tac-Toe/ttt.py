"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves,
     alternating between players. The function should return when the game is over. 
     The modified board will contain the state of the game, so the function does not return anything. 
     In other words, the function should modify the board input.
    """
    print board
    _boardClone = board.clone()
    # choise a random empty square:
    _emptySquare = random.choice(_boardClone.get_empty_squares())
    print _emptySquare



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

game = provided.TTTBoard(3)

mc_trial(game, 2)
