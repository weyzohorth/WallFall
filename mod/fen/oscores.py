#-*- coding: cp1252 -*-
import PyQt4.Qt as qt
import webbrowser as web
import sys
from os import getcwd, remove
from mod.fct.ohighscores import *
from mod.fct.mod_file import *

#try:
#	if get_ext(__file__) == "py":
#		remove(__file__)
#	elif get_ext(__file__) == "pyc":
#		try:remove(__file__[ : -1])
#		except: pass
#except:
#	print "Relancez le jeu pour avoir accés aux scores en ligne"

def sum_file_sha_py(fichier):
	if get_ext(fichier) != "py":
		return ""
	chars= [0 for i in range(257)]
	#with file(fichier) as fic:
	fic = file(fichier)
	for c in fic.read():
		chars[ord(c)] += 1
	chars[-1] = fic.size()
	fic.close()	
	sum = ""
	for i, c in enumerate(chars):
		while c / 256:
			sum += chr(c % 256)
			c = c / 256
		sum += chr(c)
	return (sha_fct(sum).hexdigest())

def sum_char_dir(dir=getcwd()):
	sum = ""
	for i in get_allfiles(dir):
		sum += sum_file_sha_py(i)
	return md5_fct(sum).hexdigest()

class OScores(qt.QWidget):
	def __init__(__, jeu, master=None):
		qt.QWidget.__init__(__, master)
		__.jeu = jeu
		__.index = 0
		__.setWindowTitle("HighScores OnLine")
		__.Title = qt.QLabel('<strong><font size=24 color="#ff0000">HighScores OnLine</font></strong>')
		__.Title.setAlignment(qt.Qt.AlignCenter)
		__.Grid = qt.QGridLayout(__)
		__.widget = qt.QWidget(__)
		__.HLayout = qt.QHBoxLayout(__.widget)
		__.Places = [__.create_label() for i in range(10)]
		__.Pseudos = [__.create_label() for i in range(10)]
		__.Scores = [__.create_label() for i in range(10)]
		__.Dates = [__.create_label() for i in range(10)]
		__.Heures = [__.create_label() for i in range(10)]
		__.Headers = [__.create_label('<strong><font color="#ff0000">'+i+"</font></strong>",
									qt.QFrame.Box | qt.QFrame.Sunken) for i in ["Place", "Pseudo", "Score", "Date", "Heure"]]
		__.Boutons = [qt.QPushButton(i, __) for i in ["<<", "<", ">", ">>"]]
		__.Page = qt.QLabel(__)
		__.Page.setFrameStyle(qt.QFrame.StyledPanel | qt.QFrame.Sunken)
		__.refresh()

		__.Grid.addWidget(__.Title, 0, 0, 1, 4)
		for i, lab in enumerate(__.Headers): __.Grid.addWidget(lab, 1, i)
		for x, cat in enumerate([__.Places, __.Pseudos, __.Scores, __.Dates, __.Heures]):
			for y, lab in enumerate(cat): __.Grid.addWidget(lab, y+2, x)
		for x, lab in enumerate(__.Boutons+[__.Page]): __.HLayout.addWidget(lab)
		__.Grid.addWidget(__.widget, 13, 0, 1, 4)
		__.widget.setLayout(__.HLayout)
		__.setLayout(__.Grid)

		for fct, bout in zip([__.index_0, __.index_m10, __.index_p10, __.index_end], __.Boutons):
			qt.qApp.connect(bout, qt.SIGNAL("clicked()"), fct)

	def create_label(__, text="", relief=qt.QFrame.Panel | qt.QFrame.Sunken):
		label = qt.QLabel(text, __)
		label.setAlignment(qt.Qt.AlignCenter)
		label.setMargin(10)
		label.setFrameStyle(relief)
		return label

	def refresh(__):
		__.index_max = score_online(__.jeu, 0)
		temp = score_online(__.jeu, limite=10, start=__.index)
		if temp:
			scores = [i for i in temp]
			if scores:
				for i, data in enumerate(scores):
					if data[0] <= 3: couleur = "ffff00"
					elif data[0] <= 10: couleur = "00ff00"
					else: couleur = "0000ff"
					__.Places[i].setText('<font color="#'+couleur+'">'+str(data[0])+'</font>')
					__.Pseudos[i].setText('<font color="#'+couleur+'">'+data[1]+'</font>')
					__.Scores[i].setText('<font color="#'+couleur+'">'+str(data[2])+'</font>')
					__.Dates[i].setText('<font color="#'+couleur+'">'+data[3][0]+'</font>')
					__.Heures[i].setText('<font color="#'+couleur+'">'+data[3][1]+'</font>')
		__.refresh_page()

	def refresh_page(__):
		max = str(__.index_max - __.index_max % 10 + 1)
		__.Page.setText(str(__.index + 1)+"/"+max)

	def index_0(__): __.index = 0; __.refresh()
	def index_end(__):
		__.index_max = score_online(__.jeu, 0)
		__.index = __.index_max - __.index_max % 10; __.refresh()
	def index_p10(__):
		__.index_max = score_online(__.jeu, 0)
		if __.index + 10 < __.index_max: __.index += 10; __.refresh()
	def index_m10(__):
		if __.index: __.index -= 10; __.refresh()

