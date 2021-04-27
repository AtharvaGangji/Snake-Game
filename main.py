# --------------------------------------- imports
import pygame


# --------------------------------------- game function
def play():
    pygame.init()

    # ---------------- Game Window
    window = pygame.display.set_mode((500, 500))
    window.fill((20, 222, 30))
    pygame.display.update()

    # ---------------- Game Loop
    running = True

    while running:
        for event in pygame.event.get():
            # ---------- Quit Window
            if event.type == pygame.QUIT:
                running = False
            # ---------- Escape Button Quit Window
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


# --------------------------------------- needed if statement
if __name__ == "__main__":
    play()
