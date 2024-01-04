class Effet:
    def __init__(self,nom,attmodif,defemodif,spamodif,spdefmodif,vitmodif,statut):
        self.nom = nom
        self.attmodif = attmodif
        self.defemodif = defemodif
        self.spamodif = spamodif
        self.spdefmodif = spdefmodif
        self.vitmodif = vitmodif
        self.statut = statut



SelfAttRaise = Effet("SelfAttRaise",1,0,0,0,0,"None")
SelfAttRaise2 = Effet("SelfAttRaise2",2,0,0,0,0,"None")
AttDrop = Effet("AttDrop",-1,0,0,0,0,"None")

SpDefDrop = Effet("SpDefDrop",0,0,0,-1,0,"None")

SpAttDrop = Effet("SpAttDrop",0,0,-1,0,0,"None")
SelfSpAttDrop2 = Effet("SelfSpAttDrop2",0,0,-2,0,0,"None")

SelfSpDefAndDefDrop = Effet("SelfSpDefAndDefDrop",0,-1,0,-1,0,"None")

SelfVitRaise = Effet("SelfVitRaise",0,0,0,0,1,"None")
SelfVitDrop = Effet("SelfVitDrop",0,0,0,0,-1,"None")

DefDrop = Effet("DefDrop",0,-1,0,0,0,"None")
SelfDefRaise = Effet("SelfSefRaise",0,1,0,0,0,"None")

Cursed = Effet("SelfCursed",1,1,0,0,-1,"None")
QuiDance = Effet("SelfQuiDance",0,0,1,1,1,"None")
DDance = Effet("SelfDDance",1,0,0,0,1,"None")
CMind = Effet("SelfCMind",0,0,1,1,0,"None")
Grow = Effet("Grow",0,0,0,0,0,"None")

Brulure = Effet("Brûlure",0,0,0,0,0,"Brûlé")
Poison = Effet("Poison",0,0,0,0,0,"Empoisonné")
Paralysie = Effet("Paralysie",0,0,0,0,0,"Paralysé")
PoisonGrv = Effet("Poison Grave",0,0,0,0,0,"Gravement Empoisonné")
Appeurer = Effet("Appeurer",0,0,0,0,0,"Appeuré")
Gele = Effet("Gêle",0,0,0,0,0,"Gelé")
Confusion = Effet("Confusion",0,0,0,0,0,"Confus")

RemoveItem = Effet("RemoveItem",0,0,0,0,0,"None")

Switch = Effet("Switch",0,0,0,0,0,"None")

NoOne = Effet("NoOne",0,0,0,0,0,"None")