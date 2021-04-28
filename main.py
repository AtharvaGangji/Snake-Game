# --------------------------------------- imports
import pygame
import time


# --------------------------------------- game function
def play():
    pygame.init()  # initialized pygame

    # ---------------- Game Window
    window = pygame.display.set_mode((500, 500))
    window.fill((20, 222, 30))
    pygame.display.update()

    # ---------------- variables
    X = 250
    Y = 200
    direction = ""
    time_sleep = 0.04

    # ---------------- Snake
    snake = pygame.image.load("resources/block.jpg").convert()  # load image

    # ---------------- snake position
    def snake_position():
        window.fill((20, 222, 30))  # fill background with defined colour
        window.blit(snake, (X, Y))  # draw image on the screen
        pygame.display.update()  # update the screen
    snake_position()

    # ---------------- Game Loop
    running = True

    while running:

        # ---------------- border thing
        if X >= 501:
            X = 0
            direction = "RIGHT"  # direction to right
        elif X <= 1:
            X = 500
            direction = "LEFT"  # direction to left
        if Y >= 501:
            Y = 0
            direction = "DOWN"  # direction to down
        elif Y <= 1:
            Y = 500
            direction = "UP"  # direction to up

        # ---------------- Move snake in some direction
        if direction == "UP":
            Y -= 10
            time.sleep(time_sleep)  # time sleep
            snake_position()
        elif direction == "DOWN":
            Y += 10
            time.sleep(time_sleep)  # time sleep
            snake_position()
        elif direction == "LEFT":
            X -= 10
            time.sleep(time_sleep)  # time sleep
            snake_position()
        elif direction == "RIGHT":
            X += 10
            time.sleep(time_sleep)  # time sleep
            snake_position()

        for event in pygame.event.get():
            # ---------- Quit Window
            if event.type == pygame.QUIT:  # Quit window if close button pressed
                running = False
            # ---------- Track Buttons
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape Button Quit Window
                    running = False
                if event.key == pygame.K_UP:  # Key up move snake
                    direction = "UP"
                if event.key == pygame.K_DOWN:  # Key down move snake
                    direction = "DOWN"
                if event.key == pygame.K_RIGHT:  # Key down move snake
                    direction = "RIGHT"
                if event.key == pygame.K_LEFT:  # Key down move snake
                    direction = "LEFT"


# --------------------------------------- needed if statement
if __name__ == "__main__":
    play()
