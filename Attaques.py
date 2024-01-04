from Effets import *

class Attaque:
    def __init__(self,name,nom,type,cat,prio,puiss,recul,soin,pp,ppmax,preci,precieffet,effet,color):
        self.name = name
        self.nom = nom
        self.type = type
        self.cat = cat #0 Statut, 1 Physique, 2 Special
        self.prio = prio
        self.puiss = puiss
        self.recul = recul
        self.soin = soin
        self.pp = pp
        self.ppmax = ppmax
        self.preci = preci
        self.precieffet = precieffet
        self.effet = effet
        self.color = color

    def copy(self):
        return Attaque(self.name, self.nom, self.type, self.cat, self.prio, self.puiss, self.recul, self.soin, self.pp, self.ppmax, self.preci, self.precieffet, self.effet, self.color)



###Acier###
BulletPunch = Attaque("Bullet Punch","Pisto Poing","Acier",1,1,40,0,0,48,48,100,0,NoOne,"#B5B5B5")
FlashCannon = Attaque("Flash Cannon","Luminocanon","Acier",2,0,80,0,0,16,16,100,10,SpDefDrop,"#B5B5B5")
GyroBall = Attaque("Gyro Ball","Gyro Balle","Acier",1,0,0,0,0,8,8,100,0,NoOne,"#B5B5B5")
IronTail = Attaque("Iron Tail","Queue de Fer","Acier",1,0,100,0,0,24,24,75,30,DefDrop,"#B5B5B5")
IronHead = Attaque("Iron Head","Tête de Fer","Acier",1,0,80,0,0,24,24,100,30,Appeurer,"#B5B5B5")
MeteorMash = Attaque("Meteor Mash","Poing Météor","Acier",1,0,90,0,0,16,16,90,20,SelfAttRaise,"#B5B5B5")
SteelWing = Attaque("Steel Wing","Aile d'Acier","Acier",1,0,70,0,0,40,40,90,10,SelfDefRaise,"#B5B5B5")

###Combat###
AuraSphere = Attaque("Aura Sphere","Aura Sphere","Combat",2,0,80,0,0,32,32,1000,0,NoOne,"#8B3401")
BodyPress = Attaque("Body Press","Big Splash","Combat",1,0,80,0,0,16,16,100,0,NoOne,"#8B3401")
BrickBreak = Attaque("Brick Break","Casse-Brique","Combat",1,0,75,0,0,24,24,100,0,NoOne,"#8B3401")
CloseCombat = Attaque("Close Combat","Close Combat","Combat",1,0,120,0,0,8,8,100,100,SelfSpDefAndDefDrop,"#8B3401")
DrainPunch = Attaque("Drain Punch","Vampi-Poing","Combat",1,0,75,0,0.5,16,16,100,0,NoOne,"#953A10")
FocusBlast = Attaque("Focus Blast", "Exploforce", "Combat", 2, 0, 120, 0, 0, 8, 8, 70, 10, SpDefDrop,"#953A10")
HammerArm = Attaque("Hammer Arm","Marto-Poing","Combat",1,0,100,0,0,16,16,90,100,SelfVitDrop,"#953A10")
MachPunch = Attaque("Mach Punch","Mach Punch","Combat",1,1,40,0,0,48,48,100,0,NoOne,"#953A10")
RollingKick = Attaque("Rolling Kick","Mawashi Geri","Combat",1,0,60,0,0,24,24,85,30,Appeurer,"#953A10")

###Dragon###
DragonClaw = Attaque("Dragon Claw","Draco Griffe","Dragon",1,0,80,0,0,24,24,100,0,NoOne,"#3A08A6")
DragonDance = Attaque("Dragon Dance","Danse Draco","Dragon",0,0,0,0,0,32,32,1000,100,DDance,"#3A08A6")
DragonPulse = Attaque("Dragon Pulse","Dracochoc","Dragon",2,0,85,0,0,16,16,100,0,NoOne,"#3A08A6")

