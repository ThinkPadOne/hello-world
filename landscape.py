# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 100
circle_x2 = 400
circle_y2 = 50
frame = 0
meteorx = 640
meteory = 0
debris1x = 700
debris1y = -80
debris2x = 750
debris2y = -120
debris3x = 650
debris3y = -150

# ---------------------------

running = True
while running:
    frame += 1
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            pos = event.pos
            code = f"pygame.draw.circle(screen, (250, 250, 250), {pos}, 40)"
            print(code)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill("#87CEEB")  # always the first drawing command

    pygame.draw.circle(screen, (255, 255, 0), (0, 0), 80)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x, circle_y), 40)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x+50, circle_y-10), 40)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x+100, circle_y), 40)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x2, circle_y2), 40)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x2+50, circle_y2-10), 40)
    pygame.draw.circle(screen, (250, 250, 250), (circle_x2+100, circle_y2), 40)

    points = [
        [300, 150],
        [150, 250],
        [450, 250],
    ]
    pygame.draw.polygon(screen, (0, 0, 0), points)

    points2 = [
        [0, 480],
        [0, 400],
        [640, 400],
        [640, 480],
    ]
    pygame.draw.polygon(screen, (0, 128, 0), points2)

    points3 = [
        [200, 250],
        [400, 250],
        [400, 400],
        [200, 400],
    ]
    pygame.draw.polygon(screen, (255, 255, 0), points3)

    points4 = [
        [225, 260],
        [275, 260],
        [275, 300],
        [225, 300], 
    ]
    pygame.draw.polygon(screen, (173, 216, 230), points4)

    points5 = [
        [325, 260],
        [375, 260],
        [375, 300],
        [325, 300], 
    ]
    pygame.draw.polygon(screen, (173, 216, 230), points5)

    points6 = [
        [275, 325],
        [325, 325],
        [325, 400],
        [275, 400], 
    ]
    pygame.draw.polygon(screen, (139, 0, 0), points6)

    points7 = [
        [0, 0],
        [640, 0],
        [640, 480],
        [0, 480], 
    ]

    if circle_x+ 50 < -70:
        circle_x += 750
    else:
        circle_x -=5

    if circle_x2+ 50 < -70:
        circle_x2 += 750
    else:
        circle_x2 -=5

    if frame >= 150:
        meteor = pygame.draw.circle(screen, (0, 0, 0), (meteorx, meteory), 60)
        debris1 = pygame.draw.circle(screen, (255,0,0), (debris1x, debris1y), 10)
        debris2 = pygame.draw.circle(screen, (255,0,0), (debris2x, debris2y), 10)
        debris3 = pygame.draw.circle(screen, (255,0,0), (debris3x, debris3y), 10)
        if meteorx < 300:
            pygame.draw.polygon(screen, (255, 224, 32), points7)
        else:
            meteorx -=3
            meteory +=5
            debris1x -=3
            debris1y +=5
            debris2x -=3
            debris2y +=5
            debris3x -=3
            debris3y +=5

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
