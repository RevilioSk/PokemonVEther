from tkinter import *
import os

from Attaques import *
from Talents import *
from Effets import *
from Objets import *
from Persos import *

script_dir = os.path.dirname(__file__)


class Pokemon:
    def __init__(self,name,nom,etat,type1,type2,talent,objet,a1,a2,a3,a4,pv,pvmax,att,spa,defe,spdef,vit,statut):
        self.name = name
        self.nom = nom
        self.etat = etat
        self.type1 = type1
        self.type2 = type2
        self.talent = talent
        self.objet = objet
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.pv = pv
        self.pvmax = pvmax
        self.att = att
        self.defe = defe # on ajoute un e pour éviter une definition
        self.spa = spa
        self.spdef = spdef
        self.vit = vit
        self.statut = statut

    def copy(self):
        return Pokemon(self.name, self.nom, self.etat, self.type1, self.type2, self.talent, self.objet, self.a1, self.a2, self.a3, self.a4, self.pv, self.pvmax, self.att, self.spa, self.defe, self.spdef, self.vit, self.statut)



###Team Test 1###
Charizard = Pokemon("Charizard","Dracaufeu","Vivant","Feu","Vol",SolarPower,FocusSash,Flamethrower.copy(),AirSlash.copy(),FocusBlast.copy(),Overheat.copy(),302,302,155,317,192,207,328,"None")
Torkoal = Pokemon("Torkoal","Chartor","Vivant","Feu","None",Drought,HeatRock,Curse.copy(),LavaPlume,Toxic.copy(),FireBlast.copy(),348,348,177,206,416,176,68,"None")
Volcarona = Pokemon("Volcarona","Pyrax","Vivant","Insecte","Feu",FlameBody,LifeOrb,BugBuzz.copy(),QuiverDance,Flamethrower.copy(),Hurricane.copy(),316,316,112,405,166,247,299,"None")
Flareon = Pokemon("Flareon","Pyroli","Vivant","Feu","None",FlashFire,ChoiceBand,FlareBlitz.copy(),QuickAttack.copy(),BodySlam.copy(),IronTail,340,340,394,203,156,257,166,"None")
MarowakAlola = Pokemon("Marowak-Alola","Ossatueur d'Alola","Vivant","Feu","Spectre",RockHead,ThickClub,FlareBlitz.copy(),IronHead.copy(),KnockOff.copy(),ShadowBone,328,328,284,122,256,198,126,"None")
Chandelure = Pokemon("Chandelure","Lugulabre","Vivant","Feu","Spectre",FlashFire,LifeOrb,ShadowBall.copy(),Flamethrower.copy(),WillOWisp,EnergyBall.copy(),266,266,103,389,216,217,284,"None")

###Team Test 2###
Empoleon = Pokemon("Empoleon","Pingoléon","Vivant","Eau","Acier",Torrent,Leftovers,IceBeam.copy(),FlashCannon.copy(),Scald.copy(),Toxic.copy(),377,377,159,353,212,238,157,"None")
Pelipper = Pokemon("Pelipper","Bekipan","Vivant","Eau","Vol",Drizzle,DampRock,Hurricane.copy(),IceBeam.copy(),Scald.copy(),Toxic.copy(),32900,32900,94,22600,328,177,1660,"None")
Floatzel = Pokemon("Floatzel","Musteflott","Vivant","Eau","None",SwiftSwim,LifeOrb,AquaJet.copy(),IceFang.copy(),Crunch.copy(),Liquidation.copy(),316,316,309,185,145,137,361,"None")
#Barraskewda = Pokemon("Barraskewda","Hastacuda","Vivant","Eau","None",SwiftSwim,ChoiceBand,CloseCombat.copy(),PoisonJab.copy(),AquaJet.copy(),Liquidation.copy(),268,268,379,140,156,137,371,"None")
Poliwrath = Pokemon("Poliwrath","Tartard","Vivant","Eau","Combat",SwiftSwim,LifeOrb,CloseCombat.copy(),Liquidation.copy(),IcePunch.copy(),Earthquake.copy(),326,326,317,158,226,217,239,"None")
Crawdaunt = Pokemon("Crawdaunt","Colhomard","Vivant","Eau","Ténèbres",Adaptability,LifeOrb,AquaJet.copy(),CloseCombat.copy(),KnockOff.copy(),Crabhammer.copy(),335,335,372,194,206,147,146,"None")

