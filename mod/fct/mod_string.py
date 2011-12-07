#=[site officiel]=====================
#<<<<<mod_string by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======
def str_comp(i1,i2,_type_=0):
      """compare les iterables i1 et i2 --> _type_ = 0 str() 0(==)  _type_ = 1(!=) ou 1 %=="""
      lim = abs(len(i2) - len(i1))
      size = len(i1)

      if len(i1) > len(i2) : i1 = i1[:len(i2)]
      elif len(i1) < len(i2):
            size = len(i2)
            i2 = i2[:len(i1)]

      if _type_ : string = 0.
      else : string = ""

      for c1, c2 in zip(i1,i2):
            if c1 == c2:
                  if _type_ : string += 1
                  elif not _type_ : string += "0"
            else:
                  if not _type_ : string += "1"

      if _type_:
            string = string/size * 100
      else:
            for i in range(lim) : string += "1"

      return string

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_lim(string,lim=20,ind=""):
    """string,int,ind= "END", "MIL" or ""---> str... """
    if ind == "END":
        caract = list(string)
        caract.reverse()
        string = ""
        for i in caract:
            string += i
    elif ind == "MIL":
        i = lim/2
        if len(string)/2 > i:
            string = "..."+string[len(string)/2-i:len(string)/2+i]+"..."

    if ind == "END" or ind == "":
        if len(string)>lim:
            string=string[:lim]+"..."
        if ind == "END":
            caract = list(string)
            caract.reverse()
            string = ""
            for i in caract:
                string += i
    return string

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_cut(string,part,sens=0):
      parts = []
      for i in range(len(string)):
            if sens:
                  if (i+1)*part+1 <= len(string): parts.append(string[len(string)-(i+1)*part:len(string)-i*part])
                  else:
                        if string[:i*-part]: parts.append(string[:i*-part])
                        break
            else:
                  if (i+1)*part <= len(string): parts.append(string[i*part:(i+1)*part])
                  else:
                        if string[i*part:]: parts.append(string[i*part:])
                        break
      return parts

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_len(nombre,taille=2):
    """ int, lenght ---> str de longueur >= taille"""
    if taille-len(str(nombre)) > 0:
        return "0"*(taille-len(str(nombre)))+str(nombre)
    else:
        return str(nombre)
