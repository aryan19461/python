import pygame

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set up the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Whiteboard")

# Set the background color to white
background_color = (255, 255, 255)
screen.fill(background_color)

# Set the drawing color to black
drawing_color = (0, 0, 0)

# Set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the drawing variables
is_drawing = False
last_pos = None

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.FINGERDOWN and event.finger_id == 0):
            is_drawing = True
        elif event.type == pygame.MOUSEBUTTONUP or (event.type == pygame.FINGERUP and event.finger_id == 0):
            is_drawing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION or (event.type == pygame.FINGERMOTION and event.finger_id == 0):
            if is_drawing:
                pos = pygame.mouse.get_pos() if event.type == pygame.MOUSEMOTION else (event.x, event.y)
                if last_pos is not None:
                    pygame.draw.line(drawing_surface, drawing_color, last_pos, pos, 3)
                last_pos = pos

    # Blit the drawing surface onto the screen
    screen.blit(drawing_surface, (0, 0))

    # Update the display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