###Team1 (Clément)###
VenusaurT1 = Pokemon("Venusaur","Florizarre","Vivant","Plante","Poison",Chlorophyll,LifeOrb,Growth.copy(),SludgeBomb.copy(),GigaDrain.copy(),EnergyBall.copy(),306,306,152,328,202,237,259,"None")
Mimikyu = Pokemon("Mimikyu","Mimiqui","Vivant","Spectre","Fée",Disguise,FocusSash,SwordDance.copy(),ShadowClaw.copy(),ShadowSneak.copy(),PlayRough.copy(),256,256,279,122,196,247,320,"None")
Krookodile = Pokemon("Krookodile","Crocorible","Vivant","Sol","Ténèbres",Moxie,ChoiceScarf,Earthquake.copy(),KnockOff.copy(),DarkestLariat.copy(),StoneEdge.copy(),336,336,333,149,196,177,311,"None")
Metagross = Pokemon("Metagross","Métalosse","Vivant","Acier","Psy",ClearBody,LifeOrb,BodyPress.copy(),MeteorMash.copy(),ZenHeadbutt.copy(),IcePunch.copy(),306,306,369,203,296,217,262,"None")
Salamence = Pokemon("Salamence","Drattak","Vivant","Dragon","Vol",Moxie,ChoiceScarf,DragonClaw.copy(),FireFang.copy(),Earthquake.copy(),StoneEdge.copy(),336,336,369,230,196,197,328,"None")
Kabutops = Pokemon("Kabutops","Kabutops","Vivant","Eau","Roche",SwiftSwim,ChoiceBand,AquaJet.copy(),FlipTurn.copy(),Liquidation.copy(),StoneEdge.copy(),266,266,361,149,246,177,259,"None")

###Team2 (Robin)###
BlazikenT2 = Pokemon("Blaziken","Braségali","Vivant","Feu","Combat",Blaze,LifeOrb,CloseCombat.copy(),BlazeKick.copy(),Protect.copy(),UTurn.copy(),306,306,372,230,176,177,259,"None")
Togekiss = Pokemon("Togekiss","Togekiss","Vivant","Vol","Fée",ChoiceScarf,ChoiceScarf,AirSlash.copy(),DazzlingGleam.copy(),Extrasensory.copy(),ShadowBall.copy(),316,316,94,339,226,267,284,"None")
Tyranitar = Pokemon("Tyranitar","Tyranocif","Vivant","Roche","Ténèbres",KeenEye,ChoiceBand,Earthquake.copy(),Crunch.copy(),BodyPress.copy(),StoneEdge.copy(),384,384,403,203,282,236,158,"None")
#Metagross = Pokemon("Metagross","Métalosse","Vivant","Acier","Psy",ClearBody,LifeOrb,BodyPress.copy(),MeteorMash.copy(),ZenHeadbutt.copy(),IcePunch.copy(),301,301,369,203,296,217,262,"None")
Snorlax = Pokemon("Snorlax","Ronflex","Vivant","Normal","None",ThickFat,Leftovers,Curse.copy(),ReturnA.copy(),Toxic.copy(),BodyPress.copy(),529,529,257,149,166,350,96,"None")
GyaradosT2 = Pokemon("Gyarados","Léviator","Vivant","Eau","Vol",Intimidate,LifeOrb,IceFang.copy(),Waterfall.copy(),Earthquake.copy(),DragonDance.copy(),336,336,383,140,194,237,261,"None")

