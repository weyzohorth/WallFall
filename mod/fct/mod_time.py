from time import localtime, ctime
from mod_string import int_len

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_time(valeur,unite="s",conv="m"):
	"""temps en unite= "s", "m" ou "h"---> temps en conv = "s", "m" ou "h" """
	if unite == "h":
		valeur = valeur * 3600
	elif unite == "m":
		valeur = valeur * 60

	if conv == "s":
		return valeur
	if conv == "h":
		h = valeur / 3600
		m = valeur  / 60 % 60
	else:
		m = valeur / 60
	s = valeur % 60
	if conv == "h":
		return int_len(h)+":"+int_len(m)+":"+int_len(s)
	else:
		return int_len(m)+":"+int_len(s)
#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_date(seconds=""):
      if type(seconds) != type(0.): temp = localtime()
      else: temp = localtime(seconds)
      jours = ("lundi","mardi","mercredi", "jeudi", "vendredi", "samedi", "dmanche")
      mois = ("janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet",
              "aout", "septembre", "octobre", "novembre", "decembre")
      
      return " ".join((jours[temp[-3]], str(temp[2]), mois[temp[1]-1], str(temp[0])))

def get_time(seconds=""):
      if type(seconds) != type(0.): temp = localtime()
      else: temp = localtime(seconds)
      return "%s:%s:%s"%(int_len(temp[3]), int_len(temp[4]), int_len(temp[5]))

#:::::::::::::::::::::::::::::::::::::::::::::::::
def horloge():
      import Tkinter as tk
      from mod_math import CoSinus

      class Horloge(tk.Canvas):
            def __init__(__, cnf={}, **arg):
                  tk.Canvas.__init__(__, cnf={}, **arg)
                  __.create_oval(100,50,200,150,outline="red")
                  __.Sec = __.create_line(150,100,150,50,fill="red")
                  __.Min = __.create_line(150,100,150,60,fill="blue")
                  __.Heu = __.create_line(150,100,150,70,fill="green")
                  __.Jou = __.create_line(150,100,150,20,fill="yellow")
                  __.Moi = __.create_line(150,100,150,10,fill="purple")
                  __.boucle()

            def boucle(__):
                  temp = localtime()
                  moi = temp[1]
                  heu, min, sec, jou = temp[3:7]
                  cos, sin = CoSinus(-(sec-15)/60.*360)
                  __.coords(__.Sec, 150, 100,150 + cos * 50, 100 - sin * 50)
                  
                  cos, sin = CoSinus(-(min-15)/60.*360)
                  __.coords(__.Min, 150, 100,150 + cos * 40, 100 - sin * 40)
                  
                  cos, sin = CoSinus(-(heu-6)/24.*360)
                  __.coords(__.Heu, 150, 100,150 + cos * 30, 100 - sin * 30)

                  cos, sin = CoSinus(-(jou-1.75)/7.*360)
                  __.coords(__.Jou, 150, 100,150 + cos * 20, 100 - sin * 20)
                  
                  cos, sin = CoSinus(-(moi-3)/12.*360)
                  __.coords(__.Moi, 150, 100,150 + cos * 10, 100 - sin * 10)
                  __.after(34,__.boucle)
                  

      fen = tk.Tk()
      Horloge(fen).pack()
      fen.bind("<Destroy>", lambda ev: fen.quit())
      fen.mainloop()

if __name__ == "__main__": horloge()
