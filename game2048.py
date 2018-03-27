"""
Clone of 2048 game.
"""

import poc_2048_gui
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

def move_tiles(worklist):
    """
    Function that slides tiles to next available position
    """
    slidelist = []
    for index in range(len(worklist)):
        if worklist[index] != 0:
            slidelist.append(worklist[index])
    zerolist = [0] * (len(worklist)-len(slidelist))
    slidelist.extend(zerolist)                                
    return slidelist

def join_tiles(worklist, index):
    """
    Function that merges two tiles with same value 
    next to each other to form one tile with double value
    """
    joinlist = list(worklist)
    if joinlist[index] == joinlist[index+1]:
        joinlist[index] *= 2
        joinlist[index+1] = 0
    return joinlist

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    worklist = list(move_tiles(line))
    #resultlist = [0]* len(worklist)
    for index in range(len(worklist)-1):
        if worklist[index] == 0:
            worklist = move_tiles(worklist)
        worklist = join_tiles(worklist, index) 
    return worklist

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._up_ind = [(0,col) for col in range(self._grid_width)]
        self._down_ind = [((self._grid_height-1),col) for col in range(self._grid_width)]
        self._left_ind = [(row,0) for row in range(self._grid_height)]
        self._right_ind = [(row,(self._grid_width-1)) for row in range(self._grid_height)]
        self._initial_tiles = {UP:self._up_ind, DOWN:self._down_ind, 
                              LEFT:self._left_ind, RIGHT:self._right_ind}
        self._step_number = {UP:self._grid_height, DOWN:self._grid_height,
                            LEFT:self._grid_width, RIGHT:self._grid_width}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        grid_string = ""
        for row in range(self._grid_height):
            grid_string += str(self._grid[row])
            grid_string += "\n"
        return grid_string

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
        """
        # replace with your code
        changed = False
        for tile in self._initial_tiles[direction]:
            temp_list = []
            index_list = []
            for step in range(self._step_number[direction]):
                row = tile[0] + step*OFFSETS[direction][0]
                col = tile[1] + step*OFFSETS[direction][1]
                temp_list.append(self._grid[row][col])
                index_list.append([row,col])
            merge_list = list(merge(temp_list))
            for index in range(len(merge_list)):
                self.set_tile(index_list[index][0],index_list[index][1],merge_list[index])
                if temp_list[index] != merge_list[index] and changed == False:
                    changed = True
        if changed:
            self.new_tile()
                

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        value = random.choice([2,2,2,2,2,2,2,2,2,4])
        empty_tiles = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    empty_tiles.append([row,col])
        if len(empty_tiles) != 0:
            pos = random.choice(empty_tiles)
            self.set_tile(pos[0],pos[1],value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#Testing
#game = TwentyFortyEight(5,3)
#print game
#print game.get_grid_height()
#print game.get_grid_width()
#game.set_tile(3,1,2)
#print game
#game.reset()
#print game
#game.set_tile(2,2,8)
#print game
#print game.get_tile(0,0)
#print game.get_tile(2,2)
#agame = TwentyFortyEight(2,2)
#print agame
#agame.new_tile()
#print agame
#agame.new_tile()
#print agame
#agame.new_tile()
#print agame
#game.move(UP)
#print game
#game.set_tile(2,0,0)
#print game