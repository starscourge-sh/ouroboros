import pygame
import random

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Initial Window")
clock = pygame.time.Clock()

SPEED = 5
TILE_SIZE = 30

tile_num_x = WINDOW_WIDTH//TILE_SIZE
tile_num_y = WINDOW_HEIGHT//TILE_SIZE

running = True 

parts = [(0,0)]
general_dir = pygame.K_RIGHT

VALID_MOVES = {
        pygame.K_RIGHT :[pygame.K_UP, pygame.K_DOWN],
        pygame.K_LEFT :[pygame.K_UP, pygame.K_DOWN],
        pygame.K_UP: [pygame.K_LEFT, pygame.K_RIGHT],
        pygame.K_DOWN: [pygame.K_LEFT, pygame.K_RIGHT],
        }

def get_tile_block_pos (x,y):
    tile_x = x//TILE_SIZE
    tile_y = y//TILE_SIZE
    return tile_x, tile_y

def get_tile_start_pos(block_x, block_y):
    return block_x * TILE_SIZE ,block_y * TILE_SIZE

def move(cur_pos, direction):
    new_x, new_y = cur_pos
    match direction:
        case pygame.K_RIGHT:
            new_x = new_x + TILE_SIZE
            if new_x >= WINDOW_WIDTH - 1:
                new_x = 0
        case pygame.K_LEFT:
            new_x = new_x - TILE_SIZE
            if new_x < WINDOW_WIDTH - WINDOW_WIDTH:
                new_x = WINDOW_WIDTH - TILE_SIZE
        case pygame.K_UP:
            new_y = new_y - TILE_SIZE
            if new_y < WINDOW_HEIGHT - WINDOW_HEIGHT:
                new_y = WINDOW_HEIGHT - TILE_SIZE
        case pygame.K_DOWN:
            new_y = new_y + TILE_SIZE
            if new_y >= WINDOW_HEIGHT - 1:
                new_y = 0
    return new_x, new_y


def spawn_food():
    f = (random.randrange(0,tile_num_x),random.randrange(0,tile_num_y))
    # Ensure food position does not overlap with snake body 
    while True:
        if f in parts:
            f = (random.randrange(0,tile_num_x),random.randrange(0,tile_num_y))
        else: 
             return f[0] *TILE_SIZE, f[1] * TILE_SIZE


food = spawn_food()
print(f""""🌭 food: {food}""")

while running:
    # 1. Handle events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: # quiting
                print("Quiting")
                running = False
            case pygame.MOUSEBUTTONDOWN: # detecting clicked grid
                click_x, click_y = event.pos
                tile_x, tile_y = get_tile_block_pos(click_x, click_y)
                food = (tile_x, tile_y)
                print(f"""👉🏻 Current tile position (0-indexed): {(tile_x,tile_y)} """)
                print(f"""👉🏻 Current tile start position cordinate: {parts[0]} """)
                print("------\n")
            case pygame.KEYDOWN:
                if event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT):
                    if event.key in VALID_MOVES[general_dir]:
                        general_dir = event.key
                else:
                    print(f"""😑 unhandled key: {event.key}""")

    # 2. Update game state
    ## main game logic
    old_head = parts[0]
    old_tail = parts[-1]
    new_head = move(parts[0], general_dir) #
    # body = parts[1:] # body (excl head)

    # loop through all parts and have each (except for head) inherit position of last
    new_whole = []
    for index, part in enumerate(parts):
        if index == 0: 
            new_whole.append(new_head)
        else:
            p = parts[index-1]
            new_whole.append(p)
    parts = new_whole

    ## check for head + food collisions
    ### food overlap?
    print(f"""🐞 parts: {parts}, food: {food}""")
    if parts[0] == food:
        print("🍫 EATING")
        food = spawn_food()
        parts.append(old_tail)

    ### body overlap?
    for index, part in enumerate(parts):
        if index == 0: #skip, this is our head/reference point
            continue
        else:
            if parts[index] == parts[0]:
                print("🔴 GAME OVER: Self-eat")
                running = False

    # 3. Render
    screen.fill((30,30,30)) # clear screen
    ## Draw objects
    for part in parts:
        pygame.draw.rect(screen, pygame.Color("limegreen"),(part[0], part[1], TILE_SIZE,TILE_SIZE))

    pygame.draw.circle(screen, pygame.Color("deeppink"), (food[0] + (TILE_SIZE//2), food[1] + (TILE_SIZE//2)), TILE_SIZE//2, 0)

    pygame.display.flip() # refreshes screen / updates display
    clock.tick(SPEED) # limit to <SPEED> FPS

pygame.quit()

