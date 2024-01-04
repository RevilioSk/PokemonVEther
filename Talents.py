class Talent:
    def __init__(self,name,nom,attmodif,defemodif,spamodif,spdefmodif,vitmodif,style):
        self.name = name
        self.nom = nom
        self.attmodif = attmodif
        self.defemodif = defemodif
        self.spamodif = spamodif
        self.spdefmodif = spdefmodif
        self.vitmodif = vitmodif
        self.style = style



Adaptability = Talent("Adaptability","Adaptabilité",1,1,1,1,1,"StatModifCapa")
Analytic = Talent("Analytic","Analyste",1,1,1,1,1,"StatModifCapa")
ArenaTrap = Talent("Arena Trap","Piège Sable",1,1,1,1,1,"Trap")

Blaze = Talent("Blaze","Brasier",1,1,1,1,1,"StatModifLow")

Chlorophyll = Talent("Chlorophyll","Chlorophylle",1,1,1,1,2,"MétéoStatModif")
ClearBody = Talent("Clear Body","Corps Sain",1,1,1,1,1,"SafeStat")
CompoundEyes = Talent("Compound Eyes","Œil Composé",1,1,1,1,1,"PreciRaise")

Disguise = Talent("Disguise","Fantômasque",1,1,1,1,1,"Tanking")
Drizzle = Talent("Drizzle","Crachin",1,1,1,1,1,"Météo")
Drought = Talent("Drought","Sécheresse",1,1,1,1,1,"Météo")

FlameBody = Talent("Flame Body","Corps Ardent",1,1,1,1,1,"AppStatut")
FlashFire = Talent("Flash Fire","Torche",1,1,1,1,1,"Absorption")
Frisk = Talent("Frisk","Fouille",1,1,1,1,1,"Affichage")

Guts = Talent("Guts","Cran",1,1,1,1,1,"BoostStat")

HugePower = Talent("Huge Power","Coloforce",1,1,1,1,1,"StatBoost")

Intimidate = Talent("Intimidate","Intimidation",1,1,1,1,1,"StatDrop")
InnerFocus = Talent("Inner Focus","Attention",1,1,1,1,1,"StatutStop")
IronFist = Talent("Iron Fist","Poing d'Acier",1,1,1,1,1,"BoostCapa")
IronKick = Talent("Iron Kick","Pied d'Acier",1,1,1,1,1,"BoostCapa")

KeenEye = Talent("Keen Eye","Regard Vif",1,1,1,1,1,"ProtectDropStat")

Levitate = Talent("Levitate","Lévitation",1,1,1,1,1,"Immunité")
LightningRod = Talent("Lightning Rod","Paratonnerre",1,1,1,1,1,"Absorption")

MagicGuard = Talent("Magic Guard","Garde Magik",1,1,1,1,1,"AntiDamage")
MagmaArmor = Talent("Magma Armor","Armumagma",1,1,1,1,1,"StatutStop")
MagnetPull = Talent("Magnet Pull","Magnépiège",1,1,1,1,1,"Trap")
MegaLauncher = Talent("Mega Launcher","Méga Baster",1,1,1,1,1,"StatModifCapa")
MotorDrive = Talent("Motor Drive","Motorisé",1,1,1,1,1,"Absorption")
Moxie = Talent("Moxie","Impudence",1,1,1,1,1,"BoostAtt")

NaturalCure = Talent("Natural Cure","Médic Nature",1,1,1,1,1,"CleanStatut")

Overgrow = Talent("Overgrow","Engrais",1,1,1,1,1,"StatModifLow")

Protean = Talent("Protean","Protéen",1,1,1,1,1,"TypeChange")

QuickFeet = Talent("Quick Feet","Pied Véloce",1,1,1,1,1,"StatModif")

Refrigerate = Talent("Refrigerate","Peau Gelée",1,1,1,1,1,"TypeChange")
RockHead = Talent("Rock Head","Tête de Roc",1,1,1,1,1,"AntiDamage")

Scrappy = Talent("Scrappy","Querelleur",1,1,1,1,1,"AvoidImmunity")
SereneGrace = Talent("Serene Grace","Sérénité",1,1,1,1,1,"EffetBoost")
ShadowTag = Talent("Shadow Tag","Marque Ombre",1,1,1,1,1,"Trap")
SheerForce = Talent("Sheer Force","Sans Limite",1,1,1,1,1,"BoostCapa")
Simple = Talent("Simple","Simple",1,1,1,1,1,"ModifStatRatio")
SolarPower = Talent("Solar Power","Force Soleil",1,1,1.5,1,1,"MétéoStatModif")
SpeedBoost = Talent("Speed Boost","Turbo",1,1,1,1,1,"BoostStats")
Static = Talent("Static","Statik",1,1,1,1,1,"AppStatut")
StrongJaw = Talent("Strong Jaw","Prognathe",1,1,1,1,1,"StatModifCapa")
Swarm = Talent("Swarm","Essaim",1,1,1,1,1,"StatModifLow")
SwiftSwim = Talent("Swift Swim","Glissade",1,1,1,1,2,"MétéoStatModif")
Synchronize = Talent("Synchronize","Synchro",1,1,1,1,1,"CopyStatut")

Technician = Talent("Technician","Technicien",1,1,1,1,1,"BoostCapa")
ThickFat = Talent("Thick Fat","Isograisse",1,1,1,1,1,"Resistance")
TintedLens = Talent("Tinted Lense","Lentiteintée",1,1,1,1,1,"BoostCapa")
Torrent = Talent("Torrent","Torrent",1,1,1,1,1,"StatModifLow")

WeakArmor = Talent("Weak Armor","Armurouillée",1,1,1,1,1,"Statmodif")
