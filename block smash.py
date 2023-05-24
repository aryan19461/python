import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Block Smasher")

# Set up game clock
clock = pygame.time.Clock()

# Set up game fonts
font = pygame.font.SysFont(None, 40)

# Set up game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up game variables
block_speed = 5
score = 0

# Set up the player paddle
paddle_width = 75
paddle_height = 15
paddle_x = WINDOW_WIDTH // 2 - paddle_width // 2
paddle_y = WINDOW_HEIGHT - paddle_height - 10

# Set up the ball
ball_radius = 10
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed_x = 3
ball_speed_y = 3

# Set up the blocks
block_width = 50
block_height = 20
block_rows = 5
block_cols = 8
blocks = []
for row in range(block_rows):
    block_row = []
    for col in range(block_cols):
        block_x = col * (block_width + 5) + 10
        block_y = row * (block_height + 5) + 10
        block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
        block_row.append(block_rect)
    blocks.append(block_row)

# Set up game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= 5
    if keys[pygame.K_RIGHT]:
        paddle_x += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WINDOW_WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius < 0:
        ball_speed_y *= -1
    if ball_y + ball_radius > WINDOW_HEIGHT:
        game_running = False

    # Check for ball collision with paddle
    if ball_rect := pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2).colliderect(pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)):
        ball_speed_y *= -1

    # Check for ball collision with blocks
    for row in range(block_rows):
        for col in range(block_cols):
            block_rect = blocks[row][col]
            if block_rect is not None and (ball_rect := pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)).colliderect(block_rect):
                blocks[row][col] = None
                ball_speed_y *= -1
                score += 1

    # Draw the game objects
    game_window.fill(WHITE)
    pygame.draw.rect(game_window, BLACK, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw
