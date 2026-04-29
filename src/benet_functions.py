import pygame

def hangman():
    screen = pygame.display.set_mode((2550, 1375))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
