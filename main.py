import pygame
import time
import os



#Creating Window
WIDTH,HEIGHT =900,600   
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")     #caption of window
BORDER=pygame.Rect(WIDTH/2,0,10,HEIGHT)
#necessary variables and functions  
WHITE=(255,255,255)
FPS=60
VEL=5
BLACK=(0,0,0)
SPACESHIP_HEIGHT,SPACESHIP_WIDTH=55,40

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))#loading image 
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),90)#image size reduction and rotation

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),270)







#function to draw items into window  in a single loop

def draw_window():
#    !!!!!!!write everything in an order  cus  it executes each line and draws on top of each other
    WIN.fill(WHITE)        #giving  color    
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))#we use blit to draw our image  within the screen size  ,images are drawn from top left(0,0) in pygame without coordinates
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()#updating      


def YELLOW_KEYBOARD_MOVEMENT(keys_pressed,yellow):

    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:         #LEFT  key pressed
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL<BORDER.x:         #RIGHT  key pressed
        yellow.x+=VEL
    if keys_pressed[pygame.K_w]:         #UP  key pressed
        yellow.y-=VEL            
    if keys_pressed[pygame.K_s]:         #DOWN key pressed
        yellow.y+=VEL     
def RED_KEYBOARD_MOVEMENT(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]:         #LEFT  key pressed
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT]:         #RIGHT  key pressed
        red.x+=VEL
    if keys_pressed[pygame.K_UP]:         #UP  key pressed
        red.y-=VEL            
    if keys_pressed[pygame.K_DOWN]:         #DOWN key pressed
        red.y+=VEL



#crating pygame event loop  inside the main function   

def main():
    clock=pygame.time.Clock()         #to set  fps  ==  looping    , we create a clock object 
    global yellow  #declaring globally 
    global red
    red=pygame.Rect(700,300,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)#creating a rectangle around our spaceship to track its movements
    yellow = pygame.Rect(100,300,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #while quitting window
            if event.type==pygame.QUIT :
                run =False
        #red.x+=1
        #yellow.x-=1        
        keys_pressed =pygame.key.get_pressed()#initializing keys
        YELLOW_KEYBOARD_MOVEMENT(keys_pressed,yellow)
        RED_KEYBOARD_MOVEMENT(keys_pressed,red)       
        draw_window()   #drawing into window  one time in one loop
    pygame.quit()            


#this below helps to only run main()  only while imported
if __name__=="__main__":
    main()