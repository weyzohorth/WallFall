# -*- coding: utf-8 -*-
from mod.fct.highscores import *
from Tkinter import *
import locale

class Show_scores(Tk):
	def __init__(__,pseudo="",score="", boss=None):
		Tk.__init__(__)
		if boss and not boss.__score__: boss.__score__ = __
		else:
			__.destroy()
			Tk.quit(__)
		__.title("Meilleurs Scores")
		__.boss = boss
		data = get_scores()
		__.Struct = Frame(__,width=350,height=380,bg="gray")

		Label(__.Struct,text="Meilleurs Scores",font=(None,20,"bold"),
			  width=23,fg="red",bg="dark gray").place(x=10,y=10)
		Label(__.Struct,text="Noms",font=(None,10,"bold"),fg="red",bg="gray").place(x=10,y=60)
		Label(__.Struct,text=": Scores",font=(None,10,"bold"),fg="red",bg="gray").place(x=175,y=60)
		i = 0
		for n,s in data:
			if n == pseudo and s == score:
				Label(__.Struct,text=str(i+1)+" - "+n,fg="red",bg="gray").place(x=10,y=85+25*i)
				Label(__.Struct,text=": "+str(s),fg="red",bg="gray").place(x=175,y=85+25*i)
			elif n == pseudo :
				Label(__.Struct,text=str(i+1)+" - "+n,fg="blue",bg="gray").place(x=10,y=85+25*i)
				Label(__.Struct,text=": "+str(s),fg="blue",bg="gray").place(x=175,y=85+25*i)
			else:
				Label(__.Struct,text=str(i+1)+" - "+n,fg="#555555",bg="gray").place(x=10,y=85+25*i)
				Label(__.Struct,text=": "+str(s),fg="#555555",bg="gray").place(x=175,y=85+25*i)
			i+=1
		Label(__.Struct,text='Appuyez sur "Suppr" pour effacer le tableau'
			  ,fg="#555555",bg="gray").place(x=10,y=85+25*(len(data)+1))

		__.bind("<Destroy>",lambda ev : __.quit())
		__.bind("<Delete>",lambda ev : __.clear())
		__.bind("<Return>",lambda ev : __.destroy())
		__.bind("<Escape>",lambda ev : __.destroy())
		__.Struct.pack()
		__.mainloop()

	def clear(__):
		create_scores()
		__.boss.scores = get_min_et_max_scores()
		__.destroy()
		__.__init__()

	def quit(__):
		__.boss.__score__ = None
		Tk.quit(__)


class Add_score(Tk):
	def __init__(__,score, boss):
		Tk.__init__(__)
		__.title("Entrez votre pseudo")
		if boss.__add_score__: __.__add_score__.destroy()
		boss.__add_score__ = __

		__.boss=boss
		__.pseudo = ""
		__.score = score
		__.frame=Frame(__,width=300,height=100,bg="dark gray")
		__.frame.pack()
		Label(__.frame,text="Pseudo :", fg="#555555", bg="dark gray").place(x=50,y=20)
		Label(__.frame,text="Score    : "+str(score), fg="#555555", bg="dark gray").place(x=50,y=45)
		Label(__.frame,text="Caractères utilisables : a-z, A-Z, 0-9"
			  , fg="#555555", bg="dark gray").place(x=50,y=70)
		__.e=Entry(__.frame,width=20,fg="#555555",bg="white")
		__.e.place(x=100,y=20)
		__.bind("<Return>",lambda ev : __.valide_usr())
		__.bind("<Destroy>",lambda ev : __.quit())
		__.mainloop()
		if __.pseudo!="":
			if boss.__score__: boss.__score__.destroy()
			Show_scores(__.pseudo,__.score, boss)

	def quit(__):
		__.boss.__add_score__ = None
		Tk.quit(__)

	def valide_usr(__):
		try:
			__.pseudo = unicode(__.e.get(), locale.getdefaultlocale()[1])
			if __.pseudo!="":
				add_score(__.pseudo, __.score)
				__.destroy()
		except:
			__.e.delete(0,END)
			__.e.insert(0,"caracteres invalides")


if __name__ == "__main__":
      Show_scores()
