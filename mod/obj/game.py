from mod.__init__ import *
from murs import nbr_lvl, liste_murs
from spheres import *
from explosion import *
from level import *
from mod.fen.scores import *
from mod.fen.oscores import *
from mod.fen.menu_pause import Menu_pause
from mod.fct.mod_time import conv_time
from mod.fct.highscores import *
from mod.wgt.wgt_label import Wgt_label
from random import randrange

#===============================================================================
#                                                                                    objet gerant le jeu
#===============================================================================#------------- objet gerant le jeu
class Game:
	def __init__(__, boss, map=K.path_map + "lvl1.wf"):
		__.init_pygame()
		__.boss = boss
		__.size = boss.size
		__.init_var(map)
		__.init_widget()
		__.game()
		K.display.blit(K.back, (0, 0))

	def init_pygame(__):
		mixer.music.load(K.musiques_jeu[randrange(K.len_musiques_jeu)])
		mixer.music.play()
		son = mixer.Sound("sons/effets/get_ready.ogg")
		son.set_volume(K.vol_effet)
		son.play()

	def init_var(__, map):
		__.scores = get_min_et_max_scores()
		__.ft = K.frame_time
		__.wait_start = 4000
		__.wait = __.wait_start
		__.stop = False
		__.niveau = 0
		__.score = 0
		__.painting = 0
		__.vie = 3
		__.temps = 50000
		__.score_temps = 0.
		__.stop_mur = 0
		__.cache_mur = 0
		__.camoufle_mur = 0
		__.MUR = []
		__.SPHERE= []
		__.EXPLO = []
		__.PARTI = []
		__.Players = []
		__.__add_score__ = None
		__.__score__ = None
		#__.level = Level_one_bloc_no_bonus(__)
		__.level = Level_load(__, map)
		#__.level = Level_random(__)
		
	def init_widget(__):
		__.font = 'data/fonts/VideoPhreak.ttf'
		height = 25
		coul = (80, 60, 80)
		coul_font = (255, 0, 0)
		__.font_size = 17
		__.back = pygame.Surface((K.w, K.h))
		__.back.fill(coul)
		__.font_wait = pygame.font.Font('data/fonts/midnight.ttf', 184)
		__.Temps = Wgt_label(K.display, K.w,  50, K.hud, height, text="Temps : 0", font=__.font, coul=coul, coul_font=coul_font, font_size=__.font_size)
		__.Score = Wgt_label(K.display, K.w,  50, K.hud, height, text="Score : 0", font=__.font, coul=coul, coul_font=coul_font, font_size=__.font_size)
		__.Score_max = Wgt_label(K.display, K.w,  50, K.hud, height, text="Score max : %d"%(__.scores[0]), font=__.font, coul=coul, coul_font=coul_font, font_size=__.font_size)
		__.Niveau = Wgt_label(K.display, K.w,  50, K.hud, height, text="Niveau : 0", font=__.font, coul=coul, coul_font=coul_font, font_size=__.font_size)
		__.Vie = Wgt_label(K.display, K.w,  50, K.hud, height, text="Vie : 0", font=__.font, coul=coul, coul_font=coul_font, font_size=__.font_size)
		__.widgets = [__.Temps, __.Score, __.Score_max, __.Niveau, __.Vie]
		for i in range(len(__.widgets)):
			__.widgets[i].y += i * __.widgets[0].h

	def game(__):
		temps = pygame.time.get_ticks()
		while not __.stop:
			if 0 < __.wait:
				if __.wait == __.wait_start:
					son = mixer.Sound(K.path_son_effet + "get_ready.ogg")
					son.set_volume(K.vol_effet)
					son.play()
				__.wait -= __.ft
			else:
				__.level.gere_bloc()
				__.time()
				__.players_live()
				__.other_end_level()
				__.configure()
				__.collision()
			__.draw()
			__.music()
			__.event()
			Mur.add_speed += 1 / (K.frame_rate * 1200.)
			temp = pygame.time.get_ticks()
			temps, temps_passe = temp, temp - temps
			pygame.time.wait(__.ft - temps_passe)
		son = mixer.Sound(K.path_son_effet + "panne.ogg")
		son.set_volume(K.vol_effet)
		son.play()
		__.end = 1

	def music(__):
		if not mixer.music.get_busy():
			mixer.music.load(K.musiques_jeu[randrange(K.len_musiques_jeu)])
			mixer.music.play()

	def time(__):
		if __.ft != K.frame_time:
			temp = K.frame_time - __.ft
			temp_abs = abs(temp)
			if abs(temp_abs) <= 1: __.ft = K.frame_time
			else: __.ft += temp / temp_abs
		__.painting -= K.d_time
		if __.painting < 0: __.painting = 0

	def players_live(__):
		for joueur in __.Players:
			if joueur.vie or joueur.temps <= 0 and joueur.vie >= 2:
				if joueur.temps > 0:
					joueur.temps -= int(K.frame_time)
				else:
					son = mixer.Sound(K.path_son_effet + "beep6.ogg")
					if K.draw_explo:
						Explosion(__, joueur.x, joueur.y, r=25, couleur=joueur.couleurs[1])
					son.set_volume(K.vol_effet)
					mixer.Sound.play(son)
					joueur.vie -= 1
					if joueur.vie <= 0:
						if 1 < len(__.Players):
							__.Players.remove(joueur)
						else:
							__.stop = True
					joueur.temps += 30000
			elif 1 < len(__.Players):
				__.Players.remove(joueur)
			else:
				__.stop = True
			if joueur.vie <= 0:
				__.score += joueur.temps / 100
				if len(__.Players) <= 1: __.anim_end()

	def other_end_level(__):
		if __.level.end == __.level.GET_ALL_BALL:
			if not len(__.SPHERE):
				for joueur in __.Players:
					__.score += joueur.vie * 100
					__.score += joueur.temps / 100
				__.stop = True
				if len(__.Players) <= 1: __.anim_end()

	def draw(__):
		K.display.blit(K.back, (0, 0))
		K.display.blit(__.back, (K.w, 0))
		K.display.blit(K.screen, (0, 0))
		if not __.painting: K.screen.blit(K.back, (0, 0))
		for i in __.EXPLO: i.draw()
		for i in __.PARTI: i.draw()
		for i in __.MUR: i.draw()
		for i in __.Players: i.draw()
		for i in __.SPHERE: i.draw()
		for i in __.widgets: i.blit()
		if 0 < __.wait:
			text = __.font_wait.render(str(int(__.wait / 1000)), 1, (255, 0, 0))
			K.screen.blit(text, (K.w / 2 - text.get_width() / 2, K.h / 2 - text.get_height() / 2))
		display.update()

	def event(__):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				__.stop = True
				K.display.fill(pygame.Color(0, 0, 0))
				display.update()
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					Menu_pause(__)
					__.wait = __.wait_start
			for joueur in __.Players:
				if 0 < joueur.vie and event.type in joueur.events: joueur.event(event)

	def set_ft(__):
		__.ft = K.frame_time
		for obj in __.Players:
			obj.dr = K.d_time * 2
			obj.i_speed = __.hero.speed = int(30 * K.d_time)
		__.sphere_score.son.set_volume(K.vol_effet)
		for i in __.MUR:
			i.get_speed()
			i.son_colli.set_volume(K.vol_effet)
			i.son_explo.set_volume(K.vol_effet)

	def collision(__):
		for i in __.EXPLO: i.bouge()
		for i in __.PARTI: i.bouge()
		for obj in __.Players: obj.bouge()
		__.level.gere_sphere()
		if not __.stop_mur:
			for mur in __.MUR: mur.bouge()
		else:
			for mur in __.MUR: mur.collision()
			if __.stop_mur > 0: __.stop_mur -= K.d_time
			else: __.stop_mur = 0
		if __.cache_mur > 0: __.cache_mur -= K.d_time
		else: __.cache_mur = 0
		if __.camoufle_mur > 0: __.camoufle_mur -= K.d_time
		else: __.camoufle_mur = 0

	def configure(__):
		__.Temps.text = "Temps : %s" % (conv_time(__.Players[0].temps / 1000))
		__.Score.text = "Score : %s" % (__.score)
		__.Niveau.text = "Niveau : %s" % (__.niveau)
		__.Vie.text = "Vies : %s" % (__.Players[0].vie)

	def reinit(__):
		__.Temps.text = "Temps : 00:00"
		__.Score.text = "Score : 0"
		__.Niveau.text = "Niveau : 0"
		__.Vie.text = "Vies : 0"
		__.Score_max.text = "Score max : %d"%(__.scores[0])

	def anim_end(__):
		son = mixer.Sound(K.path_son_effet + "game_over_1.ogg")
		son.set_volume(K.vol_effet)
		son.play()
		son = mixer.Sound(K.path_son_effet + "panne.ogg")
		son.set_volume(K.vol_effet)
		son.play()
		if not __.boss.__class__ is Editor:
			if K.display_online:
				try:
					pseudo = add_oscore(GAME + "_" + VERSION.replace(".", "_"), __.score, dir="mod")
				except: pseudo = ""
			else: pseudo = ""
			if __.score > __.scores[1]:
				if not pseudo: Add_score(__.score, __)
				else:
					add_score(pseudo, __.score)
					Show_scores(pseudo,__.score, __)
				__.scores = get_min_et_max_scores()
				try: __.Score_max.configure(text= "score max : %ld"%(__.scores[0]))
				except: pass
			else: Show_scores(boss=__)
