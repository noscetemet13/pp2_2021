import pygame, random, sys

# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

def drawLine(screen, start, end, width, color):
	x1 = start[0]
	y1 = start[1]
	x2 = end[0]
	y2 = end[1]

	dx = abs(x1 - x2)
	dy = abs(y1 - y2)

	A = y2 - y1
	B = x1 - x2
	C = x2 * y1 - x1 * y2

	if dx > dy:
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1

		for x in range(x1, x2):
			y = (-C - A * x) / B
			pygame.draw.circle(screen, color, (x, y), width)
	else:
		if y1 > y2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		for y in range(y1, y2):
			x = (-C - B * y) / A
			pygame.draw.circle(screen, color, (x, y), width)

def drawCircle(screen, start, end, width, color):
	x1=start[0]
	y1 = start[1]
	x2 = end[0]
	y2 = end[1]
	x=(x1+x2)/2
	y=(y1+y2)/2
	center=(x, y)
	radius=abs(x1-x2)/2
	pygame.draw.circle(screen, color, center, radius, width)

def drawRectangle(screen, start, end, width, color):
	x1=start[0]
	y1 = start[1]
	x2 = end[0]
	y2 = end[1]
	height=abs(y1-y2)
	widthr=abs(x1-x2)
	pygame.draw.rect(screen, color, (x1, y1, widthr, height), width)


def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	mode = 'random'
	drawmode=''
	draw_on = False
	last_pos = (0, 0)
	color = (255, 128, 0)
	radius = 10
	txtfont=pygame.font.SysFont("Courier", 20)
	txtfont2=pygame.font.SysFont("Courier", 13)
	pygame.display.set_caption("Simple paint with keyboard control")
	colors = {
		'red': (255, 0, 0),
		'blue': (0, 0, 255),
		'green': (0, 255, 0),
		'purple': (182, 68, 228),
		'pink': (236, 144, 158),
		'dark_blue': (20, 28, 150)
	}

	while True:
		pressed = pygame.key.get_pressed()
		alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
		ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and ctrl_held:
					return
				if event.key == pygame.K_F4 and alt_held:
					return
				if event.key == pygame.K_r:
					mode = 'red'
				if event.key == pygame.K_b:
					mode = 'blue'
				if event.key == pygame.K_g:
					mode = 'green'
				if event.key == pygame.K_f:
					mode = 'purple'
				if event.key == pygame.K_d:
					mode = 'dark_blue'
				if event.key == pygame.K_x:
					mode = 'pink'
				if event.key == pygame.K_UP:
					radius += 1
				if event.key == pygame.K_DOWN:
					radius -= 1
				if event.key == pygame.K_c:
					drawmode='circle'
				elif event.key == pygame.K_k:
					drawmode='rectangle'
				elif event.key == pygame.K_e:
					drawmode='eraser'
				elif event.key==pygame.K_p: 
					drawmode='pen'
				if event.key == pygame.K_s:
					rect=pygame.Rect(0, 0, 800, 520)
					image=screen.subsurface(rect)
					pygame.image.save(image, "image.png")
			if event.type == pygame.MOUSEBUTTONDOWN:
				prevpos=event.pos
				if mode == 'random':
					color = (random.randrange(256), random.randrange(256), random.randrange(256))
				else:
					color = colors[mode]
				if drawmode=='pen':
					pygame.draw.circle(screen, color, event.pos, radius)
				draw_on = True
			if event.type == pygame.MOUSEBUTTONUP:
				if draw_on and drawmode=='circle':
					drawCircle(screen, prevpos, event.pos, radius, color)
					draw_on=False
				elif draw_on and drawmode=='rectangle':
					drawRectangle(screen, prevpos, event.pos, radius, color)
					draw_on=False
				else: draw_on = False
			if event.type == pygame.MOUSEMOTION:
				if draw_on and drawmode=='pen':
					drawLine(screen, last_pos, event.pos, radius, color)
				elif draw_on and drawmode=='eraser':
					drawLine(screen, last_pos, event.pos, radius, (0, 0, 0))
				last_pos = event.pos
		screen.blit(txtfont.render("YOU SHOULD PICK COLOR AND/OR TOOL FIRST:", 1, (0, 0, 0), (255, 255, 255)), (0, 510))
		screen.blit(txtfont2.render("Colors: R - red; B - blue; G - green; F - purple; D - dark blue; X - pink.", 1, (0, 0, 0), (255, 255, 255)), (0, 540))
		screen.blit(txtfont2.render("If you did not choose a color, but chose a tool, the color will be random every time.", 1, (0, 0, 0), (255, 255, 255)), (0, 560))
		screen.blit(txtfont2.render("Tools: P - pen; C - draw a circle; K - draw a rectangle; E - eraser; S - save an image.", 1, (0, 0, 0), (255, 255, 255)), (0, 580))
		pygame.display.flip()

	pygame.quit()

main()