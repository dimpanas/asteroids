import sys
import pygame
import pygame
from asteroid import Asteroid
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    SHOT_RADIUS
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame exited by user.")
        pygame.quit()