###Team3 (Mélina)###
"""Delphox"""
Lucario = Pokemon("Lucario","Lucario","Vivant","Combat","Acier",InnerFocus,ChoiceScarf,CloseCombat.copy(),IcePunch.copy(),ExtremeSpeed.copy(),MeteorMash.copy(),286,286,319,239,176,177,306,"None")
GardevoirT3 = Pokemon("Gardevoir","Gardevoir","Vivant","Psy","Fée",Synchronize,LifeOrb,Psychic.copy(),AuraSphere.copy(),CalmMind.copy(),Moonblast.copy(),283,283,121,349,166,267,284,"None")
Talonflame = Pokemon("Talonflame","Flambusard","Vivant","Feu","Vol",FlameBody,ChoiceBand,BraveBird.copy(),FlareBlitz.copy(),UTurn.copy(),QuickAttack.copy(),303,303,261,165,178,175,385,"None")
Aurorus = Pokemon("Aurorus","Dragmara","Vivant","Roche","Glace",Refrigerate,ChoiceSpecs,FlashCannon.copy(),PowerGem.copy(),HyperVoice.copy(),Thunderbolt.copy(),455,455,143,326,180,221,152,"None")
Heliolisk = Pokemon("Heliolisk","Iguolta","Vivant","Électrique","Normal",SolarPower,ChoiceSpecs,Thunderbolt.copy(),FocusBlast.copy(),VoltSwitch.copy(),DragonPulse.copy(),270,270,103,317,140,225,348,"None")

###Team4 (Oli)###
Greninja = Pokemon("Greninja","Amphinobi","Vivant","Eau","Ténèbres",Scrappy,ChoiceSpecs,IceBeam.copy(),Surf.copy(),UTurn.copy(),Extrasensory.copy(),285,285,203,305,170,179,377,"None")
ZoroarkF1 = Pokemon("Zoroark-Hisui","Zoroark","Vivant","Spectre","Normal",Scrappy,ChoiceScarf,ShadowBall.copy(),UTurn.copy(),HyperVoice.copy(),SludgeBomb.copy(),251,251,212,349,156,157,350,"None")
##Lucario
Flygon = Pokemon("Flygon","Libégon","Vivant","Dragon","Sol",Levitate,LifeOrb,DragonClaw.copy(),DragonDance.copy(),Earthquake.copy(),UTurn.copy(),301,301,328,176,196,197,299,"None")
Ceruledge = Pokemon("Cerulege","Malvalame","Vivant","Feu","Spectre",WeakArmor,ChoiceBand,BitterBlade.copy(),ShadowSneak.copy(),ShadowClaw.copy(),PoisonJab.copy(),291,291,349,140,196,237,295,"None")
Jolteon = Pokemon("Jolteon","Voltali","Vivant","Électrique","None",QuickFeet,ChoiceSpecs,IceBeam.copy(),ShadowBall.copy(),Thunderbolt.copy(),VoltSwitch.copy(),271,271,121,319,156,227,394,"None")

###Team Gamin###
Furret = Pokemon("Furret","Fouinard","Vivant","Normal","None",Frisk,ChoiceBand,FirePunch.copy(),IcePunch.copy(),ReturnA.copy(),QuickAttack.copy(),316,316,251,113,164,147,306,"None")
Bibarel = Pokemon("Bibarel","Castorno","Vivant","Normal","Eau",Simple,LifeOrb,IceFang.copy(),ReturnA.copy(),AquaJet.copy(),Liquidation.copy(),305,305,269,131,156,157,265,"None")
Raticate = Pokemon("Raticate","Rattatac","Vivant","Normal","None",StrongJaw,ChoiceBand,Crunch.copy(),QuickAttack.copy(),HyperFang.copy(),IceFang.copy(),256,256,261,122,156,177,322,"None")
Watchog = Pokemon("Watchog","Miradar","Vivant","Normal","None",Analytic,LifeOrb,AquaTail.copy(),Crunch.copy(),ReturnA.copy(),IcePunch.copy(),266,266,269,140,174,175,278,"None")
Linoone = Pokemon("Linoone","Linéon","Vivant","Normal","Combat",QuickFeet,ChoiceBand,ExtremeSpeed.copy(),ReturnA.copy(),CloseCombat.copy(),IceTail.copy(),302,302,239,122,158,159,328,"None")
Diggersby = Pokemon("Diggersby","Excavarenne","Vivant","Normal","Sol",HugePower,ChoiceBand,ReturnA.copy(),FirePunch.copy(),Earthquake.copy(),IcePunch.copy(),380,380,464,122,190,191,192,"None")

