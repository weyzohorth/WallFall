from mod.fct.mod_file import get_allfiles
from os import mkdir
VERSION = "5.0"
GAME = "WALLFALL"

import pygame
pygame.init()
display = pygame.display
mixer = pygame.mixer

class Constantes:
	def __init__(__):
		__.hud = 200
		__.w = __.h = 700
		try:
			data = file("data/data")
			__.vol_musique = int(data.readline()) / 100.
			__.vol_effet = int(data.readline()) / 100.
			__.set_frame_rate(float(data.readline()))
			__.xdec = int(data.readline())
			__.ydec = int(data.readline())
			__.draw_explo = bool(int(data.readline()))
			__.draw_queue = bool(int(data.readline()))
			__.display_online = bool(int(data.readline()))
			data.close()
		except Exception, err:
			print err
			file("data/data", "w") .write("100\n100\n24\n0\n0\n1\n1\n640\n640\n1\n")
			__.vol_musique = __.vol_effet = 1.0
			__.set_frame_rate(40)
			__.xdec = __.ydec = 0
			__.draw_explo = __.draw_queue = True
			__.display_online = True
		mixer.music.set_volume(__.vol_musique)

		__.path_img_bloc = "data/images/jeu/blocs/"
		__.path_img_sphere = "data/images/jeu/spheres/"
		__.path_img_menu = "data/images/menu/"
		__.path_musique_jeu = "data/sons/musiques/jeu"
		__.path_musique_menu = "data/sons/musiques/menu"
		__.path_son_effet = "data/sons/effets/"
		__.path_font = "data/fonts/"
		__.path_map = "data/maps/"

		__.musiques_jeu = tuple(get_allfiles(__.path_musique_jeu))
		__.musiques_menu = tuple(get_allfiles(__.path_musique_menu))
		__.len_musiques_jeu = len(__.musiques_jeu)
		__.len_musiques_menu = len(__.musiques_menu)

		__.liste_murs = []

	def set_frame_rate(__, x):
		__.frame_rate = x
		__.frame_time = int(1000 / __.frame_rate)
		adjust = (__.frame_rate - 24) / 500.
		__.d_time = __.frame_time / 100. + adjust
		def_d_time = (1000 / 24) / 100.
		__.ratio_d_time = def_d_time / (__.d_time + adjust)

	def set_resolution(__, w, h):
		w -= __.hud
		__.display = pygame.display.set_mode((w + __.hud, h))
		__.screen = pygame.Surface((w, h))
		__.w = w
		__.h = h
		__.back = pygame.Surface((__.w, __.h))

K = Constantes()

