import pygame, sys
from pygame.locals import *
import random
import time

pygame.init()
clock=pygame.time.Clock()
blue=(0, 0, 255)
green=(0, 255, 0)
red=(255, 0, 0)
black=(0, 0, 0)
white=(255, 255, 255)
screen=pygame.display.set_mode((600,600))
class player(object):
	def __init__(self):
		self.x=300
		self.y=480
		self.width=57
		self.height=116
		self.shift=5
	def draw(self, screen):
		screen.blit(carpic, (self.x, self.y))
background=pygame.image.load("backimg.png")
bx=0
by1=0
by2=-600
speed=4
score=0
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)
font3=pygame.font.SysFont("Times", 20)
theend=pygame.image.load("gameover.png")
pygame.display.set_caption("Cars")
def Enemies(enx, eny, enemy):
	if enemy==0:
		enpic=pygame.image.load("Enemy.png")
	elif enemy==1:
		enpic=pygame.image.load("Enemy2.png")
	elif enemy==2:
		enpic=pygame.image.load("Enemy3.png")
	elif enemy==3:
		enpic=pygame.image.load("Enemy4.png")
	elif enemy==4:
		enpic=pygame.image.load("Enemy5.png")
	screen.blit(enpic, (enx, eny))
def Coins(coinx, coiny):
	coinpic=pygame.image.load("coin.png")
	screen.blit(coinpic, (coinx, coiny))
carpic=pygame.image.load("Playerr.png")
gameover=False
enspeeds=(4, 8, 12, 16, 20)
enemy_speed=random.choice(enspeeds)
enemy=0
y_en=0
enx=random.randrange(30, 450)
eny=-750
enwidth=57
enheight=116
coinx=random.randrange(30, 450)
coiny=-750
coin_speed=12
coinwidth=40
coinheight=50
car=player()
while not gameover:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover=True
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and car.x>car.shift:
		car.x-=car.shift
	if keys[pygame.K_RIGHT] and car.x<483-car.shift:
		car.x+=car.shift
	screen.blit(background, (bx, by1))
	screen.blit(background, (bx, by2))
	by1+=speed
	by2+=speed
	if by1>=600:
		by1= -600
	if by2>=600:
		by2= -600
	eny-=(enemy_speed/4)
	Enemies(enx, eny, enemy)
	eny+=enemy_speed
	coiny-=(coin_speed/4)
	Coins(coinx, coiny)
	coiny+=coin_speed
	car.draw(screen)
	if eny>600:
		eny= 0 - enheight
		enx=random.randrange(30, 450)
		enemy=random.randrange(0, 5)
	if car.y<eny+110:
		# if car.x-5>enx and car.x-5<enx+enwidth-5 or car.x+51>enx-5 and car.x+51<enx+enwidth-5:
		if enx in range(car.x-5, car.x+51):
			pygame.display.flip()
			pygame.mixer.music.stop()
			pygame.mixer.Sound('crash-sound.mp3').play()
			time.sleep(1)
			screen.blit(theend, (0,0))
			pygame.display.flip()
			time.sleep(2)
			gameover=True
		if enx+enwidth-5 in range(car.x-5, car.x+51):
			pygame.display.flip()
			pygame.mixer.music.stop()
			pygame.mixer.Sound('crash-sound.mp3').play()
			time.sleep(1)
			screen.blit(theend, (0,0))
			pygame.display.flip()
			time.sleep(2)
			gameover=True
	if coiny>600:
		coiny=-750
		coinx=random.randrange(30, 450)
	if car.y<coiny+50:
		# if car.x>=coinx and car.x<=coinx+coinwidth or car.x+56>=coinx and car.x+56<=coinx+coinwidth:
		if coinx+coinwidth in range(car.x, car.x+56):
			pygame.mixer.Sound('coin.wav').play()
			coiny=-750
			coinx=random.randrange(30, 450)
			score+=1
		if coinx in range(car.x, car.x+56):
			pygame.mixer.Sound('coin.wav').play()
			coiny=-750
			coinx=random.randrange(30, 450)
			score+=1
	screen.blit(font3.render("Score: " + str(score), True, black, white), (512, 36))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()