###Team Ouvrier###
Magnezone = Pokemon("Magnezone","Magnézone","Vivant","Acier","Électrique",MagnetPull,ChoiceScarf,BodyPress.copy(),Discharge.copy(),VoltSwitch.copy(),FlashCannon.copy(),286,286,130,359,266,217,240,"None")
Ampharos = Pokemon("Ampharos","Pharamp","Vivant","Électrique","None",Static,LifeOrb,IceBeam.copy(),Thunderbolt.copy(),VoltSwitch.copy(),PowerGem.copy(),389,389,139,361,206,218,146,"None")
Electivire = Pokemon("Electivire","Elekable","Vivant","Électrique","None",MotorDrive,ChoiceScarf,IcePunch.copy(),CloseCombat.copy(),VoltTackle.copy(),VoltSwitch.copy(),296,296,379,203,170,207,289,"None")
Raichu = Pokemon("Raichu","Raichu","Vivant","Électrique","None",Static,ChoiceSpecs,VoltSwitch.copy(),Surf.copy(),IceBeam.copy(),Thunderbolt.copy(),266,266,166,279,146,197,350,"None")
Electrode = Pokemon("Electrode","Electrode","Vivant","Électrique","None",Static,ChoiceSpecs,Discharge.copy(),Thunder.copy(),SignalBeam.copy(),IceBeam.copy(),266,266,106,259,158,196,438,"None")
Rotom = Pokemon("Rotom","Motisma","Vivant","Électrique","Spectre",Levitate,Leftovers,Hex.copy(),VoltSwitch.copy(),Discharge.copy(),DarkPulse.copy(),246,246,94,289,190,191,309,"None")

###Scout###
Butterfree = Pokemon("Butterfree","Papilusion","Vivant","Insecte","Vol",CompoundEyes,LifeOrb,BugBuzz.copy(),GigaDrain.copy(),Hurricane.copy(),SignalBeam.copy(),266,266,85,279,136,197,262,"None")
Beedrill = Pokemon("Beedrill","Dardargnan","Vivant","Insecte","Poison",Swarm,ChoiceScarf,LeechLife.copy(),PoisonJab.copy(),DrillRun.copy(),UTurn.copy(),276,276,279,113,116,197,273,"None")
Scizor = Pokemon("Scizor","Cizayox","Vivant","Insecte","Acier",Technician,ChoiceBand,BulletPunch.copy(),Trailblaze.copy(),UTurn.copy(),CloseCombat.copy(),349,349,394,131,236,198,166,"None")
Heracross = Pokemon("Heracross","Scarhino","Vivant","Insecte","Combat",Guts,FlameOrb,Facade.copy(),CloseCombat.copy(),Megahorn.copy(),KnockOff.copy(),306,306,349,104,186,227,295,"None")
Venomoth = Pokemon("Venomoth","Aéromite","Vivant","Insecte","Poison",TintedLens,LifeOrb,BugBuzz.copy(),Psychic.copy(),SludgeBomb.copy(),EnergyBall.copy(),286,286,121,279,156,187,306,"None")
Pinsir = Pokemon("Pinsir","Scarabrute","Vivant","Insecte","None",Moxie,ChoiceScarf,HighHorsepower.copy(),KnockOff.copy(),QuickAttack.copy(),Megahorn.copy(),276,276,349,131,236,177,295,"None")

