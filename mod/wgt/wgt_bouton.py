import pygame

class Wgt_bouton:
	events = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]

	def __init__(__, boss, x, y, w=100, h=20, text1="Ok", text2=None, fonction=None, coul_font1=(0, 0, 0), coul_font2=(),
				coul1=(255, 255, 255), coul2=(), font="data/fonts/comic.ttf", checkable=False, checked=False):
		__.boss = boss
		__.x, __.y = x, y
		__.w, __.h = w, h
		__.surface = pygame.Surface((w, h))
		__.checkable = checkable
		__.font = pygame.font.Font(font, int(__.h))
		if not coul2: coul2 = [i/2 for i in coul1]
		__.coul = coul1, coul2
		if not coul_font2: coul_font2 = coul_font1
		__.coul_font = coul_font1, coul_font2
		if text2 == None: text2 = text1
		__.text = text1, text2
		__.fonction = fonction
		__.checked = checked

	def blit(__):
		__.surface.fill(__.coul[__.checked])
		text = __.font.render(__.text[__.checked], 1, __.coul_font[__.checked])
		x = (__.w - text.get_width()) / 2
		if x < 0: x = 0
		__.surface.blit(text, (x, 0))
		__.boss.blit(__.surface, (__.x, __.y))

	def event(__, event):
		ev_x, ev_y = event.pos
		boss = __.boss
		while "coords" in dir(boss):
			ev_x -= boss.coords[0]
			ev_y -= boss.coords[1]
			if "boss" in dir(boss): boss = boss.boss
			else: break
		if 0 <= ev_x - __.x < __.w and 0 <= ev_y - __.y < __.h:
			if event.type == pygame.MOUSEBUTTONDOWN:
				__.checked = not __.checked
				if __.fonction: __.fonction()
			elif not __.checkable and event.type == pygame.MOUSEBUTTONUP:
				if not __.checkable: __.checked = False

if __name__ == "__main__":
	def fonction(): print "ok"
	pygame.init()
	screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
	bouton = Wgt_bouton(screen, 220, 40, coul2=(128, 128, 128), fonction=fonction)
	run = 1
	while run:
		bouton.blit()
		for i in pygame.event.get():
			if i.type == pygame.QUIT: run = 0
			if i.type in bouton.events: bouton.event(i)
		pygame.display.update()
		pygame.time.wait(100)
	pygame.quit()
