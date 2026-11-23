import pygame
import math

pygame.init()

# Window
WIDTH, HEIGHT = 1200, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sine Graph Visualizer")

clock = pygame.time.Clock()

angle = 0
points = []
n = 0

font = pygame.font.SysFont("Arial", 22)
title_font = pygame.font.SysFont("Arial", 45)

running = True
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    screen.fill((60, 65, 66))

    pygame.draw.line(screen, (255, 255, 255), (275, 0), (275, 550), 3)
    pygame.draw.line(screen, (255, 255, 255), (550, 0), (548, 550), 3)
    pygame.draw.line(screen, (255, 255, 255), (0, 275), (WIDTH, 275), 3)
    
    pygame.draw.circle(screen, (255, 255, 255), (275, 275), 200, 3)

    angle -= math.radians(1)

    if 2*math.pi + angle < 0.00001:
        angle = 0

    y = 275 + math.sin(angle) * 200
    x = 275 + math.cos(angle) * 200
    x_alt = 275 - math.cos(angle) * 200
    pygame.draw.circle(screen, (0, 255, 255), (x, y), 5)
    pygame.draw.circle(screen, (0, 255, 255), (x_alt, y), 5)

    coordinate_x = (x-275)/200
    coordinate_y = (y-275)/200

    coordinate_text = font.render(f"y={round((coordinate_y)*100)/100}", True, (0, 255, 255))
    screen.blit(coordinate_text, (min(x, x_alt), y+10))

    formula_example_text = font.render("y=sin(θ)=sin(180°-θ)", True, (255, 255, 255))

    if round(round(math.degrees(angle))%10) == 0 or n==0:
        formula_text = font.render(f"{round((coordinate_y)*100)/100}=sin({-1*round(math.degrees(angle))}°)=sin({180+round(math.degrees(angle))})", True, (255, 255, 255))
    screen.blit(formula_example_text, (750, 485))
    screen.blit(formula_text, (750, 522))

    for i in range(round(min(x, x_alt)), WIDTH-10, 25):
        pygame.draw.line(screen, (255, 255, 255), (i, y), (i + 12, y), 3)


    points.append([WIDTH-10, y])
    for point in points:
        point[0] -= 1
        if point[0] <= 550:
            points.pop(points.index(point))
        pygame.draw.circle(screen, (255, 255, 255), (point[0], point[1]), 3)

    title_line_1 = title_font.render("Sine Graph", True, (0, 255, 255))
    title_line_2 = title_font.render("Visualization", True, (0, 255, 255))
    title_line_3 = font.render("By Advik Jha", True, (0, 255, 255))
    if points[0][0] > 745:
        screen.blit(title_line_1, (575, 25))
        screen.blit(title_line_2, (575, 75))
        screen.blit(title_line_3, (575, 125))

    n=1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()