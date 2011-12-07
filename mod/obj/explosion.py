from random import randrange, randint
from mod.fct.mod_math import *
from mod.fct.hexacouleur import hexa, rvb
from mod.__init__ import *

class Explosion:
	def __init__(__, boss, x, y, r=12.5, couleur="#ffffff", ecart_coul=30, dr=-1, carre=False):
		__.frame = 0
		if boss:
			__.boss, __.x, __.y, __.couleur, __.ecart_coul = boss, x, y, list(hexa(couleur)), ecart_coul
			if dr <= 0: __.dr = K.d_time
			else: __.dr = dr
			if r <= 0: __.r = 12.5
			else: __.r = r
			__.carre = carre
			__.hexa = couleur
			for i in range(3):
				if __.couleur[i] + ecart_coul > 255: __.couleur[i] = 255 - ecart_coul
				elif __.couleur[i] - ecart_coul < 0: __.couleur[i] = ecart_coul
			__.boss.EXPLO.append(__)

	def bouge(__):
		if __.r > 0:
			__.r -= __.dr
			r = int(__.r - 3)
			if not __.frame and r > 4 * __.dr:
				X = __.x + randrange(r) - randrange(r)
				Y = __.y + randrange(r) - randrange(r)
				direct = DIRECTION(__.x, __.y, X, Y)
				speed = DISTANCE(__.x, __.y, X, Y)
				RVB = [__.couleur[i] + randrange(__.ecart_coul) - randrange(__.ecart_coul) for i in range(3)]
				Particule(__.boss, X, Y, direct, speed, randrange(1, int(__.r) + 2), rvb(RVB[0], RVB[1], RVB[2]), __.dr, __.carre)
			__.frame = (__.frame + 1) % 3
		else:
			__.boss.EXPLO.remove(__)
	
	def draw(__):
		if __.carre:
			rect = pygame.Rect((__.x, __.y), (__.r*2, __.r*2))
			rect.center = (__.x, __.y)
			pygame.draw.rect(K.screen, pygame.Color(__.hexa), rect)
		else:
			pygame.draw.circle(K.screen, pygame.Color(__.hexa), (int(__.x), int(__.y)), int(__.r))

class Particule:
	def __init__(__, boss, x, y, direction=0, speed=0, r=10, couleur="#ffffff", dr=-1, carre=False):
		__.boss, __.x, __.y, __.r = boss, x, y, r
		if __.boss:
			__.boss.PARTI.append(__)
			if dr < 0: __.dr = K.d_time * 4
			else: __.dr = dr
			__.dx = cos(direction * pi / 180) * speed * __.dr
			__.dy = - sin(direction * pi / 180) * speed * __.dr
			__.carre = carre
			__.couleur = couleur

	def bouge(__):
		__.r -= __.dr
		if __.r > 0:
			__.x += __.dx
			__.y += __.dy
		else:
			__.boss.PARTI.remove(__)

	def draw(__):
		if __.carre:
			rect = pygame.Rect((__.x, __.y), (__.r*2, __.r*2))
			rect.center = (__.x, __.y)
			pygame.draw.rect(K.screen, pygame.Color(__.couleur), rect)
		else:
			pygame.draw.circle(K.screen, pygame.Color(__.couleur), (int(__.x), int(__.y)), int(__.r))
