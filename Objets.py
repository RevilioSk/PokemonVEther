class Objet:
    def __init__(self,name,nom,attmodif,defemodif,spamodif,spdefmodif,vitmodif,capamodif,degat,soin):
        self.name = name
        self.nom = nom
        self.attmodif = attmodif
        self.defemodif = defemodif
        self.spamodif = spamodif
        self.spdefmodif = spdefmodif
        self.vitmodif = vitmodif
        self.capamodif = capamodif
        self.degat = degat
        self.soin = soin

    def copy(self):
        return Objet(self.name, self.nom, self.attmodif, self.defemodif, self.spamodif, self.spdefmodif, self.vitmodif, self.capamodif, self.degat, self.soin)
    

LifeOrb = Objet("Life Orb","Orbe Vie",1,1,1,1,1,1.3,0.1,0)
FlameOrb = Objet("Flame Orb","Orbe Flamme",1,1,1,1,1,1,0,0)
DampRock = Objet("Damp Rock","Roche Humide",1,1,1,1,1,1,0,0)
HeatRock = Objet("Heat Rock","Roche Chaude",1,1,1,1,1,1,0,0)
ChoiceSpecs = Objet("Choice Specs","Lunettes Choix",1,1,1.5,1,1,1,0,0)
ChoiceBand = Objet("Choice Band","Bandeau Choix",1.5,1,1,1,1,1,0,0)
ChoiceScarf = Objet("Choice Scarf","Mouchoir Choix",1,1,1,1,1,1.5,0,0)
Leftovers = Objet("Leftovers","Restes",1,1,1,1,1,1,0,0.06)
FocusSash = Objet("Focus Sash","Ceinture Force",1,1,1,1,1,1,0,0)
ThickClub = Objet("Thick Club","Masse Os",2,1,1,1,1,1,0,0)
NoItem = Objet("None","Aucun",1,1,1,1,1,1,0,0)