###Montagnard###
Steelix = Pokemon("Steelix","Steelix","Vivant","Acier","Sol",RockHead,Leftovers,BodyPress.copy(),Earthquake.copy(),GyroBall.copy(),StoneEdge.copy(),360,360,295,146,436,167,58,"None")
Golem = Pokemon("Golem","Grolem","Vivant","Roche","Sol",RockHead,ChoiceBand,HeadSmash.copy(),Earthquake.copy(),GyroBall.copy(),ThunderPunch.copy(),370,370,372,146,296,167,85,"None")
Rhyperior = Pokemon("Rhyperior","Rhinastoc","Vivant","Roche","Sol",RockHead,ChoiceBand,HeadSmash.copy(),Earthquake.copy(),DoubleEdge.copy(),AquaTail.copy(),440,440,416,131,296,147,116,"None")
Dugtrio = Pokemon("Dugtrio","Triopikeur","Vivant","Sol","None",ArenaTrap,LifeOrb,StoneEdge.copy(),Earthquake.copy(),ShadowClaw.copy(),BodySlam.copy(),216,216,299,122,136,177,372,"None")
Aggron = Pokemon("Aggron","Galeking","Vivant","Roche","Acier",RockHead,Leftovers,HeadSmash.copy(),Earthquake.copy(),GyroBall.copy(),DoubleEdge.copy(),350,350,350,156,396,157,94,"None")
Aerodactyl = Pokemon("Aerodactyl","Ptera","Vivant","Roche","Vol",RockHead,LifeOrb,HeadSmash.copy(),BraveBird.copy(),DragonClaw.copy(),IronHead.copy(),306,306,309,140,166,187,394,"None")

###Pecheur###
Seaking = Pokemon("Seaking","Poissoroy","Vivant","Eau","None",LightningRod,ChoiceBand,DrillRun.copy(),Waterfall.copy(),FlipTurn.copy(),PoisonJab.copy(),370,370,311,149,166,197,173,"None")
Kingler = Pokemon("Kingler","Krabboss","Vivant","Eau","None",SheerForce,ChoiceBand,HammerArm.copy(),BodySlam.copy(),Liquidation.copy(),HighHorsepower.copy(),256,256,359,122,266,137,273,"None")
Tentacruel = Pokemon("Tentacruel","Tentacruel","Vivant","Eau","Poison",ClearBody,Leftovers,GigaDrain.copy(),HydroPump.copy(),SludgeWave.copy(),IceBeam.copy(),306,306,130,259,166,277,328,"None")
Starmie = Pokemon("Starmie","Staross","Vivant","Eau","Psy",NaturalCure,LifeOrb,HydroPump.copy(),IceBeam.copy(),Thunderbolt.copy(),Psychic.copy(),266,266,139,299,206,207,361,"None")
Gyarados = Pokemon("Gyarados","Léviator","Vivant","Eau","Vol",Intimidate,ChoiceScarf,IceFang.copy(),Waterfall.copy(),Crunch.copy(),ThunderFang.copy(),336,336,349,140,194,237,287,"None")
Barraskewda = Pokemon("Barraskewda","Hastacuda","Vivant","Eau","None",SwiftSwim,ChoiceBand,FlipTurn.copy(),PoisonJab.copy(),AquaJet.copy(),Liquidation.copy(),268,268,379,140,156,137,371,"None")

###Cracheur de Feu###
Ninetales = Pokemon("Ninetales","Feunard","Vivant","Feu","Psy",Drought,HeatRock,FireBlast.copy(),Psychic.copy(),EnergyBall.copy(),ShadowBall.copy(),287,287,153,296,161,231,306,"None")
Arcanine = Pokemon("Arcanine","Arcanin","Vivant","Feu","Combat",Intimidate,ChoiceBand,CloseCombat.copy(),FlareBlitz.copy(),WildCharge.copy(),IronHead.copy(),321,321,324,151,191,131,314,"None")
Magmotar = Pokemon("Magmotar","Maganon","Vivant","Feu","None",FlameBody,LifeOrb,FireBlast.copy(),FocusBlast.copy(),IceBeam.copy(),Thunderbolt.copy(),291,291,175,349,170,227,291,"None")
Camerupt = Pokemon("Camerupt","Camérupt","Vivant","Feu","Sol",MagmaArmor,Leftovers,StoneEdge.copy(),Earthquake.copy(),FlareBlitz.copy(),ZenHeadbutt.copy(),344,344,328,221,176,187,116,"None")
Darmanitan = Pokemon("Darmanitan","Darumacho","Vivant","Feu","None",SheerForce,ChoiceBand,FlareBlitz.copy(),UTurn.copy(),BrickBreak.copy(),Earthquake.copy(),351,351,379,86,146,147,317,"None")
Houndoom = Pokemon("Houndoom","Démolosse","Vivant","Feu","Ténèbres",FlashFire,ChoiceScarf,Flamethrower.copy(),SludgeBomb.copy(),ShadowBall.copy(),DarkPulse.copy(),291,291,166,319,136,197,317,"None")

