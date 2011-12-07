# -*- coding: cp1252 -*-
from mod.__init__ import *
from mod.editor import Editor
from __init__ import Abs_menu
from random import randrange
from menu_options import Menu_options
from scores import Show_scores
from oscores import show_oscore
import webbrowser as web

class Menu(Abs_menu):
	def __init__(__, texts=['Jouer', 'Editeur', 'Règles du Jeu', 'Options', 'Meilleurs Scores', 'Meilleurs Scores Online', 'Site Officiel', 'Crédits', 'Quitter'], subtitle="Menu"):
		Abs_menu.__init__(__)
		__.play_music()
		__.wallfall = pygame.font.Font('data/fonts/midnight.ttf', 72).render("WallFall " + VERSION, True, pygame.Color(255, 0, 0))
		__.subtitle = pygame.font.Font('data/fonts/AstronBoy2.ttf', 72).render(subtitle, True, pygame.Color(255, 200, 0))
		__.__score__ = None
		__.__add_score__ = None
		__.game = None
		__.texts = texts
		__.fonts = [pygame.font.Font('data/fonts/AstronBoy1.ttf', 42), pygame.font.Font('data/fonts/AstronBoy2.ttf', 42)]
		__.boucle()

#------------- fonctions du menu
	def play_music(__):
		mixer.music.load(K.musiques_menu[randrange(K.len_musiques_menu)])
		mixer.music.play()

	def draw(__):
		K.screen.blit(__.wallfall, (20, 70))
		K.screen.blit(__.subtitle, (300, 180))

	def draw_text(__, x=50, y=250):
		for i, text in enumerate(__.texts):
			if __.select == i:
				K.screen.blit(__.fonts[0].render(text, True, pygame.Color(0, 255, 0)), (x, y + i * 42))
			else:
				K.screen.blit(__.fonts[1].render(text, True, pygame.Color(0, 255, 0)), (x, y + i * 42))

	def valider(__):
		temp = __.texts[__.select]
		import mod.obj.game as game
		import menu_regles as m_regles
		import menu_credits as m_credits
		if temp == 'Quitter': __.running = False
		elif temp == 'Jouer':
			__.game = game.Game(__)
			__.play_music()
		elif temp == 'Editeur':
			Editor(__)
		elif temp == 'Meilleurs Scores': Show_scores(boss=__)
		elif temp == 'Meilleurs Scores Online': show_oscore(GAME + "_" + VERSION.replace('.', '_'))
		elif temp == 'Règles du Jeu': m_regles.Menu_regles()
		elif temp == 'Options': Menu_options()
		elif temp == 'Site Officiel': web.open('http://progject.free.fr/')
		elif temp == 'Credits': m_credits.Menu_credits()

	def boucle(__):
		temps = pygame.time.get_ticks()
		while __.running:
			K.display.blit(K.screen, (0, 0))
			K.screen.blit(K.back, (0, 0))
			__.draw()
			__.draw_text()
			pygame.display.update()
			__.event()
			temp = pygame.time.get_ticks()
			temps, temps_passe = temp, temp - temps
			pygame.time.wait(120 - temps_passe)
		__.quit()

	def event(__):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				__.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					__.running = False
				elif event.key == 274:
					__.select += 1
					if __.select == len(__.texts): __.select = 0
				elif event.key == 273:
					__.select -= 1
					if __.select == -1: __.select = len(__.texts) - 1
				elif event.key == 13:
					__.valider()
			__.event_child(event)

	def event_child(__, event): pass
	def quit(__):
		pygame.quit()
