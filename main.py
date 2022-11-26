import pygame
import time

#Creating Window
WIDTH,HEIGHT =900,600   
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("GAME")     #caption of window

#necessary variables and functions  
WHITE=(255,255,255)
FPS=60

#function to draw items into window  in a single loop
def draw_window():
    WIN.fill(WHITE)        #giving  color
    pygame.display.update()#updating      


#crating pygame event loop  inside the main function   
def main():
    clock=pygame.time.Clock()         #to set  fps  ==  looping
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #while quitting window
            if event.type==pygame.QUIT :
                run =False
        draw_window()   #drawing into window  one time in one loop
    pygame.quit()            


#this below helps to only run main()  only while imported
if __name__=="__main__":
    main()