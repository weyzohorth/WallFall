import os
import sys
if not "mod" in os.listdir(os.getcwd()):
	os.chdir("..")
	from obj.murs import *
	from wgt.wgt_progression import *
	from wgt.wgt_bouton import *
	from __init__ import *
	from fen.__init__ import *
	if sys.platform == "win32":
		from fct.mod_reg import *
	import fen.savefen as sf
	import fct.mod_base as base
else:
	from mod.obj.murs import *
	from mod.wgt.wgt_progression import *
	from mod.wgt.wgt_bouton import *
	from mod.__init__ import *
	from mod.fen.__init__ import *
	if sys.platform == "win32":
		from mod.fct.mod_reg import *
	import mod.fen.savefen as sf
	import mod.fct.mod_base as base

class Editor(Abs_menu):
	bloc_width = liste_murs[0].sprite.get_width()
	nb_bloc = K.w / bloc_width
	map = [[{"bloc": -1, "direction": 0} for x in range(nb_bloc)] for y in range(nb_bloc)]
	filename = ""
	list_spheres = []
	flags = {"random": 1, "bonus": 1, "survival": 0, "get_all": 0, "time": 60, "score": -1}
	ext = ".wf"

	def __init__(__, boss=None, map=""):
		Abs_menu.__init__(__)
		__.boss = boss
		__.img_dir = pygame.image.load(K.path_img_menu + "direction.png").convert(32, pygame.SRCALPHA)
		__.direction = 0
		__.index_player = -1
		__.board = __.Board(__)
		__.running = True
		__.clic = 0
		if sys.platform == "win32":
			__.ext_is_in_reg()
		#if map:
		#	__.load(map)
		__.loop()

	def ext_is_in_reg(__):
		if not is_in_reg(HKEY_CLASSES_ROOT, __.ext):
			save_in_reg(__.ext[1 : ], "editor.py", get_PythonPath()[0] + "pythonw " + os.getcwd() + '\\', os.getcwd() + "\\..\\data\\images\jeu\blocs\bloc1.png")
		
	def loop(__):
		temps = pygame.time.get_ticks()
		while __.running:
			__.blit()
			__.event()
			temp = pygame.time.get_ticks()
			temps, temps_passe = temp, temp - temps
			pygame.time.wait(120 - temps_passe)
		if not __.boss: pygame.quit()
		else: K.display.fill(0)

	def event(__):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				__.running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				__.clic = event.button
				__.event_clic(event)
			elif event.type == pygame.MOUSEBUTTONUP:
				__.clic = 0
			elif event.type == pygame.MOUSEMOTION and __.clic:
				__.event_clic(event)
			__.board.event(event)

	def event_clic(__, event):
		x, y = event.pos
		if x < __.size:
			x = x / __.bloc_width
			y = y / __.bloc_width
			if __.clic == 1:
				if __.board.spheres:
					X, Y = x * __.bloc_width + 12, y * __.bloc_width + 12
					if not __.board.select:
						if __.index_player != -1:
							__.list_spheres.pop(__.index_player)
						__.index_player = len(__.list_spheres)
					else:
						for i, sph in enumerate(__.list_spheres):
							if sph["x"] == X and sph["y"] == Y:
								__.list_spheres.remove(sph)
								__.list_spheres.insert(i, {"sphere": __.board.select, "x": X, "y": Y})
								return
					__.list_spheres.append({"sphere": __.board.select, "x": X, "y": Y})
				else:
					__.map[y][x]["bloc"] = __.board.select
					__.map[y][x]["direction"] = __.direction
			elif __.clic == 3:
				if not __.board.spheres:
					__.map[y][x]["bloc"] = -1
				else:
					for sph in __.list_spheres:
						if event.pos[0] - 25 <= sph["x"] < event.pos[0] and event.pos[1] - 25 <= sph["y"] < event.pos[1]:
							if not sph["sphere"]:
								__.index_player = -1
							__.list_spheres.remove(sph)
			elif __.clic == 4:
				if __.map[y][x]["bloc"] == -1:
					__.direction = (__.direction + 1) % 4
				else:
					__.map[y][x]["direction"] = (__.map[y][x]["direction"] + 1) % 4
					__.direction = __.map[y][x]["direction"]
			elif __.clic == 5:
				if __.map[y][x]["bloc"] == -1:
					__.direction = (__.direction - 1) % 4
				else:
					__.map[y][x]["direction"] = (__.map[y][x]["direction"] - 1) % 4
					__.direction = __.map[y][x]["direction"]

	def blit(__):
		K.display.blit(K.screen, (0, 0))
		K.screen.blit(K.back, (0, 0))
		__.board.blit_widget()
		y = 0
		while y < len(__.map):
			x = 0
			while x < len(__.map[y]):
				if __.map[y][x]["bloc"] != -1:
					X, Y = x * __.bloc_width, y * __.bloc_width
					K.screen.blit(__.board.imgs_blocs[__.map[y][x]["bloc"]], (X, Y))
					K.screen.blit(pygame.transform.rotate(__.img_dir, __.map[y][x]["direction"] * 90), (X, Y))
				x += 1
			y += 1
		for sph in __.list_spheres:
			K.screen.blit(__.board.imgs_spheres[sph["sphere"]], (sph["x"], sph["y"]))
		K.display.blit(__.board, (__.size, 0))
		pygame.display.update()

	def clear(__):
		__.list_spheres = []
		__.index_player = -1
		y = 0
		while y < len(__.map):
			x = 0
			while x < len(__.map[y]):
				__.map[y][x]["bloc"] = -1
				__.map[y][x]["direction"] = 0
				x += 1
			y += 1

	def save(__, map=K.path_map + "save.wf"):
		fichier = file(map, "wb")
		__.save_spheres(fichier)
		__.save_blocs(fichier)
		fichier.close()

	def save_spheres(__, fichier):
		for sph in __.list_spheres:
			int_save = 1
			int_save = (int_save << 4) + sph["sphere"]
			int_save = (int_save << 10) + sph["x"]
			int_save = (int_save << 10) + sph["y"]
			__.save_data(fichier, int_save, base._256_()[-1])

	def save_blocs(__, fichier):
		y = 0
		while y < len(__.map):
			x = 0
			while x < len(__.map[y]):
				if __.map[y][x]["bloc"] != -1:
					__.save_bloc(fichier, __.map[y][x], x, y)
				x += 1
			y += 1

	def save_bloc(__, fichier, bloc, x, y):
		int_save = 0
		int_save = (int_save << 5) + bloc["bloc"]
		int_save = (int_save << 2) + bloc["direction"]
		int_save = (int_save << 5) + x
		int_save = (int_save << 5) + y
		__.save_data(fichier, int_save)

	def save_data(__, fichier, data, fill="0"):
		save = base.int_base(data)
		save = "".join([fill for i in range(4 - len(save))] + [save])
		fichier.write(save)

	def save_flag(__, fichier):
		int_save = __.flags["random"]
		int_save = (int_save << 1) + __.flags["bonus"]
		int_save = (int_save << 1) + __.flags["survival"]
		int_save = (int_save << 1) + __.flags["get_all"]
		int_save = (int_save << 13) + __.flags["time"]
		int_save = (int_save << 13) + __.flags["score"] + 1
		print "score", int_save
		#__.save_data(fichier, int_save)


	def load(__, file_map=K.path_map + "save.wf"):
		fichier = file(file_map, "rb")
		__.clear()
		__.load_spheres(fichier)
		fichier.close()

	def load_spheres(__, fichier):
		is_sphere = 16777216
		int_obj = base.base_int(fichier.read(4))
		__.list_spheres = []
		temp = 1
		while temp and (int_obj & is_sphere) == is_sphere:
			__.load_sphere(int_obj)
			temp = fichier.read(4)
			int_obj = base.base_int(temp)
		if temp:
			__.load_blocs(fichier, int_obj)

	def load_blocs(__, fichier, int_bloc):
		temp = 1
		while temp:
			__.load_bloc(int_bloc)
			temp = fichier.read(4)
			int_bloc = base.base_int(temp)

	def load_sphere(__, int_sphere):
		dico = {"sphere": 0, "x": 0, "y": 0}
		dico["y"] = int_sphere
		int_sphere = int_sphere >> 10
		dico["y"] -= int_sphere << 10
		dico["x"] = int_sphere
		int_sphere = int_sphere >> 10
		dico["x"] -= int_sphere << 10
		dico["sphere"] = int_sphere - (int_sphere >> 4 << 4)
		if not dico["sphere"]:
			__.index_player = len(__.list_spheres)
		__.list_spheres.append(dico)

	def load_bloc(__, int_bloc):
		y = int_bloc
		int_bloc = int_bloc >> 5
		y -= int_bloc << 5
		x = int_bloc
		int_bloc = int_bloc >> 5
		x -= int_bloc << 5
		__.map[y][x]["direction"] = int_bloc
		int_bloc = int_bloc >> 2
		__.map[y][x]["direction"] -= int_bloc << 2
		__.map[y][x]["bloc"] = int_bloc - (int_bloc >> 5 << 5)

	def load_flag(__):
		pass

	class Board(pygame.Surface):
		def __init__(__, boss):
			__.boss = boss
			pygame.Surface.__init__(__, (__.boss.size + K.hud, __.boss.size))
			__.back = pygame.Surface((__.boss.size + K.hud, __.boss.size))
			__.back.fill((40, 40, 40))
			__.coords = [__.boss.size, 0]
			__.spheres = True
			__.imgs_blocs = [pygame.image.load(K.path_img_bloc + "bloc" + str(i) + ".png").convert(32, pygame.SRCALPHA) for i in range(1, len(liste_murs) + 1)]
			__.imgs_spheres = [pygame.image.load(K.path_img_sphere + "rond" + str(i) + ".png").convert(32, pygame.SRCALPHA) for i in range(1, len(os.listdir(K.path_img_sphere)) - 3)]
			__.len_blocs = len(__.imgs_blocs)
			__.len_spheres = len(__.imgs_spheres)
			__.scroll_width = 10
			__.button_height = 20
			__.border = 5
			__.bloc_width = __.boss.bloc_width + __.border
			__.xstart = __.scroll_width + __.border
			__.ystart = __.button_height * 4 + __.border
			__.nb_img = (K.hud - __.xstart) / __.bloc_width
			but_width = (K.hud - __.scroll_width) / 2
			__.widgets = [Wgt_progression(__, 0, 0, __.scroll_width, __.boss.size, value=0, value_max=0, orient=VERTICAL),
									Wgt_bouton(__, __.scroll_width, 0, but_width, __.button_height,
									           text1="New", font=K.path_font + "VideoPhreak.ttf", fonction=__.new),
									Wgt_bouton(__, __.scroll_width + but_width, 0, but_width, __.button_height,
									           text1="Load", font=K.path_font + "VideoPhreak.ttf", fonction=__.load),

									Wgt_bouton(__, __.scroll_width, __.button_height, but_width, __.button_height,
									           text1="Save", font=K.path_font + "VideoPhreak.ttf", fonction=__.save),
									Wgt_bouton(__, __.scroll_width + but_width, __.button_height, but_width, __.button_height,
									           text1="Save As", font=K.path_font + "VideoPhreak.ttf", fonction=__.save_as),

									Wgt_bouton(__, __.scroll_width, __.button_height * 2, but_width, __.button_height,
									           text1="Blocs", font=K.path_font + "VideoPhreak.ttf", fonction=__.select_blocs),
									Wgt_bouton(__, __.scroll_width + but_width, __.button_height * 2, but_width, __.button_height,
									           text1="Spheres", font=K.path_font + "VideoPhreak.ttf", fonction=__.select_spheres),

									Wgt_bouton(__, __.scroll_width, __.button_height * 3, but_width * 2, __.button_height,
												text1="Test", font=K.path_font + "VideoPhreak.ttf", fonction=__.test,
												coul1=(55, 0, 0), coul_font1=(200, 200, 0))
									]
			__.select = 0
			__.select_img = pygame.image.load(K.path_img_menu + "select.png").convert(32, pygame.SRCALPHA)

		def event(__, event):
			for wgt in __.widgets:
				if event.type in wgt.events:
					wgt.event(event)
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					x, y = event.pos
					x -= __.coords[0] + __.xstart
					y -= __.coords[1] + __.ystart
					if 0 <= x and 0 <= y:
						temp = x / __.bloc_width + y / __.bloc_width * __.nb_img
						if temp < __.len_blocs and not __.spheres or temp < __.len_spheres and __.spheres:
							__.select = temp

		def blit_widget(__):
			__.blit(__.back, (0, 0))
			for wgt in __.widgets:
				wgt.blit()
			__.blit_imgs()

		def blit_imgs(__):
			if __.spheres: imgs = __.imgs_spheres
			else: imgs = __.imgs_blocs
			for i, img in enumerate(imgs):
				x = __.xstart + i % __.nb_img * __.bloc_width
				y = __.ystart + i / __.nb_img * __.bloc_width
				__.blit(img, (x + __.spheres * 8, y + __.spheres * 8))
				if __.select == i :
					__.blit(__.select_img, (x - 2, y - 2))

		def select_blocs(__):
			__.spheres = False

		def select_spheres(__):
			__.spheres = True

		def save_as(__):
			if __.boss.filename:
				sf.SaveFen(__.boss, True, __.boss.filename)
			else:
				sf.SaveFen(__.boss, True)
			if __.boss.filename:
				__.boss.save(__.boss.filename)

		def save(__):
			if __.boss.filename:
				__.boss.save(__.boss.filename)
			else:
				__.save_as()

		def new(__):
			__.boss.clear()
			__.boss.filename = ""

		def load(__):
			if __.boss.filename:
				sf.SaveFen(__.boss, False, __.boss.filename)
			else:
				sf.SaveFen(__.boss, False)
			if __.boss.filename:
				__.boss.load(__.boss.filename)

		def test(__):
			import mod.obj.game as game
			map = K.path_map + "temp" + __.boss.ext
			__.boss.save(map)
			game.Game(__.boss.boss, map)
			__.boss.clic = 0


if __name__ == "__main__":
	#editor = Editor()
	#Editor().save_flag(None)
	if 1 < len(sys.argv):
		Editor(map=sys.argv[1])
	else:
		Editor()
