from mod.fen.__init__ import *
from mod.wgt.wgt_bouton import Wgt_bouton
from mod.wgt.wgt_progression import Wgt_progression
from mod.wgt.wgt_label import Wgt_label

class Menu_options(Abs_menu):
	def __init__(__):
		Abs_menu.__init__(__)
		__.wallfall = pygame.font.Font('data/fonts/midnight.ttf', 72).render("WallFall " + VERSION, True, pygame.Color(255, 0, 0))
		__.options = pygame.font.Font('data/fonts/AstronBoy2.ttf', 72).render('Options', True, pygame.Color(255, 200, 0))
		__.font = 'data/fonts/AstronBoy2.ttf'
		__.wgts = [
		Wgt_label(K.screen, 50, 250, w=200, h=42, text='Volume :', font=__.font, coul_font=(0, 0, 255)),
		Wgt_label(K.screen, 80, 290, w=200, h=21, text='Musique', font=__.font, coul_font=(0, 255, 0)),
		Wgt_progression(K.screen, 280, 290, w=200, value=K.vol_musique * 100),
		Wgt_label(K.screen, 80, 310, w=200, h=21, text='Effets', font=__.font, coul_font=(0, 255, 0)),
		Wgt_progression(K.screen, 280, 310, w=200, value=K.vol_effet * 100),
		
		Wgt_label(K.screen, 50, 340, w=200, h=42, text='Effets :', font=__.font, coul_font=(0, 0, 255)),
		Wgt_label(K.screen, 80, 380, w=200, h=21, text='Explosions', font=__.font, coul_font=(0, 255, 0)),
		Wgt_bouton(K.screen, 280, 380, w=200, h=21, text2='Activer', text1='Desactiver', coul1=(0, 0, 0),
				font=__.font, coul_font2=(255, 255, 0), coul_font1=(255, 0, 0), checkable=True, checked=K.draw_explo), 
		Wgt_label(K.screen, 80, 400, w=200, h=21, text='Trainees', font=__.font, coul_font=(0, 255, 0)),
		Wgt_bouton(K.screen, 280, 400, w=200, h=21, text2='Activer', text1='Desactiver', coul1=(0, 0, 0),
				font=__.font, coul_font2=(255, 255, 0), coul_font1=(255, 0, 0), checkable=True, checked=K.draw_queue),
				
		Wgt_label(K.screen, 50, 430, w=400, h=42, text='Voir les scores en ligne', font=__.font, coul_font=(0, 0, 255)),
		Wgt_bouton(K.screen, 280, 470, w=200, h=21, text2='Oui', text1='Non', coul1=(0, 0, 0),
				font=__.font, coul_font2=(255, 255, 0), coul_font1=(255, 0, 0), checkable=True, checked=K.display_online),
				
		Wgt_label(K.screen, 50, 530, w=200, h=42, text='Decalage :', font=__.font, coul_font=(0, 0, 255)), 
		__.Wgt_decalage(K.screen, 80, 570), 
		Wgt_bouton(K.screen, 400, 600, w=200, h=42, text1='Valider', coul1=(0, 0, 0),
				font=__.font, coul_font1=(0, 255, 0), fonction=__.valider)
		]
		__.boucle()
		
	def valider(__):
		K.vol_musique = __.wgts[2].get() / 100.
		K.vol_effet = __.wgts[4].get() / 100.
		K.draw_explo = __.wgts[7].checked
		K.draw_queue = __.wgts[9].checked
		K.display_online = __.wgts[11].checked
		K.xdec, K.ydec = __.wgts[13].get()
		mixer.music.set_volume(K.vol_musique)
		file("data/data", "w") .write(str(int(__.wgts[2].get())) +"\n"+ str(int(__.wgts[4].get())) +"\n"+\
										str(K.frame_rate) +"\n"+ str(K.xdec) +"\n"+ str(K.ydec) +"\n"+\
										str(int(K.draw_explo)) +"\n"+ str(int(K.draw_queue)) + "\n" +
										str(int(K.display_online)))
		__.running = False
	
	def draw(__):
		K.screen.blit(__.wallfall, (20, 70))
		K.screen.blit(__.options, (300, 180))
		for wgt in __.wgts: wgt.blit()
	
	def boucle(__):
		temps = pygame.time.get_ticks()
		while __.running:
			K.display.blit(K.screen, (0, 0))
			K.screen.blit(K.back, (0, 0))
			__.draw()
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					__.running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == 27:
						__.running = False
				for wgt in __.wgts:
					if event.type in wgt.events: wgt.event(event)
			temp = pygame.time.get_ticks()
			temps, temps_passe = temp, temp - temps
			pygame.time.wait(120 - temps_passe)
	
	class Wgt_decalage:
		events = [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN]
		
		def __init__(__, boss, x, y, w=100, h=100, coul1=(255, 0, 0), coul2=(0, 0, 255), coul3=(0, 255, 0), coul_bg=(20, 20, 20)):
			__.boss = boss
			__.x, __.y = x, y
			__.w, __.h, __.w2, __.h2 = w, h, w / 2,  h / 2
			__.coul1, __.coul2, __.coul3 = coul1, coul2, coul3
			__.coul_bg = coul_bg
			__.surface = pygame.Surface((w, h))
			__.surface.fill(__.coul_bg)
			__.image = pygame.image.load(K.path_img_sphere + 'rond1.png').convert(32, pygame.SRCALPHA)
			__.surface.blit(__.image, (__.w2 - __.image.get_width() / 2, __.h2 - __.image.get_height() / 2))
			__.xdec, __.ydec = K.xdec + __.w2, K.ydec + __.h2
			__.draw_default_lines()
		
		def draw_default_lines(__):
			pygame.draw.line(__.surface, __.coul1, (__.xdec, 0), (__.xdec, __.h))
			pygame.draw.line(__.surface, __.coul1, (0, __.ydec), (__.w, __.ydec))
			pygame.draw.line(__.surface, __.coul3, (__.w2, 0), (__.w2, __.h))
			pygame.draw.line(__.surface, __.coul3, (0, __.h2), (__.w, __.h2))
			
		def blit(__): __.boss.blit(__.surface, (__.x, __.y))
		def get(__): return (__.xdec - __.w2, __.ydec - __.h2)
		
		def event(__, event):
			x, y = event.pos
			x -= __.x
			y -= __.y
			if 0 <= x < __.w and 0 <= y < __.h:
				__.surface.fill(__.coul_bg)
				__.surface.blit(__.image, (__.w2 - __.image.get_width() / 2, __.h2 - __.image.get_height() / 2))
				if event.type == pygame.MOUSEBUTTONDOWN: __.xdec, __.ydec = x, y
				__.draw_default_lines()
				pygame.draw.line(__.surface, __.coul2, (x, 0), (x, __.h))
				pygame.draw.line(__.surface, __.coul2, (0, y), (__.w, y))
			
