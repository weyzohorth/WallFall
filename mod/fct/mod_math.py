#=[site officiel]=====================
#<<<<<mod_math by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======
from math import sqrt,acos,pi,cos,sin
#:::::::::::::::::::::::::::::::::::::::::::::::::
def DISTANCE(x,y,x2=0,y2=0):
	"""distance entre (x,y) a (x2,y2)"""
	return sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2))

#:::::::::::::::::::::::::::::::::::::::::::::::::
def DIRECTION(x,y,x2=0,y2=0):
	"""direction de (x,y) vers (x2,y2)"""
	if x!=x2 and y!=y2:
		if x < x2:
			direction = acos((x2-x)/DISTANCE(x,y,x2,y2))*180/pi
			if y<y2 : direction = 360 - direction
		else:
			direction = acos((x-x2)/DISTANCE(x,y,x2,y2))*180/pi
			if y < y2 : direction += 180
			else : direction = 180 - direction
	elif x < x2 : direction = 0
	elif x > x2 : direction = 180
	elif y < y2 : direction = 270
	elif y > y2 : direction = 90
	else : direction = 0
	return direction
	
#:::::::::::::::::::::::::::::::::::::::::::::::::
def radian(degre):
	return degre*pi/180

#:::::::::::::::::::::::::::::::::::::::::::::::::
def CoSinus(degre):
	angle = radian(degre)
	return cos(angle),sin(angle)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def PGCD(a,b):
	r = 0
	while a % b:
		r = a % b
		a, b = b, r
	if not r:
		r = b
	return r

#:::::::::::::::::::::::::::::::::::::::::::::::::
def racine(x,n=2):
	if n:
		return pow(x,1.0/n)
	else:
		return "n == 0"

#:::::::::::::::::::::::::::::::::::::::::::::::::
def tronquer(valeur,ou=0,_type="ajust"):
	"""valeur, ou<0 x.xxx|x, ou>0 xx|xx.xx, ou=0 xxxx.|xxx, _type=type de troncature
"a"ou"ajust"arrondi, "c","ceil" ou "f","floor"
---> float ou<0 ou int ou>=0"""
	valeur=str(float(valeur)).split(".")
	if ou>=len(valeur[0]):
		valeur[0] = "0"*(ou-len(valeur[0])+1)+valeur[0]
	if -ou>=len(valeur[1]):
		valeur[1] = valeur[1]+"0"*(-ou-len(valeur[1])+1)
	if ou>0:
		val = list(valeur[0])
		val.reverse()
		test = int(val[ou-1])
		val = val[ou:len(valeur[0])]
		if _type!="f" and _type!="floor":
			val.reverse()
			if (_type=="c" or _type=="ceil") and test> 0 or (_type!="a" or _type!="ajust") and test>= 5:
				val = str(int("".join(val))+1)
			else:
				val = "".join(val)
		elif _type=="f" or _type=="floor":
			val.reverse()
		return int("".join(val))

	elif ou<0:
		val = valeur[1][:-ou]
		if _type!="f" and _type!="floor":
			test = int(valeur[1][-ou])
			lenght = len(val)
			if (_type=="c" or _type=="ceil") and test> 0  or (_type!="a" or _type!="ajust") and test>= 5:
				val=list(val)
				val = list(str(int("".join(val))+1))
			if lenght < len(val):
				valeur[0] = str(int(valeur[0])+1)
				val = "".join(val[1:len(val)])
			else:
				valeur[0] = str(int(valeur[0]))
				val = int_len("".join(val[0:len(val)]),-ou)

		elif _type=="f" and _type=="floor":
			val=valeur[1][:-ou]
		return float(".".join([valeur[0],val[:-ou]]))
	else:
		if _type!="f" and _type!="floor":
			if (_type=="c" or _type=="ceil") and int(valeur[1][0])> 0  or (_type!="a" or _type!="ajust") and int(valeur[1][0])>= 5:
				valeur[0] = str(int(valeur[0])+1)
		return int(valeur[0])

#:::::::::::::::::::::::::::::::::::::::::::::::::
def classer(iterable,_type_=0):
	"""classe la liste en decroissant(_type_=0) ou en croissant(_type_=1)"""
	liste, classement = [], []
	for i in iterable:liste.append(i)
	while len(liste) > 1:
		classement.append(min(liste))
		liste.remove(min(liste))
	classement.append(liste[0])
	if _type_:classement.reverse()
	return classement

#:::::::::::::::::::::::::::::::::::::::::::::::::
def fact(n, n0=1):
    u = n0
    if not n0 and n: u = 1
    for i in range(1, n+1): u = u * i
    return u
