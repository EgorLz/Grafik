import pygame
import sys

pygame.init()

cords = [(100, 100), (150, 150), (125, 200), (50, 350), (200, 300)]
cord = sorted(cords , key=lambda k: [k[0], k[1]])

screen = pygame.display.set_mode((400, 400))
screen.fill("white")
pygame.display.set_caption('График')

for i in range(0, len(cords) - 1):
    pygame.draw.line(screen, "red", cord[i], cord[i + 1], width=1)

for i in range(len(cords)):
    pygame.draw.circle(screen, "black", cord[i - 1], 5, width=0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for a in range(len(cords)):
                if int(cord[a - 1][0]) + 3 >= event.pos[0] >= int(cord[a - 1][0]) - 3 and int(cord[a - 1][1]) + 3 >= event.pos[1] >= int(cord[a - 1][1]) - 3:
                    pygame.draw.circle(screen, "green", cord[a - 1], 5, width=0)
                pygame.display.update()
    pygame.display.flip()
