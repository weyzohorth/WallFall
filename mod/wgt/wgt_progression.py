import pygame
from wgt_k import *

class Wgt_progression:
	events = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]

	def __init__(__, boss, x, y, w=100, h=10, value=50, value_max=100, coul=(50, 0, 0), coul2=(255, 0, 0), orient=HORIZONTAL):
		__.boss = boss
		__.x, __.y = x, y
		__.w, __.h = w, h
		__.surface = pygame.Surface((w, h), pygame.HWSURFACE)
		__.back = pygame.Surface((w, h), pygame.HWSURFACE)
		__.set_coul(coul)
		__.coul2 = coul2
		__.orient = orient
		__.value_max = value_max
		__.set_value(value)
		__.change = False

	def blit(__):
		__.surface.blit(__.back, (0, 0, __.w, __.h))
		__.surface.blit(__.progression, (0, 0))
		__.boss.blit(__.surface, (__.x, __.y))

	def set_value(__, value):
		if value < 0: value = 0
		if value > __.value_max: value = __.value_max
		__.value = value
		if __.orient == HORIZONTAL:
			if __.value_max: w = int((__.value / float(__.value_max)) * __.w)
			else: w = __.w
			__.progression = pygame.Surface((w, __.h), pygame.HWSURFACE)
		else:
			if __.value_max: h = int((__.value / float(__.value_max)) * __.h)
			else: h = __.h
			__.progression = pygame.Surface((__.w, h), pygame.HWSURFACE)
		__.progression.fill(__.coul2)
		pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"value": __.value, "widget": __}))

	def set_coul(__, coul):
		__.surface.fill(coul)
		__.back.fill(coul)
		__.coul = coul

	def set_coul2(__, coul):
		__.progression.fill(coul)
		__.coul2 = coul

	def event(__, event):
		ev_x, ev_y = event.pos
		boss = __.boss
		while "coords" in dir(boss):
			ev_x -= boss.coords[0]
			ev_y -= boss.coords[1]
			if "boss" in dir(boss): boss = boss.boss
			else: break
		if __.orient == HORIZONTAL:
			ev_x, ev_y = float(ev_x - __.x), ev_y - __.y
			if event.type == pygame.MOUSEBUTTONUP: __.change = False
			elif 0 <= ev_x <= __.w and 0 <= ev_y <= __.h:
				if event.type == pygame.MOUSEBUTTONDOWN: __.change = True
				if __.change: __.set_value(int(ev_x / __.w * __.value_max))
		else:
			ev_x, ev_y = ev_x - __.x, float(ev_y - __.y)
			if event.type == pygame.MOUSEBUTTONUP: __.change = False
			elif 0 <= ev_x <= __.w and 0 <= ev_y <= __.h:
				if event.type == pygame.MOUSEBUTTONDOWN: __.change = True
				if __.change: __.set_value(int(ev_y / __.h * __.value_max))

	def get(__): return __.value

	def set_size(__, size):
		w, h = size
		__.surface = pygame.Surface((w, h), pygame.HWSURFACE)
		__.back = pygame.Surface((w, h), pygame.HWSURFACE)

if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
	progression = Wgt_progression(screen, 220, 40, 10, 100, orient="verticale")
	run = 1
	while run:
		progression.blit()
		for i in pygame.event.get():
			if i.type == pygame.QUIT: run = 0
			if i.type in progression.events: progression.event(i)
		pygame.display.update()
		pygame.time.wait(100)
	pygame.quit()
