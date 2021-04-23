import pygame
import serial
import time

BACKGROUND = (0, 0, 0)

serCom = serial.Serial('COM7', 9600)
serCom.timeout = 1

# window's properties
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
screen.fill(BACKGROUND)

# setting servos to their base location
serCom.write("X0Y0".encode())

running = True
while running:
    screen.fill(BACKGROUND)
    mouseX,mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    portX = int(180 - mouseX / (width / 180))
    portY = int(mouseY / (width/ 180))
    print("X: ", portX)
    print("Y: ", portY)
    thinger = "X{x}Y{y}".format(x = portX, y = portY)
    serCom.write(str(thinger).encode())
    time.sleep(0.02)

    pygame.display.flip()

serCom.write("X0Y0".encode())

pygame.quit()
serCom.close()
