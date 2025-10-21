import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Define sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers to classes

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    ##infinite loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0)) # makes screen black
        updatable.update(dt)
        drawable.update(dt)
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
                
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Cap the frame rate at 60 FPS


if __name__ == "__main__":
    main()
