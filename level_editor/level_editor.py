import pygame

# Initialize pygame
pygame.init()

# Set the display size
DISPLAY_SIZE = (1920, 1080)

# Create the dislay surface
screen = pygame.display.set_mode(DISPLAY_SIZE)

# Load the images
tile_size = (64, 64)

tile_map = pygame.image.load("level_editor/tile_map.png")
width, height = tile_map.get_size()
tile_images = []

for y in range(0, height, 32):
    for x in range(0, width, 32):
        tile = tile_map.subsurface((x, y, 32, 32))
        tile_images.append(pygame.transform.scale(tile, (64, 64)))

level_data = [[0 for x in range(DISPLAY_SIZE[0] // tile_size[0])] for y in range(DISPLAY_SIZE[1] // tile_size[1])]

# Set the starting tile
current_tile = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            # Calculate the index of the tile was clicked
            x = pos[0] // tile_size[0]
            y = pos[1] // tile_size[1]
            if event.button == 1:
                if pos[1] >= 128:
                    # Left click - place or remove tile
                    try:
                        level_data[y][x] = current_tile if level_data[y][x] == 0 else 0
                    except IndexError:
                        print("List out of range")
            elif event.button == 4:
                # Mousewheel up - switch to next tile
                current_tile = (current_tile + 1) % len(tile_images)
            elif event.button == 5:
                # Mousewheel down - switch to previous tile
                current_tile = (current_tile - 1) % len(tile_images)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Save the level data to a file
                with open("levels/level.dat", "w") as f:
                    for row in level_data:
                        f.write(" ".join([str(i) for i in row]) + "\n")
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the tiles
    for y in range(len(level_data)):
        for x in range(len(level_data[y])):
            pygame.draw.line(screen, (25, 25, 25), (x * 64, y * 64), (x * 64 + 64, y * 64 + 0))
            pygame.draw.line(screen, (25, 25, 25), (x * 64, y * 64), (x * 64+ 0, y *64+ 64))
            if level_data[y][x] > 0:
                screen.blit(tile_images[level_data[y][x] - 1], (x * tile_size[0], y * tile_size[1]))
    

    # Show the current tile on screen
    pygame.draw.rect(screen, (25, 25, 25), pygame.Rect(0, 0, DISPLAY_SIZE[0], 128))
    pygame.draw.line(screen, (50,50,50), (0, 128), (DISPLAY_SIZE[0], 128))
    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(31, 31, 66, 66))
    screen.blit(tile_images[current_tile - 1], (32, 32))
    # Update the display
    pygame.display.flip()