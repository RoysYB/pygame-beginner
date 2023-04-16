import pygame
import time
import os
pygame.font.init()
pygame.mixer.init()#for sounds

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
RED=(255,0,0)
YELLOW=(255,255,0)
SPACESHIP_HEIGHT,SPACESHIP_WIDTH=55,40
red_bullets=[]
yellow_bullets=[]
max_bullets=3
bullet_vel=5
red_health=5
yellow_health=5
#getting the bullet sound
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join('Assets','laser.mp3'))
BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join('Assets','explosion.mp3'))


#creating an event for bullet collission with space ship
YELLOW_HIT=pygame.USEREVENT+1  #it would be some number of events +1 th event
RED_HIT=pygame.USEREVENT+2
SPACE=pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.jpg')),(WIDTH,HEIGHT))


YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))#loading image 
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),90)#image size reduction and rotation

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),270)



#creating fonts 
Health_font=pygame.font.SysFont('Comicsans',40)
WINNER_FONT=pygame.font.SysFont('Comicsans',100)


#function to draw items into window  in a single loop

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
#    !!!!!!!write everything in an order  cus  it executes each line and draws on top of each other
    #WIN.fill(WHITE)        #giving  background color    is not given pygame draws on top of the previous frame   
    WIN.blit(SPACE,(0,0))#giving space image as the background
    pygame.draw.rect(WIN,WHITE,BORDER)
    
    red_health_text=Health_font.render("Health:"+str(red_health),1,WHITE)
    yellow_health_text=Health_font.render("Health:"+str(yellow_health),1,WHITE)
    # 
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))#we use blit to draw our image  within the screen size  ,images are drawn from top left(0,0) in pygame without coordinates
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
         
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
         

    pygame.display.update()#updating      



def YELLOW_KEYBOARD_MOVEMENT(keys_pressed,yellow):

    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:         #LEFT  key pressed
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL+SPACESHIP_WIDTH<BORDER.x:         #RIGHT  key pressed
        yellow.x+=VEL
    if keys_pressed[pygame.K_w]   and yellow.y-VEL>0 :         #UP  key pressed
        yellow.y-=VEL            
    if keys_pressed[pygame.K_s] and yellow.y+VEL+SPACESHIP_HEIGHT<HEIGHT:         #DOWN key pressed
        yellow.y+=VEL     
def RED_KEYBOARD_MOVEMENT(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VEL>WIDTH/2:         #LEFT  key pressed
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT]  and red.x+VEL+SPACESHIP_WIDTH<WIDTH:         #RIGHT  key pressed
        red.x+=VEL
    if keys_pressed[pygame.K_UP]  and red.y-VEL>0:         #UP  key pressed   set to zero since the  border begins from zero from top
        red.y-=VEL            
    if keys_pressed[pygame.K_DOWN] and red.y+SPACESHIP_HEIGHT<HEIGHT:         #DOWN key pressed
        red.y+=VEL



#function for checking the bullet hit etc   
def bullet_hit(yellow_bullets,red_bullets,yellow, red):
    for bullet in yellow_bullets:
        bullet.x+=bullet_vel
        if red.colliderect(bullet):   #colliderect built in with pygame which returns  if pixels collided
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=bullet_vel
        if yellow.colliderect(bullet):   #colliderect built in with pygame which returns  if pixels collided
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x<0:
            red_bullets.remove(bullet)




def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


#crating pygame event loop  inside the main function
def main():
    clock=pygame.time.Clock()         #to set  fps  ==  looping    , we create a clock object 
    global yellow  #declaring globally 
    global red
    global red_health
    global yellow_health
    red=pygame.Rect(700,300,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)#creating a rectangle around our spaceship to track its movements
    yellow = pygame.Rect(100,300,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #while quitting window
            if event.type==pygame.QUIT :
                run =False
            #firing bullets
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(yellow_bullets)<max_bullets:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)#// is integer division since rect doesnot support floating point numbers
                    yellow_bullets.append(bullet) 
                    BULLET_FIRE_SOUND.play()   
                if event.key==pygame.K_RCTRL and len(red_bullets)<max_bullets:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type==RED_HIT:
                 red_health-=1
                 BULLET_HIT_SOUND.play()
            if event.type==YELLOW_HIT:
                  yellow_health-=1
                  BULLET_HIT_SOUND.play()
        
        winner_text=""
        if red_health==0:
            winner_text="Yellow Wins!!"
        if yellow_health==0:             
            winner_text="Red Wins!!"  
        if winner_text!='':
            #pass
            draw_winner(winner_text)
            break    
        #red.x+=1
        #yellow.x-=1   
        #print(red_bullets,"and ",yellow_bullets)     #just printing the bullets lists
        keys_pressed =pygame.key.get_pressed()#initializing keys
        YELLOW_KEYBOARD_MOVEMENT(keys_pressed,yellow)
        RED_KEYBOARD_MOVEMENT(keys_pressed,red)       
        bullet_hit(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)   #drawing into window  one time in one loop
    pygame.quit()            


#this below helps to only run main()  only while imported
if __name__=="__main__":
    main()
