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
        
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._need_new_tile = False
        self.reset()
        
        self._direction_dic = {}
        
        # UP
        self._direction_dic['UP'] = []
        for steps in range(self._grid_width):
            self._direction_dic['UP'].append(self.traverse((0, 0 + steps), (1, 0), self._grid_height))
        #print "UP", self._direction_dic['UP']
        
        #DOWN
        self._direction_dic['DOWN'] = []
        for steps in range(self._grid_width):
            self._direction_dic['DOWN'].append(self.traverse((self._grid_height - 1, 0 + steps), (-1, 0), self._grid_height))
        #print "DOWN", self._direction_dic['DOWN']
        
        #LEFT
        self._direction_dic['LEFT'] = []
        for steps in range(self._grid_height):
            self._direction_dic['LEFT'].append(self.traverse((0 + steps, 0), (0, 1), self._grid_width))
        #print "LEFT", self._direction_dic['LEFT']        
        
        
        #RIGHT        
        self._direction_dic['RIGHT'] = []
        
        for steps in range(self._grid_height):
            self._direction_dic['RIGHT'].append(self.traverse((0 + steps, self._grid_width - 1), (0, -1), self._grid_width))
        #print "RIGHT", self._direction_dic['RIGHT']
        #print "DICT", self._direction_dic        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        #print self._cells
        self.new_tile()
        self.new_tile()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        self.__cells_string = ""
        for line in self._cells:
            self.__cells_string = self.__cells_string + str(line) + "\n"
                    
        return self.__cells_string
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
        """
      
        if direction == 1:
            for col_number in range(self._grid_width):
                self._curren_col = []
                self._curren_col =  self._direction_dic['UP'][col_number]
                self.apply_move()
                
#                 self._temp_line = []
#                 for coordinate in range(len(self._curren_col)):
#                     self._temp_line.append(self.get_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1]))
#                 #print "Temp line:", self._temp_line 
#                 self._temp_line = self.merge(self._temp_line)
#                 #print "Merge line:", self._temp_line
#                 for coordinate in range(len(self._curren_col)):
#                     self.set_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1], self._temp_line[coordinate])
#                 #print "_cells from move:", self._cells
            #print self._cells        
                    
                    
#             print coordinate    

 
        elif direction == 2:
            for col_number in range(self._grid_width):
                self._curren_col = []
                self._curren_col =  self._direction_dic['DOWN'][col_number]
                self.apply_move()
#                 self._temp_line = []
#                 for coordinate in range(len(self._curren_col)):
#                     self._temp_line.append(self.get_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1]))
#                 #print "Temp line:", self._temp_line 
#                 self._temp_line = self.merge(self._temp_line)
#                 #print "Merge line:", self._temp_line
#                 for coordinate in range(len(self._curren_col)):
#                     self.set_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1], self._temp_line[coordinate])
#                 #print "_cells from move:", self._cells   
            #print self._cells
            
        elif direction == 3:
            for row_number in range(self._grid_height):
                self._curren_col = []
                self._curren_col =  self._direction_dic['LEFT'][row_number]
                self.apply_move()
#                 self._temp_line = []
#                 for coordinate in range(len(self._curren_col)):
#                     self._temp_line.append(self.get_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1]))
#                 #print "Temp line:", self._temp_line 
#                 self._temp_line = self.merge(self._temp_line)
#                 #print "Merge line:", self._temp_line
#                 for coordinate in range(len(self._curren_col)):
#                     self.set_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1], self._temp_line[coordinate])
#                 #print "_cells from move:", self._cells   
            #print self._cells
        
        elif direction == 4:
            for row_number in range(self._grid_height):
                self._curren_col = []
                self._curren_col =  self._direction_dic['RIGHT'][row_number]
                #print self._curren_col
                self.apply_move() 
            #print self._cells
            
        else:
            print 'You Suck It!'
        
        if self._need_new_tile == True:
            self.new_tile()
            self._need_new_tile = False        
        
    def apply_move(self):     
        """
        Apply a line merge and rewrite back
        """
        
        self._temp_line = []
        for coordinate in range(len(self._curren_col)):
            self._temp_line.append(self.get_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1]))
        #print "Temp line:", self._temp_line 
        self._temp_line2 = self.merge(self._temp_line)
        
        if self._temp_line != self._temp_line2:
            self._need_new_tile = True
        
        #print "Merge line:", self._temp_line
        for coordinate in range(len(self._curren_col)):
            self.set_tile(self._curren_col[coordinate][0], self._curren_col[coordinate][1], self._temp_line2[coordinate])
            #print "_cells from move:", self._cells
          


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        self._zero_grids = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == 0:
                    self._zero_grids.append((row,col))
        #print self._zero_grids
        
        try:
            self._chosen_grid = random.choice(self._zero_grids)
        except IndexError:
            print "NO MORE STEP"
            return
        
        
        if random.random() > 0.9:
                #10% value 4 in new tile
            self.set_tile(self._chosen_grid[0], self._chosen_grid[1], 4)
            #print self._cells
                
        else:
            #90% value 2 in new tile
            #print "row:", self._chosen_grid[0], "col:", self._chosen_grid[1]       
            self.set_tile(self._chosen_grid[0], self._chosen_grid[1], 2)
            #print self._cells
              
 

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._cells[row][col]
    
    def traverse(self, start_cell, direction, num_steps):
        """
        Create a dict to containd list of _cells for each move. The key is direction UP, DOWN, etc.
        """
        self._direction_list = []
        for step in range(num_steps):
            self._dummy_row = start_cell[0] + step * direction[0]
            self._dummy_col = start_cell[1] + step * direction[1]
            self._direction_list.append((self._dummy_row, self._dummy_col))
        return self._direction_list
            
    def order_list(self, line):
        
        """
        Ordering the input list for merge function
        """
        
        self._origin = line
        self._ordered = list()
        self._no_zeros = 0
        # push zero values back 
        for idx in range(len(self._origin)):
            if self._origin[idx] != 0:
                self._ordered.append(self._origin[idx])
            else:
                self._no_zeros += 1
    
        for idx in range(self._no_zeros):
            self._ordered.append(0)
            
        return self._ordered
    
    def merge(self, line):
        """
        Function that merges a single row or column in 2048.
        """    
        self._not_merged = self.order_list(line)
    #     print self._not_merged    
        # Start merging
        skip = False
        for idx in range(len(self._not_merged)-1):
            if skip == False:
                if self._not_merged[idx] == self._not_merged[idx + 1]:
                    self._not_merged[idx] += self._not_merged[idx + 1]
                    self._not_merged[idx + 1] = 0
                    skip = True
    #                 print self._not_merged , idx
                else:
                    continue
            else:
                skip = False
                continue
        self._merged = self.order_list(self._not_merged)    
        
        return self._merged
                     

    
    
        

#  
# game = TwentyFortyEight(4,4)
# game.set_tile(0, 0, 2)
# game.set_tile(0, 1, 0)
# game.set_tile(0, 2, 0)
# game.set_tile(0, 3, 0)
# game.set_tile(1, 0, 0)
# game.set_tile(1, 1, 2)
# game.set_tile(1, 2, 0)
# game.set_tile(1, 3, 0)
# game.set_tile(2, 0, 0)
# game.set_tile(2, 1, 0)
# game.set_tile(2, 2, 2)
# game.set_tile(2, 3, 0)
# game.set_tile(3, 0, 0)
# game.set_tile(3, 1, 0)
# game.set_tile(3, 2, 0)
# game.set_tile(3, 3, 2)
# print game
# game.move(4)
# print game
# game.move(4)
# print game











#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