###Eau###
AquaJet = Attaque("Aqua Jet","Aqua Jet","Eau",1,1,40,0,0,32,32,100,0,NoOne,"#0042CE")
AquaTail = Attaque("Aqua Tail","Hydro Queue","Eau",1,0,90,0,0,16,16,90,0,NoOne,"#0042CE")
Crabhammer = Attaque("Crabhammer","Pince-Masse","Eau",1,0,100,0,0,16,16,90,0,NoOne,"#0042CE")
FlipTurn = Attaque("Flip Turn","Eau Revoir","Eau",1,0,60,0,0,32,32,100,100,Switch,"#0042CE")
HydroPump = Attaque("Hydro Pump","Hydrocanon","Eau",2,0,110,0,0,8,8,80,0,NoOne,"#0042CE")
Liquidation = Attaque("Liquidation","Aqua-Brèche","Eau",1,0,85,0,0,16,16,100,20,DefDrop,"#0042CE")
RazorShell = Attaque("Razor Shell","Coqui-Lame","Eau",1,0,75,0,0,16,16,95,50,DefDrop,"#0042CE")
Scald = Attaque("Scald","Ébullition","Eau",2,0,80,0,0,24,24,100,30,Brulure,"#0042CE")
Surf = Attaque("Surf","Surf","Eau",2,0,90,0,0,24,24,100,0,NoOne,"#0042CE")
Waterfall = Attaque("Waterfall","Cascade","Eau",1,0,80,0,0,24,24,100,20,Appeurer,"#0042CE")

###Électrique###
Discharge = Attaque("Discharge","Coup d'Jus","Électrique",2,0,80,0,0,24,24,100,30,Paralysie,"#E2E600")
StaticKick = Attaque("Static Kick","Pied Statik","Électrique",1,0,85,0,0,16,16,90,10,Paralysie,"#E2E600")
Thunder = Attaque("Thuder","Fatal Foudre","Électrique",2,0,110,0,0,16,16,70,30,Paralysie,"#E2E600")
Thunderbolt = Attaque("Thunderbolt","Tonnerre","Électrique",2,0,90,0,0,24,24,100,10,Paralysie,"#E2E600")
ThunderFang = Attaque("Thunder Fang","Croc Éclair","Électrique",1,0,65,0,0,24,24,95,10,Paralysie,"#E2E600")
ThunderPunch = Attaque("Thunder Punch","Poing-Éclair","Électrique",1,0,75,0,0,24,24,100,10,Paralysie,"#E2E600")
VoltSwitch = Attaque("Volt Switch","Change Éclair","Électrique",2,0,70,0,0,32,32,100,100,Switch,"#E2E600")
VoltTackle = Attaque("Volt Tackle","Électacle","Électrique",1,0,120,0.33,0,24,24,100,0,NoOne,"#E2E600")
WildCharge = Attaque("Wild Charge","Éclair Fou","Électrique",1,0,90,0.25,0,24,24,100,0,NoOne,"#E2E600")

###Fée###
DazzlingGleam = Attaque("Dazzling Gleam","Éclat Magique","Fée",2,0,80,0,0,16,16,100,0,NoOne,"#F875BC")
DrainingKiss = Attaque("Draining Kiss","Vampibaiser","Fée",2,0,50,0,75,16,16,100,0,NoOne,"#F875BC")
Moonblast = Attaque("Moonblast","Pouvoir Lunaire","Fée",2,0,95,0,0,24,24,100,30,SpAttDrop,"#F875BC")
PlayRough = Attaque("Play Rough","Calinerie","Fée",1,0,90,0,0,16,16,90,10,AttDrop,"#F875BC")

###Feu###
BitterBlade = Attaque("Bitter Blade","Lame en Peine","Feu",1,0,90,0,0.5,16,16,100,0,NoOne,"#FC610E")
BlazeKick = Attaque("Blaze Kick","Pied Brûleur","Feu",1,0,85,0,0,16,16,90,10,Brulure,"#FC610E")
FireBlast = Attaque("Fire Blast","Déflagration","Feu",2,0,110,0,0,8,8,85,10,Brulure,"#FC610E")
FireFang = Attaque("Fire Fang","Croc Feu","Feu",1,0,65,0,0,24,24,95,10,Brulure,"#FC610E")
FirePunch = Attaque("Fire Punch","Poing-Feu","Feu",1,0,75,0,0,24,24,100,10,Brulure,"#FC610E")
Flamethrower = Attaque("Flamethrower", "Lance-Flamme","Feu", 2, 0, 90, 0, 0, 24, 24, 100, 10, Brulure,"#FC610E")
FlareBlitz = Attaque("Flare Blitz","Boutefeu","Feu",1,0,120,0.33,0,24,24,100,10,Brulure,"#FC610E")
HeatWave = Attaque("Heat Wave","Canicule","Feu",2,0,95,0,0,16,16,90,10,Brulure,"#FC610E")
LavaPlume = Attaque("Lava Plume","Ébullilave","Feu",2,0,80,0,0,24,24,100,30,Brulure,"#FC610E")
Overheat = Attaque("Overheat", "Surchauffe","Feu", 2, 0, 130, 0, 0, 8, 8, 90, 100, SelfSpAttDrop2,"#FC610E")
WillOWisp = Attaque("Will-O-Wisp","Feu Follet","Feu",0,0,0,0,0,24,24,85,100,Brulure,"#FC610E")

