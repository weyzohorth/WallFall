from random import randrange
from spheres import *
from murs import *
from mod.editor import Editor

class Level_random:
	max_murs = 30
	SURVIVE = 1
	GET_ALL_BALL = 2

	def __init__(__, boss):
		__.boss = boss
		__.nbr_lvl = 1
		__.end = __.SURVIVE
		__.init_obj()

	def init_obj(__, murs=liste_murs):
		__.murs = murs
		__.nbr_lvl = len(murs)
		__.boss.MUR = []
		__.boss.SPHERE = []
		__.boss.Players = [Joueur(__.boss)]
		Sphere_score(__.boss)

	def gere_sphere(__):
		bonus = False
		for i in __.boss.SPHERE:
			i.collision()
			if i.__class__ == Sphere_bonus: bonus = True
		if not bonus and not randrange(100): Sphere_bonus(__.boss)

	def gere_bloc(__):
		if __.boss.score >= __.boss.niveau * 100:
			__.boss.niveau += 1
			__.level()
			if __.max_murs < len(__.boss.MUR): #supprime le mur le plus vieux
				__.boss.MUR.pop(0)

	def level(__):
		for i in __.boss.Players: i.temps += 15000
		hasard = randrange(__.boss.niveau)
		x = 3
		#if __.nbr_lvl * x < __.niveau and not (__.niveau / x) % __.nbr_lvl and 1 < len(liste_murs):
		if __.nbr_lvl < __.boss.niveau and not (__.boss.niveau - __.nbr_lvl + 2) % x and 1 < len(__.murs):	#supprime le mur le plus faible de la liste
			__.murs.pop(0)
			__.nbr_lvl -= 1
		__.murs[(hasard / x) % __.nbr_lvl](__.boss)

class Level_random_no_bonus(Level_random):
	def gere_sphere(__):
		for i in __.boss.SPHERE:
			i.collision()

class Level_one_bloc(Level_random):
	bloc = randrange(nbr_lvl)
	def init_obj(__, mur=liste_murs[bloc % nbr_lvl], n=0):
		__.murs = [mur]
		__.boss.MUR = [mur(__.boss) for i in range(n)]
		__.boss.sphere_score = Sphere_score(__.boss)

class Level_one_bloc_no_bonus(Level_one_bloc, Level_random_no_bonus):
	def gere_sphere(__):
		Level_random_no_bonus.gere_sphere(__)

class Level_load(Level_random_no_bonus, Editor):
	def __init__(__, boss, map=K.path_map + "temp.wf"):
		__.mapname = map
		Level_random.__init__(__, boss)
		__.end = __.GET_ALL_BALL

	def init_obj(__):
		__.boss.MUR = []
		__.boss.SPHERE = []
		__.boss.Players = []
		Editor.load(__, __.mapname)
		__.level_load_spheres()
		__.level_load_blocs()

	def level_load_spheres(__):
		for sph in __.list_spheres:
			if not sph["sphere"]: __.boss.Players.append(Joueur(__.boss, sph["x"] + 12.5, sph["y"] + 12.5))
			elif sph["sphere"] == 1: Sphere_score(__.boss, sph["x"] + 12.5, sph["y"] + 12.5)
			else: Sphere_bonus(__.boss, sph["x"] + 12.5, sph["y"] + 12.5, sph["sphere"] - 1)

	def level_load_blocs(__):
		y = 0
		dec = __.bloc_width / 2
		while y < len(__.map):
			x = 0
			while x < len(__.map[y]):
				bloc = __.map[y][x]
				if bloc["bloc"] != -1:
					X, Y = x * __.bloc_width + dec, y * __.bloc_width + dec
					img = "bloc" + str(bloc["bloc"] + 1)
					for i in liste_murs:
						if i.image == img:
							i(__.boss, X, Y, bloc["direction"], loaded=True)
							break
				x += 1
			y += 1

	def level(__):
		for i in __.boss.Players: i.temps += 15000

	def gere_bloc(__):
		if __.boss.score >= __.boss.niveau * 100:
			__.boss.niveau += 1
			__.level()
