from menu import *

class Menu_pause(Menu):
	def __init__(__, game):
		__.temp = game
		Menu.__init__(__, ['Reprendre', 'Options', 'Quitter'], "PAUSE")
	
	def boucle(__):
		__.game = __.temp
		Menu.boucle(__)

#------------- fonctions du menu
	def play_music(__): pass 
	def quit(__): pass
	
	def draw_text(__):
		Menu.draw_text(__, 50, 350)
	
	def valider(__):
		temp = __.texts[__.select]
		if temp == 'Quitter': __.game.stop = True
		if temp == 'Options': Menu_options()
		else:	__.running = False
		