###Glace###
FreezingKick = Attaque("Freezing Kick","Pied Givrant","Glace",1,0,85,0,0,16,16,90,10,Gele,"#00F9E9")
IceBeam = Attaque("Ice Beam","Laser glace","Glace",2,0,90,0,0,16,16,100,10,Gele,"#00F9E9")
IceFang = Attaque("Ice Fang","Croc Givre","Glace",1,0,65,0,0,24,24,95,10,Gele,"#00F9E9")
IcePunch = Attaque("Ice Punch","Poing-Glace","Glace",1,0,75,0,0,24,24,100,10,Gele,"#00F9E9")
IceTail = Attaque("Ice Tail","Queue de Glace","Eau",1,0,95,0,0,16,16,85,0,NoOne,"#00F9E9")

###Insecte###
BugBuzz = Attaque("Bug Buzz","Bourdon","Insecte",2,0,90,0,0,16,16,100,10,SpDefDrop,"#86D000")
QuiverDance = Attaque("Quiver Dance","Papillodanse","Insecte",0,0,0,0,0,32,32,1000,100,QuiDance,"#86D000")
LeechLife = Attaque("Leech Life","Vampirisme","Insecte",1,0,80,0,0.5,16,16,100,0,NoOne,"#86D000")
Megahorn = Attaque("Megahorn","Mégacorne","Insecte",1,0,120,0,0,16,16,85,0,NoOne,"#86D000")
SignalBeam = Attaque("Signal Beam","Rayon Signale","Insecte",2,0,75,0,0,24,24,100,10,Confusion,"#86D000")
UTurn = Attaque("U-turn","Demi-Tour","Insecte",1,0,70,0,0,32,32,100,100,Switch,"#86D000")

###Normal###
BodySlam = Attaque("Body Slam","Plaquage","Normal",1,0,85,0,0,24,24,100,30,Paralysie,"#D9DDD3")
Boomburst = Attaque("Boomburst","Bang Sonique","Normal",2,0,140,0,0,16,16,100,0,NoOne,"#D9DDD3")
DoubleEdge = Attaque("Double-Edge","Damoclès","Normal",1,0,120,0.33,0,24,24,100,0,NoOne,"#D9DDD3")
ExtremeSpeed = Attaque("Extreme Speed","Vitesse Extrême","Normal",1,2,80,0,0,8,8,100,0,NoOne,"#D9DDD3")
Facade = Attaque("Facade","Facade","Normal",1,0,70,0,0,32,32,100,0,NoOne,"#D9DDD3")
Growth = Attaque("Growth","Croissance","Normal",0,0,0,0,0,32,32,1000,100,Grow,"#D9DDD3")
HyperFang = Attaque("Hyper Fang","Croc de Mort","Normal",1,0,80,0,0,24,24,90,10,Appeurer,"#D9DDD3")
HyperVoice = Attaque("Hyper Voice","Mégaphone","Normal",2,0,90,0,0,16,16,100,0,NoOne,"#D9DDD3")
Protect = Attaque("Protect","Abri","Normal",0,4,0,0,0,16,16,1000,0,NoOne,"#D9DDD3")
QuickAttack = Attaque("Quick Attack","Vive-Attaque","Normal",1,1,40,0,0,48,48,100,0,NoOne,"#D9DDD3")
SwordDance = Attaque("Sword Dance","Danse Lame","Normal",0,0,0,0,0,32,32,1000,100,SelfAttRaise2,"#D9DDD3")
ReturnA = Attaque("Return","Retour","Normal",1,0,102,0,0,32,32,100,0,NoOne,"#D9DDD3")

###Plante###
EnergyBall = Attaque("Energy Ball","Éco-Sphère","Plante",2,0,90,0,0,16,16,100,10,SpDefDrop,"#037605")
GigaDrain = Attaque("Giga Drain","Giga-Sangsue","Plante",2,0,75,0,0.5,16,16,100,0,NoOne,"#037605")
SeedBomb = Attaque("Seed Bomb","Canon Graine","Plante",1,0,80,0,0,24,24,100,0,NoOne,"#037605")
SolarBeam = Attaque("Solar Beam", "Lance-Soleil","Plante", 2, 0, 120, 0, 0, 16, 16, 100, 100, "SolarTempo","#037605")
Trailblaze = Attaque("Trailblaze","Désherbaffe","Plante",1,0,50,0,0,32,32,100,100,SelfVitRaise,"#037605")

