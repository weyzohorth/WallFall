# -*- coding: cp1252 -*-
#=[site officiel]======================
#<<<<<tkfct by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]======
from Tkinter import *
from mod_unicode import encode

class Entry256(Entry):
    def get(self):
        return encode(Entry.get(self))

class Question(Tk):
      def __init__(self,titre="Question",question="etes-vous sur ?"):
            Tk.__init__(self)
            self.title(titre)
            Struct = Frame(self)
            self.choix = False
            Struct.pack()
            Label(Struct,text=question).pack()
            F_bout = Frame(Struct)
            F_bout.pack(fill=X)
            Button(F_bout,text="Oui",command=lambda : self.CHOIX(True)).pack(fill=X)
            Button(F_bout,text="Non",command=lambda : self.CHOIX(False)).pack(fill=X)
            self.bind("<Destroy>",lambda ev : self.quit())
            self.mainloop()

      def CHOIX(self,val):
            self.choix = val
            self.destroy()

if __name__ == "__main__":
    if Question("Test","Lancer Entry256 ?").choix:
        def Print(e):
            print e.get().replace("é","e")
            print type(e.get()), "et pas unicode"

        fen = Tk()
        e = Entry256(fen)
        e.insert(0,u"é")
        e.pack()
        e.bind("<Return>", lambda ev : Print(e))
        fen.bind("<Destroy>", lambda ev : fen.quit())
        fen.mainloop()
