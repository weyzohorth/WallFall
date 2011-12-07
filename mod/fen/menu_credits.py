# -*- coding: cp1252 -*-
import webbrowser as web
from mod.__init__ import *
from menu import Menu
from mod.wgt.wgt_label import Wgt_label

remerciements = \
"""\
Je remercie les sites et artistes suivants pour
leurs oeuvres libres.
Je remercie aussi tous ceux ayant
contribué au développement.
(Matkaiser, Sogeking, Moumoune)
"""

class Menu_credits(Menu):
	def __init__(__):
		Menu.__init__(__, ["www.freesound.org", "www.grsites.com", "www.sound-fishing.net",
		"www.jamendo.com", "\tBertycoX", "\tMidoriiro", "Quitter"], "Crédits")
	
	def boucle(__):
		__.font = 'data/fonts/VideoPhreak.ttf'
		__.label = Wgt_label(K.screen, 250, 440, w=__.size - 50, h=200,
		                     text=remerciements, font=__.font, coul_font=(0, 0, 255), font_size=20)
		Menu.boucle(__)
	
	def draw(__):
		Menu.draw(__)
		__.label.blit()
		
	def valider(__):
		temp = __.texts[__.select]
		if temp == 'Quitter': __.running = False
		elif temp == "\tberticox":
			web.open("http://www.jamendo.com/fr/artist/bertycox/")
		elif temp == "\tMidoriiro":
			web.open("http://www.jamendo.com/fr/artist/Midoriiro/")
		else:
			web.open(temp)

	def quit(__): pass
