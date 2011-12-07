#=[site officiel]=====================
#<<<<<mod_reg by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======
from _winreg import *

# fonctions
#	get_current_user()
#		-> list
#	save_in_reg(extension,programme,url,image="",other_command=[])
#		-> None

def get_PythonPath():
	key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Python\\PythonCore\\2.6\\PythonPath", 0, KEY_READ)
	(pythonpath, typevaleur) = QueryValueEx(key, '')
	CloseKey(key)
	key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Python\\PythonCore\\2.6\\InstallPath", 0, KEY_READ)
	(installpath, typevaleur) = QueryValueEx(key, '')
	CloseKey(key)
	return ([installpath] + pythonpath.split(';'))
	
def get_current_user():
	key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment',0, KEY_READ)
	(homepath,typevaleur) = QueryValueEx(key,'HOMEPATH')
	(homedrive,typevaleur) = QueryValueEx(key,'HOMEDRIVE')
	(comname,typevaleur) = QueryValueEx(key,'LOGONSERVER')
	CloseKey(key)

	return [comname,homedrive,homepath.split("\\")[-1]]

def save_in_reg(extension, programme, url, image="", other_command=[]):
	key = CreateKey(HKEY_CLASSES_ROOT, "."+extension)
	SetValueEx(key, '', 0, REG_SZ, extension+"file")
	CloseKey(key)

	key = CreateKey(HKEY_CLASSES_ROOT, extension+"file")
	SetValueEx(key, '', 0, REG_SZ, ".".join(programme.split(".")[:-1]))
	CloseKey(key)

	if image != "":
		key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\DefaultIcon")
		SetValueEx(key, '', 0, REG_SZ, '"'+image+'"')
		CloseKey(key)

	key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\Shell")
	CloseKey(key)

	key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\Shell\\open")
	CloseKey(key)

	key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\Shell\\open\\command")
	if programme.split(".")[-1] == "py" or programme.split(".")[-1] == "pyw":
		py = OpenKey(HKEY_CLASSES_ROOT,"Python.File\\shell\\open\\command",0, KEY_READ)
		(dossier,typevaleur) = QueryValueEx(py,'')
		CloseKey(py)
		SetValueEx(key, '', 0, REG_SZ, '"'+dossier.split('"')[1]+'" "'+url+"\\"+programme+'" "%1"')
	else:
		SetValueEx(key, '', 0, REG_SZ, '"'+url+"\\"+programme+'" %1')
	CloseKey(key)

	if other_command != []:
		key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\Shell\\"+other_command["name"])
		CloseKey(key)

		key = CreateKey(HKEY_CLASSES_ROOT, extension+"file\\Shell\\"+other_command["name"]+"\\command")
		if other_command["command"].split(".")[-1] == "py" or other_command["command"].split(".")[-1] == "pyw":
			SetValueEx(key, '', 0, REG_SZ, '"'+dossier.split('"')[1]+'" '+other_command["command"])
		else:
			SetValueEx(key, '', 0, REG_SZ, other_command["command"])
		CloseKey(key)

def is_in_reg(hkey, keyname):
	try:
		key = OpenKey(hkey, keyname)
		CloseKey(key)
		return True
	except:
		return False
