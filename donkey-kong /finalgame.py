import pygame
import time
import random
pygame.init()
finalscore = 0
white=(255,255,255)
black=(0,0,0)
red=(255,127,0)
gold=(255,165,0)
pink=(255,0,127)
green = (0,251,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Donkey kong')
h = 480
i = 380
j = 280
k = 180
l = 80
d = 570
d2 = 570
m = 0
f = 1

gameExit = False
player_x = 0
player_y = 560
player_x_change = 0
player_y_change = 0
donkey_x = 0
state = 0
bg = pygame.image.load("mario.png")
randocoinx = random.randrange(250,550)
randocoinx2 = random.randrange(250,550)
randocoinx3 = random.randrange(250,550)
font = pygame.font.SysFont(None,25)
def message_to_screen(msg,color):
   screen_text = font.render(msg,True,color)
   gameDisplay.blit(screen_text,[400,300])
img1=pygame.image.load('coin.gif')
img=pygame.image.load('ladder.jpg')
img = pygame.transform.scale(img,(40,90))
clock = pygame.time.Clock()
while not gameExit:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	    	gameExit = True
	    if event.type == pygame.KEYDOWN:
	    	if event.key == pygame.K_a:
	            player_x_change = -10
	            player_y_change = 0
	        elif event.key == pygame.K_w:
	            player_y_change = -10
	            player_x_change = 0
	        elif event.key == pygame.K_d:
	            player_x_change = 10
	            player_y_change = 0
	        elif event.key == pygame.K_s:
	            player_y_change = 10
	            player_x_change = 0
	    if event.type == pygame.KEYUP:
	        if event.key == pygame.K_a or event.key == pygame.K_d:
	            player_x_change = 0
	            player_y_change = 0
	        elif event.key == pygame.K_w or event.key == pygame.K_s:
	            player_x_change = 0
	            player_y_change = 0
    if player_x >= 760 and player_x_change > 0:
        player_x_change = 0
    if player_y <= 10 and player_y_change < 0:
    	player_y_change = 0
    if player_x <= 10 and player_x_change < 0:
    	player_x_change = 0
    if player_y >= 560 and player_y_change > 0:
	player_y_change = 0
    t = player_x + player_x_change
    s = player_y + player_y_change    
    if  (finalscore)%85 == 0 and player_y < 50:
	h = 480
        i = 380
        j = 280
        k = 180
        l = 80
        d = 570
        d2 = 570
	player_x = 0
	player_y = 560
	m = 0
	message_to_screen("you sucessfully completed the game",green)
	pygame.display.update()
	time.sleep(2)
    if ((s <= 550 and s >= 490) and (t < 400 or t > 410)) or ((s <= 460 and s >= 390) and (t < 200 or t > 210)) or ((s <= 360 and s >= 290) and (t < 350 or t > 360)) or((s <= 260 and s >= 190) and (t < 200 or t > 210)) or ((s <= 65 and s >= 40) and (t < 200 or t > 300)) or ((s <= 160 and s >= 90) and (t < 500 or t > 510)):
        player_y_change = 0    
    if state == 0:	
        donkey_x = donkey_x + 5
    if donkey_x > 300 and state == 0:
        donkey_x = donkey_x - 5
        state = 1	
    if state == 1:
	donkey_x = donkey_x - 5
    if state == 1 and donkey_x < 10:
        donkey_x = donkey_x + 5
        state = 0	
    player_x += player_x_change
    player_y += player_y_change
    if (player_x <= (randocoinx + 20)    and player_y >= (h - 20)):
    	if player_x >= (randocoinx - 20):
		if (player_y <= (h + 20)):
			finalscore = finalscore + 5
			h = 922
    if (player_x <= (randocoinx2 + 20)):
    	if player_x >= (randocoinx2 - 20):
		if  (player_y <= (i + 20)): 
			if player_y >= (i - 20):
				finalscore = finalscore + 5
				i = 921
    if (player_x <= (randocoinx + 20)):
    	if  player_x >= (randocoinx - 20):
		if (player_y <= (j + 20)):
			if  player_y >= (j - 20):
				finalscore = finalscore + 5
				j = 920
    if (player_x <= (randocoinx2 + 20)) :
    	if  player_x >= (randocoinx2 - 20):
		if  (player_y <= (k + 20)):
			if  player_y >= (k - 20):
				finalscore = finalscore + 5
				k = 910
    if player_x <= (randocoinx3 + 20):
    	if  (player_x >= (randocoinx3 - 20)):
		if  player_y <= (l + 20) and player_y >= (l - 20):
			finalscore = finalscore + 5
			l = 909
    if (player_x <= (randocoinx + 20) and player_x >= (randocoinx - 20)) and (player_y <= (d + 20) and player_y >= (d - 20)):
	finalscore = finalscore + 5
	d = 906
    if (player_x <= (randocoinx3 + 20) and player_x >= (randocoinx3 - 20)) and (player_y <= (d2 + 20) and player_y >= (d2 - 20)):
	finalscore = finalscore + 5
	d2 = 900
    if  ((player_x <= 290 and player_x >= 200)  and (player_y >= 0 and player_y <= 50)) and (m == 0):
        finalscore = finalscore + 50	    
	m = 1
  
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,black,[0,590,800,10])
    pygame.draw.rect(gameDisplay,black,[100,400,800,10])    
    pygame.draw.rect(gameDisplay,black,[120,200,800,10])
    pygame.draw.rect(gameDisplay,black,[0,100,600,10])
    pygame.draw.rect(gameDisplay,black,[0,300,600,10])
    pygame.draw.rect(gameDisplay,black,[200,0,10,50])
    pygame.draw.rect(gameDisplay,pink,[230,20,30,30])
    pygame.draw.rect(gameDisplay,black,[290,0,10,50])
    pygame.draw.rect(gameDisplay,black,[200,50,100,10])
    pygame.draw.rect(gameDisplay,black,[0,500,600,10])
    img = pygame.transform.scale(img,(40,90))
    gameDisplay.blit(img,(400,500))
    img = pygame.transform.scale(img,(40,105))
    gameDisplay.blit(img,(200,400))
    gameDisplay.blit(img,(350,300))
    gameDisplay.blit(img,(500,100))
    gameDisplay.blit(img,(200,200))
    img = pygame.transform.scale(img,(40,30))
    gameDisplay.blit(img,(50,570))
    gameDisplay.blit(img,(50,500))
    gameDisplay.blit(img,(400,270))
    gameDisplay.blit(img,(400,200))	
    gameDisplay.blit(img1,(randocoinx,h))
    gameDisplay.blit(img1,(randocoinx2,i))
    gameDisplay.blit(img1,(randocoinx,j))
    gameDisplay.blit(img1,(randocoinx2,k))
    gameDisplay.blit(img1,(randocoinx3,l))
    gameDisplay.blit(img1,(randocoinx,d))
    gameDisplay.blit(img1,(randocoinx3,d2))
    if (player_y+20) % 200==100 or (player_y+10)%200 == 100:
	if player_x>600:
		player_y=player_y+100
    if (player_y+20)%200 ==0 or (player_y+10)%200==0:
	if player_x<100:
		player_y=player_y+100	
    pygame.draw.rect(gameDisplay,red,[player_x,player_y,20,30])
    gameDisplay.blit(bg,(donkey_x,80))
    pygame.display.update()
    clock.tick(20)	
message_to_screen("score =="+str(finalscore),red)
time.sleep(2)
pygame.display.update()
pygame.quit()
quit()

