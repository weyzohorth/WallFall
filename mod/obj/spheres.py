# -*- coding: cp1252 -*-
from random import randrange
from mod.fct.mod_math import *
from mod.__init__ import *
from explosion import *
from murs import Mur
from murs import liste_murs
from math import cos, sin, pi

#===============================================================================
#                                                                              joueur
#===============================================================================
class Joueur:
	events = [pygame.MOUSEMOTION]
	i_speed = int(30 * K.d_time)
	images = ["rond1", "rond-last", "rond-god", "rond-berserk", "rond-inverse"]
	sprites = [pygame.image.load(K.path_img_sphere + img + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA) for img in images]
	couleurs = ["#7c1504","#d20000", "#f6be0a", "#6b0e04","#ba7301"]
	__DOC__ = ["Mode normal : Ceci c'est vous",
"""Mode survive : Ceci c'est vous lorsque vous n'avez plus
qu'une vie .""",
"""Mode god : vous êtes invulnérable pendant un temps limité""",
"""Mode berserk : vous êtes représentés comme celà, et vous
pouvez détruire un bloc, après l'effet se termine
(attention: cet effet se stop au bout de 10 sec et vous êtes à 
nouveau fragile .""",
"""Mode inverse : vous avancer dans la direction opposée, à 
laquelle votre souris pointe ."""
]

	def __init__(__, boss, x=None, y=None):
		__.size = boss.size
		__.boss = boss
		__.i_special = 0
		__.i_particule = 0
		__.vie = 3
		__.x, __.y = x, y
		if __.x == None: __.x = __.size / 2
		if __.y == None: __.y = __.size / 2
		__.x2 = __.x
		__.y2 = __.y
		__.score = 0
		__.temps = 50000
		__.dr = K.d_time * 2
		__.direction = 0
		__.speed = __.i_speed
		__.etat = 1
		if __.speed < 1: __.speed = 1
		__.god = 10
		__.berserk = __.inverse = 0
		__.sprite = __.sprites[2]
		__.w, __.h = __.sprite.get_size()
		__.rect = pygame.Rect((__.x, __.y), (__.w, __.h))

	def event(__, event):
		if event.type == pygame.MOUSEMOTION:
			ev_x, ev_y = event.pos
			__.x2 = ev_x - K.xdec
			__.y2 = ev_y - K.ydec

	def move(__):
		sens = 1 - bool(__.inverse) * 2
		__.direction = DIRECTION(__.x, __.y, __.x2, __.y2)
		speed = DISTANCE(__.x, __.y, __.x2, __.y2)
		if speed > __.speed: speed = __.speed
		if __.speed >= 0:
			if __.speed < __.i_speed: __.speed += .05
		else: __.speed = 0
		temp = __.x + cos(pi*__.direction/180)*speed*sens
		if 12.5 <= temp <= __.boss.size - 12.5: __.x = temp
		temp = __.y - sin(pi*__.direction/180)*speed*sens
		if 12.5 <= temp <= __.boss.size - 12.5: __.y = temp
		return (speed)
	
	def gere_inverse(__, speed):
		if K.draw_explo: __.special_particule(__.inverse)
		if K.draw_queue and speed: __.draw_particule(4)
		if __.etat != 4: __.change_image(4)
		__.inverse -= K.d_time
		
	def gere_berserk(__, speed):
		if K.draw_explo: __.special_particule(__.berserk)
		if K.draw_queue and speed: __.draw_particule(3)
		if __.etat != 3: __.change_image(3)
		__.berserk -= K.d_time
	
	def gere_god(__, speed):
		if K.draw_explo: __.special_particule(__.god)
		if K.draw_queue and speed: __.draw_particule(2)
		if __.etat != 2: __.change_image(2)
		__.god -= K.d_time
	
	def gere_normal(__, speed):
		__.god = 0
		__.berserk = 0
		__.inverse = 0
		if __.vie > 1:
			if K.draw_queue and speed: __.draw_particule(0)
			if __.etat != 0: __.change_image(0)
		else:
			if K.draw_queue and speed: __.draw_particule(1)
			if __.etat != 1: __.change_image(1)
	
	def special_particule(__, max):
		__.i_special += K.d_time
		if max <= __.i_special:
			Explosion(__.boss, __.x, __.y, couleur=__.couleurs[1])
			__.i_special = 0
			
	def special(__, speed):
		if __.inverse > 0: __.gere_inverse(speed)
		elif __.berserk > 0: __.gere_berserk(speed)
		elif __.god > 0: __.gere_god(speed)
		else:__.gere_normal(speed)
	
	def bouge(__):
		__.special(__.move())
	
	def draw(__):
		__.rect.center = (__.x, __.y)
		K.screen.blit(__.sprite, __.rect)

	def change_image(__, etat):
		__.etat = etat
		__.sprite = __.sprites[__.etat]
		__.w, __.h = __.sprite.get_size()
		__.rect = pygame.Rect((__.x, __.y), (__.w, __.h))
		if K.draw_explo: Explosion(__.boss, __.x, __.y, couleur=__.couleurs[__.etat])

	def draw_particule(__, index):
		__.i_particule += 1
		if K.ratio_d_time <= __.i_particule:
			Particule(__.boss, __.x, __.y, couleur=__.couleurs[index], dr=__.dr)
			__.i_particule = 0
		