###Telekinesiste###
Alakazam = Pokemon("Alakazam","Alakazam","Vivant","Psy","None",MagicGuard,LifeOrb,Psychic.copy(),EnergyBall.copy(),SignalBeam.copy(),ShadowBall.copy(),251,251,94,369,126,227,372,"None")
Medicham = Pokemon("Medicham","Charmina","Vivant","Psy","Combat",HugePower,ChoiceBand,DrainPunch.copy(),CloseCombat.copy(),ZenHeadbutt.copy(),BulletPunch.copy(),261,261,438,140,186,187,284,"None")
Reuniclus = Pokemon("Reuniclus","Symbios","Vivant","Psy","None",MagicGuard,Leftovers,Psychic.copy(),EnergyBall.copy(),Thunder.copy(),ShadowBall.copy(),424,424,121,383,186,207,96,"None")
Gardevoir = Pokemon("Gardevoir","Gardevoir","Vivant","Psy","Fée",Synchronize,ChoiceScarf,Psychic.copy(),AuraSphere.copy(),SignalBeam.copy(),Moonblast.copy(),277,277,121,349,166,267,284,"None")
Hypno = Pokemon("Hypno","Hypnomade","Vivant","Psy","None",FlameBody,LifeOrb,Psychic.copy(),FocusBlast.copy(),DazzlingGleam.copy(),DrainingKiss.copy(),374,374,135,269,176,267,170,"None")
Gothitelle = Pokemon("Gothitelle","Sidérella","Vivant","Psy","None",ShadowTag,Leftovers,Psychic.copy(),FocusBlast.copy(),DarkPulse.copy(),ShadowBall.copy(),344,344,103,317,226,257,166,"None")

###Karateca###
Hitmonchan = Pokemon("Hitmonchan","Tygnon","Vivant","Combat","None",IronFist,ChoiceBand,IcePunch.copy(),ThunderPunch.copy(),MachPunch.copy(),DrainPunch.copy(),242,242,309,95,194,256,276,"None")
Hitmonlee = Pokemon("Hitmonlee","Kicklee","Vivant","Combat","None",IronKick,ChoiceBand,BlazeKick.copy(),RollingKick.copy(),StaticKick.copy(),FreezingKick.copy(),304,304,339,106,142,256,211,"None")
Hitmontop = Pokemon("Hitmontop","Kapoera","Vivant","Combat","None",Technician,LifeOrb,AerialAce.copy(),BulletPunch.copy(),MachPunch.copy(),Earthquake.copy(),241,241,289,95,226,257,262,"None")
Machamp = Pokemon("Machamp","Mackogneur","Vivant","Combat","None",Guts,FlameOrb,Facade.copy(),BulletPunch.copy(),CloseCombat.copy(),StoneEdge.copy(),383,383,394,149,196,208,146,"None")
Throh = Pokemon("Throh","Judokrak","Vivant","Combat","None",InnerFocus,LifeOrb,BodySlam.copy(),BrickBreak.copy(),FirePunch.copy(),IcePunch.copy(),444,444,328,86,206,207,126,"None")
Sawk = Pokemon("Sawk","Karaclée","Vivant","Combat","None",InnerFocus,ChoiceScarf,IcePunch.copy(),FirePunch.copy(),Earthquake.copy(),BrickBreak.copy(),291,291,349,86,186,187,295,"None")

