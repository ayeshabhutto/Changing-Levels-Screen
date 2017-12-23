#This program is written by Ayesha Bhutto 
from pygame import *
import pygame 

init() #Initializes pygame.
SIZE = 800, 600 #Sets the screen size to 800,600.
screen = display.set_mode(SIZE) 

#sets colours by specfic RGB codes 
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (0,153,153)

running = True
fontHello = font.SysFont("Monospace",37)
text3 = fontHello.render("Your current level is 1", 1, (PINK))

def randomscreen(screen):
    draw.rect(screen, BLUE,(0,0,800,600)) 
    display.flip()
    
def mainmenu(screen):
    draw.rect(screen, BLACK, (0,0,800,800))
    draw.rect(screen, PINK,(250, 125, 330, 100))    
    text = fontHello.render("Start Program" , 1, (RED))	
    screen.blit(text, Rect(275,150,400,100))
    
    draw.rect(screen, PINK,(250, 275, 330, 100))        
    text1 = fontHello.render("Change Level" , 1, (RED))	
    screen.blit(text1, Rect(275,300,400,100))
    
    draw.rect(screen, PINK,(250, 425, 330, 100))        
    text2 = fontHello.render("Exit Game" , 1, (RED))
    screen.blit(text2, Rect(300,450,400,100))
    
    text3
    screen.blit(text3, Rect(200,25,400,100))    

    display.flip()

def levels(screen):
    draw.rect(screen, PINK,(250, 125, 330, 100))    
    text = fontHello.render("   Level 1" , 1, (RED))	
    screen.blit(text, Rect(275,150,400,100))
        
    draw.rect(screen, PINK,(250, 275, 330, 100))        
    text1 = fontHello.render("   Level 2" , 1, (RED))	
    screen.blit(text1, Rect(275,300,400,100))
        
    draw.rect(screen, PINK,(250, 425, 330, 100))        
    text2 = fontHello.render("  Level 3" , 1, (RED))
    screen.blit(text2, Rect(300,450,400,100))    
    display.flip()
    

state = 0

# Main Loop
while running:
    button = 0
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT:
            running = False
        elif evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos          
            button = evnt.button
            if state == 0:
                if mx > 250 and mx < 580 and my > 125 and my < 225:
                    state = 1
                elif mx > 250 and mx < 580 and my > 275 and my < 375:
                    state = 2        
                elif mx > 250 and mx < 580 and my > 425 and my < 525:
                    state = 3
                else:
                    state = 0
            elif state == 1:
                if button == 3:
                    state = 0
            elif state == 2:
                if mx > 250 and mx < 580 and my > 125 and my < 225:
                    text3 = fontHello.render("Your current level is 1", 1, (PINK))
                    state = 0
                elif mx > 250 and mx < 580 and my > 275 and my < 375:
                    text3 = fontHello.render("Your current level is 2", 1, (PINK))
                    state = 0                    
                elif mx > 250 and mx < 580 and my > 425 and my < 525:
                    text3 = fontHello.render("Your current level is 3", 1, (PINK))
                    state = 0                           

    if state == 0:
        mainmenu(screen)
    
    elif state == 1:
        randomscreen(screen)
    
    elif state == 2:
        levels(screen)
        
    elif state == 3:
        running == False
        quit()

    



quit() 

