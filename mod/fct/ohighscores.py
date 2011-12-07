#-*- coding:cp1252 -*-
import urllib
from os import remove
from mod_file import sha_fct, get_ext

#try:
#	if get_ext(__file__) == "py":
#		remove(__file__)
#	elif get_ext(__file__) == "pyc":
#		try:remove(__file__[ : -1])
#		except: pass
#except:
#	print "Relancez le jeu pour avoir accés aux scores en ligne"

def score_online_confirm(sum, num):
	sum = sha_fct(sum + sha_fct(str(num)).hexdigest()).hexdigest()
	url = "http://progject.free.fr/api/score_confirm.php?sum="+sum
	#url = "http://127.0.0.1/progject/api/score_confirm.php?sum="+sum
	page = urllib.urlopen(url)
	message = page.read().split("<!-- MESSAGE -->")
	if 1 < len(message):
		return (message[1])
	return None
	
def score_online(jeu, limite=5, start=0, pseudo="", mdp="", score="###", seed=""):
	url = "http://progject.free.fr/api/scores.php?jeu="+jeu
	#url = "http://127.0.0.1/progject/api/scores.php?jeu="+jeu
	if limite:
		url += "&limite="+str(limite)
		if start:
			url += "&start="+str(start)
		if pseudo and mdp and type(u"") != type(score) != type(""):
			url += "&score=%s&pseudo=%s&mdp=%s"%(str(score), pseudo, sha_fct(mdp).hexdigest())
		if seed:
			url += "&seed=" + seed
		page = urllib.urlopen(url)
		if not pseudo:
			splits = page.read().split("<!-- LISTE SCORES -->")
			if len(splits) > 1:
				splits = splits[1].split('<span class="lien_sommaire">')
				if len(splits) > 1:
					splits = splits[1:]

					if str(limite).count(","):
						decal = int(limite.split(",")[0])

					scores = []
					for i,el in enumerate(splits):
						if not (i % 4):
							score = [int(el.replace(" - </span>",""))]
						elif (i % 4) == 1:
							score.append(el.replace("</span> ",""))
						elif (i % 4) == 2:
							score.append(int(el.replace("</span> ","")))
						else:
							score.append(el.replace("</span></p>","").replace("<p>","").split("|"))
							scores.append(score)
					return scores
		else:
			message = page.read().split("<!-- MESSAGE -->")
			if len(message) > 1:
				try: return score_online_confirm(seed, int(message[1]))
				except: return message[1]
	else:
		page = urllib.urlopen(url)
		splits = page.read().split("<!-- LISTE SCORES -->")
		if splits and splits[1]: return int(splits[1])

if __name__ == "__main__":
	for i in score_online("test", 5, 0): print i


