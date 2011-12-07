# -*- coding:cp1252 -*-
from mod.__init__ import *
#from options import *
#from credits import *
#from regles import *
#from scores import Show_scores
from mod.fct.highscores import get_min_et_max_scores
from mod.obj.game import *
from mod.wgt.wgt_bouton import Wgt_bouton
#from mod.obj.spheres import Joueur, Sphere_score, Sphere_bonus
#from mod.obj.murs import liste_murs
from random import randrange
import webbrowser as web

#===============================================================================
#                                                                   objet fenetre
#===============================================================================
class WallFall:
	def __init__(__):
		#Tk.__init__(__)
		mixer.music.load(K.musiques_menu[randrange(K.len_musiques_menu)])
		mixer.music.play()
		display.set_caption("WallFall " + version + " by W3YZOH0RTH")
		__.running = True
		__.size = 700
		K.set_resolution(__.size, __.size)
		__.game = None
		__.anim = True
		__.__regles__ = None
		__.__options__ = None
		__.__score__ = None
		__.__add_score__ = None
		__.__credit__ = None

#------------- test de l'existence du fichier data + creation si inexistant
		__.scores = get_min_et_max_scores()

		#__.structure = Frame(__, width=__.size+200, height=__.size, bd=5, relief="flat")
		__.back = pygame.Surface((K.w, K.h))
		#__.panneau = Frame(__.structure, width=200, height=__.size, bd=5, relief="groove")
		#__.start = [0,-300]

		#__.img_j = [PhotoImage(master=__.c,file="images/jeu/spheres/"+i+".gif") for i in Joueur.images]
		#__.img_score = PhotoImage(master=__.c,file="images/jeu/spheres/"+Sphere_score.image+".gif")
		#__.img_wey = PhotoImage(master=__.c,file="images/menu/W3YZOH0RTH.gif")
		#__.wey = __.c.create_image(-500, 250, image=__.img_wey)
		#for i in liste_murs: setattr(__, "img_"+i.image, PhotoImage(master=__.c,file="images/jeu/blocs/"+i.image+".gif"))
		#__.img_bonus = [PhotoImage(master=__.c,file="images/jeu/spheres/"+i+".gif") for i in Sphere_bonus.images]
		__.path_img_cache = K.path_img_bloc + "bloc-cache.gif"

#------------- creation du menu
		#__.Menu = Menubutton(__.structure, text="menu",width=25, bd=3, relief="raised",
#							   bg="#aaaaaa",fg="#555555")
#
#		__.menu = Menu(__.Menu)
#		__.menu.add_command(command=__.start_game, label="Nouvelle partie   [Entree]")
#		__.menu.add_command(command=__.pause,          label="Pause                [Retour]")
#		__.menu.add_separator()
#		__.menu.add_command(command=__.show_regles, label="Regles du jeu     [     r    ]")
#		__.menu.add_command(command=__.show_options, label="Options de jeu     [     o    ]")
#		__.menu.add_command(command=__.show_scores,       label="Meilleurs scores[    m    ]")
#		__.menu.add_separator()
#		__.menu.add_command(command=lambda: web.open('http://progject.free.fr/'), label="Visiter le site officiel")
#		__.menu.add_command(command=__.show_credits, label="Remerciements")
#
#		__.Menu.configure(menu=__.menu)

#------------- creation des labels d'affichage du score, des vies etc...
#		__.Temps = Label(__.panneau, text = "temps : 00:00")
#		__.Score = Label(__.panneau, text = "score : 0")
#		__.Niveau = Label(__.panneau, text = "niveau : 0")
#		__.Vie = Label(__.panneau, text = "vies : 0")
#		__.Score_max = Label(__.panneau, text = "score max : %ld"%(__.scores[0]))

#------------- positionnement de tous les widgets sur la fenetre
#		__.structure.pack()
#		__.c.pack(side=RIGHT)
#		__.panneau.pack(side=LEFT)
#
#		__.Menu.place(x=5,y=5)
#
#		__.Temps.place(x=5,y=100)
#		__.Score.place(x=5,y=140)
#		__.Niveau.place(x=5,y=160)
#		__.Vie.place(x=5,y=200)
#		__.Score_max.place(x=5,y=260)


#------------- bindage des widgets
#		__.bind("<Destroy>",lambda ev :  __.quit())
#		__.bind("<Return>",lambda ev :  __.start_game())
#		__.bind("<BackSpace>",lambda ev :  __.pause())
#		__.bind("<r>",lambda ev :  __.show_regles())
#		__.bind("<o>",lambda ev :  __.show_options())
#		__.bind("<m>",lambda ev :  __.show_scores())

		#__.anim_start()
		#__.boucle()
		__.start_game()

#------------- fonctions du menu
	def boucle(__):
		while __.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					__.running = False
					__.quit()
	def quit(__):
#		if __.__regles__: __.__regles__.destroy()
#		if __.__options__: __.__options__.destroy()
#		if __.__score__: __.__score__.destroy()
#		if __.__add_score__: __.__add_score__.destroy()
#		if __.__credit__: __.__credit__.destroy()
		pygame.quit()

	def start_game(__):
		if __.game: __.game.stop = 1
		__.game = Game(__)
		pygame.quit()

	def pause(__):
		if __.game:
			if __.game.stop:
				if not __.__options__:
					__.c.delete(__.PAUSE)
					__.game.stop = False
					__.game.game()
			else:
				__.game.stop = True
				__.PAUSE = __.c.create_text(__.size/2,__.size/2,text="PAUSE",fill="red",
											font=(None,1,"bold"))
				__.anim_pause()

	def show_regles(__): Regles(__)
	def show_options(__): Options(__)
	def show_scores(__): Show_scores(boss=__)
	def show_credits(__): Credits(__)

#------------- autres fonctions
	def anim_start(__):
		if __.start[0] == 1:
			if __.start[1] < __.size + 200:
				__.start[1] += 7
				__.c.coords(__.wall_fall, __.start[1], __.size / 2 + 100)
			else:
				__.c.delete(__.wall_fall)
				__.start = [2, 70]
				__.wall_fall = __.c.create_text(__.size/2,__.size/2 + 100,text="WALLFALL " + version,fill="red",
											font=(None,70,"bold"))
		elif __.start[0]:
			if __.start[0] == 3:
				if __.start[1] < 20: __.start[1] += 1
			elif __.start[0] == 2:
				if __.start[1] > 5: __.start[1] -= 5
				else: __.start[0] = 3
			__.c.itemconfig(__.wall_fall,font=(None,__.start[1],"bold"))
		else:
			if __.start[1] < __.size / 2:
				__.start[1] += 5
				__.c.coords(__.wey, __.start[1], __.size / 2)
			else:
				__.start = [1, -200]
				__.wall_fall = __.c.create_text(__.start[1], __.size / 2 + 100, text="vous présente",fill="red",
											font=(None,30,"bold"))
		if __.start[0] == 3 and __.start[1] == 20 or not __.anim: pass
		else: __.c.after(40, __.anim_start)

	def anim_pause(__, i=0):
		if __.game.stop:
			i += 1
			__.c.itemconfig(__.PAUSE,font=(None,i,"bold"))
			if i < 70: __.c.after(40, lambda: __.anim_pause(i))