#===============================================================================
#                                                                              IA
#===============================================================================
class IA(Joueur):
	events = []

	def bouge(__):
		Joueur.bouge(__)
		__.event()

	def event(__):
		if __.boss:
			if not __.berserk or not __.boss.MUR:
				x = y = 0
				if __.god < 2:
					distance = 40 + __.speed
					for i in __.boss.MUR:
						if DISTANCE(__.x, __.y, i.x, i.y) < distance + i.speed :
							Cos, Sin = CoSinus(DIRECTION(i.x, i.y, __.x, __.y))
							x += Cos
							y -= Sin
					__.x2 = __.x + x * __.speed
					__.y2 = __.y + y * __.speed
				if x == y == 0:
					if __.boss.sphere_bonus:
						__.x2 = __.boss.sphere_bonus.x
						__.y2 = __.boss.sphere_bonus.y
					elif __.boss.sphere_score:
						__.x2 = __.boss.sphere_score.x
						__.y2 = __.boss.sphere_score.y
			else:
				ind = 0
				mur = 0
				if __.boss.MUR:
					for i in __.boss.MUR:
						temp = liste_murs.index(i.__class__)
						if temp >= ind:
							ind = temp
							mur = i

					__.x2 = mur.x
					__.y2 = mur.y

#===============================================================================
#																						sphere
#===============================================================================
class Sphere:
	def __init__(__, boss, x, y, image):
		__.boss = boss
		__.boss.SPHERE.append(__)
		__.coords(x, y)
		__.sprite = pygame.image.load(K.path_img_sphere + image +".png")
		__.w, __.h = __.sprite.get_size()
		__.rect = pygame.Rect((0, 0), (__.w, __.h))

	def coords(__, x=None, y=None):
		__.x, __.y = x, y
		if __.x != None != __.y:
			return
		if __.x == None: __.x = randrange(10, __.boss.size - 10)
		if __.y == None: __.y = randrange(10, __.boss.size - 10)
		good = False
		if __.boss.MUR:
			while not good:
				for m in __.boss.MUR:
					if __.x <= m.x +32 and __.x >= m.x - 32 and __.y <= m.y +32 and __.y >= m.y - 32:
						if x == None: __.x = randrange(10, __.boss.size - 10)
						if y == None: __.y = randrange(10, __.boss.size - 10)
						good = False
						break
					else:
						good = True

	def draw(__):
		__.rect.center = (__.x, __.y)
		K.screen.blit(__.sprite, __.rect)
	
	def destroy(__):
		if __ in __.boss.SPHERE:
			__.boss.SPHERE.remove(__)

#===============================================================================
#																		sphere score
#===============================================================================
class Sphere_score(Sphere):
	"""Sphere de score : vous devez ramasser 10 boules dorée
	comme celle-ci pour passer au niveau suivant.
	(Si vous allez assez vite vous aurez un bonus)"""
	image = "rond2"

	def __init__(__, boss, x=None, y=None):
		Sphere.__init__(__, boss, x, y, __.image)
		__.reappear = bool(x == y == None)
		__.temps_bonus = __.boss.temps
		__.son = mixer.Sound(K.path_son_effet + "scifi048.ogg")
		__.son.set_volume(K.vol_effet)

	def collision(__):
		for obj in __.boss.Players:
			if DISTANCE(__.x, __.y, obj.x, obj.y) < 25:
				if K.draw_explo: Explosion(__.boss, __.x, __.y, couleur="#ff8e00")
				temp = (__.boss.temps - __.temps_bonus) / 250
				__.boss.score += 10 + temp * bool(temp  > 0)
				x, y = __.x, __.y
				__.son.play()
				__.temps_bonus = __.boss.temps - int(DISTANCE(x, y, __.x, __.y) * 80 / Joueur.i_speed)
				Mur.mult_speed += 0.001
				if __.reappear: __.coords()
				else: __.destroy()
				break

