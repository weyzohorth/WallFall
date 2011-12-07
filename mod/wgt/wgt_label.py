import pygame

class Wgt_label:
	events = []

	def __init__(__, boss, x, y, w=100, h=20, text="", coul=(0, 0, 0), coul_font=(255, 255, 255), font="data/fonts/comic.ttf", font_size=None):
		__.boss = boss
		__.x, __.y = x, y
		__.w, __.h = w, h
		__.text = text
		__.font = font
		__.surface = pygame.Surface((__.w, __.h))
		__.coul_font = coul_font
		__.coul = coul
		__.temp_font = None
		__.temp_text = None
		__.font_size = font_size
		if not __.font_size:
			__.font_size = int(__.h)
		__.font_size_fixed = bool(font_size != None)
		__.font_render = pygame.font.Font(__.font, __.font_size)

	def blit(__):
		if __.temp_font != __.font or __.temp_text != __.text:
			if not __.font_size_fixed:
				__.font_size = int(__.h / (__.text.count("\n") + 1))
			__.font_render = pygame.font.Font(__.font, __.font_size)
			__.temp_font = __.font[ : ]
			__.temp_text = __.text[ : ]
			__.text_cut = __.text.split('\n')
		__.surface.fill(__.coul)
		for i, line in enumerate(__.text_cut):
			__.surface.blit(__.font_render.render(line, 1, __.coul_font), (0, i * __.font_size))
		__.boss.blit(__.surface, (__.x, __.y))
