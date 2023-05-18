import pygame
from random import choice

# Determine the structure and design of the maze
TILES = 50
size = (WIDTH, HEIGHT) = 600, 600
column = WIDTH // TILES
rows = HEIGHT // TILES
GREY = ('grey')
x = 0
y = 0


# standard framework for setting up pygame for the application
pygame.init()
Screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("A STAR ALGORITHM")


# the class keeps track of the cell in the grid
class cell:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # setting the walls as a dictionary
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        # assuming it isn't visited yet
        self.visited = False

    # this function draws starting nodes in rectangular shape
    def draw_first_cell(self, a, b):
        a = self.a * TILES
        b = self.b * TILES
        pygame.draw.rect(Screen, pygame.Color('black'), (a + 2, b + 2, TILES - 2, TILES - 2))

    # The draw function will draw the size and colors of the cells
    def draw(self):
        a, b = self.a * TILES, self.b * TILES
        if self.visited == True:
            pygame.draw.rect(Screen, pygame.Color('darkred'), (a, b, TILES, TILES))

    # check cells in the grid using a and b parameters
    def check_cell(self, a, b):
        index = lambda a, b: a + b * column
        if a < 0 or a > column - 1 or b < 0 or b > rows - 1:
            return False
        return grid[index(a, b)]

    # check neighboring cells
    # The function uses recursion to search the cells and return its neighboring cell if it's found.
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

    # This function removes walls in the cells.
    def remove_walls(self, current, next):
        dx = current.a - next.a
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.b - next.b
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False

        pygame.display.update()


# instance of the 'cell' class in a one-dimensional array
grid = [cell(col, row) for row in range(rows) for col in range(column)]
current_cell = grid[0]
stack = []

# while loop loops through to close the application
while True:
    Screen.fill('darkslateblue')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Draw grid lines
    for x in range(0, WIDTH, TILES):
        pygame.draw.line(Screen, GREY, (x, 0), (x, HEIGHT), 2)
    for y in range(0, HEIGHT, TILES):
        pygame.draw.line(Screen, GREY, (0, y), (WIDTH, y), 2)

    [cell.draw() for cell in grid]
    current_cell.visited = True
    current_cell.draw_first_cell(2, 2)
    second_cell = current_cell.Neighbour()
    if second_cell:
        second_cell.visited = True
        stack.append(current_cell)
        current_cell.remove_walls(current_cell, second_cell)
        current_cell = second_cell

    pygame.mouse.get_pos()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)