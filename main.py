import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # limits game to at most 60fps, computes & returns how much time has passed since prev call
        dt_in_ms = clock.tick(60)
        dt = dt_in_ms / 1000  # convert to seconds


if __name__ == "__main__":
    main()