class Add_oscore(OScores):
	PSEUDO = ""
	
	def __init__(__, jeu, score, master=None, dir=getcwd()):
		qt.QWidget.__init__(__, master)
		__.dir = dir
		__.jeu = jeu
		__.score = score
		__.setWindowTitle("Add HighScores OnLine")
		__.Layout = qt.QVBoxLayout(__)
		__.Title = qt.QLabel('<strong><font size=24 color="#ff0000">Add HighScores OnLine</font></strong>')
		__.Title.setAlignment(qt.Qt.AlignCenter)
		__.Score = qt.QLabel("Score : "+str(__.score))
		__.pseudo = qt.QLineEdit(__)
		__.mdp = qt.QLineEdit(__)
		__.mdp.setEchoMode(qt.QLineEdit.Password)
		__.form = qt.QFormLayout()
		__.form.addRow("Pseudo :", __.pseudo)
		__.form.addRow("Mdp :", __.mdp)
		__.valider = qt.QPushButton("Valider", __)
		__.new = qt.QPushButton("Créer un Compte", __)
		__.erreur = qt.QLabel(__)

		__.Layout.addWidget(__.Title)
		__.Layout.addWidget(__.Score)
		__.Layout.addLayout(__.form)
		__.Layout.addWidget(__.valider)
		__.Layout.addWidget(__.new)
		__.Layout.addWidget(__.erreur)
		__.setLayout(__.Layout)

		qt.qApp.connect(__.valider, qt.SIGNAL("clicked()"), __.ok)
		qt.qApp.connect(__.new, qt.SIGNAL("clicked()"), __.new_account)

	def ok(__):
		if __.pseudo.text() and __.mdp.text():
			temp = score_online(__.jeu, 1, 0, unicode(__.pseudo.text(), "cp1252"), unicode(__.mdp.text(), "cp1252"), __.score, sum_char_dir(__.dir))
			if temp:
				msg = unicode(temp, "cp1252")
				if msg == "OK":	__.close()
				else: __.erreur.setText(msg)
			else: __.erreur.setText("Erreur serveur.")
			__.PSEUDO = unicode(__.pseudo.text(), "cp1252")

	def new_account(__):
		web.open("http://progject.free.fr/pages/inscription.php")

def add_oscore(jeu, score="", dir=getcwd()):
	app = qt.QApplication(sys.argv)
	oscores = Add_oscore(jeu, score, dir=dir)
	oscores.show()
	app.exec_()
	pseudo = oscores.PSEUDO
	app = None
	show_oscore(jeu)
	return pseudo

def show_oscore(jeu):
	app = None
	app = qt.QApplication(sys.argv)
	oscores = OScores(jeu)
	oscores.show()
	app.exec_()

if __name__ == "__main__":
	add_score("test", 200)
