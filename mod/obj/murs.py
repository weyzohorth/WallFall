# -*- coding: cp1252 -*-
from random import randrange
from math import cos, sin, pi
from mod.__init__ import *
from explosion import *

#===============================================================================
#                                                                             murs
#===============================================================================
class Mur:
	"""Bloc normal : Vous fait perdre 1 vie en cas de contact,
inutile de vous dire de les eviter ."""
	image = "bloc1"
	couleur = "#0310eb"
	son_colli = mixer.Sound(K.path_son_effet + "scifi002.ogg")
	son_colli.set_volume(K.vol_effet)
	son_explo = mixer.Sound(K.path_son_effet + "scifi017.ogg")
	son_explo.set_volume(K.vol_effet)
	coord_start = 80
	coord_explo_start = -10
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
	increase_speed = K.d_time
	add_speed = 0
	mult_speed = 1

	def __init__(__, boss, x=None, y=None, dir=None, loaded=False):
		son = mixer.Sound(K.path_son_effet + "1up.ogg")
		son.set_volume(K.vol_effet)
		if not loaded: son.play()
		__.i_special = 0
		__.boss = boss
		__.boss.MUR.append(__)
		__.particule = 0
		__.speed = 0
		__.i_start = 0
		__.direction = dir
		__.x, __.y = x, y
		__.ystart, __.xstart = __.y, __.x
		if __.x == None or __.y == None or __.direction == None:
			__.new_coords()
		__.get_speed()
		__.caract()
		__.image_sprite = __.image[:]
		#__.sprite = pygame.image.load(K.path_img_bloc + __.image_sprite + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
		__.W, __.H = __.sprite.get_size()
		__.w, __.h = __.W, __.H
		__.sprite_cache = __.sprite_camoufle = False
		if K.draw_explo and not loaded: __.__explosion__()

	def caract(__): pass

	def get_speed(__):
		__.speed = int(10 * K.d_time)
		if __.speed < 1: __.speed = 1

	def get_real_speed(__):
		return (__.speed + __.add_speed) * __.mult_speed
		
	def bouge(__):
		if __.direction == 1:
			if __.y > -20: __.y -= __.get_real_speed()
			else: __.new_coords()
		elif __.direction == 2:
			if __.x > -20: __.x -= __.get_real_speed()
			else: __.new_coords()
		elif __.direction == 3:
			if __.y < __.boss.size + 20: __.y += __.get_real_speed()
			else: __.new_coords()
		else:
			if __.x < __.boss.size + 20: __.x += __.get_real_speed()
			else: __.new_coords()

		__.special()
		__.collision()

	def draw(__):
		rect = pygame.Rect((__.x, __.y), (__.w, __.h))
		rect.center = (__.x, __.y)
		K.screen.blit(__.sprite, rect)

	def special(__):
		__.i_special += 1
		if K.ratio_d_time <= __.i_special:
			__.i_special = 0
			if __.boss.camoufle_mur > 0:
				if not __.sprite_camoufle:
					__.sprite_camoufle = True
					__.image_sprite = Mur_camoufle.image[:]
					__.sprite = pygame.image.load(K.path_img_bloc + __.image_sprite + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
			elif __.sprite_camoufle:
					__.sprite_camoufle = False
					__.image_sprite = __.image[:]
					__.sprite = pygame.image.load(K.path_img_bloc + __.image_sprite + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
	
			if __.boss.cache_mur > 0:
				if not __.sprite_cache:
					__.sprite_cache = True
					__.w, __.h = __.w/2, __.h/2
					__.sprite = pygame.transform.scale(__.sprite, (__.w, __.h))
			else:
				if __.sprite_cache:
					__.sprite_cache = False
					__.w, __.h = __.W, __.H
					__.sprite = pygame.image.load(K.path_img_bloc + __.image_sprite + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
				if K.draw_queue: __.__particule__()

	def __explosion__(__, destroy=False):
		if destroy: x, y = __.x, __.y
		else: x, y = __.xstart, __.ystart
		if K.draw_explo:
			if __.boss.camoufle_mur > 0:
				Explosion(__.boss, x, y, 20, Mur_camoufle.couleur, dr = K.d_time/2, carre = True)
			else:
				Explosion(__.boss, x, y, 20, __.couleur, dr = K.d_time/2, carre = True)
		
	def __particule__(__):
		if __.speed:
			if not __.particule:
				if __.boss.camoufle_mur > 0: Particule(__.boss, __.x, __.y, 0, 0, 20, Mur_camoufle.couleur, K.d_time*2, True)
				else: Particule(__.boss, __.x, __.y, 0, 0, 20, __.couleur, K.d_time*2, True)
				if 0 < __.i_start:
					__.particule_start()
					__.i_start -= 1
			__.particule += 1
			if __.particule >= 5 + 2 * (K.ratio_d_time - 1): __.particule = 0
	
	def particule_start(__):
		if K.draw_queue and __.speed:
			if __.boss.camoufle_mur > 0:
				Particule(__.boss, __.x, __.y, __.direction * 90, __.get_real_speed() * 5, 20, Mur_camoufle.couleur, K.d_time * 1.5, True)
			else:
				Particule(__.boss, __.x, __.y, __.direction * 90, __.get_real_speed() * 5, 20, __.couleur, K.d_time * 1.5, True)

	def new_coords(__):
		bool = True
		while bool:
			__.direction = randrange(4)
			if __.direction == 1:
				__.y = __.boss.size + __.coord_start
				__.x = randrange(20,__.boss.size - 20)
				__.xstart, __.ystart = __.x, __.y - __.coord_start + __.coord_explo_start
			elif __.direction == 2:
				__.x = __.boss.size + __.coord_start
				__.y = randrange(20,__.boss.size - 20)
				__.ystart, __.xstart = __.y, __.x - __.coord_start + __.coord_explo_start
			elif __.direction == 3:
				__.y = -__.coord_start
				__.x = randrange(20,__.boss.size - 20)
				__.xstart, __.ystart = __.x, __.y + __.coord_start - __.coord_explo_start
			else:
				__.x = -__.coord_start
				__.y = randrange(20,__.boss.size - 20)
				__.ystart, __.xstart = __.y, __.x + __.coord_start - __.coord_explo_start
			__.i_start = 3
			bool = False
			for i in __.boss.MUR:
				if i != __ and i.x < __.x + 40 and i.x > __.x - 40 and  i.y < __.y + 40 and i.y > __.y - 40:
					bool = True
					break


	def malus(__, obj):
		obj.vie -= 1
		obj.god = 10

	def collision(__):
		for obj in __.boss.Players:
			if not obj.god or obj.berserk:
				if obj.y < __.y +32 and obj.y > __.y - 32 and obj.x < __.x +32 and obj.x > __.x - 32:
					if not obj.berserk:
						__.malus(obj)
						if K.draw_explo: Explosion(__.boss, obj.x, obj.y, r=25, couleur=obj.couleurs[2])
						__.son_colli.play()
					else:
						obj.berserk = 0
						if K.draw_explo: Explosion(__.boss, obj.x, obj.y, r=25, couleur=obj.couleurs[3])
						__.destroy()

	def destroy(__):
		__.boss.MUR.remove(__)
		__.son_explo.play()
		if K.draw_explo: __.__explosion__(True)

#===============================================================================
#                                                  			   mur speed
#===============================================================================
class Mur_speed(Mur):
	"""Bloc de vitesse : Ceux-ci se déplace 1.5 fois plus 
rapidement que les normaux ."""
	image = "bloc5"
	couleur = "#0018ff"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def get_speed(__):
		Mur.get_speed(__)
		__.speed = int(__.speed * 1.5)

#===============================================================================
#                                                  			   mur charge
#===============================================================================
class Mur_charge(Mur):
	"""Bloc charge : Ceux-ci se déplace 2 fois moins vite que les 
normaux . Mais, il accélèrera si vous passez dans sa trajectoire ."""
	image = "bloc12"
	couleur = "#541af7"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def get_speed(__):
		Mur.get_speed(__)
		__.speed_max = int(__.speed * 2)
		__.speed = __.speed_min = int(__.speed * .5)

	def change_speed(__):
		bool = False
		for obj in __.boss.Players:
			if obj.x > __.x and obj.y < __.y + 32 and obj.y > __.y - 32 and __.direction == 0 or\
			obj.x < __.x and obj.y < __.y + 32 and obj.y > __.y - 32 and __.direction == 2 or\
			obj.y > __.y and obj.x < __.x + 32 and obj.x > __.x - 32 and __.direction == 3 or\
			obj.y < __.y and obj.x < __.x + 32 and obj.x > __.x - 32 and __.direction == 1:
				bool = True
				break
		if bool: __.speed = __.speed_max
		else: __.speed = __.speed_min

	def bouge(__):
		__.change_speed()
		Mur.bouge(__)

	def new_coords(__):
		try: __.speed = __.speed_min
		except: pass
		Mur.new_coords(__)

#===============================================================================
#                                                  			   mur accel
#===============================================================================
class Mur_accel(Mur):
	"""Bloc accel : Ils apparaisent avec une vitesse nulle et
accélèrent par la suite ."""
	image = "bloc13"
	couleur = "#24b6fc"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def get_speed(__):
		__.speed = 0

	def bouge(__):
		__.speed += K.d_time / 2
		Mur.bouge(__)

	def new_coords(__):
		__.speed = 0
		Mur.new_coords(__)
#===============================================================================
#                                                              mur immobile
#===============================================================================
class Mur_immobile(Mur):
	"""Bloc fixe : Même chose que les précédents, excepté qu'ils 
sont immobiles ."""
	image = "bloc2"
	couleur = "#414141"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def new_coords(__):
		temp = False
		while not temp:
			__.x = randrange(20,__.boss.size - 20)
			__.y = randrange(20,__.boss.size - 20)
			for i in __.boss.SPHERE:
				if DISTANCE(__.x, __.y, i.x, i.y) >= 20:
					temp = True
				else:
					temp = False
					break
			if temp:
				for obj in __.boss.Players:
					if DISTANCE(__.x, __.y, obj.x, obj.y) <= 40:
						temp = False
						break
			if temp:
				for obj in __.boss.MUR:
					if obj != __ and (__.x - 40 < obj.x < __.x + 40  or __.y - 40 < obj.y < __.y + 40):
						temp = False
						break
		__.xstart, __.ystart = __.x, __.y

	def __particule__(__):pass

	def bouge(__):
		__.special()
		__.collision()

#===============================================================================
#                                                              mur bloqueur
#===============================================================================
class Mur_bloqueur(Mur_immobile):
	"""Bloc bloqueur : Ces blocs sont immobiles et vous bloquent.
Mais ils ne font aucun dégâts."""
	image = "bloc18"
	couleur = "#cdcdcc"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
	
	def collision(__):
		for obj in __.boss.Players:
			if obj.y < __.y +32 and obj.y > __.y - 32 and obj.x < __.x +32 and obj.x > __.x - 32:
				if not obj.berserk:
					__.malus(obj)
				else:
					obj.berserk = 0
					if K.draw_explo: Explosion(__.boss, obj.x, obj.y, r=25, couleur=obj.couleurs[3])
					__.destroy()

	def malus(__, obj):
		if DISTANCE(obj.x, obj.y, __.x, __.y) < 20:
			obj.vie -= 1
		obj.x = obj.x - cos(obj.direction * pi / 180) * obj.speed
		obj.y = obj.y + sin(obj.direction * pi / 180) * obj.speed

#===============================================================================
#                                                  			   mur suiveur
#===============================================================================
class Mur_suiveur(Mur_immobile, Mur):
	"""Bloc suiveur : Un bloc immobile, mais lorsque vous êtes en 
face de lui, il se déplacera vers vous"""
	image = "bloc7"
	couleur = "#901602"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def bouge(__):
		y1, y2 = __.y - 32, __.y + 32
		x1, x2 = __.x - 32, __.x + 32
		for obj in __.boss.Players:
			if obj.y < __.y and x1 <= obj.x <= x2: __.y -= __.get_real_speed()
			elif obj.y > __.y and x1 <= obj.x <= x2: __.y += __.get_real_speed()
			elif obj.x < __.x and y1 <= obj.y <= y2: __.x -= __.get_real_speed()
			elif obj.x > __.x and y1 <= obj.y <= y2: __.x += __.get_real_speed()
		__.collision()
		__.special()

	def __particule__(__):
		Mur.__particule__(__)

#===============================================================================
#                                                  			   mur de temps
#===============================================================================
class Mur_temps(Mur):
	"""Bloc de temporel : Ceux-là sont mobiles et en plus, de vous 
enlever de la vie, ils vous feront perdre 10 secondes ."""
	image = "bloc3"
	couleur = "#7c029b"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		obj.temps -= 5000

#===============================================================================
#                                                  			   mur de score
#===============================================================================
class Mur_score(Mur):
	"""Bloc score : Vous fait perdre 100 de score en cas de contact ."""
	image = "bloc6"
	couleur = "#05a000"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		obj.score -= 100

#===============================================================================
#                                                  			   mur de ralenti
#===============================================================================
class Mur_ralenti(Mur):
	"""Bloc de ralenti : Ces blocs vous ralentirons fortement mais
vous réaccélérerer progressiment après ."""
	image = "bloc8"
	couleur = "#3d3d3d"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		obj.speed -= obj.i_speed

#===============================================================================
#                                                  			   mur inverse
#===============================================================================
class Mur_inverse(Mur):
	"""Bloc inverse : Ces blocs vous feront avancer en marche arrière."""
	image = "bloc14"
	couleur = "#9c9c9c"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		obj.inverse += 30

#===============================================================================
#                                                  			   mur berserk
#===============================================================================
class Mur_berserk(Mur):
	"""Bloc berserk : Le moindre contact avec ce bloc
et c'est le game over, même si vous posséder 10 vies ."""
	image = "bloc9"
	couleur = "#630001"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def get_speed(__):
		Mur.get_speed(__)
		__.speed = int(__.speed * .5)

	def malus(__, obj): obj.vie = 0
#===============================================================================
#                                                               mur rebond
#===============================================================================
class Mur_rebond(Mur):
	"""Bloc rebond : Ceux-ci sont pareil que les normaux,
mais rebondissent sur tous les blocs ."""
	image = "bloc4"
	couleur = "#960000"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def collision(__):
		for m in __.boss.MUR:
			if m != __:
				if m.y < __.y +20 and m.y > __.y - 20 and\
				   m.x < __.x +40 and m.x > __.x + 20: __.direction = 2
				elif m.y < __.y +20 and m.y > __.y - 20 and\
				   m.x > __.x - 40 and m.x < __.x - 20: __.direction = 0
				elif m.x < __.x +20 and m.x > __.x - 20 and\
				   m.y < __.y +40 and m.y > __.y + 20: __.direction = 1
				elif m.x < __.x +20 and m.x > __.x - 20 and\
					m.y > __.y - 40 and m.y < __.y - 20: __.direction = 3
		Mur.collision(__)

#===============================================================================
#                                                               mur direction
#===============================================================================
class Mur_direction(Mur):
	"""Bloc direction : Ce bloc change de direction dès que vous 
êtes en face de lui ."""
	image = "bloc10"
	couleur = "#6c1404"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
	
	def caract(__): __.obj = __.boss.Players[randrange(len(__.boss.Players))]

	def bouge(__):
		y1, y2 = __.y - 32, __.y + 32
		x1, x2 = __.x - 32, __.x + 32
		if __.obj.y < __.y and x1 <= __.obj.x <= x2: __.direction = 1
		elif __.obj.y > __.y and x1 <= __.obj.x <= x2: __.direction = 3
		elif __.obj.x < __.x and y1 <= __.obj.y <= y2: __.direction = 2
		elif __.obj.x > __.x and y1 <= __.obj.y <= y2: __.direction = 0
		Mur.bouge(__)

#===============================================================================
#                                                               mur depart
#===============================================================================
class Mur_depart(Mur):
	"""Bloc depart : Apparaît de facon à être directement en face
de vous ."""
	image = "bloc11"
	couleur = "#02eaa3"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def new_coords(__):
		obj = __.boss.Players[randrange(len(__.boss.Players))]
		__.direction = randrange(4)
		if __.direction == 1:
			__.y = __.boss.size + __.coord_start
			__.x = obj.x
			__.xstart, __.ystart = __.x, __.y - __.coord_start + __.coord_explo_start
		elif __.direction == 2:
			__.x = __.boss.size + __.coord_start
			__.y = obj.y
			__.ystart, __.xstart = __.y, __.x - __.coord_start + __.coord_explo_start
		elif __.direction == 3:
			__.y = -__.coord_start
			__.x = obj.x
			__.xstart, __.ystart = __.x, __.y + __.coord_start - __.coord_explo_start
		else:
			__.x = -__.coord_start
			__.y = obj.y
			__.ystart, __.xstart = __.y, __.x + __.coord_start - __.coord_explo_start
		__.i_start = 3

#===============================================================================
#                                                               mur near
#===============================================================================
class Mur_near(Mur):
	"""Bloc near : Apparaît de facon à être le plus proche de vous.
de vous ."""
	image = "bloc19"
	couleur = "#00de60"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def new_coords(__):
		obj = __.boss.Players[randrange(len(__.boss.Players))]
		temp = __.boss.size / 2
		__.direction = int((DIRECTION(obj.x, obj.y, temp, temp) + 45) % 360 ) / 90
		if __.direction == 1:
			__.y = __.boss.size + __.coord_start
			__.x = obj.x
			__.xstart, __.ystart = __.x, __.y - __.coord_start + __.coord_explo_start
		elif __.direction == 2:
			__.x = __.boss.size + __.coord_start
			__.y = obj.y
			__.ystart, __.xstart = __.y, __.x - __.coord_start + __.coord_explo_start
		elif __.direction == 3:
			__.y = -__.coord_start
			__.x = obj.x
			__.xstart, __.ystart = __.x, __.y + __.coord_start - __.coord_explo_start
		else:
			__.x = -__.coord_start
			__.y = obj.y
			__.ystart, __.xstart = __.y, __.x + __.coord_start - __.coord_explo_start
		__.i_start = 3
	
#===============================================================================
#                                                               mur cache
#===============================================================================
class Mur_cache(Mur):
	"""Bloc cacheur : son apparence est trompeuse,
il semble être plus petit que la moyenne, mais ce n'est pas le cas.
Si vous touchez ce bloc, tous les autres auront une apparence
plus petite ."""
	image = "bloc15"
	couleur = "#383700"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		__.boss.cache_mur += 300

#===============================================================================
#                                                               mur camoufle
#===============================================================================
class Mur_camoufle(Mur):
	"""Bloc de cammouflage : Si vous touchez ce bloc, tous les
autres blocs prendront son apparence, ce qui n'est pas commode
du tout pour les différencier ."""
	image = "bloc16"
	couleur = "#ffe200"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		__.boss.camoufle_mur += 300

#===============================================================================
#                                                               mur painting
#===============================================================================
class Mur_painting(Mur):
	"""Bloc de cammouflage : Si vous touchez ce bloc,
tous les autres blocs prendront son apparence,
ce qui n'est pas commode  du tout pour les différencier."""
	image = "bloc17"
	couleur = "#ffe200"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		__.boss.painting += 300

#===============================================================================
#                                                               mur go_ahead
#===============================================================================
class Mur_go_ahead(Mur):
	"""Bloc go ahead : Ces blocs iront toujours dans la même,
direction et sur le même axe."""
	image = "bloc20"
	couleur = "#6163ba"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)
	coord_start = 40
	coord_explo_start = -10

	def new_coords(__):
		if __.direction == None:
			__.direction = randrange(4)
		if __.direction == 1:
			__.y = __.boss.size + __.coord_start
			if __.x == None:
				__.x = randrange(20,__.boss.size - 20)
			__.xstart, __.ystart = __.x, __.y - __.coord_start + __.coord_explo_start
		elif __.direction == 2:
			__.x = __.boss.size + __.coord_start
			if __.y == None:
				__.y = randrange(20,__.boss.size - 20)
			__.ystart, __.xstart = __.y, __.x - __.coord_start + __.coord_explo_start
		elif __.direction == 3:
			__.y = -__.coord_start
			if __.x == None:
				__.x = randrange(20,__.boss.size - 20)
			__.xstart, __.ystart = __.x, __.y + __.coord_start - __.coord_explo_start
		else:
			__.x = -__.coord_start
			if __.y == None:
				__.y = randrange(20,__.boss.size - 20)
			__.ystart, __.xstart = __.y, __.x + __.coord_start - __.coord_explo_start
		__.i_start = 3

#===============================================================================
#                                                               mur turn_back
#===============================================================================
class Mur_turn_back(Mur_go_ahead):
	"""Bloc turn back : Ces blocs font demi tour sur le même axe."""
	image = "bloc21"
	couleur = "#514f98"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def new_coords(__):
		if __.direction == None: __.direction = randrange(4)
		else: __.direction = (__.direction + 2) % 4
		Mur_go_ahead.new_coords(__)

class Mur_boost_speed(Mur):
	"""Bloc boost speed : Ces blocs accelerent la vitesse de tous
les blocs"""
	image = "bloc22"
	couleur = "#34bbbf"
	sprite = pygame.image.load(K.path_img_bloc + image + ".png").convert(32, pygame.HWSURFACE | pygame.SRCALPHA)

	def malus(__, obj):
		Mur.malus(__, obj)
		Mur.add_speed += 0.5
		Mur.mult_speed += 0.25

#===============================================================================
#       			 liste_murs : liste utilisee pour l'ordre d'apparition des murs au cour du jeu
#===============================================================================
liste_murs = [
Mur,
Mur_immobile,
Mur_rebond,
Mur_camoufle,
Mur_bloqueur,
Mur_charge,
Mur_depart,
Mur_temps,
Mur_score,
Mur_speed,
Mur_painting,
Mur_near,
Mur_turn_back,
Mur_go_ahead,
Mur_cache,
Mur_suiveur,
Mur_ralenti,
Mur_accel,
Mur_direction,
Mur_boost_speed,
Mur_inverse,
Mur_berserk
]
nbr_lvl = len(liste_murs)

