import pygame
import time
import random

pygame.init()

yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)               #Potential colour pallette
red = (255, 0, 0)
white = (255, 255, 255)               
blue = (0, 0, 255)

display_width = 800
display_height = 600

Snake_block = 10

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snakey Jakey')

game_over = False
 

x1 = (int(display_width/2))
y1 = (int(display_height/2))

x1_change = 0  
y1_change = 0

def gameLoop():
    game_over = False
    game_close = False


foodx = round(random.randrange(0, display_width - Snake_block) / 10.0) * 10.0                #Generates food randomly
foody = round(random.randrange(0, display_height - Snake_block) / 10.0) * 10.0
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

Snake_list = []
Length_of_snake = 1

def Snakey_Jakey(Snake_block, Snake_list):
    for x in Snake_list:                                            #Supposed to make define the snake so I can make it longer later
        pygame.draw.rect(dis, white, [x[0], x[1], 10, 10])
    


def message(msg,color):
    mesg = font_style.render(msg, True, color)            
    dis.blit(mesg, [100, 300])


while not game_over:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
             game_over= True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:           #Controls
               x1_change = -Snake_block
               y1_change = 0
            elif event.key == pygame.K_RIGHT:
               x1_change = Snake_block
               y1_change = 0
            elif event.key == pygame.K_UP:
               x1_change = 0
               y1_change = -Snake_block
            elif event.key == pygame.K_DOWN:
               x1_change = 0
               y1_change = Snake_block

       if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:          # Boundary
           game_over = True

       x1 += x1_change
       y1 += y1_change
       dis.fill(black)
       pygame.draw.rect(dis, white, [x1, y1, Snake_block, Snake_block])
       pygame.draw.rect(dis, green, [(int(foodx)), (int(foody)), Snake_block, Snake_block])          
       Snake_head = []
       Snake_head.append(x1)
       Snake_head.append(y1)                                    #To make the snake longer
       Snake_list.append(Snake_head)
       if len(Snake_list) > Length_of_snake:
          del Snake_list[0]

       for x in Snake_list[:-1]:                          #So if you eat yourself game is over
           if x == Snake_head:
              game_close = True

       Snakey_Jakey(Snake_block, Snake_list)

       pygame.display.update()
  
       if x1 == foodx and y1 == foody:
          foodx = round(random.randrange(0, display_width - Snake_block) / 10.0) * 10.0
          foody = round(random.randrange(0, display_height - Snake_block) / 10.0) * 10.0
          Length_of_snake += 1 
          

   

       clock.tick(30)

message("Snakey Jakey is no longer awakey",red)
pygame.display.update()
time.sleep(2)
   
pygame.quit()
quit()  

gameLoop()