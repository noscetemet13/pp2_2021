import pygame, sys
from pygame.locals import *
import random
import time

pygame.init()
clock=pygame.time.Clock()
black=(0, 0, 0)
white=(255, 255, 255)
screen=pygame.display.set_mode((600,600))
# images
backgroundpic=pygame.image.load("backimg.png")
carpic=pygame.image.load("Playerr.png")
theend=pygame.image.load("gameover.png")
# bg music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

score=0
font3=pygame.font.SysFont("Times", 20)

pygame.display.set_caption("Cars")
# classes for player, enemy, bg and coins
class player(object):
	def __init__(self):
		self.x=300
		self.y=480
		self.width=57
		self.height=116
		self.shift=5
	def draw(self, screen):
		screen.blit(carpic, (self.x, self.y))

class background(object):
	def __init__(self):
		self.x=0
		self.y1=0
		self.y2=-600
		self.speed=4
	def draw(self, screen):
		screen.blit(backgroundpic, (self.x, self.y1))
		screen.blit(backgroundpic, (self.x, self.y2))

class enemy(object):
	def __init__(self):
		self.en=0
		self.x=random.randrange(30, 450)
		self.y=-750
		self.width=57
		self.height=116
		self.speeds=(4, 8, 12, 16, 20)
		self.speed=random.choice(self.speeds)
	def draw(self, screen):
		if self.en==0:
			enpic=pygame.image.load("Enemy.png")
		elif self.en==1:
			enpic=pygame.image.load("Enemy2.png")
		elif self.en==2:
			enpic=pygame.image.load("Enemy3.png")
		elif self.en==3:
			enpic=pygame.image.load("Enemy4.png")
		elif self.en==4:
			enpic=pygame.image.load("Enemy5.png")
		screen.blit(enpic, (self.x, self.y))

class coin(object):
	def __init__(self):
		self.x=random.randrange(30, 450)
		self.y=-750
		self.speed=12
		self.width=40
		self.height=50
	def draw(self, screen):
		coinpic=pygame.image.load("coin.png")
		screen.blit(coinpic, (self.x, self.y))

gameover=False
# initializing obj
car=player()
back=background()
opp=enemy()
coins=coin()
# game loop
while not gameover:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover=True
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and car.x>car.shift:
		car.x-=car.shift
	if keys[pygame.K_RIGHT] and car.x<483-car.shift:
		car.x+=car.shift
	back.draw(screen)
	back.y1+=back.speed
	back.y2+=back.speed
	if back.y1>=600:
		back.y1= -600
	if back.y2>=600:
		back.y2= -600
	opp.y-=(opp.speed/4)
	opp.draw(screen)
	opp.y+=opp.speed
	coins.y-=(coins.speed/4)
	coins.draw(screen)
	coins.y+=coins.speed
	car.draw(screen)
	if opp.y>600:
		opp.y= 0 - opp.height
		opp.x=random.randrange(30, 450)
		opp.en=random.randrange(0, 5)
		opp.speed=random.choice(opp.speeds)
	if car.y<opp.y+110:
		# if car.x-5>enx and car.x-5<enx+enwidth-5 or car.x+51>enx-5 and car.x+51<enx+enwidth-5:
		if opp.x in range(car.x-5, car.x+51):
			pygame.display.flip()
			pygame.mixer.music.stop()
			pygame.mixer.Sound('crash-sound.mp3').play()
			time.sleep(1)
			screen.blit(theend, (0,0))
			pygame.display.flip()
			time.sleep(2)
			gameover=True
		if opp.x+opp.width-5 in range(car.x-5, car.x+51):
			pygame.display.flip()
			pygame.mixer.music.stop()
			pygame.mixer.Sound('crash-sound.mp3').play()
			time.sleep(1)
			screen.blit(theend, (0,0))
			pygame.display.flip()
			time.sleep(2)
			gameover=True
	if coins.y>600:
		coins.y=-750
		coins.x=random.randrange(30, 450)
	if car.y<coins.y+50:
		# if car.x>=coinx and car.x<=coinx+coinwidth or car.x+56>=coinx and car.x+56<=coinx+coinwidth:
		if coins.x+coins.width in range(car.x, car.x+56):
			pygame.mixer.Sound('coin.wav').play()
			coins.y=-750
			coins.x=random.randrange(30, 450)
			score+=1
		if coins.x in range(car.x, car.x+56):
			pygame.mixer.Sound('coin.wav').play()
			coins.y=-750
			coins.x=random.randrange(30, 450)
			score+=1
	screen.blit(font3.render("Score: " + str(score), True, black, white), (512, 36))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()