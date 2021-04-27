# --------------------------------------- imports
import pygame
import random


# --------------------------------------- game function
def play(W, H):
    pygame.init()

    # ---------------- Game Window
    window = pygame.display.set_mode((W, H))
    window.fill((255, 255, 255))
    BCKGR = (255, 255, 255)
    pygame.display.update()
    fps = 50
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # ---------------- Game Variables
    running = True

    snakeSize = 40
    snakePos = [W/2 - 10, H/2-snakeSize]
    speed = 5
    margin = 5
    points = 0

    appleSize = 25
    applePos = [random.randint(
                margin, W-margin), random.randint(margin, H-margin)]

    dirs = [False, False, False, False]  # Format as [Left, Right, Up, Down]

    # ---------------- Game Loop
    clock = pygame.time.Clock()

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            # ---------- Quit Window
            if event.type == pygame.QUIT:
                running = False
            # ---------- Escape Button Quit Window
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                dirs[0] = True
                for i in range(1, len(dirs)):
                    dirs[i] = False

            if keys[pygame.K_RIGHT]:
                dirs[1] = True
                for i in [0, 2, 3]:
                    dirs[i] = False

            if keys[pygame.K_UP]:
                dirs[2] = True
                for i in [0, 1, 3]:
                    dirs[i] = False

            if keys[pygame.K_DOWN]:
                dirs[3] = True
                for i in [0, 1, 2]:
                    dirs[i] = False

        # Left
        if dirs[0] == True:
            snakePos[0] -= speed
            if snakePos[0] < -margin:
                snakePos[0] = W

        # Right
        if dirs[1] == True:
            snakePos[0] += speed
            if snakePos[0] > W+margin:
                snakePos[0] = 0

        # Up
        if dirs[2] == True:
            snakePos[1] -= speed
            if snakePos[1] < -margin:
                snakePos[1] = H

        # Down
        if dirs[3] == True:
            snakePos[1] += speed
            if snakePos[1] > H+margin:
                snakePos[1] = 0

        window.fill(BCKGR)
        pygame.draw.rect(window, GREEN, pygame.Rect(
            snakePos[0], snakePos[1], snakeSize, snakeSize))
        pygame.draw.rect(window, RED, pygame.Rect(
            applePos[0], applePos[1], appleSize, appleSize))

        if pygame.Rect(snakePos[0], snakePos[1], snakeSize, snakeSize).colliderect(pygame.Rect(applePos[0], applePos[1], appleSize, appleSize)):
            applePos = [random.randint(
                margin, W-margin), random.randint(margin, H-margin)]
            pygame.draw.rect(window, RED, pygame.Rect(
                applePos[0], applePos[1], appleSize, appleSize))
            points += 1

        pygame.display.update()


# --------------------------------------- needed if statement
if __name__ == "__main__":
    play(600, 500)
