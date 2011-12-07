from mod.__init__ import *
from menu import Menu
from mod.wgt.wgt_label import Wgt_label
from mod.obj.spheres import Joueur, Sphere_score, Sphere_bonus
from mod.obj.murs import liste_murs

class Menu_obj(Menu):
	SPHERES = "SPHERES"
	BLOCS = "BLOCS"
	def __init__(__, obj):
		if obj == __.SPHERES:
			__.obj_type = __.SPHERES
			__.obj_text = Joueur.__DOC__
			__.obj_text += [Sphere_score.__doc__]
			__.obj_text += Sphere_bonus.__DOC__
			__.obj_img = [pygame.image.load(K.path_img_sphere + img + ".png").convert(32, pygame.SRCALPHA) for img in Joueur.images]
			__.obj_img += [pygame.image.load(K.path_img_sphere + Sphere_score.image + ".png").convert()]
			__.obj_img += [pygame.image.load(K.path_img_sphere + img + ".png").convert(32, pygame.SRCALPHA) for img in Sphere_bonus.images]
		else:
			__.obj_type = __.BLOCS
			__.obj_text = [i.__doc__ for i in liste_murs]
			__.obj_img = [i.sprite for i in liste_murs]
		__.obj_title = [i.split(" : ")[0] for i in __.obj_text]
		Menu.__init__(__, __.obj_title + ['Quitter'], __.obj_type)
	
	def boucle(__):
		__.selected_obj = __.select
		__.font = 'data/fonts/VideoPhreak.ttf'
		__.label = Wgt_label(K.screen, 150, 500, w=__.size - 50, h=100,
		                     text=__.obj_text[__.selected_obj], font=__.font, coul_font=(0, 0, 255), font_size=15)
		Menu.boucle(__)
		
	def draw(__):
		Menu.draw(__)
		__.label.blit()
		if __.selected_obj != None:
			K.screen.blit(__.obj_img[__.selected_obj], (__.label.x - 50, __.label.y + __.label.h / 2))
	
	def valider(__):
		temp = __.texts[__.select]
		if temp == 'Quitter': __.running = False
		else:
			__.label.text = __.obj_text[__.select]
			__.selected_obj = __.select
		
	def draw_text(__, x=50, y=250):
		for i, text in enumerate(__.texts):
			if i == __.selected_obj: color = (255, 0, 0)
			else: color = (0, 255, 0)
			if __.select == i:
				K.screen.blit(__.fonts[0].render(text, True, color), (x, y + (i - __.select + 2) * 42))
			elif __.select - 2 <= i < __.select + 3:
				K.screen.blit(__.fonts[1].render(text, True, color), (x, y + (i - __.select + 2) * 42))
		
	def quit(__): pass
