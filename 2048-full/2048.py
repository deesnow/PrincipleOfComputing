"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def order_list(line):
    
    """
    Ordering the input list for merge function
    """
    
    origin = line
    ordered = list()
    no_zeros = 0
    # push zero values back 
    for idx in range(len(origin)):
        if origin[idx] != 0:
            ordered.append(origin[idx])
        else:
            no_zeros += 1

    for idx in range(no_zeros):
        ordered.append(0)
        
    return ordered

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """    
    not_merged = order_list(line)
#     print not_merged    
    # Start merging
    skip = False
    for idx in range(len(not_merged)-1):
        if skip == False:
            if not_merged[idx] == not_merged[idx + 1]:
                not_merged[idx] += not_merged[idx + 1]
                not_merged[idx + 1] = 0
                skip = True
#                 print not_merged , idx
            else:
                continue
        else:
            skip = False
            continue
    merged = order_list(not_merged)    
    
    return merged

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        
        
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        #print self.cells
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        self.zero_grids = []
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.cells[row][col] == 0:
                    self.zero_grids.append((row,col))
        #print self.zero_grids
        for self.newtiles_no in range(2):
            self.chosen_grid = random.choice(self.zero_grids)
            if random.random() > 0.9:
                #10% value 4 in new tile
                self.set_tile(self.chosen_grid[0], self.chosen_grid[1], 4)
                #print self.cells
                
            else:
                #90% value 2 in new tile
                #print "row:", self.chosen_grid[0], "col:", self.chosen_grid[1]       
                self.set_tile(self.chosen_grid[0], self.chosen_grid[1], 2)
                #print self.cells
            self.zero_grids.remove(self.chosen_grid)      
 

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cells[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.cells[row][col]


game = TwentyFortyEight(3,4)
print game
print game.get_grid_height()
print game.get_grid_width()




#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
