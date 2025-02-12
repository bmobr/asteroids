# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # main loop
    continue_game = True
    while continue_game:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False

        # last line
        dt = (game_clock.tick(60))/1000
        screen.fill("black")
        pygame.display.flip()
    pygame.quit()
    

if __name__ == "__main__":
    main()