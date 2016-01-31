"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
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
    #print board
    
    current_player = player
    won_game = False
    
    
    while won_game == False:
        # choise a random empty square:
        try:
            empty_square = random.choice(board.get_empty_squares())
            #print "Ures :", empty_square
            #print "Current Player:", current_player
            board.move(empty_square[0], empty_square[1], current_player)
            
            #print board
            if board.check_win() == None:
                current_player = provided.switch_player(current_player)
                
            else:
                won_game = True
                
            
        
        except IndexError:
            # List is no more empty_square
            #print "Empty LIST - END"
            break
            
#     print "Winner:", board.check_win()
#     print board
     

def init_scores(dim):
    """
    Init a scores list with 
    """
    zero_scores = [[0 for dummycol in range(dim)] for dummyrow in range(dim)]
    return zero_scores
    

def get_scores_min(scores, dim):
    """
    Helper function for update_score
    """
    scores_min = min(scores[0])
    for dummyrow in range(1, dim):
        if min(scores[dummyrow]) < scores_min:
            scores_min = min(scores[dummyrow])
            
    return scores_min
        
        
    
    
    
    

    
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
    """
    This function takes a current board and a grid of scores. 
    The function should find all of the empty squares with the 
    maximum score and randomly return one of them as a (row, column) tuple. 
    It is an error to call this function with a board that has 
    no empty squares (there is no possible next move), so your function may 
    do whatever it wants in that case. The case where the board is full will not be tested.
    """
    #print "Get BS Started"
    best_score = get_scores_min(scores, board.get_dim())
    best_squares = []
    empty_squares = board.get_empty_squares()
    for square in empty_squares:
        if scores[square[0]][square[1]] > best_score:
            best_score = scores[square[0]][square[1]]
            best_squares = []
            best_squares.append(square)
            
        elif scores[square[0]][square[1]] == best_score:
            
            best_squares.append(square)
            
    
            
    #print "best_score:", best_score        
    if len(best_squares) > 1:
        return random.choice(best_squares)
    else:
        return best_squares[0]


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. The function should use the Monte Carlo 
    simulation described above to return a move for the machine player in the 
    form of a (row, column) tuple. Be sure to use the other functions you have written!
    """
    scores = init_scores(board.get_dim())
    
    
    for dummytrial in range(trials):
        temp_game = board.clone()
        mc_trial(temp_game, player)
        mc_update_scores(scores, temp_game, player)
        
    #print scores
    print "Scores:", scores
    #print temp_game
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


# """
#  TESTING Phase
# """
#    
# 
# game1 = provided.TTTBoard(3)
#      
# game1.move(0, 0, 2)
# game1.move(0, 1, 2)
# game1.move(0, 2, 3)
# #game1.move(1, 0, 3)
# game1.move(1, 1, 2)
# # game1.move(1, 2, 2)
# game1.move(2, 0, 3)
# #game1.move(2, 1, 3)
# game1.move(2, 2, 3)   
#     
#     
# print "Game board"
# print game1
# 
# 
# # scores = [[0, 0, 0], [-9, 0, 3], [0, 14, 0]]
# # 
# # print "Best move:", get_best_move(game1, scores) 
# 
# print "Next move:", mc_move(game1, 2, NTRIALS)   
 

    
 
  

  
  



#mc_trial(game, 2)
#print 
#print game
