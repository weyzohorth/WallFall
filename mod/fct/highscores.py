# -*- coding: utf-8 -*-

from os import mkdir

def create_scores(size=10,valeur=0,nom="pas de score"):
      """créer un tableau pour les meilleurs scores"""
      if not size:
            size = 10
      try:
            file = open("data/highscores","wb")
      except:
            mkdir("data")
            file = open("data/highscores","wb")
      for i in range(size):
            file.write("%s\x00%ld\n"%(str(nom),valeur))
      file.close()

def add_score(nom,valeur,size_def=10,nom_def="pas de score",valeur_def=0):
      try:
            file = open("data/highscores","rb")
            data = file.readlines()
            file.close()
            scores = []
            i = 0
            while i < len(data):
                  score = int(data[i].split("\x00")[1])
                  if score <= valeur and not scores.count("%s\x00%ld\n"%(str(nom),valeur)):
                        scores.append("%s\x00%ld\n"%(str(nom),valeur))
                        scores.append(data[i])
                        i += 1
                  else:
                        scores.append(data[i])
                        i += 1
            file = open("data/highscores","wb")
            for i in scores[:len(data)]:
                  file.write(i)
            file.close()
      except :
            create_scores(size_def,valeur_def,nom_def)
            add_score(nom,valeur,size_def,nom_def,valeur_def)

def get_scores(size=0,valeur=0,nom="pas de score"):
      """Montre tous (0) ou une partie (1+) des scores contenus dans le fichiers"""
      try:
            file = open("data/highscores","rb")
            data = file.readlines()
            file.close()

            scores = []
            for i in data:
                  i = i.split("\x00")
                  scores.append((i[0],int(i[1])))

            if size:
                  return scores[:size]
            else:
                  return scores
      except:
            create_scores(size,valeur,nom)
            try:
                  return get_scores(size,valeur,nom)
            except Exception,erreur:
                  print erreur
                  return [[nom,valeur]]*(size+10*int(not bool(size)))

def get_min_et_max_scores():
  try:
      f = open("data/highscores","rb")
      scores = get_scores()
      max_score = scores[0][1]
      min_score = scores[-1][1]
      f.close()
      return max_score,min_score
  except :
      return 0,0
