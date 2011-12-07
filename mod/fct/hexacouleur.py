#=[site officiel]==========================
#<<<<<hexacouleur2.0 by W3YZOH0RTH>>>>>
#================[http://progject.free.fr/]=
def antifloat(valeur):
    valeur=str(valeur)
    try:
        valeur = int(valeur)
    except:
        list = valeur.split(".")
        valeur = int(list[0])
    return valeur
    
def rvb(rouge=0,vert=0,bleu=0):
    r=hex(antifloat(rouge) % 256).split("0x")
    v=hex(antifloat(vert) % 256).split("0x")
    b=hex(antifloat(bleu) % 256).split("0x")
    rouge="0"*(2-len(r[1]))+r[1]
    vert="0"*(2-len(v[1]))+v[1]
    bleu="0"*(2-len(b[1]))+b[1]
    
    return "#"+str(rouge+vert+bleu)

def rvblinux(rouge=0,vert=0,bleu=0):
    r=hex((antifloat(rouge) % 256)*257).split("0x")
    v=hex((antifloat(vert) % 256)*257).split("0x")
    b=hex((antifloat(bleu) % 256)*257).split("0x")
    rouge="0"*(4-len(r[1]))+r[1]
    vert="0"*(4-len(v[1]))+v[1]
    bleu="0"*(4-len(b[1]))+b[1]

    return "#"+str(rouge+vert+bleu)

def rvb_(couleur):
    """string "#RRVVBB" ou tuple(R,V,B) ---> string "#RRVVBB" """
    if type(couleur)==type(""):
        R, V, B = int(couleur[1:3],16), int(couleur[3:5],16), int(couleur[5:7],16)
    else:
        R, V, B = couleur[0], couleur[1], couleur[2]
    return rvb(255-R,255-V,255-B)

def hexa(couleur):
     return int(couleur[1:3],16), int(couleur[3:5],16), int(couleur[5:7],16)
