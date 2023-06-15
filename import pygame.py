import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
screen = pygame.display.set_mode((600, 400))

# Define player properties
player_color = (255, 0, 0)
player_size = 50
player_x = 300
player_y = 300

# Define obstacle properties
obstacle_color = (0, 255, 0)
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, 550)
obstacle_y = random.randint(0, 350)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get player inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Check for collision with obstacle
    if player_x + player_size > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_size > obstacle_y and player_y < obstacle_y + obstacle_height:
        print("Game Over")
        running = False

    # Draw player
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, player_color, player)

    # Draw obstacle
    obstacle = pygame.Rect(obstacle_x, obstacle_y,
                           obstacle_width, obstacle_height)
    pygame.draw.rect(screen, obstacle_color, obstacle)

    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()
