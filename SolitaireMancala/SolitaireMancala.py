"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.config = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.config = configuration
        
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        self.reserve_config = list(reversed(self.config))
        return str(self.reserve_config)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return str(self.config[house_num])

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        self.won = True
        for i in range(1,len(self.config)):
            if self.config[i] != 0:
                self.won = False
                break                
        return self.won
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        self.legal = False
        if self.config[house_num] == house_num:
            self.legal = True
        
        return self.legal

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        self.config[house_num] = 0
        for i in range(house_num):
            self.config[i] += 1 

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        self.move = 0
        for i in range(1,len(self.config)):
            if self.is_legal_move(i) == True:
                self.move = i
                break
        return self.move
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        self.moves = []
        self.config_backup = self.config [:]
        tempgame = SolitaireMancala()
        tempgame.set_board(self.config_backup)
        print "temp game:", tempgame
        while not tempgame.is_game_won():
#            print "In while"
            nextStep = tempgame.choose_move()
#            print nextStep
            if nextStep != 0:
                self.moves.append(nextStep)
                tempgame.apply_move(nextStep)
#                 print "Temp game:", tempgame
#                 print "Moves:", self.moves
            else:
                break
            
        return self.moves

 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
#   print "Is the game won ?", my_game.is_game_won()
#    print my_game.is_legal_move(5)
#    my_game.apply_move(5)
#    print my_game
    print "Choose", my_game.choose_move()
    print my_game.plan_moves()

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])

    # add more tests here
    
test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
