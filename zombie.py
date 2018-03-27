"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._human_list = []
        self._zombie_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        return (zombie for zombie in self._zombie_list)

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        return (human for human in self._human_list)
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        grid_height = poc_grid.Grid.get_grid_height(self)
        grid_width = poc_grid.Grid.get_grid_width(self)
        visited = poc_grid.Grid(grid_height, grid_width)
        distance_field = [[grid_height * grid_width for dummy_col in range(grid_width)]
                          for dummy_row in range(grid_height)]
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        elif entity_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
        for entity in boundary:
            visited.set_full(entity[0], entity[1])
            distance_field[entity[0]][entity[1]] = 0
        while len(boundary) > 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for idx, human in enumerate(self._human_list):
            neighbors = self.eight_neighbors(human[0],human[1])
            maxi = zombie_distance_field[human[0]][human[1]]
            move = human
            for neighbor in neighbors:
                if (self.is_empty(neighbor[0], neighbor[1]) and 
                    zombie_distance_field[neighbor[0]][neighbor[1]] > maxi):
                    maxi = zombie_distance_field[neighbor[0]][neighbor[1]]
                    move = neighbor
            self._human_list[idx] = move
                
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for idx, zombie in enumerate(self._zombie_list):
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            mini = human_distance_field[zombie[0]][zombie[1]]
            move = zombie
            for neighbor in neighbors:
                if human_distance_field[neighbor[0]][neighbor[1]] < mini:
                    mini = human_distance_field[neighbor[0]][neighbor[1]]
                    move = neighbor
            self._zombie_list[idx] = move
        

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))

#test = Apocalypse(5,6,[(2,1),(3,2)],[(1,1),(2,5),(0,4)],[(0,1),(3,0)])
#print test
#print test._human_list
#print test._zombie_list
#test.clear()
#print test
#print test._human_list
#print test._zombie_list
#test.add_zombie(3,1)
#print test._zombie_list
#print test.num_zombies()
#print test.zombies()
#dist = test.compute_distance_field('HUMAN')
#for row in range(5):
#    print dist[row]
#test.move_zombies(dist)
#print test._zombie_list