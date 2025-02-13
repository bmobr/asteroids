# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import * 
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # pygame group permite adicionar sprites a um grupo, para chamar métodos comuns a classe sprite de uma vez para todos do grupo
    # usar esse método antes de declarar as instâncias
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
    player = Player(x,y)
    asteroidfield = AsteroidField()

    # usar esse método para adicionar no grupo após instanciar
    # updatable.add(player)
    # drawable.add(player)

    # main loop
    continue_game = True
    while continue_game:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False

        updatable.update(dt)

        # checar colisão
        for obj in asteroids:
            if (player.check_collision(obj)):
                print("Game over!")
                sys.exit()

        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)   

        pygame.display.flip()

        # limita framerate a 60 fps
        dt = game_clock.tick(60)/1000

    pygame.quit()
    

if __name__ == "__main__":
    main()