# A * algorithm implementation of a maze application.
# Depth first search is used to create the maze application


import pygame
from random import choice

#Determine the structure and design of the maze
TILES = 50
size = (WIDTH, HEIGHT) = 600, 600
colunm = WIDTH // TILES
rows = HEIGHT // TILES
GREY = ('grey')
x = 0
y = 0



# standard frame work for setting up pygame for the application
pygame.init()
Screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("A STAR ALGORITHM")



# the class keeps track of the cell in the grid
class cell:
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        # setting the walls as dictionary
        self.walls = {'top': True, 'right': True, 'buttom': True, 'left': True}
        # assumming it isn't visited yet
        self.visited = False

    # this function draws starting nodes in rectangular shape
    def draw_first_cell( self, a, b):
        a = self.a * TILES
        b = self.b * TILES
        pygame.draw.rect(Screen,pygame.Color('black'), (a + 2, b + 2, TILES - 2, TILES - 2))
    
        
    # The draw function will draw the size and colours of the cells
    def draw(self):
        a, b = self.a * TILES, self.b * TILES
        if self.visited:
            pygame.draw.rect(Screen, pygame.Color('darkred'), (a, b, TILES, TILES))
            
        for x in range(0, 600, 50):
            pygame.draw.line(Screen, GREY, (1,x), (600,x),2)
            pygame.draw.line(Screen, GREY, (x,1), (x,600),2)


    # check cells in the grid using a and b parameters
    def check_cell(self, a, b):
        index = lambda a, b: a + b * colunm
        if a < 0 or a > colunm - 1 or b < 0 or b > rows - 1:
            return False
        return grid[index(a, b)]


    # check neighbouring cells 
    # The function uses recursion to search the cells and return its neighbouring cell if it's found.
    def Neighbour(self):
        neighbour = []
        top = self.check_cell(self.a, self.b - 1)
        right = self.check_cell(self.a + 1, self.b)
        bottom = self.check_cell(self.a, self.b + 1)
        left = self.check_cell(self.a - 1, self.b)
        if top and not top.visited:
            neighbour.append(top)
        if right and not right.visited:
            neighbour.append(right)
        if bottom and not bottom.visited:
            neighbour.append(bottom)
        if left and not left.visited:
            neighbour.append(left)
        return choice(neighbour) if neighbour else False


    # # This functions removes walls in the cells.
    def remove_walls(current):
        x = current.a
        if x == 1:
            current.walls['left'] = False
        elif x == -1:
            current.walls['right'] = False
        y = current.b
        if y == 1:
            current.walls['top'] = False
        elif y == -1:
            current.walls['bottom'] = False

        pygame.display.update()



    
# instance of the 'cell' class in one dimentional array
grid = [cell(col, row) for row in range(rows) for col in range(colunm)]
current_cell = grid[0]
stack = []



# while loop loops through, to close the application 
while True:
    Screen.fill('darkslateblue')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    [cell.draw() for cell in grid]
    current_cell.visited = True
    current_cell.draw_first_cell(2, 2)
    second_cell = current_cell.Neighbour()
    if second_cell:
        cell.visited = True
        stack.append(current_cell)
        current_cell.remove_walls()
        current_cell = second_cell
        
    pygame.mouse.get_pos()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)