#this was written by Aidan Mcdonald on january 22th of 2022 
#written 1 month into learning programing and python
import random
import pygame
import time
pygame.font.init()


#this is to create the window 
WID = 800
HIG = 500
WIN = pygame.display.set_mode((WID, HIG))

#ball postition and movement on the x and y coordinates
B_X = 397
B_Y = 247 
BMX = 4
BMY = 4

#right side paddle coordinates
RP_X = 790
RP_Y = 235

#left side paddle coordinates
LP_X = 3
LP_Y = 235

#colors used
WHITE = (255,255,255)
DARK_GREY = (128,128,128)

#right and left side score 
L_SCORE = 0
R_SCORE = 0
FONT = pygame.font.SysFont('comicsans', 40)

#this enables the fps throttleing fucntion down below
clock = pygame.time.Clock()

#this draws the points onto the score 
def POINT_PROJECTION ():
    RIGHT_SCORE_TEXT = FONT.render(str(L_SCORE), 1, WHITE)
    WIN.blit(RIGHT_SCORE_TEXT, (10, 10))
    LEFT_SCORE_TEXT = FONT.render(str(R_SCORE), 1, WHITE)
    WIN.blit(LEFT_SCORE_TEXT, (765, 10))

RUN = True
while RUN:
    
#this draws the black background  
    WIN.fill((0,0,0))

#this draws the centerline into the game
    pygame.draw.rect(WIN, (DARK_GREY), (398,0,4,500))
    
#this draws the ball into the game    
    pygame.draw.rect(WIN, (WHITE), (B_X,B_Y,6,6))

#this is to reflect the ball off the top and bottom of window
    B_X += BMX 
    B_Y += BMY
    if B_Y< 494:
        BMY = BMY* -1
    if B_Y> 0:
        BMY = BMY* -1 

#this is to reflect the ball off the paddle 
    if B_Y< RP_Y+ 30 and B_Y> RP_Y and B_X>= 787:
        BMX = BMX* -1
    if B_Y< LP_Y+ 30 and B_Y> LP_Y and B_X<= 6:
        BMX = BMX* -1
       
#these two place the paddles on the screen and they operate key input to make the paddles move     
    pygame.draw.rect(WIN, (WHITE), (LP_X,LP_Y,6,30))
    KEY_PRESSED = pygame.key.get_pressed()
    if ((KEY_PRESSED[pygame.K_w]) and (LP_Y> 0)):
        LP_Y -= 9
    if ((KEY_PRESSED[pygame.K_s])and (LP_Y< 470)):
        LP_Y += 9   

    pygame.draw.rect(WIN, (WHITE), (RP_X,RP_Y,6,30))
    KEY_PRESSED = pygame.key.get_pressed()
    if ((KEY_PRESSED[pygame.K_UP]) and (RP_Y> 0)):
        RP_Y -= 9
    if ((KEY_PRESSED[pygame.K_DOWN]) and (RP_Y< 470)):
        RP_Y += 9

#this is to moniter if ball breaks the left or right barrier and add to the score, also it cahnges which side to serve to 
    if B_X< 0:
        R_SCORE = R_SCORE + 1
        B_X = 397
        B_Y = 247
        if BMX<0:
            BMX = -1
            BMX= BMX* -1
            RANDOM_MOVEMENT = random.randint(2,5)
            BMX= BMX* RANDOM_MOVEMENT
    if B_X> 800:
        L_SCORE = L_SCORE + 1
        B_X = 397
        B_Y = 247
        if BMX> 0:
            BMX = 1
            BMX = BMX* -1
            RANDOM_MOVEMENT = random.randint(2,5)
            BMX= BMX* RANDOM_MOVEMENT

    POINT_PROJECTION ()

    pygame.display.update()

    if L_SCORE == 5:
        LEFT_WON = FONT.render('LEFT SIDE PLAYER WON', 1, WHITE)
        WIN.blit(LEFT_WON, (150, 10))
        pygame.display.update()
        time.sleep(5)
        RUN = False
    if R_SCORE == 5:
        RIGHT_WON = FONT.render('RIGHT SIDE PLAYER WON', 1, WHITE)
        WIN.blit(RIGHT_WON, (150, 10))
        pygame.display.update()
        time.sleep(5)
        RUN = False

#this limits the fps to 60 so the game doesnt run faster and slower based on whos computer is being used
    clock.tick(30)

#this lets you exit the game if you x out of the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False 
pygame.quit()