###Ornithologue###
Pidgeot = Pokemon("Pidgeot","Roucarnage","Vivant","Vol","Normal",KeenEye,ChoiceBand,BraveBird.copy(),DoubleEdge.copy(),UTurn.copy(),SteelWing.copy(),307,307,259,158,186,177,331,"None")
Fearow = Pokemon("Fearow","Rapasdepic","Vivant","Vol","Normal",KeenEye,ChoiceBand,DrillPeck,DoubleEdge.copy(),QuickAttack.copy(),SteelWing.copy(),271,271,279,142,166,159,328,"None")
Noctowl = Pokemon("Noctowl","Noarfang","Vivant","Vol","Psy",KeenEye,LifeOrb,AirSlash.copy(),ShadowBall.copy(),Moonblast.copy(),Psychic.copy(),341,341,94,271,136,229,262,"None")
Swellow = Pokemon("Swellow","Heledelle","Vivant","Vol","Normal",Scrappy,ChoiceSpecs,Boomburst.copy(),Hurricane.copy(),UTurn.copy(),HeatWave.copy(),261,261,185,249,156,137,383,"None")
Braviary = Pokemon("Braviary","Gueriaigle","Vivant","Vol","Combat",SheerForce,ChoiceScarf,BraveBird.copy(),CloseCombat.copy(),UTurn.copy(),IronHead.copy(),341,341,345,135,186,187,284,"None")
Staraptor = Pokemon("Staraptor","Etouraptor","Vivant","Vol","Normal",Intimidate,ChoiceBand,BraveBird.copy(),DoubleEdge.copy(),CloseCombat.copy(),QuickAttack.copy(),311,311,339,122,176,157,328,"None")

###Pokemaniac###
VenusaurPkMn = Pokemon("Venusaur","Florizarre","Vivant","Plante","Poison",Overgrow,Leftovers,EarthPower.copy(),EnergyBall.copy(),SludgeBomb.copy(),GigaDrain.copy(),301,301,152,299,202,237,284,"None")
Feraligatr = Pokemon("Feraligatr","Aligatueur","Vivant","Eau","None",Torrent,ChoiceBand,AquaJet.copy(),IcePunch.copy(),Waterfall.copy(),DragonClaw.copy(),374,374,339,174,236,203,192,"None")
BlazikenPkMn = Pokemon("Blaziken","Braségali","Vivant","Feu","Combat",Blaze,LifeOrb,CloseCombat.copy(),FirePunch.copy(),PoisonJab.copy(),ThunderPunch.copy(),301,301,339,230,176,177,284,"None")
Torterra = Pokemon("Torterra","Torterra","Vivant","Plante","Sol",Overgrow,Leftovers,Earthquake.copy(),IronHead.copy(),SeedBomb.copy(),BodySlam.copy(),394,394,348,167,246,207,148,"None")
Samurott = Pokemon("Samurott","Clamiral","Vivant","Eau","None",Torrent,ChoiceBand,AquaJet.copy(),RazorShell.copy(),BrickBreak.copy(),Megahorn.copy(),394,394,328,226,206,177,176,"None")
Delphox = Pokemon("Delphox","Goupelin","Vivant","Feu","Psy",Blaze,ChoiceScarf,FireBlast.copy(),FocusBlast.copy(),Psychic.copy(),ShadowBall.copy(),291,291,128,327,180,237,337,"None")



CapaAura = {"Dark Pulse", "Aura Sphere", "Water Pulse","Terrain Pulse","Dragon Pulse","Origin Pulse","Heal Pulse"}
CapaDegel = {"Flame Wheel", "Sacred Fire", "Flare Blitz","Scald","Fusion Flare","Steam Eruption"}
CapaMorsure = {"Bite", "Crunch.copy()", "Fire Fang","Hyper Fang","Ice Fang","Poison Fang","Psychic.copy() Fangs","Thunder Fang","Fishious Rend","JawLock"}
Punch = {"Thunder Punch","Ice Punch","Fire Punch","Mach Punch","Drain Punch"}
Kick = {"Static Kick","Rolling Kick","Blaze Kick","Freezing Kick"}
Statuts = {"Brûlé","Endormi","Paralysé","Gelé","Empoisonné","Gravement Empoisonné"}
PhysiqueNonDirecte = {"Earthquake","Seed Bomb","Stone Edge"}
SpecialDirecte = {"Drain Kiss"}

