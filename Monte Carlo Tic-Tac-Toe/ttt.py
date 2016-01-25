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
    _currentPlayer = player
    _wonGame = False
    
    
    while _wonGame == False:
        # choise a random empty square:
        try:
            _emptySquare = random.choice(_boardClone.get_empty_squares())
            #print "Ures :", _emptySquare
            #print "Current Player:", _currentPlayer
            _boardClone.move(_emptySquare[0], _emptySquare[1], _currentPlayer)
            
            #print _boardClone
            if _boardClone.check_win() == None:
                _currentPlayer = provided.switch_player(_currentPlayer)
                
            else:
                _wonGame = True
                
            
        
        except IndexError:
            # List is no more emptySquare
            #print "Empty LIST - END"
            break
            
    print "Winner:", _boardClone.check_win()
    print _boardClone
    
    
    
def mc_update_scores(scores, board, player):
    
    
    
    
    pass
        




def get_best_move(board, scores):
    pass


def mc_move(board, player, trials):
    pass


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


"""
TESTING Phase
"""

game = provided.TTTBoard(3)

# game.move(0, 0, 2)
# game.move(0, 1, 3)
# game.move(1, 0, 2)
# print game.get.emptySquare()
# print game

mc_trial(game, 2)
print 
#print game
