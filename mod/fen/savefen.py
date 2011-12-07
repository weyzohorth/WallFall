# -*- coding: cp1252 -*-
#=[site officiel]====================
#<<<<<savefen by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]====
import Tkinter as tk
from mod.__init__ import *
from mod.fct.mod_file import try_file, get_files, get_name, get_ext
from mod.fct.tkfct import *
from os import remove, rename, mkdir

class SaveFen(tk.Tk):
	def __init__(__,boss,mode=True,name=K.path_map + "save.wf"):
		"""Fenetre 'exploreur' pour sauvegarder et charger les maps . mode = 1 (save) ou 0 (load)"""
		tk.Tk.__init__(__)
		text_mode = "Sauvegarder" * bool(mode) + "Charger" * bool(not mode)
		__.title(text_mode)
		__.mode = mode
		__.boss = boss
		__.old_ind = 0

		__.Struct = tk.Frame(__)
		__.Struct2 = tk.Frame(__)

		__.Entry = Entry256(__.Struct2,width=30)
		if mode:
			__.Entry.insert(0, get_name(try_file(name)))
		else:
			__.Entry.insert(0, get_name(name))

		__.Scroll = tk.Scrollbar(__.Struct, width=20)
		__.List = tk.Listbox(__.Struct, width=50,height=30)
		__.refresh()
		__.Scroll.config(command = __.List.yview)
		__.List.config(yscrollcommand = __.Scroll.set)

		__.Erreur = tk.Label(__.Struct2, fg="red")

		__.Struct.pack(side=tk.LEFT)
		__.Struct2.pack(side=tk.RIGHT)
		__.List.pack(side = tk.RIGHT, fill = tk.Y)
		__.Scroll.pack(side = tk.LEFT, fill = tk.Y)
		__.Entry.pack()
		tk.Button(__.Struct2, text=text_mode, command=__.valider).pack(fill=tk.X)
		tk.Button(__.Struct2, text="Supprimer", command=__.suppr).pack(fill=tk.X)
		tk.Button(__.Struct2,text="Renommer" , command=__.renommer).pack(fill=tk.X)
		__.Erreur.pack(fill=tk.X)

		__.List.bind('<ButtonRelease-1>',lambda ev : __.clic(True))
		__.bind("<Destroy>",lambda ev: __.quit())
		__.mainloop()

#--------------------------------------------------------------------------------
	def clic(__,mode=False):
		try:
			i = __.List.curselection()
			if i:
				__.old_ind = i
				name = __.List.get(i)
				if name and mode:
					__.Entry.delete(0,tk.END)
					__.Entry.insert(0,name[ : -3])
				else: return name
		except Exception, err: __.Erreur.configure(text=err[-1])

#--------------------------------------------------------------------------------
	def valider(__):
		try:
			if __.mode:#mode sauveagarder
				name = __.Entry.get()
				if name:
					save = True
					if get_ext(name) != "wf": name += ".wf"
					temp = K.path_map + name
					if temp != try_file(temp):
						if not Question("Remplacer",
									"Le fichier '%s' existe déjà .\nVoulez-vous l'écraser ?"%(name)).choix:
							save = False
					if save:
						__.boss.filename = K.path_map + name
						__.destroy()
			else:#mode charger
				name = __.clic()
				if name:
					__.boss.filename = K.path_map + name
					__.destroy()
		except Exception, err: __.Erreur.configure(text=err[-1])

#--------------------------------------------------------------------------------
	def suppr(__):
		try:
			name = __.clic()
			if name:
				if Question("Supprimer","Voulez - vous supprimer '%s' ?"%(name)).choix:
					remove(K.path_map + name)
					__.refresh()
		except Exception, err: __.Erreur.configure(text=err[-1])

#--------------------------------------------------------------------------------
	def renommer(__):
		try:
			old_name = __.List.get(__.old_ind)
			new_name = __.Entry.get()
			if old_name and new_name:
				if get_ext(new_name) != "wf": new_name += ".wf"
				if Question("Renommer", "Voulez - vous renommer '%s' en '%s' ?"%(old_name, new_name)).choix:
					rename(K.path_map + old_name, K.path_map + new_name)
					__.refresh()
		except Exception, err: __.Erreur.configure(text=err[-1])

#--------------------------------------------------------------------------------
	def refresh(__):
		__.List.delete(0,tk.END)
		erreur = 0
		for i,f in enumerate(get_files(K.path_map)):
			if get_ext(f) == "wf": __.List.insert(i - erreur, get_name(f))
			else: erreur += 1

if __name__ == "__main__":
	SaveFen(None)
