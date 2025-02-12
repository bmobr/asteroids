# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # screen colors, RGB
    black_screen = (0, 0, 0)
    white_screen = (255, 255, 255)

    # main loop
    continue_game = True
    while continue_game:
        screen.fill(black_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False

        # last line
        pygame.display.flip()
    pygame.quit()
    

if __name__ == "__main__":
    main()