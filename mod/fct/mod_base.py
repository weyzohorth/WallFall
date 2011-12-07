#=[site officiel]=====================
#<<<<<mod_base by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======

# fonctions
#	all_caract()
#		-> list
#	_256_()
#		-> list
#	caract_text()
#		-> list
#	xor(a,b)
#		-> bool
#	bin(c, base=256, caract=_256_())
#		-> str
#	bins(c, base=256, caract=_256_())
#		-> str
#	base_to_base(string, base1=256, base2=16, caract=_256_())
#		-> str
#	str_int(string)
#		-> int
#	int_str(x)
#		-> str
#	int_base(x, base=256, caract=_256_())
#		-> str
#	base_int(string, base=256, caract=_256_())
#		-> int
#	str_val_max(n)
#		-> int
#	base_int_max(n, base)
#		-> int
#	int_base2(x, base=256**2, caract=_256_())
#		-> str
#	base_int2(string, base=256**2, caract=_256_())
#		-> int
#	bin_group(string, octet=8)
#		-> list

def all_caract(): return [chr(i) for i in range(256)]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def _256_():
	return [
 "\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39", "\x61","\x62","\x63","\x64","\x65",
 "\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74",
 "\x75","\x76","\x77","\x78","\x79","\x7a","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49",
 "\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58",
 "\x59","\x5a","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2c","\x2e","\x3a",
 "\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x5b","\x5c","\x5d","\x5e","\x5f","\x60", "\x7b","\x7c","\x7d",
 "\x7e","\x09","\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x0b","\x0c","\x0e",
 "\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d",
 "\x1e","\x1f","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c",
 "\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b",
 "\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3", "\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa",
 "\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9",
 "\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2", "\xc3", "\xc4","\xc5","\xc6","\xc7","\xc8",
 "\xc9", "\xca","\xcb","\xcc", "\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7",
 "\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6",
 "\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3", "\xf4","\xf5",
 "\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff", "\x2a","\x2b","\x2d","\x2f","\x0a","\x0d"]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def caract_text():
	return [
 "\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39", "\x61","\x62","\x63","\x64","\x65",
 "\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74",
 "\x75","\x76","\x77","\x78","\x79","\x7a","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49",
 "\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58",
 "\x59","\x5a","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2c","\x2e","\x3a",
 "\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x5b","\x5c","\x5d","\x5e","\x5f","\x60", "\x7b","\x7c","\x7d",
 "\x7e","\x09","\x2a",

 "\x2b","\x2d","\x2f","\x0a","\x0d","\xa0","\xe8","\xe9",

 "\x00","\x01","\x02","\x03","\x04","\x05","\x06",
 "\x07","\x08","\x0b","\x0c","\x0e", "\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18",
 "\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86",
 "\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95",
 "\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa1","\xa2","\xa3", "\xa4",
 "\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3",
 "\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2",
 "\xc3", "\xc4","\xc5","\xc6","\xc7","\xc8","\xc9", "\xca","\xcb","\xcc", "\xcd","\xce","\xcf","\xd0","\xd1",
 "\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0",
 "\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xea","\xeb","\xec","\xed","\xee","\xef",
 "\xf0","\xf1","\xf2","\xf3", "\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff"]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def xor(a,b):
    """porte logique ou-exclusif"""
    return a and not b or not a and b

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bin(c,base=256,caract=_256_()):
    """change UN caractere de base 'base' en base 2"""
    return  int_len(int_base(base_int(c,base,caract),2,caract),8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bins(string,base=256,caract=_256_()):
    """change une string de base 'base' en base 2"""
    return "".join([bin(c,caract)for c in string])

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_to_base(string,base1=256,base2=16, caract=_256_()):
    """change une string de base1 en base2"""
    return  int_base(base_int(string,base1,caract),base2,caract)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_int(string):
	valeur = 0
	for n,c in enumerate(string): valeur += ord(c)*256**n
	return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_str(x):
	s=""
	while x != 0:
		s += chr(x%256)
		x = x/256
	if s == "": s = "0"
	return s

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_base(x,base=256,caract=_256_()):
	s=[]
	caract = caract[:base]
	while x != 0:
		s.append(caract[x%base])
		x = x/base
	if not s: s.append(0)
	s.reverse()
	return "".join([str(i) for i in s])

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int(string,base=256,caract=_256_()):
	valeur = 0
	caract = caract[:base]
	for i in range(len(string)): valeur += caract.index(string[-i-1])*pow(base,i)
	return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_val_max(n):
	"""nombre de caractere de la chaine ---> int maximum"""
	valeur = 0
	for i in range(n): valeur += 255*pow(256,i)
	return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int_max(n,base):
	"""nombre de caractere de la chaine ---> int maximum"""
	valeur = 0
	for i in range(n): valeur += (base-1)*pow(base,i)
	return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_base2(x,base=256**2,caract=_256_()):
	"""meme fonction que int_base(string,avec base>256)"""
	s=[]
	while x != 0:
			s.append(int_len(int_base(x%base, caract=caract), len(int_base(base, caract=caract))-1))
			x = x/base
	if s ==[]:
			s.append(0)
	s.reverse()
	b=""
	for i in s:
			b+=str(i)
	return b

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int2(string,base=256**2,caract=_256_()):
	valeur = 0
	paquet = len(int_base(base, caract=caract))-1
	string = cut(string,paquet,1)
	for i,v in enumerate(string) : valeur += base_int(v, caract=caract) * pow(base, i)
	return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bin_group(string,octet=8):
	from mod_string import str_cut
	return str_cut(bins(string),octet,1)


