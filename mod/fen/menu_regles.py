# -*- coding: cp1252 -*-
from menu import *
from menu_but import Menu_but
from menu_obj import Menu_obj
from mod.fen.__init__ import *
from mod.wgt.wgt_bouton import Wgt_bouton

class Menu_regles(Menu):
	def __init__(__):
		Menu.__init__(__, ['But', 'Spheres', 'Blocs', 'Quitter'], "Règles du jeu")
	
	def valider(__):
		temp = __.texts[__.select]
		if temp == 'Quitter': __.running = False
		elif temp == 'But': Menu_but()
		elif temp == 'Spheres': Menu_obj(Menu_obj.SPHERES)
		elif temp == 'Blocs': Menu_obj(Menu_obj.BLOCS)
	
	def boucle(__):
		__.wallfall = pygame.font.Font('data/fonts/midnight.ttf', 72).render("WallFall " + VERSION, True, pygame.Color(255, 0, 0))
		__.regles = pygame.font.Font('data/fonts/AstronBoy2.ttf', 72).render('Regles', True, pygame.Color(255, 200, 0))
		Menu.boucle(__)
		
	def quit(__): pass
