import pygame
import math

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Initial Window")
clock = pygame.time.Clock()

SPEED = 8
TILE_SIZE = 30
grid_x = WINDOW_WIDTH 
grid_y = WINDOW_HEIGHT

LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN

running = True 
pos = (0,0)
general_dir = RIGHT

def get_tile_block_pos (x,y):
    tile_x = x//TILE_SIZE
    tile_y = y//TILE_SIZE
    return tile_x, tile_y

def get_tile_start_pos(block_x, block_y):
    x = block_x * TILE_SIZE 
    y = block_y * TILE_SIZE
    return x, y

def move(cur_pos, dir):
    new_x, new_y = cur_pos
    if dir == RIGHT:
        new_x = new_x + TILE_SIZE
        if new_x >= WINDOW_WIDTH-1:
            new_x = 0
    elif dir == LEFT:
        new_x = new_x - TILE_SIZE
        if new_x < WINDOW_WIDTH - WINDOW_WIDTH:
            new_x = WINDOW_WIDTH - TILE_SIZE
    elif dir == UP:
        new_y = new_y - TILE_SIZE
        if new_y < WINDOW_HEIGHT - WINDOW_HEIGHT:
            new_y = WINDOW_HEIGHT - TILE_SIZE
    elif dir == DOWN:
        new_y = new_y + TILE_SIZE
        if new_y >= WINDOW_HEIGHT - TILE_SIZE:
            new_y = 0

    return new_x, new_y

while running:
    print(f"""👉🏻 General direction: {general_dir} 👈🏻""")
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quiting
            print("Quiting")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # detecting clicked grid
            click_x, click_y = event.pos
            tile_x, tile_y = get_tile_block_pos(click_x, click_y)
            pos = get_tile_start_pos(tile_x, tile_y)
            print(f"""👉🏻 Current tile position (0-indexed): {(tile_x,tile_y)} """)
            print(f"""👉🏻 Current tile start position cordinate: {pos} """)
            print("------\n")
        elif event.type == pygame.KEYDOWN:
            print(f"""👀 key {event}""")
            print(f"""👀 pygame key {pygame.K_LEFT}""")
            print(f"""👀 pygame key {pygame.K_UP}""")
            print(f"""👀 pygame key {pygame.K_RIGHT}""")
            print(f"""👀 pygame key {pygame.K_DOWN}""")
            general_dir = event.type
            if event.key in (LEFT, UP, RIGHT, DOWN):
                general_dir = event.key
            else:
                print(f"""😑 unhandled key: {event.key}""")





    # 2. Update game state
    ## main game logic
#    if general_dir == RIGHT:
#        pos = ()
    pos = move(pos, general_dir)


    # 3. Render
    screen.fill((30,30,30)) # clear screen
    # Draw objects
    pygame.draw.rect(screen, pygame.Color("limegreen"),(pos[0], pos[1], TILE_SIZE,TILE_SIZE))
    pygame.draw.circle(screen, pygame.Color("deeppink"), (TILE_SIZE//2, TILE_SIZE//2), TILE_SIZE//2, 1)



    pygame.display.flip() # refreshes screen/ updates display
    clock.tick(SPEED) # limit to 60 FPS

pygame.quit()

