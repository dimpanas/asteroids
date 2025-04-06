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
)
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    asteroid_field =  AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        updateable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit() 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame exited by user.")
        pygame.quit()