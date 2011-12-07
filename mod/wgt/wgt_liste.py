import pygame

class Wgt_liste:
	events = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]

	def __init__(__, boss, x, y, w, h, nbr_item_visible=10,
				coul_font1=(0, 0, 0), coul_font2=(), couleur1=(255, 255, 255), couleur2=(),
				coul_sel1=(0, 0, 0), coul_sel2=(), coul_font_sel1=(255, 255, 255), coul_font_sel2=(),
				coul_scroll_cursor=(200, 0, 0), coul_scroll_cursor_sel=(255, 0, 0), coul_scroll=(50, 0, 0), font="data/fonts/comic.ttf"):
		__.boss = boss
		__.x, __.y = x, y
		__.w, __.h = w, h
		__.scroll_h = h
		__.surface = pygame.Surface((__.w, __.h))
		__.Scroll = pygame.Surface((10, __.h))
		__.Sous_scroll = pygame.Surface((10, __.h))
		__.Scroll.fill(coul_scroll_cursor)
		__.Sous_scroll.fill(coul_scroll)
		__.nbr_item_visible = nbr_item_visible
		__.item_h = __.h/float(nbr_item_visible)
		__.lignes = [pygame.Surface((__.w-10, __.item_h + 1)) for i in range(nbr_item_visible)]
		__.font = pygame.font.Font(font, int(__.item_h / 2))
		if not couleur2: couleur2 = couleur1
		__.coul = couleur1, couleur2
		if not coul_sel2: coul_sel2 = coul_sel1
		__.coul_sel = coul_sel1, coul_sel2
		if not coul_font2: coul_font2 = coul_font1
		__.coul_font = coul_font1, coul_font2
		if not coul_font_sel2: coul_font_sel2 = coul_font_sel1
		__.coul_font_sel = coul_font_sel1, coul_font_sel2
		__.coul_scroll_cursor = coul_scroll_cursor, coul_scroll_cursor_sel
		__.scroll_sel = False
		__.scroll_speed = 10
		__.select = 0
		__.scroll_y = 0
		__.items = []
		__.nbr_item = 0
		__.mousey_init = 0

	def blit(__):
		__.boss.blit(__.surface, (__.x, __.y))
		for ind, ligne in enumerate(__.lignes):
			temp = ind*__.item_h
			__.surface.blit(ligne, (10, temp))
			if __.select == __.scroll_y + ind: ligne.fill(__.coul_sel[ind % 2])
			else: ligne.fill(__.coul[ind % 2])

			if __.nbr_item > __.scroll_y + ind:
				if __.select == __.scroll_y + ind:
					__.surface.blit( __.font.render(__.items[__.scroll_y + ind], 1, __.coul_font_sel[ind % 2]), (10, temp))
				else:
					__.surface.blit( __.font.render(__.items[__.scroll_y + ind], 1, __.coul_font[ind % 2]), (10, temp))
		__.surface.blit(__.Sous_scroll, (0, 0))
		__.surface.blit(__.Scroll, (0, __.scroll_speed * __.scroll_y))

	def event(__, event):
		ev_x, ev_y = event.pos
		ev_x -= __.x
		ev_y -= __.y
		if event.type == pygame.MOUSEBUTTONUP:
			__.scroll_sel = False
			__.Scroll.fill(__.coul_scroll_cursor[__.scroll_sel])
		elif 0 <= ev_x < __.w and 0 <= ev_y < __.h:
			if event.type == pygame.MOUSEBUTTONDOWN:
				temp = __.scroll_y * __.scroll_speed
				if 0 <= ev_x < 10 and temp <= ev_y < __.scroll_h + temp:
					__.scroll_sel = True
					__.Scroll.fill(__.coul_scroll_cursor[__.scroll_sel])
				else:
					for i in range(__.nbr_item_visible):
						if i * __.item_h <= ev_y < (i+1) * __.item_h: __.select = __.scroll_y + i; break

			elif event.type == pygame.MOUSEMOTION and __.scroll_sel:
				__.scroll_y = int((ev_y+1- __.scroll_h) / __.scroll_speed)
				if __.scroll_y < 0: __.scroll_y = 0
				elif __.scroll_y * __.scroll_speed + __.scroll_h > __.h+1: __.scroll_y = int((__.h+1 - __.scroll_h) / __.scroll_speed)

	def get(__, index=None):
		if index == None: index = __.select
		if index < __.nbr_item:
			return __.items[index]
		return ""

	def get_index(__):
		return __.select

	def remove(__, index):
		__.items.pop(index)
		__.resize_scroll()

	def remove_all(__):
		__.items = []
		__.resize_scroll()

	def add_item(__, text):
		__.items.append(text)
		__.resize_scroll()

	def insert(__, index, text):
		__.items.insert(index, text)
		__.resize_scroll()

	def item_exists(__, text):
		return bool(text in __.items)

	def find_item(__, text):
		if __.item_exists(text): return __.items.index(text)
		return -1

	def resize_scroll(__):
		__.nbr_item = len(__.items)
		temp = __.nbr_item - __.nbr_item_visible
		if temp < 0: temp = 0
		__.scroll_h = __.h - temp * 10
		if __.scroll_h < 10:
			__.scroll_h = 10
			__.scroll_speed = __.h / float(__.nbr_item)
		else: __.scroll_speed = 10
		__.Scroll = pygame.transform.scale(__.Scroll, (10, __.scroll_h))

if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
	liste = Wgt_liste(screen, 220, 40, 300, 400, couleur2=(128, 128, 128))
	for i in range(256): liste.add_item(str(i))
	run = 1
	while run:
		liste.blit()
		for i in pygame.event.get():
			if i.type == pygame.QUIT: run = 0
			if i.type in liste.events: liste.event(i)
		pygame.display.update()
		pygame.time.wait(100)
	pygame.quit()
