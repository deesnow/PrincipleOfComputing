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



class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        
        """
        create dictionary for grid list (row, col), the key is direction UP, DOWN, .....
        It's a helper for cell move
        """
        self.direction_dic = {}
        
        # UP
        self.direction_dic['UP'] = []
        for steps in range(self.grid_width):
            self.direction_dic['UP'].append(self.traverse((0, 0 + steps), (1, 0), self.grid_height))
        #print "UP", self.direction_dic['UP']
        
        #DOWN
        self.direction_dic['DOWN'] = []
        for steps in range(self.grid_width):
            self.direction_dic['DOWN'].append(self.traverse((self.grid_height - 1, 0 + steps), (-1, 0), self.grid_height))
        #print "DOWN", self.direction_dic['DOWN']
        
        #LEFT
        self.direction_dic['LEFT'] = []
        for steps in range(self.grid_height):
            self.direction_dic['LEFT'].append(self.traverse((0 + steps, 0), (0, 1), self.grid_width))
        #print "LEFT", self.direction_dic['LEFT']        
        
        
        #RIGHT        
        self.direction_dic['RIGHT'] = []
        
        for steps in range(self.grid_height):
            self.direction_dic['RIGHT'].append(self.traverse((0, self.grid_width - steps - 1), (0, -1), self.grid_width))
        #print "RIGHT", self.direction_dic['RIGHT']
        #print "DICT", self.direction_dic        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        #print self.cells
        self.new_tile()
        self.new_tile()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self.cells_string = ""
        for line in self.cells:
            self.cells_string = self.cells_string + str(line) + "\n"
                    
        return self.cells_string
    
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
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
        """
      
        if direction == 'UP':
            for col_number in range(self.grid_width):
                self.curren_col = []
                self.curren_col =  self.direction_dic['UP'][col_number]
                self.apply_move()
                
#                 self.temp_line = []
#                 for coordinate in range(len(self.curren_col)):
#                     self.temp_line.append(self.get_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1]))
#                 #print "Temp line:", self.temp_line 
#                 self.temp_line = self.merge(self.temp_line)
#                 #print "Merge line:", self.temp_line
#                 for coordinate in range(len(self.curren_col)):
#                     self.set_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1], self.temp_line[coordinate])
#                 #print "Cells from move:", self.cells
            #print self.cells        
                    
                    
#             print coordinate    

 
        elif direction == 'DOWN':
            for col_number in range(self.grid_width):
                self.curren_col = []
                self.curren_col =  self.direction_dic['DOWN'][col_number]
                self.apply_move()
#                 self.temp_line = []
#                 for coordinate in range(len(self.curren_col)):
#                     self.temp_line.append(self.get_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1]))
#                 #print "Temp line:", self.temp_line 
#                 self.temp_line = self.merge(self.temp_line)
#                 #print "Merge line:", self.temp_line
#                 for coordinate in range(len(self.curren_col)):
#                     self.set_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1], self.temp_line[coordinate])
#                 #print "Cells from move:", self.cells   
            #print self.cells
            
        elif direction == 'LEFT':
            for row_number in range(self.grid_height):
                self.curren_col = []
                self.curren_col =  self.direction_dic['LEFT'][row_number]
                self.apply_move()
#                 self.temp_line = []
#                 for coordinate in range(len(self.curren_col)):
#                     self.temp_line.append(self.get_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1]))
#                 #print "Temp line:", self.temp_line 
#                 self.temp_line = self.merge(self.temp_line)
#                 #print "Merge line:", self.temp_line
#                 for coordinate in range(len(self.curren_col)):
#                     self.set_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1], self.temp_line[coordinate])
#                 #print "Cells from move:", self.cells   
            #print self.cells
        
        elif direction == 'RIGHT':
            for row_number in range(self.grid_height):
                self.curren_col = []
                self.curren_col =  self.direction_dic['RIGHT'][row_number]
                #print self.curren_col
                self.apply_move() 
            #print self.cells
            
        else:
            print 'You Suck It!'
        
        self.new_tile()        
        
    def apply_move(self):     
        """
        Apply a line merge and rewrite back
        """
        
        self.temp_line = []
        for coordinate in range(len(self.curren_col)):
            self.temp_line.append(self.get_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1]))
        print "Temp line:", self.temp_line 
        self.temp_line = self.merge(self.temp_line)
        print "Merge line:", self.temp_line
        for coordinate in range(len(self.curren_col)):
            self.set_tile(self.curren_col[coordinate][0], self.curren_col[coordinate][1], self.temp_line[coordinate])
            #print "Cells from move:", self.cells
          


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
    
    def traverse(self, start_cell, direction, num_steps):
        """
        Create a dict to containd list of cells for each move. The key is direction UP, DOWN, etc.
        """
        self.direction_list = []
        for step in range(num_steps):
            self.dummy_row = start_cell[0] + step * direction[0]
            self.dummy_col = start_cell[1] + step * direction[1]
            self.direction_list.append((self.dummy_row, self.dummy_col))
        return self.direction_list
            
    def order_list(self, line):
        
        """
        Ordering the input list for merge function
        """
        
        self.origin = line
        self.ordered = list()
        self.no_zeros = 0
        # push zero values back 
        for idx in range(len(self.origin)):
            if self.origin[idx] != 0:
                self.ordered.append(self.origin[idx])
            else:
                self.no_zeros += 1
    
        for idx in range(self.no_zeros):
            self.ordered.append(0)
            
        return self.ordered
    
    def merge(self, line):
        """
        Function that merges a single row or column in 2048.
        """    
        self.not_merged = self.order_list(line)
    #     print self.not_merged    
        # Start merging
        skip = False
        for idx in range(len(self.not_merged)-1):
            if skip == False:
                if self.not_merged[idx] == self.not_merged[idx + 1]:
                    self.not_merged[idx] += self.not_merged[idx + 1]
                    self.not_merged[idx + 1] = 0
                    skip = True
    #                 print self.not_merged , idx
                else:
                    continue
            else:
                skip = False
                continue
        self.merged = self.order_list(self.not_merged)    
        
        return self.merged
                     

    
    
        


game = TwentyFortyEight(4,4)
game.set_tile(0, 0, 2)
game.set_tile(0, 1, 0)
game.set_tile(0, 2, 0)
game.set_tile(0, 3, 0)
game.set_tile(1, 0, 0)
game.set_tile(1, 1, 2)
game.set_tile(1, 2, 0)
game.set_tile(1, 3, 0)
game.set_tile(2, 0, 0)
game.set_tile(2, 1, 0)
game.set_tile(2, 2, 2)
game.set_tile(2, 3, 0)
game.set_tile(3, 0, 0)
game.set_tile(3, 1, 0)
game.set_tile(3, 2, 0)
game.set_tile(3, 3, 2)
print game
game.move('RIGHT')
print game











#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
