from mod.__init__ import *
from wgt_k import *

class Wgt_toolbar(pg.Surface):
	events = [pg.MOUSEBUTTONDOWN]
	def __init__(__, boss, coords, liste_img, liste_fct, size_action = 32, couleur_bg=(0, 0, 0), orient=HORIZONTAL):
		__.boss = boss
		__.coords= coords
		__.imgs = liste_img
		__.fcts = liste_fct
		__.size_case = size_action
		__.bg = couleur_bg
		__.nbr_action = len(__.imgs)
		__.orient = orient
		__.w = __.size_case+bool(orient == HORIZONTAL)*(__.nbr_action - 1)*__.size_case
		__.h = __.size_case+bool(orient == VERTICAL)*(__.nbr_action - 1)*__.size_case
		pg.Surface.__init__(__, (__.w, __.h), pg.HWSURFACE)
		__.fill(pg.Color(__.bg[0], __.bg[1], __.bg[2]))
		__.refresh()

	def refresh(__):
		__.w = __.size_case+bool(__.orient == HORIZONTAL)*(__.nbr_action - 1)*__.size_case
		__.h = __.size_case+bool(__.orient == VERTICAL)*(__.nbr_action - 1)*__.size_case
		pg.Surface.__init__(__, (__.w, __.h), pg.HWSURFACE)
		__.fill(pg.Color(__.bg[0], __.bg[1], __.bg[2]))
		for i, img in enumerate(__.imgs):
			surface = pg.Surface((__.size_case, __.size_case), pg.SRCALPHA)
			surface.set_colorkey(pg.Color(0, 0, 0))
			surface.blit(pg.transform.scale(pg.image.load(img).convert(32, pg.SRCALPHA), (__.size_case, __.size_case)), (0, 0))
			__.blit(surface, (bool(__.orient==HORIZONTAL)*i*__.size_case, bool(__.orient==VERTICAL)*i*__.size_case))

	def event(__, ev):
		if ev.type == pg.MOUSEBUTTONDOWN:
			ev_x, ev_y = ev.pos
			boss = __.boss
			while "coords" in dir(boss):
				ev_x -= boss.coords[0]
				ev_y -= boss.coords[1]
				if "boss" in dir(boss): boss = boss.boss
				else: break
			ev_x -= __.coords[0]
			ev_y -= __.coords[1]
			if 0 <= ev_x < __.w and 0 <= ev_y < __.h:
				if __.orient == HORIZONTAL: __.fcts[ev_x / __.size_case]()
				else: __.fcts[ev_y / __.size_case]()

	def draw(__):
		__.boss.blit(__, __.coords)