###Poison###
PoisonJab = Attaque("Poison Jab","Direct Toxik","Poison",1,0,80,0,0,32,32,100,30,Poison,"#550090")
SludgeBomb = Attaque("Sludge Bomb","Bombe Beurk","Poison",2,0,90,0,0,16,16,100,30,Poison,"#550090")
SludgeWave = Attaque("Sludge Wave","Cradovague","Poison",2,0,95,0,0,16,16,100,10,Poison,"#550090")
Toxic = Attaque("Toxic","Toxik","Poison",0,0,0,0,0,16,16,90,100,PoisonGrv,"#550090")

###Psy###
CalmMind = Attaque("Calm Mind","Plénitude","Psy",0,0,0,0,0,32,32,1000,100,CMind,"#FF36F5")
Extrasensory = Attaque("Extrasensory","Extrasenseur","Psy",2,0,80,0,0,32,32,100,10,Appeurer,"#FF36F5")
Psychic = Attaque("Psychic","Psyko","Psy",2,0,90,0,0,16,16,100,10,SpDefDrop,"#FF36F5")
ZenHeadbutt = Attaque("Zen Headbutt","Psykoud'Boul","Psy",1,0,80,0,0,24,24,90,20,Appeurer,"#FF36F5")

###Roche###
HeadSmash = Attaque("Head Smach","Fracass'Tête","Roche",1,0,150,0.5,0,8,8,80,0,NoOne,"#543E15")
StoneEdge = Attaque("Stone Edge","Lame de Roc","Roche",1,0,100,0,0,8,8,80,0,NoOne,"#543E15")
PowerGem = Attaque("Power Gem","Rayon Gemme","Roche",2,0,80,0,0,32,32,100,0,NoOne,"#543E15")

###Sol###
DrillRun = Attaque("Drill Run","Tunnelier","Sol",1,0,80,0,0,16,16,95,0,NoOne,"#FFBA3A")
EarthPower = Attaque("Earth Power","Telluriforce","Sol",2,0,90,0,0,16,16,100,10,SpDefDrop,"#FFBA3A")
Earthquake = Attaque("Earthquake","Séisme","Sol",1,0,100,0,0,16,16,100,0,NoOne,"#FFBA3A")
HighHorsepower = Attaque("High Horsepower","Cavalerie Lourde","Sol",1,0,95,0,0,16,16,95,0,NoOne,"#FFBA3A")

###Spectre###
Curse = Attaque("Curse","Malédiction","Spectre",0,0,0,0,0,16,16,1000,100,Cursed,"#1F0933")
Hex = Attaque("Hex","Châtiment","Sepectre",2,0,65,0,0,16,16,100,0,NoOne,"#1F0933")
ShadowBone = Attaque("Shadow Bone","Os'Ombre","Spectre",1,0,85,0,0,16,16,100,20,DefDrop,"#1F0933")
ShadowBall = Attaque("Shadow Ball","Ball'Ombre","Spectre",2,0,80,0,0,24,24,100,20,SpDefDrop,"#1F0933")
ShadowClaw = Attaque("Shadow Claw","Griffe Ombre","Spectre",1,0,70,0,0,24,24,100,0,NoOne,"#1F0933")
ShadowSneak = Attaque("Shadow Sneak","Ombre Portée","Spectre",1,1,40,0,0,48,48,100,0,NoOne,"#1F0933")

###Ténèbres###
Crunch = Attaque("Crunch","Mâchouille","Ténèbres",1,0,80,0,0,24,24,100,20,DefDrop,"#000000")
DarkestLariat = Attaque("Darkest Lariat","Dark Lariat","Ténèbres",1,0,85,0,0,16,16,100,0,NoOne,"#000000")
DarkPulse = Attaque("Drak Pulse","Vibrobscure","Ténèbres",2,0,80,0,0,24,24,100,20,Appeurer,"#000000")
KnockOff = Attaque("Knock Off","Sabotage","Ténèbres",1,0,65,0,0,32,32,100,100,RemoveItem,"#000000")

###Vol###
AerialAce = Attaque("Aerial Ace","Aéropique","Vol",1,0,60,0,0,32,32,1000,0,NoOne,"#9FFAFE")
AirSlash = Attaque("Air Slash", "Lame d'air","Vol", 2, 0, 75, 0, 0, 24, 24, 95, 30, Appeurer,"#9FFAFE")
BraveBird = Attaque("Brave Bird","Rapace","Vol",1,0,120,0.33,0,24,24,100,0,NoOne,"#9FFAFE")
DrillPeck = Attaque("Drill Peck","Bec Vrille","Vol",1,0,80,0,0,32,32,100,0,NoOne,"#9FFAFE")
Hurricane = Attaque("Hurricane","Vent Violent","Vol",2,0,110,0,0,16,16,70,30,"Confusion","#9FFAFE")