#===============================================================================
#                                                                sphere bonus
#===============================================================================
class Sphere_bonus(Sphere):
	__doc__ = "Sphere donnant un bonus aléatoire ."
	__DOC__ = ["""Sphere de la win :  vous rapporte 50 points, pas besoin
de vous dire que c'est cool d'en ramasser quand il y en a .""",
"""Sphere de vie : vous rapporte une vie,
pas besoin de vous dire de la ramasser .""",
"""Sphère de vitesse : vous permet de vous déplacer plus vite .""",
"""Sphere de temps : vous donne 10 secondes suplémentaires .""",
"""Sphère d'invulnérabilité : vous serez invulnérable
pendant 10 secondes .""",
"""Sphere de ralentissement : ralenti le jeu vous laissant
plus de temps pour les déplacements délicats .
(donne une impression de lagging,
qui n'est en aucun cas dangereux) .""",
"""Sphere de puissance : Vous confère la puissance
du mode berserk .""",
"""Sphère destructrice : détruit les 3 blocs les plus anciens .""",
"""Sphère stop motion : stop tous les blocs pendant 5 secondes."""]
	images = ["rond"+str(i) for i in range(3, 12)]

	def __init__(__, boss, x=None, y=None, index=None):
		__.ind = index
		__.boss = boss
		if __.ind == None:
			__.ind = __.get_index()
		__.couleur = ["#09b900", "#c00004", "#006aff", "#c400c9", "#fe6c00", "#6c6c6c", "#6b0e04", "#8300d6", "#17cc71"][__.ind - 1]
		__.temps = 30
		Sphere.__init__(__, boss, x, y, __.images[__.ind - 1])
		if x != None != y: __.temps = None

	def collision(__):
		for obj in __.boss.Players:
			if DISTANCE(__.x, __.y, obj.x, obj.y) < 25:
				if __.ind == 1: obj.score += 50
				elif __.ind == 2: obj.vie += 1
				elif __.ind == 3: obj.speed = int(obj.speed + 1.25 * K.d_time)
				elif __.ind == 4: obj.temps += 10000
				elif __.ind == 5: obj.god = 30
				elif __.ind == 6: __.boss.ft += 150
				elif __.ind == 7: obj.berserk += 30
				elif __.ind == 8:
					i = 0
					while i < 3 and __.boss.MUR:
						__.boss.MUR[0].destroy()
						i += 1
				elif __.ind == 9: __.boss.stop_mur += 50
				__.destroy(True)
				break

		if __.temps != None:
			__.temps -= K.d_time
			if __.temps <= 0: __.destroy()

	def get_index(__):
		pos = [1 for i in range(5)]
		pos += [3 for i in range(5)]
		pos += [5 for i in range(5)]
		pos += [9 for i in range(5)]
		if __.boss.Players:
			pos += [2 for i in range(5 / (sum(p.vie for p in __.boss.Players) / len(__.boss.Players)))]
			tmp =  ((sum(p.temps for p in __.boss.Players) / (len(__.boss.Players) * 10000)))
			if tmp:
				pos += [4 for i in range(5 / ((sum(p.temps for p in __.boss.Players) / (len(__.boss.Players) * 10000))))]
		if __.boss.MUR:
			tmp = int(7. / len(__.boss.MUR))
			if tmp:
				pos += [6 for i in range(5 / tmp)]
			tmp = int(10. / len(__.boss.MUR))
			if tmp:
				pos += [7 for i in range(5 / tmp)]
			tmp = int(15. / len(__.boss.MUR))
			if tmp:
				pos += [8 for i in range(5 / tmp)]
		return pos[randrange(len(pos))]
		
	def destroy(__, prise=False):
		if K.draw_explo: Explosion(__.boss, __.x, __.y, r=25*prise, couleur=__.couleur)
		__.x = -20
		__.y = -20
		if __.ind != 6: son = mixer.Sound(K.path_son_effet + "scifi011.ogg")
		else: son = mixer.Sound(K.path_son_effet + "Cosmolazer.ogg")
		son.set_volume(K.vol_effet)
		son.play()
		Sphere.destroy(__)
