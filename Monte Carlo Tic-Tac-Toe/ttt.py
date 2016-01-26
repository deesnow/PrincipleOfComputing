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
SCORE_CURRENT = 2 # Score for squares played by the current player
SCORE_OTHER = 1   # Score for squares played by the other player
    
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
    
    _currentPlayer = player
    _wonGame = False
    
    
    while _wonGame == False:
        # choise a random empty square:
        try:
            _emptySquare = random.choice(board.get_empty_squares())
            #print "Ures :", _emptySquare
            #print "Current Player:", _currentPlayer
            board.move(_emptySquare[0], _emptySquare[1], _currentPlayer)
            
            #print board
            if board.check_win() == None:
                _currentPlayer = provided.switch_player(_currentPlayer)
                
            else:
                _wonGame = True
                
            
        
        except IndexError:
            # List is no more emptySquare
            #print "Empty LIST - END"
            break
            
    print "Winner:", board.check_win()
    print board
    

def iniScores(dim):
    zeroScores = [[0 for dummycol in range(dim)] for dummyrow in range(dim)]
    return zeroScores
    
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions
    as the Tic-Tac-Toe board, a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid. As the function updates
    the scores grid directly, it does not return anything,
    """
    dim = board.get_dim()
    
    if board.check_win() == 4:
        return scores
    
    elif board.check_win() == player:
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == 1:
                    continue
                elif board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                
                else:
                    scores[row][col] -= SCORE_OTHER
                        
        return scores
    
    else:
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == 1:
                    continue
                elif board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                
                else:
                    scores[row][col] += SCORE_OTHER
                
        return scores
    
    
    
        




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

#scores = iniScores(game.get_dim())
scores = [[-1, 2, -1], [2, 2, 2], [0, 0, -1]]
mc_trial(game, 2)
print mc_update_scores(scores, game, 2)



#mc_trial(game, 2)
#print 
#print game
