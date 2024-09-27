# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    updatable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    print(
        f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
