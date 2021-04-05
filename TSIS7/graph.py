import pygame
import math
pygame.init()
width=800
height=600
white=(255,255,255)
black=(0,0,0)
red=(151,32,32)
blue=(32,32,151)
font1=pygame.font.SysFont("Times", 18)
font1.set_italic(True)
font2=pygame.font.SysFont("Times", 18)
font2.set_italic(True)
font2.set_underline(True)
font3=pygame.font.SysFont("Times", 29)
font4=pygame.font.SysFont("Times", 18)
fontbold=pygame.font.SysFont("Times", 18)
fontbold.set_bold(True)
fontbold.set_italic(True)
ys=('1.00', '0.75', '0.50', '0.25', '0.00', '-0.25', '-0.50', '-0.75', '-1.00')
xs=('-3п', '-2п', '-п', '0', 'п', '2п', '3п')
xs1=('5п', '3п', 'п', 'п', '3п', '5п')
sin_coor=[]
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sine and Cosine Waves')
screen.fill(white)
pygame.draw.rect(screen, black, (60, 15, 712, 520), 2)
pygame.draw.line(screen, black, (416, 15), (416, 535), 2)
pygame.draw.line(screen, black, (60, 275), (772, 275), 2)
for lin in range(80, 772, 112):
	pygame.draw.line(screen, black, (lin, 15), (lin, 535))
for lin in range(35, 535, 60):
	pygame.draw.line(screen, black, (60, lin), (772, lin))
for lin in range(136, 772, 112):
	pygame.draw.line(screen, black, (lin, 15), (lin, 30))
	pygame.draw.line(screen, black, (lin, 520), (lin, 535))
for lin in range(108, 772, 56):
	pygame.draw.line(screen, black, (lin, 15), (lin, 25))
	pygame.draw.line(screen, black, (lin, 525), (lin, 535))
for lin in range(94, 740, 28):
	pygame.draw.line(screen, black, (lin, 15), (lin, 20))
	pygame.draw.line(screen, black, (lin, 530), (lin, 535))
for lin in range(65, 535, 60):
	pygame.draw.line(screen, black, (60, lin), (70, lin))
	pygame.draw.line(screen, black, (762, lin), (772, lin))
for lin in range(50, 515, 30):
	pygame.draw.line(screen, black, (60, lin), (65, lin))
	pygame.draw.line(screen, black, (767, lin), (772, lin))
screen.blit(font4.render("-3", True, black), (82, 315))
screen.blit(font4.render("-2", True, black), (173, 315))
screen.blit(font4.render("-1", True, black), (262, 315))
for x in range(80,752):
	y=int(math.sin((x-80)/783.00*7*math.pi)*240+275)
	sin_coor.append([x, y])
pygame.draw.aalines(screen, red, False, sin_coor, 2)
for x in range(80,752, 3):
	y1=int(math.cos((x-80)/783.00*7*math.pi)*240+275)
	y2=int(math.cos((x-79)/783.00*7*math.pi)*240+275)
	pygame.draw.aalines(screen, blue, False, [(x, y1), ((x+1), y2)], 2)
point=22
for i in ys:
	if (i=='-0.25') or (i=='-0.50') or (i=='-0.75') or (i=='-1.00'):
		screen.blit(font1.render(i, True, black), (8, point))
	else:	
		screen.blit(font1.render(i, True, black), (15, point))
	point+=60
pointx=80
for i in xs:
	if (i=='-3п') or (i=='-2п'):
		screen.blit(font1.render(i, True, black), (pointx-17,540))
	elif (i=='-п'):
		screen.blit(font1.render(i, True, black), (pointx-10,540))
	elif (i=='0'):
		screen.blit(font1.render(i, True, black), (pointx,535))
	else:
		screen.blit(font1.render(i, True, black), (pointx, 540))
	pointx+=110
pointx1=125
for i in xs1:
	if (i=='п'):
		screen.blit(font2.render(i, True, black), (pointx1+5,535))
	else:
		screen.blit(font2.render(i, True, black), (pointx1, 535))
	pointx1+=112
pointmin=115
for i in range(3):
	if i==2:
		screen.blit(font1.render("-", True, black), (pointmin+5, 541))
	else:
		screen.blit(font1.render("-", True, black), (pointmin, 541))
	pointmin+=112
point2=130
for i in range(6):
	screen.blit(font1.render("2", True, black), (point2, 551))
	point2+=112
screen.blit(font3.render("sin x", True, black, white), (512, 36))
screen.blit(font3.render("cos x", True, black, white), (507, 62.5))
pygame.draw.line(screen, red, (572, 55), (603, 55), 1)
dashpoint=572
for i in range(3):
	pygame.draw.line(screen, blue, (dashpoint, 80), (dashpoint+7, 80), 1)
	dashpoint+=12
screen.blit(fontbold.render("X", True, black), (406, 567))
run=True
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	pygame.display.flip()