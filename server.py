import pygame
import random
import sys
import socket

pygame.init()

screen_width, screen_height = 800, 600

white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Шарики")


class Ball:
    def __init__(self):
        self.radius = random.randint(20, 50)
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


balls = []


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.23.21.223', 16789))
server_socket.listen(1)
connection, address = server_socket.accept()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for ball in balls:
        ball.draw()

    pygame.display.flip()


    data = connection.recv(1024)
    if data == b'button_pressed':
        new_ball = Ball()
        balls.append(new_ball)


    balls = [ball for ball in balls if ball.y + ball.radius < screen_height]


    for ball in balls:
        ball.y += 2


    screen.fill(white)