modifstats = {0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3, 5: 3.5, 6: 4, -1: (2/3), -2: 0.5, -3: 0.4, -4: (1/3), -5: (2/7), -6: 0.25}

types = {
    "Normal": {
        "Faiblesses": ["Combat"],
        "Résistances": [],
        "Immunites": ["Spectre"]
    },
    "Feu": {
        "Faiblesses": ["Eau", "Roche", "Sol"],
        "Résistances": ["Feu", "Plante", "Glace", "Insecte", "Acier", "Fée"],
        "Immunites": []
    },
    "Eau": {
        "Faiblesses": ["Électrique", "Plante"],
        "Résistances": ["Feu", "Eau", "Glace", "Acier"],
        "Immunites": []
    },
    "Électrique": {
        "Faiblesses": ["Sol"],
        "Résistances": ["Électrique", "Vol", "Acier"],
        "Immunites": []
    },
    "Plante": {
        "Faiblesses": ["Feu", "Glace", "Poison", "Vol", "Insecte"],
        "Résistances": ["Eau", "Électrique", "Plante", "Sol"],
        "Immunites": []
    },
    "Glace": {
        "Faiblesses": ["Feu", "Combat", "Roche", "Acier"],
        "Résistances": ["Glace"],
        "Immunites": []
    },
    "Combat": {
        "Faiblesses": ["Vol", "Psy", "Fée"],
        "Résistances": ["Roche", "Acier"],
        "Immunites": ["Spectre"]
    },
    "Poison": {
        "Faiblesses": ["Sol", "Psy"],
        "Résistances": ["Combat", "Poison", "Insecte", "Fée"],
        "Immunites": []
    },
    "Sol": {
        "Faiblesses": ["Eau", "Plante", "Glace"],
        "Résistances": ["Poison", "Roche"],
        "Immunites": ["Électrique"]
    },
    "Vol": {
        "Faiblesses": ["Électrique", "Roche", "Glace"],
        "Résistances": ["Plante", "Combat", "Insecte"],
        "Immunites": ["Sol"]
    },
    "Psy": {
        "Faiblesses": ["Insecte", "Ténèbres", "Spectre"],
        "Résistances": ["Combat", "Psy"],
        "Immunites": []
    },
    "Insecte": {
        "Faiblesses": ["Feu", "Vol", "Roche"],
        "Résistances": ["Plante", "Combat", "Sol"],
        "Immunites": []
    },
    "Roche": {
        "Faiblesses": ["Eau", "Plante", "Combat", "Sol", "Acier"],
        "Résistances": ["Normal", "Feu", "Poison", "Vol"],
        "Immunites": []
    },
    "Spectre": {
        "Faiblesses": ["Ténèbres"],
        "Résistances": ["Insecte", "Poison"],
        "Immunites": ["Normal", "Combat"]
    },
    "Dragon": {
        "Faiblesses": ["Glace", "Fée", "Dragon"],
        "Résistances": ["Feu", "Eau", "Plante", "Électrique"],
        "Immunites": []
    },
    "Ténèbres": {
        "Faiblesses": ["Combat", "Insecte", "Fée"],
        "Résistances": ["Spectre", "Ténèbres"],
        "Immunites": ["Psy"]
    },
    "Acier": {
        "Faiblesses": ["Feu", "Combat", "Sol"],
        "Résistances": ["Normal", "Plante", "Glace", "Vol", "Roche", "Dragon", "Acier", "Fée"],
        "Immunites": ["Poison"]
    },
    "None": {
        "Faiblesses": [],
        "Résistances": [],
        "Immunites": []
    },
    "Fée": {
        "Faiblesses": ["Poison", "Acier"],
        "Résistances": ["Combat", "Insecte", "Ténèbres"],
        "Immunites": ["Dragon"]
    }
}