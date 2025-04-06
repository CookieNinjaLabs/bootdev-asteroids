from sys import exit

import pygame

from constants import MAX_FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from objects.asteroid import Asteroid
from objects.asteroidfield import AsteroidField
from objects.player import Player
from objects.shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                exit("Game over!")
            for bullet in shots:
                if bullet.isColliding(asteroid):
                    asteroid.kill()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        delta = clock.tick(MAX_FPS)
        dt = delta / 1000
        pass


if __name__ == "__main__":
    main()
