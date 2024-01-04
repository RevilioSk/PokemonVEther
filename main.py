from tkinter import *
import os
import Pokemon as P
import time
import random
import pygame
import subprocess



script_dir = os.path.dirname(__file__)
image_dir = os.path.join(script_dir, 'Images')
musique_dir = os.path.join(script_dir, 'Musiques')





####################################
##########  Tkinter Loops ##########
####################################

root = Tk()  
root.title( "Pokémon Éther : Bêta 0.0" )    
canvas = Canvas(root, width = 1024, height = 768)      
canvas.pack()    

background = PhotoImage(file=os.path.join(image_dir,"pokebg.gif"))      
canvas.create_image(0,0, anchor=NW, image=background)    

Title = PhotoImage(file=os.path.join(image_dir,"Title.gif"))      
canvas.create_image(300,50, anchor=NW, image=Title)

ChooseTeam = PhotoImage(file=os.path.join(image_dir,"ChoosePoke.gif"))      
canvas.create_image(335,175, anchor=NW, image=ChooseTeam)


imgEquipe1 = PhotoImage(file=os.path.join(image_dir,"TC1.gif"))
imgEquipe2 = PhotoImage(file=os.path.join(image_dir,"TC2.gif"))
imgEquipe3 = PhotoImage(file=os.path.join(image_dir,"TC3.gif"))
imgEquipe4 = PhotoImage(file=os.path.join(image_dir,"TC4.gif"))      
imageEqp = canvas.create_image(205,290, anchor=NW, image=imgEquipe1)    

ecran=1

EquipeJ1 = P.Equipe(P.VenusaurT1.copy(),P.Mimikyu.copy(),P.Krookodile.copy(),P.Metagross.copy(),P.Salamence.copy(),P.Kabutops.copy())
EquipeJ2 = P.Equipe(P.BlazikenT2.copy(),P.Togekiss.copy(),P.Tyranitar.copy(),P.Metagross.copy(),P.Snorlax.copy(),P.GyaradosT2.copy())
EquipeJ3 = P.Equipe(P.Delphox.copy(),P.Lucario.copy(),P.GardevoirT3.copy(),P.Talonflame.copy(),P.Aurorus.copy(),P.Heliolisk.copy())
EquipeJ4 = P.Equipe(P.Greninja.copy(),P.ZoroarkF1.copy(),P.Lucario.copy(),P.Flygon.copy(),P.Ceruledge.copy(),P.Jolteon.copy())

Pokemon1n1 = P.Charizard.copy()
Pokemon1n2 = P.Torkoal.copy()
Pokemon1n3 = P.Volcarona.copy()
Pokemon1n4 = P.Flareon.copy()
Pokemon1n5 = P.MarowakAlola.copy()
Pokemon1n6 = P.Chandelure.copy()


Pokemon2n1 = P.Raticate.copy()
Pokemon2n2 = P.Furret.copy()
Pokemon2n3 = P.Linoone.copy()
Pokemon2n4 = P.Bibarel.copy()
Pokemon2n5 = P.Watchog.copy()
Pokemon2n6 = P.Diggersby.copy()

Equipe1 = P.Equipe(Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6)
Equipe2 = P.Equipe(Pokemon2n1,Pokemon2n2,Pokemon2n3,Pokemon2n4,Pokemon2n5,Pokemon2n6)

PokemonCombat1 = Pokemon1n1
PokemonCombat2 = Pokemon2n1

numerocombat = 0
nbequipe=9
EquipeD1 = P.Equipe(P.Pidgeot.copy(),P.Fearow.copy(),P.Noctowl.copy(),P.Staraptor.copy(),P.Swellow.copy(),P.Braviary.copy())
EquipeD2 = P.Equipe(P.Butterfree.copy(),P.Beedrill.copy(),P.Scizor.copy(),P.Venomoth.copy(),P.Heracross.copy(),P.Pinsir.copy())
EquipeD3 = P.Equipe(P.Steelix.copy(),P.Golem.copy(),P.Rhyperior.copy(),P.Dugtrio.copy(),P.Aggron.copy(),P.Aerodactyl.copy())
EquipeD4 = P.Equipe(P.Seaking.copy(),P.Kingler.copy(),P.Tentacruel.copy(),P.Starmie.copy(),P.Gyarados.copy(),P.Barraskewda.copy())
EquipeD5 = P.Equipe(P.Ninetales.copy(),P.Arcanine.copy(),P.Magmotar.copy(),P.Camerupt.copy(),P.Darmanitan.copy(),P.Houndoom.copy())
EquipeD6 = P.Equipe(P.Alakazam.copy(),P.Medicham.copy(),P.Reuniclus.copy(),P.Gardevoir.copy(),P.Hypno.copy(),P.Gothitelle.copy())
EquipeD7 = P.Equipe(P.Hitmonchan.copy(),P.Hitmonlee.copy(),P.Hitmontop.copy(),P.Machamp.copy(),P.Throh.copy(),P.Sawk.copy())
EquipeD8 = P.Equipe(P.Magnezone.copy(),P.Ampharos.copy(),P.Electivire.copy(),P.Raichu.copy(),P.Electrode.copy(),P.Rotom.copy())
EquipeD9 = P.Equipe(P.VenusaurPkMn.copy(),P.Feraligatr.copy(),P.BlazikenPkMn.copy(),P.Torterra.copy(),P.Samurott.copy(),P.Delphox.copy())

NiveauDebutant = [EquipeD1,EquipeD2,EquipeD3,EquipeD4,EquipeD5,EquipeD6,EquipeD7,EquipeD8,EquipeD9]


nbPokemon1=6
nbPokemon2=6

fincombat = False

ialevel = "Debutant"

modifatt1 = 1
modifspa1 = 1
modifspdef1 = 1
modifdefe1 = 1
modifvit1 = 1

compteurmodifatt1 = 0
compteurmodifspa1 = 0
compteurmodifspdef1 = 0
compteurmodifdefe1 = 0
compteurmodifvit1 = 0

modifatt2 = 1
modifspa2 = 1
modifspdef2 = 1
modifdefe2 = 1
modifvit2 = 1

compteurmodifatt2 = 0
compteurmodifspa2 = 0
compteurmodifspdef2 = 0
compteurmodifdefe2 = 0
compteurmodifvit2 = 0

modifspaclimat1 = 1
modifspaclimat2 = 1

modifvitclimat1 = 1
modifvitclimat2 = 1

attBloquee = 0
attBloqueeIA = 0
TempsClimat = 0
TypeClimat = "Aucun"

FlashFireAct1=False
FlashFireAct2=False

LightningRodAct1=False
LightningRodAct2=False

FinTour = False
Prio1 = True

attdegel1=False
attdegel2=False

compteurattdgt1=0  #0 = pas ini      1 = statut     2 = Degat
compteurattdgt2=0

compteursash1 = 0
compteursash2 = 0

numeroatt = 0
numeroattbis = 1
numeroechoue1 = 0
numeroechoue2 = 0

dgtpdttour1 = 100
dgtpdttour2 = 100

protect1 = False
protect2 = False

imun1=False
imun2=False

Poke1Mort = False
Poke2Mort = False

Poke1MortCeTour = False
Poke2MortCeTour = False

chgmpkmn1mort=False

chgmpkmn1combat = False
chgmpkmn2combat = False

fantomasque1 = 1
fantomasque2 = 1

skipintro=False
menu=3
numequipe=0

colorpv1 = '#15FC0E'
colorpv2 = '#15FC0E'
pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100



RectMenu = canvas.create_rectangle(600, 500, 1020, 764,width=3,fill="#FFFFFF",outline="#6F0000")
RectTexte = canvas.create_rectangle(6, 6, 400, 100,fill='#FFFFFF')

RectAttaque = canvas.create_rectangle(605, 510, 805, 710,outline='#0E4BFC',tag="Attaque")
RectPokemon = canvas.create_rectangle(815, 510, 1015, 710,outline='#0E4BFC',tag="Pokemon")
TexteAttaque = canvas.create_text(655,612, anchor =W, text ="Attaque", fill ="blue", font="Arial 20")
TextePokemon = canvas.create_text(865,612, anchor =W, text ="Pokemon", fill ="blue", font="Arial 20")

canphrase = canvas.create_text(8,50, anchor =W, text ="", fill ="black", font="Arial 15")

RectangleAttaque1 = canvas.create_rectangle(605, 510, 805, 605,outline='#000000')
RectangleAttaque2 = canvas.create_rectangle(815, 510, 1015, 605,outline='#000')
RectangleAttaque3 = canvas.create_rectangle(605, 615, 805, 710,outline='#000')
RectangleAttaque4 = canvas.create_rectangle(815, 615, 1015, 710,outline='#000')
TexteAttaque1 = canvas.create_text(606,557, anchor =W, text = PokemonCombat1.a1.nom, fill = PokemonCombat1.a1.color, font="Arial 20")
TexteAttaque2 = canvas.create_text(816,557, anchor =W, text = PokemonCombat1.a2.nom, fill = PokemonCombat1.a2.color, font="Arial 20")
TexteAttaque3 = canvas.create_text(606,665, anchor =W, text = PokemonCombat1.a3.nom, fill = PokemonCombat1.a3.color, font="Arial 20")
TexteAttaque4 = canvas.create_text(816,665, anchor =W, text = PokemonCombat1.a4.nom, fill = PokemonCombat1.a4.color, font="Arial 20")

texte_attaque1_pp = str(PokemonCombat1.a1.pp)+"/"+str(PokemonCombat1.a1.ppmax)
TexteAttaque1PP = canvas.create_text(745,594, anchor =W, text=texte_attaque1_pp, fill="black", font="Arial 17")
texte_attaque2_pp = str(PokemonCombat1.a2.pp)+"/"+str(PokemonCombat1.a2.ppmax)
TexteAttaque2PP = canvas.create_text(955,594, anchor =W, text=texte_attaque2_pp, fill="black", font="Arial 17")
texte_attaque3_pp = str(PokemonCombat1.a3.pp)+"/"+str(PokemonCombat1.a3.ppmax)
TexteAttaque3PP = canvas.create_text(745,694, anchor =W, text=texte_attaque3_pp, fill="black", font="Arial 17")
texte_attaque4_pp = str(PokemonCombat1.a4.pp)+"/"+str(PokemonCombat1.a4.ppmax)
TexteAttaque4PP = canvas.create_text(955,694, anchor =W, text=texte_attaque4_pp, fill="black", font="Arial 17")



RectanglePokemon1 = canvas.create_rectangle(605, 510, 805, 565,outline='#000000')
RectanglePokemon2 = canvas.create_rectangle(815, 510, 1015, 565,outline='#000')
RectanglePokemon3 = canvas.create_rectangle(605, 575, 805, 630,outline='#000')
RectanglePokemon4 = canvas.create_rectangle(815, 575, 1015, 630,outline='#000')
RectanglePokemon5 = canvas.create_rectangle(705, 640, 905, 700,outline='#000')

TextePokemon1 = canvas.create_text(606,540, anchor =W, text = Pokemon1n2.nom, fill = "blue", font="Arial 20")
TextePokemon2 = canvas.create_text(816,540, anchor =W, text = Pokemon1n3.nom, fill = "blue", font="Arial 20")
TextePokemon3 = canvas.create_text(606,605, anchor =W, text = Pokemon1n4.nom, fill = "blue", font="Arial 20")
TextePokemon4 = canvas.create_text(816,605, anchor =W, text = Pokemon1n5.nom, fill = "blue", font="Arial 20")
TextePokemon5 = canvas.create_text(706,670, anchor =W, text = Pokemon1n6.nom, fill = "blue", font="Arial 20")


RectRetour = canvas.create_rectangle(665, 720, 965, 754,outline='#0E4BFC',tag="Retour")
TexteRetour = canvas.create_text(770,737, anchor =W, text ="Retour", fill ="blue", font="Arial 20")
#RectDialogue = canvas.create_rectangle(385, 85, 395, 95,outline='#15FC0E',tag="Dialogue")  #Canvas dialogue
Valide = False



canvas.itemconfigure(RectAttaque, state='hidden')
canvas.itemconfigure(RectPokemon, state='hidden')

canvas.itemconfigure(TexteAttaque, state='hidden')
canvas.itemconfigure(TextePokemon, state='hidden')

canvas.itemconfigure(RectMenu, state='hidden')
canvas.itemconfigure(RectTexte, state='hidden')

canvas.itemconfigure(RectangleAttaque1, state='hidden')
canvas.itemconfigure(RectangleAttaque2, state='hidden')
canvas.itemconfigure(RectangleAttaque3, state='hidden')
canvas.itemconfigure(RectangleAttaque4, state='hidden')

canvas.itemconfigure(TexteAttaque1, state='hidden')
canvas.itemconfigure(TexteAttaque2, state='hidden')
canvas.itemconfigure(TexteAttaque3, state='hidden')
canvas.itemconfigure(TexteAttaque4, state='hidden')

canvas.itemconfigure(RectRetour, state='hidden')
canvas.itemconfigure(TexteRetour, state='hidden')

canvas.itemconfigure(RectanglePokemon1, state='hidden')
canvas.itemconfigure(RectanglePokemon2, state='hidden')
canvas.itemconfigure(RectanglePokemon3, state='hidden')
canvas.itemconfigure(RectanglePokemon4, state='hidden')
canvas.itemconfigure(RectanglePokemon5, state='hidden')

canvas.itemconfigure(TexteAttaque1PP, state='hidden')
canvas.itemconfigure(TexteAttaque2PP, state='hidden')
canvas.itemconfigure(TexteAttaque3PP, state='hidden')
canvas.itemconfigure(TexteAttaque4PP, state='hidden')

canvas.itemconfigure(TextePokemon1, state='hidden')
canvas.itemconfigure(TextePokemon2, state='hidden')
canvas.itemconfigure(TextePokemon3, state='hidden')
canvas.itemconfigure(TextePokemon4, state='hidden')
canvas.itemconfigure(TextePokemon5, state='hidden')

pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100



def att1sec():
    time.sleep(0.01)



#################Affichage###############

#phrase = "Mais cela échoue !"

def afficherTexte1(phrase):
    global menu
    if menu !=-1:
        menu = -1
        print("A")
        resetAffMenu()
        canvas.itemconfigure(canphrase,text="")
        delay = 10
        global Valide
        for i in range (len(phrase)+1):
            s = phrase[:i]
            canvas.itemconfigure(canphrase,text=s)
            canvas.update()
            canvas.after(delay)
            delay+=1
            
        root.after(delay,att1sec)


def afficherTexte2(phrase):
    global menu
    canvas.itemconfigure(canphrase,text="")
    delay = 40
    global Valide
    for i in range (len(phrase)+1):
        s = phrase[:i]
        canvas.itemconfigure(canphrase,text=s)
        canvas.update()
        canvas.after(delay)
        
    root.after(delay,att1sec)




def resetAffMenu():
    canvas.itemconfigure(RectAttaque, state='normal', outline='red')
    canvas.itemconfigure(TexteAttaque, state='normal', fill='red')
    canvas.itemconfigure(RectPokemon, state='normal', outline='red')
    canvas.itemconfigure(TextePokemon, state='normal', fill='red')

    canvas.itemconfigure(canphrase,text="")
    canvas.itemconfigure(RectangleAttaque1, state='hidden')
    canvas.itemconfigure(RectangleAttaque2, state='hidden')
    canvas.itemconfigure(RectangleAttaque3, state='hidden')
    canvas.itemconfigure(RectangleAttaque4, state='hidden')

    canvas.itemconfigure(TexteAttaque1, state='hidden')
    canvas.itemconfigure(TexteAttaque2, state='hidden')
    canvas.itemconfigure(TexteAttaque3, state='hidden')
    canvas.itemconfigure(TexteAttaque4, state='hidden')

    canvas.itemconfigure(TexteAttaque1PP, state='hidden')
    canvas.itemconfigure(TexteAttaque2PP, state='hidden')
    canvas.itemconfigure(TexteAttaque3PP, state='hidden')
    canvas.itemconfigure(TexteAttaque4PP, state='hidden')

    canvas.itemconfigure(RectanglePokemon1, state='hidden')
    canvas.itemconfigure(RectanglePokemon2, state='hidden')
    canvas.itemconfigure(RectanglePokemon3, state='hidden')
    canvas.itemconfigure(RectanglePokemon4, state='hidden')
    canvas.itemconfigure(RectanglePokemon5, state='hidden')

    canvas.itemconfigure(TextePokemon1, state='hidden')
    canvas.itemconfigure(TextePokemon2, state='hidden')
    canvas.itemconfigure(TextePokemon3, state='hidden')
    canvas.itemconfigure(TextePokemon4, state='hidden')
    canvas.itemconfigure(TextePokemon5, state='hidden')

    canvas.itemconfigure(RectRetour, state='hidden')
    canvas.itemconfigure(TexteRetour, state='hidden')




def resetMenu():
    global menu,Prio1
    menu=0
    
    print("B")
    resetAffMenu()
    canvas.itemconfigure(canphrase,text="")
    canvas.itemconfigure(RectAttaque, state='normal', outline='blue')
    canvas.itemconfigure(TexteAttaque, state='normal', fill='blue')
    canvas.itemconfigure(RectPokemon, state='normal', outline='blue')
    canvas.itemconfigure(TextePokemon, state='normal', fill='blue')



def ChangerTexturePokemon():
    if PokemonCombat1==Pokemon1n1:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n1)
    elif PokemonCombat1==Pokemon1n2:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n2)
    elif PokemonCombat1==Pokemon1n3:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n3)
    elif PokemonCombat1==Pokemon1n4:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n4)
    elif PokemonCombat1==Pokemon1n5:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n5)
    elif PokemonCombat1==Pokemon1n6:
        canvas.itemconfigure(imgpkmn1,state='normal',image=pkmn1n6)
    canvas.update()


def AffChangerPokemon():
    global TextePokemon1
    canvas.itemconfigure(TextePokemon1, text=Equipe1.Slot2.nom)
    canvas.itemconfigure(TextePokemon2, text=Equipe1.Slot3.nom)
    canvas.itemconfigure(TextePokemon3, text=Equipe1.Slot4.nom)
    canvas.itemconfigure(TextePokemon4, text=Equipe1.Slot5.nom)
    canvas.itemconfigure(TextePokemon5, text=Equipe1.Slot6.nom)
    

    canvas.itemconfigure(RectanglePokemon1, state='normal')
    canvas.itemconfigure(RectanglePokemon2, state='normal')
    canvas.itemconfigure(RectanglePokemon3, state='normal')
    canvas.itemconfigure(RectanglePokemon4, state='normal')
    canvas.itemconfigure(RectanglePokemon5, state='normal')

    canvas.itemconfigure(TextePokemon1, state='normal')
    canvas.itemconfigure(TextePokemon2, state='normal')
    canvas.itemconfigure(TextePokemon3, state='normal')
    canvas.itemconfigure(TextePokemon4, state='normal')
    canvas.itemconfigure(TextePokemon5, state='normal')




def Victoire1():
    global backgroundpst,Commentateur,TypeClimat

    TypeClimat = "Aucun"

    

    backgroundpst = PhotoImage(file=os.path.join(image_dir,"presentation.gif"))      
    canvas.create_image(0,0, anchor=NW, image=backgroundpst)

    Commentateur = PhotoImage(file=os.path.join(image_dir,"commentateur.gif"))      
    canvas.create_image(380,200, anchor=NW, image=Commentateur)

    

    pygame.mixer.stop()
    playMusiqueVictoireFinale()

    canvas.tag_raise(RectTexte)
    canvas.tag_raise(canphrase)
    canvas.itemconfigure(RectTexte,state='normal')

    afficherTexte2("Félicitation à notre challenger"+'\n'+" qui vient de remporter le tournoi !    ")
    afficherTexte2("Nous nous retrouverons bientôt"+'\n'+"pour de nouveaux combats !    ")
    canvas.itemconfigure(Commentateur,state='hidden')

def Victoire2():
    global menu
    print("C")
    resetAffMenu()
    screenlose = PhotoImage(file=os.path.join(image_dir,"defaite.gif"))
    canvas.create_image(0,0, anchor=NW, image=screenlose)
    menu=15




###########Entrée Pokemon####################


def EntreePokemon1():
    global TempsClimat,modifvitclimat1,modifspaclimat1,canimgclimat,Poke1Mort,TypeClimat,FlashFireAct1,attBloquee,poisongrv1,LightningRodAct1,dgtpdttour1
    global modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1,compteurmodifatt1,compteurmodifdefe1,compteurmodifspa1,compteurmodifspdef1,compteurmodifvit1
    global compteurmodifatt2
    global pdr1,picots1,pictoxic1

    attBloquee = 0
    dgtpdttour1 = 100
    Poke1Mort = False
    FlashFireAct1=False
    LightningRodAct1 = False

    if PokemonCombat1.name=="Greninja":
        PokemonCombat1.type1="Eau"
        PokemonCombat1.type2="Ténèbres"

    modifatt1 = 1
    modifspa1 = 1
    modifspdef1 = 1
    modifdefe1 = 1
    modifvit1 = 1

    compteurmodifatt1 = 0
    compteurmodifspa1 = 0
    compteurmodifspdef1 = 0
    compteurmodifdefe1 = 0
    compteurmodifvit1 = 0

    if PokemonCombat1.talent.name=="Frisk":
        afficherTexte2(PokemonCombat1.nom+" fouille "+PokemonCombat2.objet.nom+"     ")
    
    if PokemonCombat1.talent.name=="Intimidate" and PokemonCombat2.talent.name!="Inner Focus":
        afficherTexte2(PokemonCombat1.talent.nom+" de "+PokemonCombat1.nom+" "+'\n'+" baisse l'attaque adverse     ")
        compteurmodifatt2-=1

    if PokemonCombat1.objet.name=="Flame Orb":
        PokemonCombat1.statut="Brûlé"
        if PokemonCombat1.talent.name!="Guts":
            modifatt1 = modifatt1/2
        canvas.itemconfig(statutpoke1, text ="Brûlé", fill ="#FC610E")
        afficherTexte2(PokemonCombat1.nom+" devient Brûlé     ")


    canvas.itemconfig(TexteAttaque1,text = PokemonCombat1.a1.nom, fill = PokemonCombat1.a1.color, font="Arial 20")
    canvas.itemconfig(TexteAttaque2,text = PokemonCombat1.a2.nom, fill = PokemonCombat1.a2.color, font="Arial 20")
    canvas.itemconfig(TexteAttaque3,text = PokemonCombat1.a3.nom, fill = PokemonCombat1.a3.color, font="Arial 20")
    canvas.itemconfig(TexteAttaque4,text = PokemonCombat1.a4.nom, fill = PokemonCombat1.a4.color, font="Arial 20")

    texte_attaque1_pp = str(PokemonCombat1.a1.pp)+"/"+str(PokemonCombat1.a1.ppmax)
    canvas.itemconfig(TexteAttaque1PP, text=texte_attaque1_pp)
    texte_attaque2_pp = str(PokemonCombat1.a2.pp)+"/"+str(PokemonCombat1.a2.ppmax)
    canvas.itemconfig(TexteAttaque2PP, text=texte_attaque2_pp)
    texte_attaque3_pp = str(PokemonCombat1.a3.pp)+"/"+str(PokemonCombat1.a3.ppmax)
    canvas.itemconfig(TexteAttaque3PP, text=texte_attaque3_pp)
    texte_attaque4_pp = str(PokemonCombat1.a4.pp)+"/"+str(PokemonCombat1.a4.ppmax)
    canvas.itemconfig(TexteAttaque4PP, text=texte_attaque4_pp)

    if PokemonCombat1==Pokemon1n1:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n1)
    elif PokemonCombat1==Pokemon1n2:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n2)
    elif PokemonCombat1==Pokemon1n3:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n3)
    elif PokemonCombat1==Pokemon1n4:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n4)
    elif PokemonCombat1==Pokemon1n5:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n5)
    elif PokemonCombat1==Pokemon1n6:
        canvas.itemconfigure(imgpkmn1,image=pkmn1n6)



    if PokemonCombat1.talent.name=="Quick Feet" and PokemonCombat1.statut!="None":
        compteurmodifvit1+=1

    if PokemonCombat1.statut=="Gravement Empoisonné":
        poisongrv1=1/16



    if PokemonCombat1.talent.name=="Drizzle":
        TypeClimat="Rain"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgrain)
        if PokemonCombat1.objet.name=="Damp Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat1.talent.name=="Drought":
        TypeClimat="Sun"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgsun)
        if PokemonCombat1.objet.name=="Heat Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat1.talent.name=="Snow Warning":
        TypeClimat="HailStorm"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imghail)
        if PokemonCombat1.objet.name=="Icy Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat1.talent.name=="Sand Stream":
        TypeClimat="SandStorm"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgsand)
        if PokemonCombat1.objet.name=="Smooth Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    
    if TypeClimat=="Rain" and PokemonCombat1.talent.name=="Swift Swim":
        modifvitclimat1 = PokemonCombat1.talent.vitmodif
    if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Chlorophyll":
        modifvitclimat1 = PokemonCombat1.talent.vitmodif
    if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Solar Power":
        modifspaclimat1 = PokemonCombat1.talent.spamodif
    
def EntreePokemon2():
    global TempsClimat,modifvitclimat2,modifspaclimat2,TypeClimat,canimgclimat,Poke2Mort,FlashFireAct2,attBloqueeIA,poisongrv2,LightningRodAct2,dgtpdttour2
    global modifatt2,modifdefe2,modifspa2,modifspdef2,modifvit2,compteurmodifatt2,compteurmodifdefe2,compteurmodifspa2,compteurmodifspdef2,compteurmodifvit2
    global pdr2,picots2,pictoxic2
    global compteurmodifatt1

    attBloqueeIA = 0
    dgtpdttour2 = 100

    Poke2Mort = False
    FlashFireAct2=False
    LightningRodAct2 = False


    if PokemonCombat2.name=="Greninja":
        PokemonCombat2.type1="Eau"
        PokemonCombat2.type2="Ténèbres"


    modifatt2 = 1
    modifspa2 = 1
    modifspdef2 = 1
    modifdefe2 = 1
    modifvit2 = 1

    compteurmodifatt2 = 0
    compteurmodifspa2 = 0
    compteurmodifspdef2 = 0
    compteurmodifdefe2 = 0
    compteurmodifvit2 = 0


    if PokemonCombat2.objet.name=="Flame Orb":
        PokemonCombat2.statut="Brûlé"
        if PokemonCombat2.talent.name!="Guts":
            modifatt2 = modifatt2/2
        canvas.itemconfig(statutpoke2, text ="Brûlé", fill ="#FC610E")
        afficherTexte2(PokemonCombat2.nom+" devient Brûlé     ")



    if PokemonCombat2.talent.name=="Frisk":
        afficherTexte2(PokemonCombat2.nom+" fouille "+PokemonCombat1.objet.nom+"     ")
    
    if PokemonCombat2.talent.name=="Intimidate" and PokemonCombat1.talent.name!="Inner Focus":
        afficherTexte2(PokemonCombat2.talent.nom+" de "+PokemonCombat2.nom+" "+'\n'+" baisse l'attaque adverse     ")
        compteurmodifatt1-=1



    if PokemonCombat2.talent.name=="Quick Feet" and PokemonCombat2.statut!="None":
        compteurmodifvit2+=1

    if PokemonCombat2.statut=="Gravement Empoisonné":
        poisongrv2=1/16

    if PokemonCombat2.talent.name=="Drizzle":
        TypeClimat="Rain"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgrain)
        if PokemonCombat2.objet.name=="Damp Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat2.talent.name=="Drought":
        TypeClimat="Sun"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgsun)
        if PokemonCombat2.objet.name=="Heat Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat2.talent.name=="Snow Warning":
        TypeClimat="HailStorm"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imghail)
        if PokemonCombat2.objet.name=="Icy Rock":
            TempsClimat=8
        else:
            TempsClimat=5
    elif PokemonCombat2.talent.name=="Sand Stream":
        TypeClimat="SandStorm"
        canvas.delete(canimgclimat)
        canimgclimat = canvas.create_image(930,10, anchor=NW, image=imgsand)
        if PokemonCombat2.objet.name=="Smooth Rock":
            TempsClimat=8
        else:
            TempsClimat=5

    if TypeClimat=="Rain" and PokemonCombat2.talent.name=="Swift Swim":
        modifvitclimat2 = PokemonCombat2.talent.vitmodif
    if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Chlorophyll":
        modifvitclimat2 = PokemonCombat2.talent.vitmodif
    if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Solar Power":
        modifspaclimat2 = PokemonCombat2.talent.spamodif


############Calcul###############




def calcFaiblesse(Att,Pokemon1,Pokemon2):
    type_attaque = Att.type
    compteurtinted = 0

    multipl_type = 1
    if type_attaque in P.types[Pokemon2.type1]["Faiblesses"]:
        multipl_type *= 2
    
    elif type_attaque in P.types[Pokemon2.type1]["Résistances"]:
        if compteurtinted<1 and Pokemon1.talent.name=="Tinted Lens":
            compteurtinted += 1
        else: multipl_type /= 2

    if type_attaque in P.types[Pokemon2.type2]["Faiblesses"]:
        multipl_type *= 2

    elif type_attaque in P.types[Pokemon2.type2]["Résistances"]:
        if compteurtinted<1 and Pokemon1.talent.name=="Tinted Lens":
            compteurtinted += 1
        else: multipl_type /= 2

    if Pokemon2.talent.name=="Thick Fat" and Att.type=="Feu" or Att.type=="Glace":
        multipl_type /= 2

    elif type_attaque in P.types[Pokemon2.type1]["Immunites"] or type_attaque in P.types[Pokemon2.type2]["Immunites"]:
        multipl_type = 0
    return multipl_type


def calcdamage(Att,Pokemon1,Pokemon2):
    global FlashFireAct1,LightningRodAct1,compteurattdgt1,numeroechoue1,fantomasque1,compteurmodifvit1,compteurmodifdefe1,modifdefe1,modifvit1,protect1

    global FlashFireAct2,LightningRodAct2,compteurattdgt2,numeroechoue2,DgtAtt,fantomasque2,compteurmodifvit2,compteurmodifdefe2,modifdefe2,modifvit2,protect2

    if Pokemon1.talent.name=="Protean":
        afficherTexte2(Pokemon1.nom+" devient de type "+Att.type+"     ")
        Pokemon1.type1=Att.type
        Pokemon1.type2="None"

    DgtAtt = Att.puiss*Pokemon1.objet.capamodif

    if Att.name=="Protect":
        if Pokemon1==PokemonCombat1:
            protect1=True
        if Pokemon2==PokemonCombat2:
            protect2=True

    if Att.name not in P.PhysiqueNonDirecte or Att.name in P.SpecialDirecte:
        if Pokemon2.talent=="Flame Body":
            if random.randint(1,100)<30:
                Pokemon1.statut="Brûlé"
                AffStatut1()
                AffStatut2()

        if Pokemon2.talent=="Static":
            if random.randint(1,100)<30:
                Pokemon1.statut="Paralysé"
                AffStatut1()
                AffStatut2()

        if Pokemon2.talent=="Weak Armor":
            if Pokemon2==PokemonCombat1:
                compteurmodifvit1+=2
                compteurmodifdefe1-=1
            if Pokemon2==PokemonCombat2:
                compteurmodifvit2+=2
                compteurmodifdefe2-=1

            if compteurmodifdefe2<6:
                compteurmodifdefe2=6
            if compteurmodifdefe1<6:
                compteurmodifdefe1=6
            
            if compteurmodifvit1>6:
                compteurmodifvit1=6

            if compteurmodifvit2>6:
                compteurmodifvit2=6

            modifdefe1 = P.modifstats[compteurmodifdefe1]
            modifdefe2 = P.modifstats[compteurmodifdefe2]
            modifvit1 = P.modifstats[compteurmodifvit1]
            modifvit2 = P.modifstats[compteurmodifvit2]

            
    if Att.type=="Normal" and Pokemon1.talent.name=="Refrigerate":
        Att.type=="Glace"
        DgtAtt*=1.2

    if Att.name=="Gyro Ball":
        DgtAtt = (25*(Pokemon2.vit/Pokemon1.vit))*Pokemon1.objet.capamodif
    

    if Pokemon1.objet.name=="Thick Club":
        if Pokemon1.name!="Marowak" or Pokemon1.name!="Marowak-Alola":
            Pokemon1.objet.attmodif=1


    if Att.name=="Knock Off" and Pokemon2.objet.nom!="None":
        DgtAtt=DgtAtt*1.5
        afficherTexte2(Pokemon1.nom+" fait tomber "+'\n'+Pokemon2.objet.nom+" de "+Pokemon2.nom)
        Pokemon2.objet=P.NoItem.copy()

    if Att.name=="Hex" and Pokemon2.statut in P.Statuts:
        DgtAtt*=2

    if Pokemon1.talent.name=="Strong Jaw" and Att.name in P.CapaMorsure:
        DgtAtt=DgtAtt*1.5

    if Pokemon1.talent.name=="Iron Kick" and Att.name in P.Kick:
        DgtAtt=DgtAtt*1.3

    if Pokemon1.talent.name=="Iron Punch" and Att.name in P.Punch:
        DgtAtt=DgtAtt*1.3

    if Pokemon1.talent.name=="Technician" and Att.puiss<=60:
        DgtAtt=DgtAtt*1.5

    if (Pokemon1.talent.name=="Analytic" and Pokemon1==PokemonCombat1 and Prio1==False) or (Pokemon1.talent.name=="Analytic" and Pokemon1==PokemonCombat2 and Prio1==True):
        DgtAtt=DgtAtt*1.3
        print("Analytic")

    if Pokemon1 == PokemonCombat1 and FlashFireAct1==True:
        if Att.type=="Feu":
            DgtAtt=DgtAtt*1.5
    if Pokemon1 == PokemonCombat2 and FlashFireAct2==True:
        if Att.type=="Feu":
            DgtAtt=DgtAtt*1.5

    if Pokemon1 == PokemonCombat1 and LightningRodAct1==True:
        if Att.type=="Électrique":
            DgtAtt=DgtAtt*1.5
    if Pokemon1 == PokemonCombat2 and LightningRodAct2==True:
        if Att.type=="Électrique":
            DgtAtt=DgtAtt*1.5

    if Pokemon1.talent.name=="Torrent" and Att.type=="Eau" and Pokemon1.pv<=(1/3)*Pokemon1.pvmax:
        DgtAtt=DgtAtt*1.5
    if Pokemon1.talent.name=="Overgrow" and Att.type=="Plante" and Pokemon1.pv<=(1/3)*Pokemon1.pvmax:
        DgtAtt=DgtAtt*1.5
    if Pokemon1.talent.name=="Blaze" and Att.type=="Feu" and Pokemon1.pv<=(1/3)*Pokemon1.pvmax:
        DgtAtt=DgtAtt*1.5
    if Pokemon1.talent.name=="Swarm" and Att.type=="Insecte" and Pokemon1.pv<=(1/3)*Pokemon1.pvmax:
        DgtAtt=DgtAtt*1.5

    if Pokemon1.talent.name=="Sheer Force" and Att.effet.nom!="NoOne":
        DgtAtt=DgtAtt*1.3

    if TypeClimat=="Sun":
        if Att.type=="Feu":
            DgtAtt=DgtAtt*1.5
        elif Att.type=="Eau":
            DgtAtt=DgtAtt*0.5

    if TypeClimat=="Rain":
        if Att.type=="Feu":
            DgtAtt=DgtAtt*0.5
        elif Att.type=="Eau":
            DgtAtt=DgtAtt*1.5

    if (Pokemon1.type1==Att.type or Pokemon1.type2 == Att.type):
        if Pokemon1.talent.name=="Adaptability":
            DgtAtt = DgtAtt*2
        else:
            DgtAtt = DgtAtt*1.5
    eff = calcFaiblesse(Att,Pokemon1,Pokemon2)
    DgtAtt = DgtAtt * eff
    
    if Pokemon1.talent.name == "Compound Eyes":
        preciatt = Att.preci*1.33
    else:
        preciatt = Att.preci

    global attaquelancee
    attaquelancee = False

    if random.randint(1,100)<=preciatt:
        attaquelancee = True
        if Pokemon1==PokemonCombat1:

            if Att.cat == 0:
                dmg=0
                compteurattdgt1=1

            elif Att.cat == 1:
                compteurattdgt1=2

            elif Att.cat == 2:
                compteurattdgt1=2

            if Att.cat == 1 and TypeClimat=="Aucun":
                if Pokemon1.talent.name=="Guts" and Pokemon1.statut in P.Statuts:
                    dmg = ((42*(Pokemon1.att*2)*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe2*50))
                else:
                    dmg = ((42*Pokemon1.att*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe2*50))
            elif Att.cat == 1 and TypeClimat!="Aucun":
                if Pokemon1.talent.name=="Guts" and Pokemon1.statut in P.Statuts:
                    dmg = ((42*(Pokemon1.att*2)*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.spdef*modifspdef1*50))
                else:
                    dmg = ((42*Pokemon1.att*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.spdef*modifspdef1*50))

            elif Att.cat == 2 and TypeClimat=="Aucun":
                dmg = ((42*Pokemon1.spa*modifspa1*Pokemon1.objet.spamodif*DgtAtt)/(Pokemon2.spdef*modifspdef2*50))
            elif Att.cat == 2 and TypeClimat!="Aucun":
                dmg = ((42*Pokemon1.spa*modifspa1*Pokemon1.objet.spamodif*modifspaclimat1*DgtAtt)/(Pokemon2.defe*modifdefe2*50))

            elif Att.name=="Body Press":
                dmg = ((42*Pokemon1.defe*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe2*50))

            elif Att.name=="Darkest Lariat":
                dmg = ((42*Pokemon1.defe*modifatt1*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*50))

            if Pokemon2.talent.name=="Disguise" and fantomasque2==1:
                fantomasque2 = 0
                dmg = 0

        elif Pokemon1==PokemonCombat2:
            if Att.cat == 0:
                dmg=0
                compteurattdgt2=1

            elif Att.cat == 1:
                compteurattdgt2=2

            elif Att.cat == 2:
                compteurattdgt2=2

            if Att.cat == 1 and TypeClimat=="Aucun":
                if Pokemon1.talent.name=="Guts" and Pokemon1.statut in P.Statuts:
                    dmg = ((42*(Pokemon1.att*2)*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe1*50))
                else: 
                    dmg = ((42*Pokemon1.att*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe1*50))
            elif Att.cat == 1 and TypeClimat!="Aucun":
                if Pokemon1.talent.name=="Guts" and Pokemon1.statut in P.Statuts:
                    dmg = ((42*(Pokemon1.att*2)*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe1*50))
                else:
                    dmg = ((42*Pokemon1.att*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe1*50))

            elif Att.cat == 2 and TypeClimat=="Aucun":
                dmg = ((42*Pokemon1.spa*modifspa2*Pokemon1.objet.spamodif*DgtAtt)/(Pokemon2.spdef*modifspdef1*50))
            elif Att.cat == 2 and TypeClimat!="Aucun":
                dmg = ((42*Pokemon1.spa*modifspa2*Pokemon1.objet.spamodif*modifspaclimat2*DgtAtt)/(Pokemon2.spdef*modifspdef1*50))

            elif Att.name=="Body Press":
                dmg = ((42*Pokemon1.defe*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*modifdefe1*50))

            elif Att.name=="Darkest Lariat":
                dmg = ((42*Pokemon1.defe*modifatt2*Pokemon1.objet.attmodif*DgtAtt)/(Pokemon2.defe*50))

            if Pokemon2.talent.name=="Disguise" and fantomasque1==1:
                fantomasque1 = 0
                dmg = 0


    if Att.type=="Feu" and Pokemon2.talent.name=="Flash Fire":
        if Pokemon2 == PokemonCombat1 and not FlashFireAct1:
            FlashFireAct1=True

        if Pokemon2 == PokemonCombat2 and not FlashFireAct2:
            FlashFireAct2=True
        afficherTexte2(Pokemon2.talent.nom+" l'immunise à "+Att.nom)
        dmg=0

    if Att.type=="Électrique" and Pokemon2.talent.name=="Lightning Rod":
        if Pokemon2 == PokemonCombat1 and not LightningRodAct1:
            LightningRodAct1=True

        if Pokemon2 == PokemonCombat2 and not LightningRodAct2:
            LightningRodAct2=True
        afficherTexte2(Pokemon2.talent.nom+" l'immunise à "+Att.nom)
        dmg=0
    
    if Att.type=="Électrique" and Pokemon2.talent.name=="Motor Drive":
        dmg=0
        afficherTexte2(Pokemon2.talent.nom+" l'immunise à "+Att.nom)
        if Pokemon2==PokemonCombat2:
            compteurmodifvit2+=1
        elif Pokemon2==PokemonCombat1:
            compteurmodifvit1+=1

    if Att.type=="Sol" and Pokemon2.talent.name=="Levitate":
        dmg=0
        afficherTexte2(Pokemon2.talent.nom+" l'immunise à "+Att.nom)
            
    if attaquelancee == False:
        dmg = 0
        numeroechoue2 = 1
        numeroechoue1 = 1
        compteurattdgt2=0
        compteurattdgt1=0
    return dmg



def FinDuTour():
    global ft1,ft2,FinTour,TempsClimat,TypeClimat,poisongrv1,poisongrv2,modifspaclimat2,modifspaclimat1,modifvitclimat1,modifvitclimat2
    if fincombat:
        print("1")
        resetMenu()
    else:
        TempsClimat-=1
        if TempsClimat==0:
            TypeClimat="Aucun"
            canvas.delete(canimgclimat)
            modifvitclimat1 = 1
            modifvitclimat2 = 1
            modifspaclimat1 = 1
            modifspaclimat2 = 1
        FinTour=True

        ft2=PokemonCombat2.pv
        ft1=PokemonCombat1.pv

        if PokemonCombat2.statut=="Gravement Empoisonné":
            ft2=PokemonCombat2.pv-(poisongrv2*PokemonCombat2.pvmax)
            poisongrv2=poisongrv2+(1/16)
        if PokemonCombat1.statut=="Gravement Empoisonné":
            ft1=PokemonCombat1.pv-(poisongrv1*PokemonCombat1.pvmax)
            poisongrv1=poisongrv1+(1/16)


        if PokemonCombat2.statut=="Empoisonné":
            ft2=PokemonCombat2.pv-((1/16)*PokemonCombat2.pvmax)
        if PokemonCombat1.statut=="Empoisonné":
            ft1=PokemonCombat1.pv-((1/8)*PokemonCombat1.pvmax)

        if PokemonCombat2.statut=="Brûlé":
            ft2=PokemonCombat2.pv-((1/16)*PokemonCombat2.pvmax)
        if PokemonCombat1.statut=="Brûlé":
            ft1=PokemonCombat1.pv-((1/16)*PokemonCombat1.pvmax)       


        if PokemonCombat1.talent.name=="Magic Guard":
            ft1=PokemonCombat1.pv

        if PokemonCombat2.talent.name=="Magic Guard":
            ft2=PokemonCombat2.pv

        if Prio1:
            if PokemonCombat2.statut=="Brûlé" and PokemonCombat2.talent.name!="Magic Guard":
                afficherTexte2(PokemonCombat2.nom+" subit des dégats de la brûlure     ")
            if (PokemonCombat2.statut=="Empoisonné" or PokemonCombat2.statut=="Gravement Empoisonné") and PokemonCombat2.talent.name!="Magic Guard":
                afficherTexte2(PokemonCombat2.nom+" subit des dégats du poison     ")
            PVPkmn2FT()
        else:
            if PokemonCombat1.statut=="Brûlé" and PokemonCombat1.talent.name!="Magic Guard":
                afficherTexte2(PokemonCombat1.nom+" subit des dégats de la brûlure     ")
            if (PokemonCombat1.statut=="Empoisonné" or PokemonCombat1.statut=="Gravement Empoisonné") and PokemonCombat1.talent.name!="Magic Guard":
                afficherTexte2(PokemonCombat1.nom+" subit des dégats du poison     ")
            PVPkmn1FT()


def DgtClimat():
    global ft1,ft2
    if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Solar Power":
        ft1=PokemonCombat1.pv-PokemonCombat1.pv*0.125
    else: ft1=PokemonCombat1.pv
    if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Solar Power":
        ft2=PokemonCombat2.pv-PokemonCombat2.pv*0.125
    else: ft2=PokemonCombat2.pv

    if PokemonCombat1.talent.name=="Magic Guard":
        ft1=PokemonCombat1.pv

    if PokemonCombat2.talent.name=="Magic Guard":
        ft2=PokemonCombat2.pv

    if Prio1:
        if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Solar Power":
            afficherTexte2(PokemonCombat2.talent.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
        PVPkmn2CD()
    else:
        if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Solar Power":
            afficherTexte2(PokemonCombat1.talent.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
        PVPkmn1CD()



def DgtObj():
    global ft1,ft2

    if PokemonCombat2.objet.name=="Life Orb" and compteurattdgt2==2 and dgtpdttour2<100:
        ft2=PokemonCombat2.pv-((1/10)*PokemonCombat2.pvmax)
    else:
        ft2=PokemonCombat2.pv

    if PokemonCombat1.objet.name=="Life Orb" and compteurattdgt1==2 and dgtpdttour1<100:
        ft1=PokemonCombat1.pv-((1/10)*PokemonCombat1.pvmax)
    else:
        ft1=PokemonCombat1.pv

    if PokemonCombat1.talent.name=="Magic Guard":
        ft1=PokemonCombat1.pv

    if PokemonCombat2.talent.name=="Magic Guard":
        ft2=PokemonCombat2.pv

    if Prio1:
        if PokemonCombat2.objet.name=="Life Orb" and compteurattdgt2==2 and dgtpdttour2<100 and PokemonCombat2.talent.name!="Magic Guard":
            afficherTexte2(PokemonCombat2.objet.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
        PVPkmn2Obj()
    else:
        if PokemonCombat1.objet.name=="Life Orb" and compteurattdgt1==2 and dgtpdttour1<100 and PokemonCombat1.talent.name!="Magic Guard":
            afficherTexte2(PokemonCombat1.objet.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
        PVPkmn1Obj()



def SoinObj():
    global gainpv1,gainpv2,modifvit1,compteurmodifvit1,modifvit2,compteurmodifvit2

    if PokemonCombat2.objet.name=="Leftovers":
        gainpv2=PokemonCombat2.pv+((1/16)*PokemonCombat2.pvmax)
        if gainpv2>PokemonCombat2.pvmax:
            gainpv2=PokemonCombat2.pvmax
    else:
        gainpv2=PokemonCombat2.pv

    if PokemonCombat1.objet.name=="Leftovers":
        gainpv1=PokemonCombat1.pv+((1/16)*PokemonCombat1.pvmax)
        if gainpv1>PokemonCombat1.pvmax:
            gainpv1=PokemonCombat1.pvmax
    else:
        gainpv1=PokemonCombat1.pv

    

    if Prio1:
        if PokemonCombat2.objet.name=="Leftovers" and PokemonCombat2.pv<PokemonCombat2.pvmax:
            afficherTexte2(PokemonCombat2.objet.nom+" de " +PokemonCombat2.nom+'\n'+"le soigne    ")
        GainPVPkmn2Obj()
    else:
        if PokemonCombat1.objet.name=="Leftovers" and PokemonCombat1.pv<PokemonCombat1.pvmax:
            afficherTexte2(PokemonCombat1.objet.nom+" de " +PokemonCombat1.nom+'\n'+"le soigne    ")
        GainPVPkmn1Obj()
    if PokemonCombat1.talent.name=="Speed Boost":
        compteurmodifvit1+=1     
        if compteurmodifvit1>6:
            compteurmodifvit1=6
        modifvit1 = P.modifstats[compteurmodifvit1]

    if PokemonCombat2.talent.name=="Speed Boost":
        compteurmodifvit2+=1     
        if compteurmodifvit2>6:
            compteurmodifvit2=6
        modifvit2 = P.modifstats[compteurmodifvit2]

    if Poke1Mort != True:
        print("2")
        resetMenu()



############Effets###############

def AffStatut1():
    global compteurmodifvit1,poisongrv1,modifatt1,compteurmodifvit1,modifvit1
    
    if PokemonCombat1.statut=="Brûlé":
        if PokemonCombat1.talent.name!="Guts":
            modifatt1 = modifatt1/2
        canvas.itemconfig(statutpoke1, text ="Brûlé", fill ="#FC610E")
        if PokemonCombat1.talent.name=="Quick Feet":
            compteurmodifvit1+=1

    if PokemonCombat1.statut=="Gelé":
        canvas.itemconfig(statutpoke1, text ="Gelé", fill ="#81FFF5")
        if PokemonCombat1.talent.name=="Quick Feet":
            compteurmodifvit1+=1
    
    if PokemonCombat1.statut=="Empoisonné" or PokemonCombat1.statut=="Gravement Empoisonné":
        canvas.itemconfig(statutpoke1, text ="Empoisonné", fill ="#780A85")
        poisongrv1=1/16
        if PokemonCombat1.talent.name=="Quick Feet":
            compteurmodifvit1+=1

    if PokemonCombat1.statut=="Paralysé":
        modifvit1 = modifvit1/4
        canvas.itemconfig(statutpoke1, text ="Paralysé", fill ="#E5E509")
        if PokemonCombat1.talent.name=="Quick Feet":
            compteurmodifvit1+=1



def AffStatut2():
    global compteurmodifvit2,poisongrv2,modifatt2,compteurmodifvit2,modifvit2

    if PokemonCombat2.statut=="Brûlé":
        if PokemonCombat2.talent.name!="Guts":
            modifatt2 = modifatt2/2
        canvas.itemconfig(statutpoke2, text ="Brûlé", fill ="#FC610E")
        if PokemonCombat2.talent.name=="Quick Feet":
            compteurmodifvit2+=1

    if PokemonCombat2.statut=="Gelé":
        canvas.itemconfig(statutpoke2, text ="Gelé", fill ="#81FFF5")
        if PokemonCombat2.talent.name=="Quick Feet":
            compteurmodifvit2+=1

    if PokemonCombat2.statut=="Empoisonné" or PokemonCombat2.statut=="Gravement Empoisonné":
        canvas.itemconfig(statutpoke2, text ="Empoisonné", fill ="#780A85")
        poisongrv2=1/16
        if PokemonCombat2.talent.name=="Quick Feet":
            compteurmodifvit2+=1
        
    if PokemonCombat2.statut=="Paralysé":
        modifvit2 = modifvit2/4
        canvas.itemconfig(statutpoke2, text ="Paralysé", fill ="#E5E509")
        if PokemonCombat2.talent.name=="Quick Feet":
            compteurmodifvit2+=1



def AppliEffet1(Att,Effet):
    global modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1,statutpoke1,poisongrv1
    global modifatt2,modifdefe2,modifspa2,modifspdef2,modifvit2,statutpoke2,poisongrv2
    global compteurmodifatt1,compteurmodifdefe1,compteurmodifspa1,compteurmodifspdef1,compteurmodifvit1
    global compteurmodifatt2,compteurmodifdefe2,compteurmodifspa2,compteurmodifspdef2,compteurmodifvit2
    global chgmpkmn1combat,preceff
    
    
    if PokemonCombat1.talent.name=="Serene Grace":
        preceff = Att.precieffet*2
    else: preceff = Att.precieffet



    if random.randint(1,100)<=preceff and PokemonCombat1.talent.name!="Sheer Force":
        if Effet.nom == "Switch":
            chgmpkmn1combat=True
        if Effet.nom == "Growth":
            if TypeClimat=="Sun":
                compteurmodifatt1+=2
                compteurmodifspa1+=2
            else:
                compteurmodifatt1+=1
                compteurmodifspa1+=1
        if Effet.nom.startswith("Self"):
            if PokemonCombat1.talent.name=="Simple":
                compteurmodifatt1 = compteurmodifatt1+Effet.attmodif*2
                compteurmodifdefe1 = compteurmodifdefe1+Effet.defemodif*2
                compteurmodifspa1 = compteurmodifspa1+Effet.spamodif*2
                compteurmodifspdef1 = compteurmodifspdef1+Effet.spdefmodif*2
                compteurmodifvit1 = compteurmodifvit1+Effet.vitmodif*2
            
            else:
                compteurmodifatt1 = compteurmodifatt1+Effet.attmodif
                compteurmodifdefe1 = compteurmodifdefe1+Effet.defemodif
                compteurmodifspa1 = compteurmodifspa1+Effet.spamodif
                compteurmodifspdef1 = compteurmodifspdef1+Effet.spdefmodif
                compteurmodifvit1 = compteurmodifvit1+Effet.vitmodif

            c1 = [compteurmodifatt1,compteurmodifdefe1,compteurmodifspa1,compteurmodifspdef1,compteurmodifvit1]
            for i in c1:
                if i<0 and PokemonCombat1.talent.name=="Clear Body":
                    i=0

            if modifspa1<0.125: modifspa1=0.125

            if PokemonCombat1.statut=="None":

                if PokemonCombat1.talent.name=="Magma Armor" and Effet.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.talent.nom+" l'empèche de geler     ")
                else : PokemonCombat1.statut=Effet.statut

                if PokemonCombat1.talent.name=="Inner Focus" and Effet.statut=="Appeuré":
                    afficherTexte2(PokemonCombat1.nom+" reste attentif    ")
                else : PokemonCombat1.statut=Effet.statut

                if PokemonCombat1.talent.name=="Synchronize":
                    afficherTexte2(PokemonCombat1.talent.nom+" de "+PokemonCombat1.nom+"     ")
                    PokemonCombat2.statut=Effet.statut

                if PokemonCombat1.statut!="None" and PokemonCombat1.statut!="Appeuré":
                    afficherTexte2(PokemonCombat1.nom+" devient "+Effet.statut+"     ")

                AffStatut1()
                AffStatut2()


            modifatt1 = P.modifstats[compteurmodifatt1]
            modifspa1 = P.modifstats[compteurmodifspa1]
            modifdefe1 = P.modifstats[compteurmodifdefe1]
            modifspdef1 = P.modifstats[compteurmodifspdef1]
            modifvit1 = P.modifstats[compteurmodifvit1]


        else: 
            if PokemonCombat2.talent.name=="Simple":
                compteurmodifatt2 = compteurmodifatt2+Effet.attmodif*2
                compteurmodifdefe2 = compteurmodifdefe2+Effet.defemodif*2
                compteurmodifspa2 = compteurmodifspa2+Effet.spamodif*2
                compteurmodifspdef2 = compteurmodifspdef2+Effet.spdefmodif*2
                compteurmodifvit2 = compteurmodifvit2+Effet.vitmodif*2

            else:
                compteurmodifatt2 = compteurmodifatt2+Effet.attmodif
                compteurmodifdefe2 = compteurmodifdefe2+Effet.defemodif
                compteurmodifspa2 = compteurmodifspa2+Effet.spamodif
                compteurmodifspdef2 = compteurmodifspdef2+Effet.spdefmodif
                compteurmodifvit2 = compteurmodifvit2+Effet.vitmodif

            c2 = [compteurmodifatt2,compteurmodifdefe2,compteurmodifspa2,compteurmodifspdef2,compteurmodifvit2]
            for i in c2:
                if i<0 and PokemonCombat2.talent.name=="Clear Body":
                    i=0

            if PokemonCombat2.statut=="None":

                if PokemonCombat2.talent.name=="Magma Armor" and Effet.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.talent.nom+" l'empèche de geler     ")
                else :PokemonCombat2.statut=Effet.statut

                if PokemonCombat2.statut!="None" and PokemonCombat2.statut!="Appeuré":
                    afficherTexte2(PokemonCombat2.nom+" devient "+Effet.statut+"     ")
                
                if PokemonCombat2.talent.name=="Inner Focus" and Effet.statut=="Appeuré":
                    afficherTexte2(PokemonCombat2.nom+" reste attentif    ")
                else : PokemonCombat2.statut=Effet.statut

                if PokemonCombat2.talent.name=="Synchronize":
                    afficherTexte2(PokemonCombat2.talent.nom+" de "+PokemonCombat2.nom+"     ")
                    PokemonCombat1.statut=Effet.statut

                AffStatut1()
                AffStatut2()

            modifatt2 = P.modifstats[compteurmodifatt2]
            modifspa2 = P.modifstats[compteurmodifspa2]
            modifdefe2 = P.modifstats[compteurmodifdefe2]
            modifspdef2 = P.modifstats[compteurmodifspdef2]
            modifvit2 = P.modifstats[compteurmodifvit2]

    compteurs = [compteurmodifatt1, compteurmodifdefe1, compteurmodifspa1, compteurmodifspdef1 ,compteurmodifvit1, compteurmodifatt2 ,compteurmodifdefe2 ,compteurmodifspa2 ,compteurmodifspdef2 ,compteurmodifvit2]
    for c in compteurs:
        if c>5:
            c=5
        elif c<-5:
            c=-5
    
""" 
    canvas.itemconfig(affmodifatt1, text="Stat attaque "+PokemonCombat1.nom+" : x"+str(modifatt1))
    canvas.itemconfig(affmodifspa1, text="Stat attaque spéciale "+PokemonCombat1.nom+" : x"+str(modifspa1))
    canvas.itemconfig(affmodifdefe1, text="Stat défense "+PokemonCombat1.nom+" : x"+str(modifdefe1))
    canvas.itemconfig(affmodifspedef1, text="Stat défense spéciale "+PokemonCombat1.nom+" : x"+str(modifspdef1))
    canvas.itemconfig(affmodifvit1, text="Stat vitesse "+PokemonCombat1.nom+" : x"+str(modifvit1))

    canvas.itemconfig(affmodifatt2, text="Stat attaque "+PokemonCombat2.nom+" : x"+str(modifatt2))
    canvas.itemconfig(affmodifspa2, text="Stat attaque spéciale "+PokemonCombat2.nom+" : x"+str(modifspa2))
    canvas.itemconfig(affmodifdefe2, text="Stat défense "+PokemonCombat2.nom+" : x"+str(modifdefe2))
    canvas.itemconfig(affmodifspedef2, text="Stat défense spéciale "+PokemonCombat2.nom+" : x"+str(modifspdef2))
    canvas.itemconfig(affmodifvit2, text="Stat vitesse "+PokemonCombat2.nom+" : x"+str(modifvit2)) """




def AppliEffet2(Att,Effet):
    global modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1,statutpoke1,poisongrv1
    global modifatt2,modifdefe2,modifspa2,modifspdef2,modifvit2,statutpoke2,poisongrv2
    global compteurmodifatt1,compteurmodifdefe1,compteurmodifspa1,compteurmodifspdef1,compteurmodifvit1
    global compteurmodifatt2,compteurmodifdefe2,compteurmodifspa2,compteurmodifspdef2,compteurmodifvit2
    global chgmpkmn2combat,preceff
    
    
    if PokemonCombat2.talent.name=="Serene Grace":
        preceff = Att.precieffet*2
    else: preceff = Att.precieffet

    if random.randint(1,100)<=preceff and PokemonCombat2.talent.name!="Sheer Force":
        if Effet.nom == "Switch":
            chgmpkmn2combat=True 
        if Effet.nom == "Growth":
            if TypeClimat=="Sun":
                compteurmodifatt2+=2
                compteurmodifspa2+=2
            else:
                compteurmodifatt2+=1
                compteurmodifspa2+=1
        if Effet.nom.startswith("Self"):
            if PokemonCombat2.talent.name=="Simple":
                compteurmodifatt2 = compteurmodifatt2+Effet.attmodif*2
                compteurmodifdefe2 = compteurmodifdefe2+Effet.defemodif*2
                compteurmodifspa2 = compteurmodifspa2+Effet.spamodif*2
                compteurmodifspdef2 = compteurmodifspdef2+Effet.spdefmodif*2
                compteurmodifvit2 = compteurmodifvit2+Effet.vitmodif*2

            else:
                compteurmodifatt2 = compteurmodifatt2+Effet.attmodif
                compteurmodifdefe2 = compteurmodifdefe2+Effet.defemodif
                compteurmodifspa2 = compteurmodifspa2+Effet.spamodif
                compteurmodifspdef2 = compteurmodifspdef2+Effet.spdefmodif
                compteurmodifvit2 = compteurmodifvit2+Effet.vitmodif

            c2 = [compteurmodifatt2,compteurmodifdefe2,compteurmodifspa2,compteurmodifspdef2,compteurmodifvit2]
            for i in c2:
                if i<0 and PokemonCombat2.talent.name=="Clear Body":
                    i=0
            

            if PokemonCombat2.statut=="None":

                if PokemonCombat2.talent.name=="Magma Armor" and Effet.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.talent.nom+" l'empèche de geler     ")
                else :PokemonCombat2.statut=Effet.statut

                if PokemonCombat2.statut!="None" and PokemonCombat2.statut!="Appeuré":
                    afficherTexte2(PokemonCombat2.nom+" devient "+Effet.statut+"     ")

                if PokemonCombat2.talent.name=="Inner Focus" and Effet.statut=="Appeuré":
                    afficherTexte2(PokemonCombat2.nom+" reste attentif    ")
                else : PokemonCombat2.statut=Effet.statut

                if PokemonCombat2.talent.name=="Synchronize":
                    afficherTexte2(PokemonCombat2.talent.nom+" de "+PokemonCombat2.nom+"     ")
                    PokemonCombat1.statut=Effet.statut

                AffStatut1()
                AffStatut2()
            
            modifatt2 = P.modifstats[compteurmodifatt2]
            modifspa2 = P.modifstats[compteurmodifspa2]
            modifdefe2 = P.modifstats[compteurmodifdefe2]
            modifspdef2 = P.modifstats[compteurmodifspdef2]
            modifvit2 = P.modifstats[compteurmodifvit2]

        else: 
            if PokemonCombat1.talent.name=="Simple":
                compteurmodifatt1 = compteurmodifatt1+Effet.attmodif*2
                compteurmodifdefe1 = compteurmodifdefe1+Effet.defemodif*2
                compteurmodifspa1 = compteurmodifspa1+Effet.spamodif*2
                compteurmodifspdef1 = compteurmodifspdef1+Effet.spdefmodif*2
                compteurmodifvit1 = compteurmodifvit1+Effet.vitmodif*2
            
            else:
                compteurmodifatt1 = compteurmodifatt1+Effet.attmodif
                compteurmodifdefe1 = compteurmodifdefe1+Effet.defemodif
                compteurmodifspa1 = compteurmodifspa1+Effet.spamodif
                compteurmodifspdef1 = compteurmodifspdef1+Effet.spdefmodif
                compteurmodifvit1 = compteurmodifvit1+Effet.vitmodif

            c1 = [compteurmodifatt1,compteurmodifdefe1,compteurmodifspa1,compteurmodifspdef1,compteurmodifvit1]
            for i in c1:
                if i<0 and PokemonCombat1.talent.name=="Clear Body":
                    i=0

            if PokemonCombat1.statut=="None":

                if PokemonCombat1.talent.name=="Magma Armor" and Effet.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.talent.nom+" l'empèche de geler     ")
                else :PokemonCombat1.statut=Effet.statut

                if PokemonCombat1.statut!="None" and PokemonCombat1.statut!="Appeuré":
                    afficherTexte2(PokemonCombat1.nom+" devient "+Effet.statut)

                if PokemonCombat1.talent.name=="Inner Focus" and Effet.statut=="Appeuré":
                    afficherTexte2(PokemonCombat1.nom+" reste attentif    ")
                else : PokemonCombat1.statut=Effet.statut

                if PokemonCombat1.talent.name=="Synchronize":
                    afficherTexte2(PokemonCombat1.talent.nom+" de "+PokemonCombat1.nom+"     ")
                    PokemonCombat2.statut=Effet.statut

                AffStatut1()
                AffStatut2()
            
            modifatt1 = P.modifstats[compteurmodifatt1]
            modifspa1 = P.modifstats[compteurmodifspa1]
            modifdefe1 = P.modifstats[compteurmodifdefe1]
            modifspdef1 = P.modifstats[compteurmodifspdef1]
            modifvit1 = P.modifstats[compteurmodifvit1]

    compteurs = [compteurmodifatt1, compteurmodifdefe1, compteurmodifspa1, compteurmodifspdef1 ,compteurmodifvit1, compteurmodifatt2 ,compteurmodifdefe2 ,compteurmodifspa2 ,compteurmodifspdef2 ,compteurmodifvit2]
    for c in compteurs:
        if c>5:
            c=5
        elif c<-5:
            c=-5
    
"""   canvas.itemconfig(affmodifatt2, text="Stat attaque "+PokemonCombat2.nom+" : x"+str(modifatt2))
    canvas.itemconfig(affmodifspa2, text="Stat attaque spéciale "+PokemonCombat2.nom+" : x"+str(modifspa2))
    canvas.itemconfig(affmodifdefe2, text="Stat défense "+PokemonCombat2.nom+" : x"+str(modifdefe2))
    canvas.itemconfig(affmodifspedef2, text="Stat défense spéciale "+PokemonCombat2.nom+" : x"+str(modifspdef2))
    canvas.itemconfig(affmodifvit2, text="Stat vitesse "+PokemonCombat2.nom+" : x"+str(modifvit2))

    canvas.itemconfig(affmodifatt1, text="Stat attaque "+PokemonCombat1.nom+" : x"+str(modifatt1))
    canvas.itemconfig(affmodifspa1, text="Stat attaque spéciale "+PokemonCombat1.nom+" : x"+str(modifspa1))
    canvas.itemconfig(affmodifdefe1, text="Stat défense "+PokemonCombat1.nom+" : x"+str(modifdefe1))
    canvas.itemconfig(affmodifspedef1, text="Stat défense spéciale "+PokemonCombat1.nom+" : x"+str(modifspdef1))
    canvas.itemconfig(affmodifvit1, text="Stat vitesse "+PokemonCombat1.nom+" : x"+str(modifvit1)) """









############Changement Poke###############


def ChangementPokemonAttaque():
    global chgmpkmn1combat,menu
    menu=2
    canvas.itemconfigure(RectAttaque, state='hidden')
    canvas.itemconfigure(TexteAttaque, state='hidden')
    canvas.itemconfigure(RectPokemon, state='hidden')
    canvas.itemconfigure(TextePokemon, state='hidden')
    AffChangerPokemon()


def ChangementPokemon(Pokemon):
    global PokemonCombat1,modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1,statutpoke1,chgmpkmn1mort,chgmpkmn1combat

    print("D")
    resetAffMenu()

    PokemonCombat1=Pokemon
    afficherTexte2("En avant "+PokemonCombat1.nom)

    EntreePokemon1()

    pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
    canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
    if pcvie1>50: colorpv1 = '#15FC0E'
    elif pcvie1>25: colorpv1 = '#FB7B11'
    else: colorpv1 = '#E50404'
    canvas.itemconfigure("vieP1",fill=colorpv1)

    canvas.itemconfigure(nompokecombat1,text=PokemonCombat1.nom)
    ChangerTexturePokemon()
    
    modifatt1 = 1
    modifspa1 = 1
    modifspdef1 = 1
    modifdefe1 = 1
    modifvit1 = 1

    """ canvas.itemconfig(affmodifatt1, text="Stat attaque "+PokemonCombat1.nom+" : x"+str(modifatt1))
    canvas.itemconfig(affmodifspa1, text="Stat attaque spéciale "+PokemonCombat1.nom+" : x"+str(modifspa1))
    canvas.itemconfig(affmodifdefe1, text="Stat défense "+PokemonCombat1.nom+" : x"+str(modifdefe1))
    canvas.itemconfig(affmodifspedef1, text="Stat défense spéciale "+PokemonCombat1.nom+" : x"+str(modifspdef1))
    canvas.itemconfig(affmodifvit1, text="Stat vitesse "+PokemonCombat1.nom+" : x"+str(modifvit1)) """

    canvas.itemconfig(statutpoke1, text ="")

    if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                PokemonCombat2.statut="None"
                canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")

    canvas.update()
    if chgmpkmn1mort:
        print("3")
        resetMenu()
    if chgmpkmn1combat==True:
        if Prio1:
            IAmoove()
        else:
            FinDuTour()
    elif chgmpkmn1combat==False and chgmpkmn1mort==False: 
        if PokemonCombat2.statut=="Gelé":
            afficherTexte2(PokemonCombat2.nom+" est gelé     ")
            print("4")
            resetMenu()
        elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
            afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
            print("5")
            resetMenu()
        else: IAmoove()
    if chgmpkmn1mort==False:
        chgmpkmn1combat = False
    chgmpkmn1mort = False


def ChangementEquipeBot():
    global nbequipe,numerocombat,PokemonCombat2,nbPokemon2
    global Pokemon2n1,Pokemon2n2,Pokemon2n3,Pokemon2n4,Pokemon2n5,Pokemon2n6

    nbPokemon2=6

    Pokemon2n1=NiveauDebutant[numerocombat].Slot1
    Pokemon2n2=NiveauDebutant[numerocombat].Slot2
    Pokemon2n3=NiveauDebutant[numerocombat].Slot3
    Pokemon2n4=NiveauDebutant[numerocombat].Slot4
    Pokemon2n5=NiveauDebutant[numerocombat].Slot5
    Pokemon2n6=NiveauDebutant[numerocombat].Slot6

    PokemonCombat2 = Pokemon2n1


    CreationImagePoke2Team()

    EnvoisPokemon2()
        
    numerocombat+=1

    ProchainDress()

    






def AnimDeathPoke2():
    global mouvement
    if mouvement> 0:
        mouvement-=1
        canvas.move(imgpkmn2,0,10)
        canvas.after(20,AnimDeathPoke2)
    else: canvas.itemconfig(imgpkmn2,state='hidden')

def AnimDeathPoke1():
    global mouvement2
    if mouvement2> 0:
        mouvement2-=1
        canvas.move(imgpkmn1,0,10)
        canvas.after(20,AnimDeathPoke1)
    else: canvas.itemconfig(imgpkmn1,state='hidden')



def ChangementAttaquePokemon2():
    global PokemonCombat2,chgmpkmn2combat
    if ialevel=="Debutant":
            if Pokemon2n1.pv>5 and PokemonCombat2!=Pokemon2n1:
                PokemonCombat2=Pokemon2n1
            elif Pokemon2n2.pv>5 and PokemonCombat2!=Pokemon2n2:
                PokemonCombat2=Pokemon2n2
            elif Pokemon2n3.pv>5 and PokemonCombat2!=Pokemon2n3:
                PokemonCombat2=Pokemon2n3
            elif Pokemon2n4.pv>5 and PokemonCombat2!=Pokemon2n4:
                PokemonCombat2=Pokemon2n4
            elif Pokemon2n5.pv>5 and PokemonCombat2!=Pokemon2n5:
                PokemonCombat2=Pokemon2n5
            elif Pokemon2n6.pv>5 and PokemonCombat2!=Pokemon2n6:
                PokemonCombat2=Pokemon2n6
    chgmpkmn2combat=False
    EnvoisPokemon2()


def EnvoisPokemon2():
    global imgpkmn2,fincombat
    afficherTexte2("dresseur 2 envoie "+PokemonCombat2.nom)

    canvas.update()

    pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
    canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
    if pcvie2>50: colorpv2 = '#15FC0E'
    elif pcvie2>25: colorpv2 = '#FB7B11'
    else: colorpv2 = '#E50404'
    if Poke2MortCeTour or fincombat:
        canvas.move(imgpkmn2,0,-100)
    canvas.itemconfigure("vieP2",fill=colorpv2)

    if PokemonCombat2==Pokemon2n1:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n1)
    elif PokemonCombat2==Pokemon2n2:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n2)
    elif PokemonCombat2==Pokemon2n3:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n3)
    elif PokemonCombat2==Pokemon2n4:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n4)
    elif PokemonCombat2==Pokemon2n5:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n5)
    elif PokemonCombat2==Pokemon2n6:
        canvas.itemconfig(imgpkmn2,state='normal',image=pkmn2n6)

    canvas.itemconfigure(nompokecombat2,text=PokemonCombat2.nom)

    """     canvas.itemconfig(affmodifatt2, text="Stat attaque "+PokemonCombat2.nom+" : x"+str(modifatt2))
    canvas.itemconfig(affmodifspa2, text="Stat attaque spéciale "+PokemonCombat2.nom+" : x"+str(modifspa2))
    canvas.itemconfig(affmodifdefe2, text="Stat défense "+PokemonCombat2.nom+" : x"+str(modifdefe2))
    canvas.itemconfig(affmodifspedef2, text="Stat défense spéciale "+PokemonCombat2.nom+" : x"+str(modifspdef2))
    canvas.itemconfig(affmodifvit2, text="Stat vitesse "+PokemonCombat2.nom+" : x"+str(modifvit2)) """
    if PokemonCombat2.statut!="None":
        canvas.itemconfig(statutpoke2, text = PokemonCombat2.statut)
    else: canvas.itemconfig(statutpoke2, text = "")
    canvas.update()
    fincombat=False
    EntreePokemon2()

def Pokemon2Dead():
    global PokemonCombat2, mouvement,nbPokemon2,ialevel,modifatt2,modifdefe2,modifspa2,modifspdef2,modifvit2,statutpoke2,imun2,Poke2Mort,Poke2MortCeTour
    global fincombat

    PokemonCombat2.etat="Mort"

    Poke2Mort = True

    Poke2MortCeTour = True

    imun2=True

    nbPokemon2-=1
    mouvement = 10

    AnimDeathPoke2()
    if nbPokemon2<=0:
        fincombat=True
        if numerocombat<9:
            CommentateurFinCombat()
        else:
            Victoire1()
    else:
        

        modifatt2 = 1
        modifspa2 = 1
        modifspdef2 = 1
        modifdefe2 = 1
        modifvit2 = 1

            
        
        if ialevel=="Debutant":
            if Pokemon2n1.pv>5 and PokemonCombat2!=Pokemon2n1:
                PokemonCombat2=Pokemon2n1
            elif Pokemon2n2.pv>5 and PokemonCombat2!=Pokemon2n2:
                PokemonCombat2=Pokemon2n2
            elif Pokemon2n3.pv>5 and PokemonCombat2!=Pokemon2n3:
                PokemonCombat2=Pokemon2n3
            elif Pokemon2n4.pv>5 and PokemonCombat2!=Pokemon2n4:
                PokemonCombat2=Pokemon2n4
            elif Pokemon2n5.pv>5 and PokemonCombat2!=Pokemon2n5:
                PokemonCombat2=Pokemon2n5
            elif Pokemon2n6.pv>5 and PokemonCombat2!=Pokemon2n6:
                PokemonCombat2=Pokemon2n6

        EnvoisPokemon2()
        if chgmpkmn1combat:
            ChangementPokemonAttaque()







def Pokemon1Dead():
    global PokemonCombat1, mouvement2,nbPokemon1,ialevel,modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1,statutpoke1,imun1,menu,chgmpkmn1mort,Poke1Mort,Poke1MortCeTour
    PokemonCombat1.etat="Mort"

    Poke1Mort = True
    Poke1MortCeTour = True

    print("6")
    resetMenu()

    chgmpkmn1mort=True

    imun1=True
    
    nbPokemon1-=1

    if nbPokemon1<=0:
        Victoire2()

    else:
        menu=2

        mouvement2 = 10

        modifatt1 = 1
        modifspa1 = 1
        modifspdef1 = 1
        modifdefe1 = 1
        modifvit1 = 1

            
        AnimDeathPoke1()


        canvas.update()

        pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
        canvas.coords("vieP1",577, 157, 573+pcvie1*2, 167)
        if pcvie1>50: colorpv1 = '#15FC0E'
        elif pcvie1>25: colorpv1 = '#FB7B11'
        else: colorpv1 = '#E50404'
        canvas.move(imgpkmn1,0,-100)
        canvas.itemconfigure("vieP1",fill=colorpv1)


        canvas.itemconfigure(nompokecombat1,text=PokemonCombat1.nom)

        """     canvas.itemconfig(affmodifatt1, text="Stat attaque "+PokemonCombat1.nom+" : x"+str(modifatt1))
        canvas.itemconfig(affmodifspa1, text="Stat attaque spéciale "+PokemonCombat1.nom+" : x"+str(modifspa1))
        canvas.itemconfig(affmodifdefe1, text="Stat défense "+PokemonCombat1.nom+" : x"+str(modifdefe1))
        canvas.itemconfig(affmodifspedef1, text="Stat défense spéciale "+PokemonCombat1.nom+" : x"+str(modifspdef1))
        canvas.itemconfig(affmodifvit1, text="Stat vitesse "+PokemonCombat1.nom+" : x"+str(modifvit1)) """

        canvas.itemconfig(statutpoke1, text ="")


        canvas.itemconfigure(RectAttaque, state='hidden')
        canvas.itemconfigure(TexteAttaque, state='hidden')
        canvas.itemconfigure(RectPokemon, state='hidden')
        canvas.itemconfigure(TextePokemon, state='hidden')

        AffChangerPokemon()
        canvas.update()
    

    







#######################BOUCLE IA###############################################








def IAmoove():
    global d,PokemonCombat1,PokemonCombat2,numeroechoue2,pvapresrecul2,attBloqueeIA,attaqueP2,pvapressoin2,dgtpdttour2,compteursash1,soin2
    dgtpdttour2 = 100
    if ialevel == "Debutant":
        if PokemonCombat2.objet.name.startswith("Choice") and attBloqueeIA==0:
                attBloqueeIA = attaqueP2
        if attBloqueeIA != 0: attaqueP2 = attBloqueeIA
        if attaqueP2 == 1 :
            afficherTexte2(PokemonCombat2.nom+" utilise "+PokemonCombat2.a1.nom+"     ")
            damage = int(calcdamage(PokemonCombat2.a1,PokemonCombat2,PokemonCombat1))
            if damage >= PokemonCombat1.pvmax and PokemonCombat1.pv==PokemonCombat1.pvmax:
                compteursash1 = 1
            if PokemonCombat2.talent.name=="Rock Head" or PokemonCombat2.talent.name=="Magic Guard" or PokemonCombat2.talent.name=="Sheer Force":
                recul2 = 0
            else : recul2 = damage*PokemonCombat2.a1.recul
            d=PokemonCombat1.pv-damage
            soin2 = damage*PokemonCombat2.a1.soin
            pvapresrecul2 = PokemonCombat2.pv-recul2
            if numeroechoue2 != 1:
                AppliEffet2(PokemonCombat2.a1,PokemonCombat2.a1.effet)
            PVPkmn1()
        if attaqueP2 == 2 :
            afficherTexte2(PokemonCombat2.nom+" utilise "+PokemonCombat2.a2.nom+"     ")
            damage = int(calcdamage(PokemonCombat2.a2,PokemonCombat2,PokemonCombat1))
            if damage >= PokemonCombat1.pvmax and PokemonCombat1.pv==PokemonCombat1.pvmax:
                compteursash1 = 1
            if PokemonCombat2.talent.name=="Rock Head" or PokemonCombat2.talent.name=="Magic Guard" or PokemonCombat2.talent.name=="Sheer Force":
                recul2 = 0
            else : recul2 = damage*PokemonCombat2.a2.recul
            d=PokemonCombat1.pv-damage
            soin2 = damage*PokemonCombat2.a2.soin
            pvapresrecul2 = PokemonCombat2.pv-recul2
            if numeroechoue2 != 1:
                AppliEffet2(PokemonCombat2.a2,PokemonCombat2.a2.effet)
            PVPkmn1()
        if attaqueP2 == 3 :
            afficherTexte2(PokemonCombat2.nom+" utilise "+PokemonCombat2.a3.nom+"     ")
            damage = int(calcdamage(PokemonCombat2.a3,PokemonCombat2,PokemonCombat1))
            if damage >= PokemonCombat1.pvmax and PokemonCombat1.pv==PokemonCombat1.pvmax:
                compteursash1 = 1
            if PokemonCombat2.talent.name=="Rock Head" or PokemonCombat2.talent.name=="Magic Guard" or PokemonCombat2.talent.name=="Sheer Force":
                recul2 = 0
            else : recul2 = damage*PokemonCombat2.a3.recul
            d=PokemonCombat1.pv-damage
            soin2 = damage*PokemonCombat2.a3.soin
            pvapresrecul2 = PokemonCombat2.pv-recul2
            if numeroechoue2 != 1:
                AppliEffet2(PokemonCombat2.a3,PokemonCombat2.a3.effet)
            PVPkmn1()
        if attaqueP2 == 4 :
            afficherTexte2(PokemonCombat2.nom+" utilise "+PokemonCombat2.a4.nom+"     ")
            damage = int(calcdamage(PokemonCombat2.a4,PokemonCombat2,PokemonCombat1))
            if damage >= PokemonCombat1.pvmax and PokemonCombat1.pv==PokemonCombat1.pvmax:
                compteursash1 = 1
            if PokemonCombat2.talent.name=="Rock Head" or PokemonCombat2.talent.name=="Magic Guard" or PokemonCombat2.talent.name=="Sheer Force":
                recul2 = 0
            else : recul2 = damage*PokemonCombat2.a4.recul
            d=PokemonCombat1.pv-damage
            soin2 = damage*PokemonCombat2.a4.soin
            pvapresrecul2 = PokemonCombat2.pv-recul2
            if numeroechoue2 != 1:
                AppliEffet2(PokemonCombat2.a4,PokemonCombat2.a4.effet)
            PVPkmn1()















##########################################################################################
#######################MAIN BOUCLE#############################################
##########################################################################################


def changemenu1(event):
    global menu,t,d,Prio1,numeroatt,numeroattbis,numeroechoue1,recul1,pvapresrecul1,attBloquee,attaqueP2,dgtpdttour2,compteursash2
    global Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6,PokemonCombat1,dgtpdttour1,soin1,compteursash1,Poke1MortCeTour

    dgtpdttour1 = 100
    Poke1MortCeTour = False
    ###Attaque 1###
    if event.x>605 and event.x<805 and event.y>510 and event.y<605 and menu==1 and not (attBloquee==0 or attBloquee==1):
        afficherTexte1(PokemonCombat1.objet.nom+" de "+PokemonCombat1.nom +'\n'+"l'empêche de changer d'attaque !        ")
        canvas.after(20,resetMenu)
    if event.x>605 and event.x<805 and event.y>510 and event.y<605 and menu==1 and (attBloquee==0 or attBloquee==1):
        if PokemonCombat1.a1.pp>0:
            afficherTexte1("")
            if PokemonCombat1.statut=="Gelé" and random.randint(1,5)==1:
                afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                PokemonCombat1.statut="None"
            if PokemonCombat1.a1.name in P.CapaDegel:
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                    PokemonCombat1.statut="None"
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                    PokemonCombat2.statut="None"
                    canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
            if PokemonCombat1.objet.name.startswith("Choice"):
                if attBloquee == 0:
                    attBloquee = 1
            numeroatt=1
            numeroattbis = 1
            PokemonCombat1.a1.pp-=1
            if PokemonCombat1.a1.pp==0:
                attBloquee=0
            texte_attaque1_pp = str(PokemonCombat1.a1.pp)+"/"+str(PokemonCombat1.a1.ppmax)
            canvas.itemconfig(TexteAttaque1PP, text=texte_attaque1_pp)
            damage = int(calcdamage(PokemonCombat1.a1,PokemonCombat1,PokemonCombat2))
            if damage >= PokemonCombat2.pvmax and PokemonCombat2.pv==PokemonCombat2.pvmax:
                compteursash2 = 1
            if PokemonCombat1.talent.name!="Rock Head" and PokemonCombat1.talent.name!="Magic Guard" or PokemonCombat1.talent.name!="Sheer Force":
                recul1 = damage*PokemonCombat1.a1.recul
            else: recul1 = 0
            t=PokemonCombat2.pv-damage
            pvapresrecul1 = PokemonCombat1.pv-recul1
            soin1 = damage*PokemonCombat1.a1.soin
            vit1 = PokemonCombat1.vit*modifvitclimat1*modifvit1*PokemonCombat1.objet.vitmodif
            vit2 = PokemonCombat2.vit*modifvitclimat2*modifvit2*PokemonCombat2.objet.vitmodif
            attaqueP2 = random.randint(1,4)
            if attaqueP2==1:
                att=PokemonCombat2.a1
            elif attaqueP2==2:
                att=PokemonCombat2.a2
            elif attaqueP2==3:
                att=PokemonCombat2.a3
            elif attaqueP2==4:
                att=PokemonCombat2.a4
            if att.prio==PokemonCombat1.a1.prio:
                if vit1>vit2:
                    Prio1=True
                    if PokemonCombat1.statut=="Gelé":
                        afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                        IAmoove()
                    else: PVPkmn2()
                else:
                    Prio1=False
                    if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                    if PokemonCombat2.statut=="Gelé":
                        afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                        PVPkmn2()
                    elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                        afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                        PVPkmn2()
                    else: IAmoove()
            elif att.prio>PokemonCombat1.a1.prio:
                Prio1=False
                if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                    PVPkmn2()
                elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                        afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                        PVPkmn2()
                else: IAmoove()
            else:
                Prio1=True
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                    IAmoove()
                else: PVPkmn2()
        else:
            afficherTexte1("La capacité "+PokemonCombat1.a1.nom+" n'a plus de PP")
            canvas.after(20,resetMenu)


    ###Attaque 2###
    if event.x>815 and event.x<1015 and event.y>510 and event.y<605 and menu==1 and not (attBloquee==0 or attBloquee==2):
        afficherTexte1(PokemonCombat1.objet.nom+" de "+PokemonCombat1.nom +'\n'+"l'empêche de changer d'attaque !        ")
        canvas.after(20,resetMenu)
    if event.x>815 and event.x<1015 and event.y>510 and event.y<605 and menu==1 and (attBloquee==0 or attBloquee==2):
        if PokemonCombat1.a2.pp>0:
            afficherTexte1("")
            if PokemonCombat1.statut=="Gelé" and random.randint(1,5)==1:
                afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                PokemonCombat1.statut="None"
            if PokemonCombat1.a2.name in P.CapaDegel:
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                    PokemonCombat1.statut="None"
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                    PokemonCombat2.statut="None"
                    canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
            if PokemonCombat1.objet.name.startswith("Choice"):
                if attBloquee == 0:
                    attBloquee = 2
            numeroatt=2
            numeroattbis = 1
            PokemonCombat1.a2.pp-=1
            if PokemonCombat1.a2.pp==0:
                attBloquee=0
            texte_attaque2_pp = str(PokemonCombat1.a2.pp)+"/"+str(PokemonCombat1.a2.ppmax)
            canvas.itemconfig(TexteAttaque2PP, text=texte_attaque2_pp)
            damage = int(calcdamage(PokemonCombat1.a2,PokemonCombat1,PokemonCombat2))
            if damage >= PokemonCombat2.pvmax and PokemonCombat2.pv==PokemonCombat2.pvmax:
                compteursash2 = 1
            if PokemonCombat1.talent.name!="Rock Head" and PokemonCombat1.talent.name!="Magic Guard" or PokemonCombat1.talent.name!="Sheer Force":
                recul1 = damage*PokemonCombat1.a2.recul
            else: recul1 = 0
            t=PokemonCombat2.pv-damage
            soin1 = damage*PokemonCombat1.a2.soin
            pvapresrecul1 = PokemonCombat1.pv-recul1
            vit1 = PokemonCombat1.vit*modifvitclimat1*modifvit1*PokemonCombat1.objet.vitmodif
            vit2 = PokemonCombat2.vit*modifvitclimat2*modifvit2*PokemonCombat2.objet.vitmodif
            attaqueP2 = random.randint(1,4)
            if attaqueP2==1:
                att=PokemonCombat2.a1
            elif attaqueP2==2:
                att=PokemonCombat2.a2
            elif attaqueP2==3:
                att=PokemonCombat2.a3
            elif attaqueP2==4:
                att=PokemonCombat2.a4
            if att.prio==PokemonCombat1.a2.prio:
                if vit1>vit2:
                    Prio1=True
                    if PokemonCombat1.statut=="Gelé":
                        afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                        IAmoove()
                    else: PVPkmn2()
                else:
                    Prio1=False
                    if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                    if PokemonCombat2.statut=="Gelé":
                        afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                        PVPkmn2()
                    elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                        afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                        PVPkmn2()
                    else: IAmoove()
            elif att.prio>PokemonCombat1.a2.prio:
                Prio1=False
                if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                    PVPkmn2()
                elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                    afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                    PVPkmn2()
                else: IAmoove()
            else:
                Prio1=True
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                    IAmoove()
                else: PVPkmn2()
        else:
            afficherTexte1("La capacité "+PokemonCombat1.a2.nom+" n'a plus de PP")
            canvas.after(20,resetMenu)


    ###Attaque 3###
    if event.x>605 and event.x<805 and event.y>615 and event.y<710 and menu==1 and not (attBloquee==0 or attBloquee==3):
        afficherTexte1(PokemonCombat1.objet.nom+" de "+PokemonCombat1.nom +'\n'+"l'empêche de changer d'attaque !        ")
        canvas.after(20,resetMenu)
    if event.x>605 and event.x<805 and event.y>615 and event.y<710 and menu==1 and (attBloquee==0 or attBloquee==3):
        if PokemonCombat1.a3.pp>0:
            afficherTexte1("")
            if PokemonCombat1.statut=="Gelé" and random.randint(1,5)==1:
                afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                PokemonCombat1.statut="None"
            if PokemonCombat1.a3.name in P.CapaDegel:
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                    PokemonCombat1.statut="None"
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                    PokemonCombat2.statut="None"
                    canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
            if PokemonCombat1.objet.name.startswith("Choice"):
                if attBloquee == 0:
                    attBloquee = 3
            numeroatt=3
            numeroattbis = 1
            PokemonCombat1.a3.pp-=1
            if PokemonCombat1.a3.pp==0:
                attBloquee=0
            texte_attaque3_pp = str(PokemonCombat1.a3.pp)+"/"+str(PokemonCombat1.a3.ppmax)
            canvas.itemconfig(TexteAttaque3PP, text=texte_attaque3_pp)
            damage = int(calcdamage(PokemonCombat1.a3,PokemonCombat1,PokemonCombat2))
            if damage >= PokemonCombat2.pvmax and PokemonCombat2.pv==PokemonCombat2.pvmax:
                compteursash2 = 1 
            if PokemonCombat1.talent.name!="Rock Head" and PokemonCombat1.talent.name!="Magic Guard" or PokemonCombat1.talent.name!="Sheer Force":
                recul1 = damage*PokemonCombat1.a3.recul
            else: recul1 = 0
            t=PokemonCombat2.pv-damage
            soin1 = damage*PokemonCombat1.a3.soin
            pvapresrecul1 = PokemonCombat1.pv-recul1
            vit1 = PokemonCombat1.vit*modifvitclimat1*modifvit1*PokemonCombat1.objet.vitmodif
            vit2 = PokemonCombat2.vit*modifvitclimat2*modifvit2*PokemonCombat2.objet.vitmodif
            attaqueP2 = random.randint(1,4)
            if attaqueP2==1:
                att=PokemonCombat2.a1
            elif attaqueP2==2:
                att=PokemonCombat2.a2
            elif attaqueP2==3:
                att=PokemonCombat2.a3
            elif attaqueP2==4:
                att=PokemonCombat2.a4
            if att.prio==PokemonCombat1.a3.prio:
                if vit1>vit2:
                    Prio1=True
                    if PokemonCombat1.statut=="Gelé":
                        afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                        IAmoove()
                    else: PVPkmn2()
                else:
                    Prio1=False
                    if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                    if PokemonCombat2.statut=="Gelé":
                        afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                        PVPkmn2()
                    elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                        afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                        PVPkmn2()
                    else: IAmoove()
            elif att.prio>PokemonCombat1.a3.prio:
                Prio1=False
                if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                    PVPkmn2()
                elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                    afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                    PVPkmn2()
                else: IAmoove()
            else:
                Prio1=True
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                    IAmoove()
                else: PVPkmn2()
        else:
            afficherTexte1("La capacité "+PokemonCombat1.a3.nom+" n'a plus de PP")
            canvas.after(20,resetMenu)


    ###Attaque 4###
    if event.x>815 and event.x<1015 and event.y>615 and event.y<710 and menu==1 and not (attBloquee==0 or attBloquee==4):
        afficherTexte1(PokemonCombat1.objet.nom+" de "+PokemonCombat1.nom +'\n'+"l'empêche de changer d'attaque !        ")
        canvas.after(20,resetMenu)
    if event.x>815 and event.x<1015 and event.y>615 and event.y<710 and menu==1 and (attBloquee==0 or attBloquee==4):
        if PokemonCombat1.a4.pp>0:
            afficherTexte1("")
            if PokemonCombat1.statut=="Gelé" and random.randint(1,5)==1:
                afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                PokemonCombat1.statut="None"
            if PokemonCombat1.a4.name in P.CapaDegel:
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" n'est plus gelé !        ")
                    PokemonCombat1.statut="None"
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                    PokemonCombat2.statut="None"
                    canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
            if PokemonCombat1.objet.name.startswith("Choice"):
                if attBloquee == 0:
                    attBloquee = 4
            numeroatt=4
            numeroattbis = 1
            PokemonCombat1.a4.pp-=1
            if PokemonCombat1.a4.pp==0:
                attBloquee=0
            texte_attaque4_pp = str(PokemonCombat1.a4.pp)+"/"+str(PokemonCombat1.a4.ppmax)
            canvas.itemconfig(TexteAttaque4PP, text=texte_attaque4_pp)
            damage = int(calcdamage(PokemonCombat1.a4,PokemonCombat1,PokemonCombat2))
            if damage >= PokemonCombat2.pvmax and PokemonCombat2.pv==PokemonCombat2.pvmax:
                compteursash2 = 1
            if PokemonCombat1.talent.name!="Rock Head" and PokemonCombat1.talent.name!="Magic Guard" or PokemonCombat1.talent.name!="Sheer Force":
                recul1 = damage*PokemonCombat1.a4.recul
            else: recul1 = 0
            t=PokemonCombat2.pv-damage
            soin1 = damage*PokemonCombat1.a4.soin
            pvapresrecul1 = PokemonCombat1.pv-recul1
            vit1 = PokemonCombat1.vit*modifvitclimat1*modifvit1*PokemonCombat1.objet.vitmodif
            vit2 = PokemonCombat2.vit*modifvitclimat2*modifvit2*PokemonCombat2.objet.vitmodif
            attaqueP2 = random.randint(1,4)
            if attaqueP2==1:
                att=PokemonCombat2.a1
            elif attaqueP2==2:
                att=PokemonCombat2.a2
            elif attaqueP2==3:
                att=PokemonCombat2.a3
            elif attaqueP2==4:
                att=PokemonCombat2.a4
            if att.prio==PokemonCombat1.a4.prio:
                if vit1>vit2:
                    Prio1=True
                    if PokemonCombat1.statut=="Gelé":
                        afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                        IAmoove()
                    else: PVPkmn2()
                else:
                    Prio1=False
                    if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                    if PokemonCombat2.statut=="Gelé":
                        afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                        PVPkmn2()
                    elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                        afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                        PVPkmn2()
                    else: IAmoove()
            elif att.prio>PokemonCombat1.a4.prio:
                Prio1=False
                if PokemonCombat2.statut=="Gelé" and random.randint(1,5)==1:
                        afficherTexte2(PokemonCombat2.nom+" n'est plus gelé !        ")
                        PokemonCombat2.statut="None"
                        canvas.itemconfig(statutpoke2, text ="", fill ="#81FFF5")
                if PokemonCombat2.statut=="Gelé":
                    afficherTexte2(PokemonCombat2.nom+" est gelé     ")
                    PVPkmn2()
                elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
                    afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
                    PVPkmn2()
                else: IAmoove()
            else:
                Prio1=True
                if PokemonCombat1.statut=="Gelé":
                    afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                    IAmoove()
                else: PVPkmn2()
        else:
            afficherTexte1("La capacité "+PokemonCombat1.a4.nom+" n'a plus de PP")
            canvas.after(20,resetMenu)
    if event.x>605 and event.x<805 and event.y>510 and event.y<710 and menu==0:
        #canvas.delete(RectAttaque,RectPokemon,TextePokemon,TexteAttaque)

        canvas.itemconfigure(RectAttaque, state='hidden')
        canvas.itemconfigure(TexteAttaque, state='hidden')
        canvas.itemconfigure(RectPokemon, state='hidden')
        canvas.itemconfigure(TextePokemon, state='hidden')

        canvas.itemconfigure(RectangleAttaque1, state='normal')
        canvas.itemconfigure(RectangleAttaque2, state='normal')
        canvas.itemconfigure(RectangleAttaque3, state='normal')
        canvas.itemconfigure(RectangleAttaque4, state='normal')

        canvas.itemconfigure(TexteAttaque1, state='normal')
        canvas.itemconfigure(TexteAttaque2, state='normal')
        canvas.itemconfigure(TexteAttaque3, state='normal')
        canvas.itemconfigure(TexteAttaque4, state='normal')

        canvas.itemconfigure(TexteAttaque1PP, state='normal')
        canvas.itemconfigure(TexteAttaque2PP, state='normal')
        canvas.itemconfigure(TexteAttaque3PP, state='normal')
        canvas.itemconfigure(TexteAttaque4PP, state='normal')

        canvas.itemconfigure(RectRetour, state='normal')
        canvas.itemconfigure(TexteRetour, state='normal')
        menu = 1
    elif event.x>815 and event.x<1015 and event.y>510 and event.y<710 and menu==0:

        canvas.itemconfigure(RectAttaque, state='hidden')
        canvas.itemconfigure(TexteAttaque, state='hidden')
        canvas.itemconfigure(RectPokemon, state='hidden')
        canvas.itemconfigure(TextePokemon, state='hidden')

        AffChangerPokemon()

        canvas.itemconfigure(RectRetour, state='normal')
        canvas.itemconfigure(TexteRetour, state='normal')

        menu = 2
    elif event.x>665 and event.x<965 and event.y>720 and event.y<754 and (menu==1 or (menu==2 and Poke1Mort==False) or (menu==2 and chgmpkmn1combat==False)):
        print("8")
        resetMenu()

    
    elif event.x>605 and event.x<805 and event.y>510 and event.y<565 and menu==2:
        attaqueP2 = random.randint(1,4)
        if attaqueP2==1:
            att=PokemonCombat2.a1
        elif attaqueP2==2:
            att=PokemonCombat2.a2
        elif attaqueP2==3:
            att=PokemonCombat2.a3
        elif attaqueP2==4:
            att=PokemonCombat2.a4
        afficherTexte1("")
        Pokemon1n2=Equipe1.Slot2
        if Pokemon1n2.etat=="Mort":
            afficherTexte2(Pokemon1n2.nom+" n'a plus assez "+'\n'+" de PV pour combattre       ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Magnet Pull" and (PokemonCombat1.type1=="Acier" or PokemonCombat1.type2=="Acier"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Arena Trap" and ((PokemonCombat1.type1!="Vol" or PokemonCombat1.type2!="Vol") or PokemonCombat1.talent.name!="Levitation"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Shadow Tag" and PokemonCombat1.talent.name!="Shadow Tag":
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        else : 
            if PokemonCombat1.talent.name=="Natural Cure":
                PokemonCombat1.statut="None"
                afficherTexte2(PokemonCombat1.talent.name+" le guérit de "+PokemonCombat1.statut+"    ")
            Equipe1.Slot2 = PokemonCombat1 
            ChangementPokemon(Pokemon1n2)

    elif event.x>815 and event.x<1015 and event.y>510 and event.y<565 and menu==2:
        attaqueP2 = random.randint(1,4)
        if attaqueP2==1:
            att=PokemonCombat2.a1
        elif attaqueP2==2:
            att=PokemonCombat2.a2
        elif attaqueP2==3:
            att=PokemonCombat2.a3
        elif attaqueP2==4:
            att=PokemonCombat2.a4
        afficherTexte1("")
        Pokemon1n3=Equipe1.Slot3
        if PokemonCombat2.talent.name=="Magnet Pull" and (PokemonCombat1.type1=="Acier" or PokemonCombat1.type2=="Acier"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Arena Trap" and ((PokemonCombat1.type1!="Vol" or PokemonCombat1.type2!="Vol") or PokemonCombat1.talent.name!="Levitation"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Shadow Tag" and PokemonCombat1.talent.name!="Shadow Tag":
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if Pokemon1n3.etat=="Mort":
            afficherTexte2(Pokemon1n3.nom+" n'a plus assez "+'\n'+" de PV pour combattre       ")
            canvas.after(20,resetMenu)
        else : 
            if PokemonCombat1.talent.name=="Natural Cure":
                PokemonCombat1.statut="None"
                afficherTexte2(PokemonCombat1.talent.name+" le guérit de "+PokemonCombat1.statut+"    ")
            Equipe1.Slot3 = PokemonCombat1
            ChangementPokemon(Pokemon1n3)

    elif event.x>605 and event.x<805 and event.y>575 and event.y<630 and menu==2:
        attaqueP2 = random.randint(1,4)
        if attaqueP2==1:
            att=PokemonCombat2.a1
        elif attaqueP2==2:
            att=PokemonCombat2.a2
        elif attaqueP2==3:
            att=PokemonCombat2.a3
        elif attaqueP2==4:
            att=PokemonCombat2.a4
        afficherTexte1("")
        Pokemon1n4=Equipe1.Slot4
        if PokemonCombat2.talent.name=="Magnet Pull" and (PokemonCombat1.type1=="Acier" or PokemonCombat1.type2=="Acier"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Arena Trap" and ((PokemonCombat1.type1!="Vol" or PokemonCombat1.type2!="Vol") or PokemonCombat1.talent.name!="Levitation"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Shadow Tag" and PokemonCombat1.talent.name!="Shadow Tag":
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if Pokemon1n4.etat=="Mort":
            afficherTexte2(Pokemon1n4.nom+" n'a plus assez "+'\n'+" de PV pour combattre       ")
            canvas.after(20,resetMenu)
        else : 
            if PokemonCombat1.talent.name=="Natural Cure":
                PokemonCombat1.statut="None"
                afficherTexte2(PokemonCombat1.talent.name+" le guérit de "+PokemonCombat1.statut+"    ")
            Equipe1.Slot4 = PokemonCombat1
            ChangementPokemon(Pokemon1n4)

    elif event.x>815 and event.x<1015 and event.y>575 and event.y<630 and menu==2:
        attaqueP2 = random.randint(1,4)
        if attaqueP2==1:
            att=PokemonCombat2.a1
        elif attaqueP2==2:
            att=PokemonCombat2.a2
        elif attaqueP2==3:
            att=PokemonCombat2.a3
        elif attaqueP2==4:
            att=PokemonCombat2.a4
        afficherTexte1("")
        Pokemon1n5=Equipe1.Slot5
        if PokemonCombat2.talent.name=="Magnet Pull" and (PokemonCombat1.type1=="Acier" or PokemonCombat1.type2=="Acier"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Arena Trap" and ((PokemonCombat1.type1!="Vol" or PokemonCombat1.type2!="Vol") or PokemonCombat1.talent.name!="Levitation"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Shadow Tag" and PokemonCombat1.talent.name!="Shadow Tag":
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if Pokemon1n5.etat=="Mort":
            afficherTexte2(Pokemon1n5.nom+" n'a plus assez "+'\n'+" de PV pour combattre      ")
            canvas.after(20,resetMenu)
        else : 
            if PokemonCombat1.talent.name=="Natural Cure":
                PokemonCombat1.statut="None"
                afficherTexte2(PokemonCombat1.talent.name+" le guérit de "+PokemonCombat1.statut+"    ")
            Equipe1.Slot5 = PokemonCombat1
            ChangementPokemon(Pokemon1n5)

    elif event.x>705 and event.x<905 and event.y>640 and event.y<700 and menu==2:
        attaqueP2 = random.randint(1,4)
        if attaqueP2==1:
            att=PokemonCombat2.a1
        elif attaqueP2==2:
            att=PokemonCombat2.a2
        elif attaqueP2==3:
            att=PokemonCombat2.a3
        elif attaqueP2==4:
            att=PokemonCombat2.a4
        afficherTexte1("")
        Pokemon1n6=Equipe1.Slot6
        if PokemonCombat2.talent.name=="Magnet Pull" and (PokemonCombat1.type1=="Acier" or PokemonCombat1.type2=="Acier"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Arena Trap" and ((PokemonCombat1.type1!="Vol" or PokemonCombat1.type2!="Vol") or PokemonCombat1.talent.name!="Levitation"):
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if PokemonCombat2.talent.name=="Shadow Tag" and PokemonCombat1.talent.name!="Shadow Tag":
            afficherTexte2(PokemonCombat2.talent.nom+" empêche"+'\n'+PokemonCombat1.nom+"de revenir         ")
            canvas.after(20,resetMenu)
        if Pokemon1n6.etat=="Mort":
            afficherTexte2(Pokemon1n6.nom+" n'a plus assez "+'\n'+" de PV pour combattre      ")
            canvas.after(20,resetMenu)
        else : 
            if PokemonCombat1.talent.name=="Natural Cure":
                PokemonCombat1.statut="None"
                afficherTexte2(PokemonCombat1.talent.name+" le guérit de "+PokemonCombat1.statut+"    ")
            Equipe1.Slot6 = PokemonCombat1
            ChangementPokemon(Pokemon1n6)




def changeecran(event):
    global ecran,menu,skipintro,numequipe
    global Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6
    global TexteEntree,TexteA,TexteFleche
    if event.keysym == "a":
        if skipintro:
            skipintro=False
            canvas.itemconfig(TexteIntro,text="Intro : Oui")
        else: 
            skipintro=True
            canvas.itemconfig(TexteIntro,text="Intro : Non")
    if menu==3:
        if event.keysym == "Right":
            ecran+=1
        elif event.keysym == "Left":
            ecran-=1
        if ecran>4:
            ecran=1
        if ecran<1:
            ecran=4
        if ecran==1:
            canvas.itemconfig(imageEqp,state='normal',image=imgEquipe1)
            numequipe=1
            Pokemon1n1 = EquipeJ1.Slot1
            Pokemon1n2 = EquipeJ1.Slot2
            Pokemon1n3 = EquipeJ1.Slot3
            Pokemon1n4 = EquipeJ1.Slot4
            Pokemon1n5 = EquipeJ1.Slot5
            Pokemon1n6 = EquipeJ1.Slot6
        if ecran==2:
            canvas.itemconfig(imageEqp,state='normal',image=imgEquipe2)
            numequipe=2
            Pokemon1n1 = EquipeJ2.Slot1
            Pokemon1n2 = EquipeJ2.Slot2
            Pokemon1n3 = EquipeJ2.Slot3
            Pokemon1n4 = EquipeJ2.Slot4
            Pokemon1n5 = EquipeJ2.Slot5
            Pokemon1n6 = EquipeJ2.Slot6
        if ecran==3:
            canvas.itemconfig(imageEqp,state='normal',image=imgEquipe3)
            numequipe=3
            Pokemon1n1 = EquipeJ3.Slot1
            Pokemon1n2 = EquipeJ3.Slot2
            Pokemon1n3 = EquipeJ3.Slot3
            Pokemon1n4 = EquipeJ3.Slot4
            Pokemon1n5 = EquipeJ3.Slot5
            Pokemon1n6 = EquipeJ3.Slot6
        if ecran==4:
            canvas.itemconfig(imageEqp,state='normal',image=imgEquipe4)
            numequipe=4
            Pokemon1n1 = EquipeJ4.Slot1
            Pokemon1n2 = EquipeJ4.Slot2
            Pokemon1n3 = EquipeJ4.Slot3
            Pokemon1n4 = EquipeJ4.Slot4
            Pokemon1n5 = EquipeJ4.Slot5
            Pokemon1n6 = EquipeJ4.Slot6
        if event.keysym == "Return":
            menu=0
            canvas.delete(TexteEntree)
            canvas.delete(TexteA)
            canvas.delete(TexteFleche)
            if skipintro:
                DebutCombat()
            else: Presentation()

    





######Esthétique######


    
canvas.bind("<Button-1>",changemenu1)

canvas.bind("<KeyPress>",changeecran)
canvas.focus_set()
TexteEntree = canvas.create_text(0,670, anchor =W, text ="Appuyez sur 'Entrée' pour sélectionner l'équipe", fill ="#F9FC14", font="Arial 20")
TexteA = canvas.create_text(0,710, anchor =W, text ="Appuyez sur 'A' pour Activer/Désactiver l'intro", fill ="#F9FC14", font="Arial 20")
TexteFleche = canvas.create_text(0,750, anchor =W, text ="Appuyez sur 'Flèches directionelles' pour changer d'équipe", fill ="#F9FC14", font="Arial 20")
if skipintro:
    TexteIntro = canvas.create_text(895,750, anchor =W, text ="Intro : Non", fill ="#F9FC14", font="Arial 20")
else : TexteIntro = canvas.create_text(895,750, anchor =W, text ="Intro : Oui", fill ="#F9FC14", font="Arial 20")

def CreationImagePoke2Team():
    global pkmn2n1,pkmn2n2,pkmn2n3,pkmn2n4,pkmn2n5,pkmn2n6



    pkmn2n1 = PhotoImage(file=os.path.join(image_dir,Pokemon2n1.name+"2.gif"))
    pkmn2n2 = PhotoImage(file=os.path.join(image_dir,Pokemon2n2.name+"2.gif"))
    pkmn2n3 = PhotoImage(file=os.path.join(image_dir,Pokemon2n3.name+"2.gif"))      
    pkmn2n4 = PhotoImage(file=os.path.join(image_dir,Pokemon2n4.name+"2.gif"))
    pkmn2n5 = PhotoImage(file=os.path.join(image_dir,Pokemon2n5.name+"2.gif"))
    pkmn2n6 = PhotoImage(file=os.path.join(image_dir,Pokemon2n6.name+"2.gif"))


def Presentation():
    global backgroundpst,Commentateur

    backgroundpst = PhotoImage(file=os.path.join(image_dir,"presentation.gif"))      
    canvas.create_image(0,0, anchor=NW, image=backgroundpst)

    Commentateur = PhotoImage(file=os.path.join(image_dir,"commentateur.gif"))      
    canvas.create_image(380,200, anchor=NW, image=Commentateur)

    

    pygame.mixer.stop()
    playMusiquePresentation()

    canvas.tag_raise(RectTexte)
    canvas.tag_raise(canphrase)
    canvas.itemconfigure(RectTexte,state='normal')

    afficherTexte2("Bonjour et bienvenue à cette première "+'\n'+" édition du tournoi Éther !!!            ")
    afficherTexte2("Pour commencer "+'\n'+" voici un petit rappel des règles !            ")
    afficherTexte2("Nous accueuillons aujourd'hui un challenger "+'\n'+" qui va devoir affronter les dix dresseurs "+'\n'+" sélectionés par la league !               ")
    afficherTexte2("S'il parvient à les vaincre sans une seule "+'\n'+" défaite il sera alors qualifié pour "+'\n'+" la league suivante !")
    afficherTexte2("Vous êtes prêts ? Alors c'est partit !      ")
    canvas.itemconfigure(Commentateur,state='hidden')
    DebutCombat()


def CommentateurFinCombat():
    global backgroundpst,Commentateur,TypeClimat

    TypeClimat = "Aucun"

    

    backgroundpst = PhotoImage(file=os.path.join(image_dir,"presentation.gif"))      
    canvas.create_image(0,0, anchor=NW, image=backgroundpst)

    Commentateur = PhotoImage(file=os.path.join(image_dir,"commentateur.gif"))      
    canvas.create_image(380,200, anchor=NW, image=Commentateur)

    

    pygame.mixer.stop()
    playMusiqueVictoire()

    canvas.tag_raise(RectTexte)
    canvas.tag_raise(canphrase)
    canvas.itemconfigure(RectTexte,state='normal')

    afficherTexte2("Félicitation à notre challenger"+'\n'+" qui vient de remporter ce combat !    ")
    afficherTexte2("Passons tout de suite"+'\n'+"au combat numéro "+str(numerocombat+2)+" !    ")
    canvas.itemconfigure(Commentateur,state='hidden')
    canvas.after(40,ChangementEquipeBot)


def ProchainDress():
    global pkmn1n1,pkmn1n2,pkmn1n3,pkmn1n4,pkmn1n5,pkmn1n6
    global imgpkmn1,nompokecombat1,statutpoke1,statutpoke2,imgsun,imgrain,imghail,imgsand,canimgclimat,imgpkmn2,nompokecombat2
    global Equipe1,Equipe2,PokemonCombat1,PokemonCombat2,nbPokemon1
    global Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6
    global backgroundcb
    global modifatt1,modifdefe1,modifspa1,modifspdef1,modifvit1
    global dgtpdttour1,dgtpdttour2,numeroechoue1,numeroechoue2,protect1,protect2,imun1,imun2,Poke1Mort,Poke2Mort,Poke1MortCeTour,Poke2MortCeTour,chgmpkmn1mort,chgmpkmn1combat,chgmpkmn2combat,fantomasque1,fantomasque2

    EquipeJ1 = P.Equipe(P.VenusaurT1.copy(),P.Mimikyu.copy(),P.Krookodile.copy(),P.Metagross.copy(),P.Salamence.copy(),P.Kabutops.copy())
    EquipeJ2 = P.Equipe(P.BlazikenT2.copy(),P.Togekiss.copy(),P.Tyranitar.copy(),P.Metagross.copy(),P.Snorlax.copy(),P.GyaradosT2.copy())
    EquipeJ3 = P.Equipe(P.Delphox.copy(),P.Lucario.copy(),P.GardevoirT3.copy(),P.Talonflame.copy(),P.Aurorus.copy(),P.Heliolisk.copy())
    EquipeJ4 = P.Equipe(P.Greninja.copy(),P.ZoroarkF1.copy(),P.Lucario.copy(),P.Flygon.copy(),P.Ceruledge.copy(),P.Jolteon.copy())

    nbPokemon1=6
    
    if numequipe==1:
        Pokemon1n1 = EquipeJ1.Slot1
        Pokemon1n2 = EquipeJ1.Slot2
        Pokemon1n3 = EquipeJ1.Slot3
        Pokemon1n4 = EquipeJ1.Slot4
        Pokemon1n5 = EquipeJ1.Slot5
        Pokemon1n6 = EquipeJ1.Slot6

    elif numequipe==2:
        Pokemon1n1 = EquipeJ2.Slot1
        Pokemon1n2 = EquipeJ2.Slot2
        Pokemon1n3 = EquipeJ2.Slot3
        Pokemon1n4 = EquipeJ2.Slot4
        Pokemon1n5 = EquipeJ2.Slot5
        Pokemon1n6 = EquipeJ2.Slot6
    
    elif numequipe==3:
        Pokemon1n1 = EquipeJ3.Slot1
        Pokemon1n2 = EquipeJ3.Slot2
        Pokemon1n3 = EquipeJ3.Slot3
        Pokemon1n4 = EquipeJ3.Slot4
        Pokemon1n5 = EquipeJ3.Slot5
        Pokemon1n6 = EquipeJ3.Slot6

    elif numequipe==4:
        Pokemon1n1 = EquipeJ4.Slot1
        Pokemon1n2 = EquipeJ4.Slot2
        Pokemon1n3 = EquipeJ4.Slot3
        Pokemon1n4 = EquipeJ4.Slot4
        Pokemon1n5 = EquipeJ4.Slot5
        Pokemon1n6 = EquipeJ4.Slot6

    backgroundcb = PhotoImage(file=os.path.join(image_dir,"BattleBackground.gif"))      
    canvas.create_image(0,0, anchor=NW, image=backgroundcb)



    Equipe1 = P.Equipe(Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6)
    ListPkmn1=[Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6]

    for i in ListPkmn1:
        i.a1.pp=i.a1.ppmax
        i.a2.pp=i.a2.ppmax
        i.a3.pp=i.a3.ppmax
        i.a4.pp=i.a4.ppmax

    PokemonCombat1 = Pokemon1n1

    pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
    canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
    if pcvie1>50: colorpv1 = '#15FC0E'
    elif pcvie1>25: colorpv1 = '#FB7B11'
    else: colorpv1 = '#E50404'
    canvas.itemconfigure("vieP1",fill=colorpv1)

    canvas.itemconfigure(nompokecombat1,text=PokemonCombat1.nom)
    ChangerTexturePokemon()
    
    modifatt1 = 1
    modifspa1 = 1
    modifspdef1 = 1
    modifdefe1 = 1
    modifvit1 = 1

    numeroechoue1 = 0
    numeroechoue2 = 0

    dgtpdttour1 = 100
    dgtpdttour2 = 100

    protect1 = False
    protect2 = False

    imun1=False
    imun2=False

    Poke1Mort = False
    Poke2Mort = False

    Poke1MortCeTour = False
    Poke2MortCeTour = False

    chgmpkmn1mort=False

    chgmpkmn1combat = False
    chgmpkmn2combat = False

    fantomasque1 = 1
    fantomasque2 = 1

    canvas.itemconfig(statutpoke1, text ="")

    canvas.tag_raise(RectTexte)
    canvas.tag_raise(canphrase)
    canvas.itemconfigure(RectTexte,state='normal')
    canvas.tag_raise(RectMenu)
    canvas.itemconfigure(RectMenu,state='normal')
    

    canvas.tag_raise(RectAttaque)
    canvas.tag_raise(RectPokemon)
    canvas.tag_raise(TexteAttaque)
    canvas.tag_raise(TextePokemon)

    canvas.tag_raise(canphrase)

    canvas.tag_raise(RectangleAttaque1)
    canvas.tag_raise(RectangleAttaque2)
    canvas.tag_raise(RectangleAttaque3)
    canvas.tag_raise(RectangleAttaque4)
    canvas.tag_raise(TexteAttaque1)
    canvas.tag_raise(TexteAttaque2)
    canvas.tag_raise(TexteAttaque3)
    canvas.tag_raise(TexteAttaque4)

    canvas.tag_raise(texte_attaque1_pp)
    canvas.tag_raise(TexteAttaque1PP)
    canvas.tag_raise(texte_attaque2_pp)
    canvas.tag_raise(TexteAttaque2PP)
    canvas.tag_raise(texte_attaque3_pp)
    canvas.tag_raise(TexteAttaque3PP)
    canvas.tag_raise(texte_attaque4_pp)
    canvas.tag_raise(TexteAttaque4PP)



    canvas.tag_raise(RectanglePokemon1)
    canvas.tag_raise(RectanglePokemon2)
    canvas.tag_raise(RectanglePokemon3)
    canvas.tag_raise(RectanglePokemon4)
    canvas.tag_raise(RectanglePokemon5)

    canvas.tag_raise(TextePokemon1)
    canvas.tag_raise(TextePokemon2)
    canvas.tag_raise(TextePokemon3)
    canvas.tag_raise(TextePokemon4)
    canvas.tag_raise(TextePokemon5)


    canvas.tag_raise(RectRetour)
    canvas.tag_raise(TexteRetour)

    canvas.tag_raise(imgpkmn1)
    canvas.tag_raise(imgpkmn2)

    canvas.tag_raise(barrebgVieP1)
    canvas.tag_raise(barrebgVieP2)

    canvas.tag_raise(barrevieP1)
    canvas.tag_raise(barrevieP2)

    canvas.tag_raise(nompokecombat1)
    canvas.tag_raise(nompokecombat2)

    canvas.tag_raise(statutpoke1)
    canvas.tag_raise(statutpoke2)


    canvas.itemconfigure(nompokecombat1,text=PokemonCombat1.nom)

    pygame.mixer.stop()
    playMusiqueCombat()


    EntreePokemon1()
 


def DebutCombat():
    global pkmn1n1,pkmn1n2,pkmn1n3,pkmn1n4,pkmn1n5,pkmn1n6
    global imgpkmn1,nompokecombat1,statutpoke1,statutpoke2,imgsun,imgrain,imghail,imgsand,canimgclimat,imgpkmn2,nompokecombat2
    global Equipe1,Equipe2,PokemonCombat1,PokemonCombat2
    global Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6
    global backgroundcb
    global barrebgVieP1,barrebgVieP2,barrevieP1,barrevieP2
    
    backgroundcb = PhotoImage(file=os.path.join(image_dir,"BattleBackground.gif"))      
    canvas.create_image(0,0, anchor=NW, image=backgroundcb)

    

    Equipe1 = P.Equipe(Pokemon1n1,Pokemon1n2,Pokemon1n3,Pokemon1n4,Pokemon1n5,Pokemon1n6)
    Equipe2 = P.Equipe(Pokemon2n1,Pokemon2n2,Pokemon2n3,Pokemon2n4,Pokemon2n5,Pokemon2n6)

    PokemonCombat1 = Pokemon1n1
    PokemonCombat2 = Pokemon2n1

    
    canvas.tag_raise(RectTexte)
    canvas.tag_raise(canphrase)
    canvas.itemconfigure(RectTexte,state='normal')
    canvas.tag_raise(RectMenu)
    canvas.itemconfigure(RectMenu,state='normal')
    

    canvas.tag_raise(RectAttaque)
    canvas.tag_raise(RectPokemon)
    canvas.tag_raise(TexteAttaque)
    canvas.tag_raise(TextePokemon)

    canvas.tag_raise(canphrase)

    canvas.tag_raise(RectangleAttaque1)
    canvas.tag_raise(RectangleAttaque2)
    canvas.tag_raise(RectangleAttaque3)
    canvas.tag_raise(RectangleAttaque4)
    canvas.tag_raise(TexteAttaque1)
    canvas.tag_raise(TexteAttaque2)
    canvas.tag_raise(TexteAttaque3)
    canvas.tag_raise(TexteAttaque4)

    canvas.tag_raise(texte_attaque1_pp)
    canvas.tag_raise(TexteAttaque1PP)
    canvas.tag_raise(texte_attaque2_pp)
    canvas.tag_raise(TexteAttaque2PP)
    canvas.tag_raise(texte_attaque3_pp)
    canvas.tag_raise(TexteAttaque3PP)
    canvas.tag_raise(texte_attaque4_pp)
    canvas.tag_raise(TexteAttaque4PP)



    canvas.tag_raise(RectanglePokemon1)
    canvas.tag_raise(RectanglePokemon2)
    canvas.tag_raise(RectanglePokemon3)
    canvas.tag_raise(RectanglePokemon4)
    canvas.tag_raise(RectanglePokemon5)

    canvas.tag_raise(TextePokemon1)
    canvas.tag_raise(TextePokemon2)
    canvas.tag_raise(TextePokemon3)
    canvas.tag_raise(TextePokemon4)
    canvas.tag_raise(TextePokemon5)


    canvas.tag_raise(RectRetour)
    canvas.tag_raise(TexteRetour)

    
    print("9")
    resetMenu()


    CreationImagePoke2Team()
    pkmn1n1 = PhotoImage(file=os.path.join(image_dir,Pokemon1n1.name+"1.gif"))
    pkmn1n2 = PhotoImage(file=os.path.join(image_dir,Pokemon1n2.name+"1.gif"))
    pkmn1n3 = PhotoImage(file=os.path.join(image_dir,Pokemon1n3.name+"1.gif"))      
    pkmn1n4 = PhotoImage(file=os.path.join(image_dir,Pokemon1n4.name+"1.gif"))
    pkmn1n5 = PhotoImage(file=os.path.join(image_dir,Pokemon1n5.name+"1.gif"))
    pkmn1n6 = PhotoImage(file=os.path.join(image_dir,Pokemon1n6.name+"1.gif"))


    imgpkmn1 = canvas.create_image(175,450, anchor=NW, image=pkmn1n1) 
    barrebgVieP1 = canvas.create_rectangle(200, 410, 400, 425,fill='#000000',tag="bgVieP1")
    barrevieP1 = canvas.create_rectangle(202, 412, 198+pcvie1*2, 423,fill=colorpv1,tag="vieP1")
    nompokecombat1 = canvas.create_text(202,400, anchor =W, text =PokemonCombat1.nom, fill ="black", font="Arial 13")

    statutpoke1 = canvas.create_text(302,400, text ="", fill ="#FC610E", font="Arial 13")
    statutpoke2 = canvas.create_text(717,145, text ="", fill ="#FC610E", font="Arial 13")



    imgsun = PhotoImage(file=os.path.join(image_dir,"vivillon_sun.gif"))
    imgrain = PhotoImage(file=os.path.join(image_dir,"vivillon_rain.gif"))
    imghail = PhotoImage(file=os.path.join(image_dir,"vivillon_hail.gif"))      
    imgsand = PhotoImage(file=os.path.join(image_dir,"vivillon_sandstorm.gif"))

    canimgclimat = canvas.create_image(1500,10, anchor=NW, image=imgsand)



    imgpkmn2 = canvas.create_image(570,200, anchor=NW, image=pkmn2n1)
    barrebgVieP2 = canvas.create_rectangle(575, 155, 775, 170,fill='#000000',tag="bgVieP2")
    barrevieP2 = canvas.create_rectangle(577, 157, 573+pcvie2*2, 167,fill=colorpv2,tag="vieP2")
    nompokecombat2 = canvas.create_text(577,145, anchor =W, text =PokemonCombat2.nom, fill ="white", font="Arial 13")
    pygame.mixer.stop()
    playMusiqueCombat()


    EntreePokemon1()
    EntreePokemon2()


    """ affmodifatt1 = canvas.create_text(10,125, anchor =W, text ="Stat attaque "+PokemonCombat1.nom+" : x"+str(modifatt1), fill ="black", font="Arial 15")
    affmodifdefe1 = canvas.create_text(10,145, anchor =W, text ="Stat défense "+PokemonCombat1.nom+" : x"+str(modifdefe1), fill ="black", font="Arial 15")
    affmodifspa1 = canvas.create_text(10,165, anchor =W, text ="Stat attaque spéciale "+PokemonCombat1.nom+" : x"+str(modifspa1), fill ="black", font="Arial 15")
    affmodifspedef1 = canvas.create_text(10,185, anchor =W, text ="Stat défense spéciale "+PokemonCombat1.nom+" : x"+str(modifspdef1), fill ="black", font="Arial 15")
    affmodifvit1 = canvas.create_text(10,205, anchor =W, text ="Stat vitesse "+PokemonCombat1.nom+" : x"+str(modifvit1), fill ="black", font="Arial 15")


    affmodifatt2 = canvas.create_text(10,265, anchor =W, text ="Stat attaque "+PokemonCombat2.nom+" : x"+str(modifatt2), fill ="black", font="Arial 15")
    affmodifdefe2 = canvas.create_text(10,285, anchor =W, text ="Stat défense "+PokemonCombat2.nom+" : x"+str(modifdefe2), fill ="black", font="Arial 15")
    affmodifspa2 = canvas.create_text(10,305, anchor =W, text ="Stat attaque spéciale "+PokemonCombat2.nom+" : x"+str(modifspa2), fill ="black", font="Arial 15")
    affmodifspedef2 = canvas.create_text(10,325, anchor =W, text ="Stat défense spéciale "+PokemonCombat2.nom+" : x"+str(modifspdef2), fill ="black", font="Arial 15")
    affmodifvit2 = canvas.create_text(10,345, anchor =W, text ="Stat vitesse "+PokemonCombat2.nom+" : x"+str(modifvit2), fill ="black", font="Arial 15") """

    
pygame.mixer.init()
def playMusiqueCombat():
    pygame.mixer.music.load(os.path.join(musique_dir,"first-battle-trainer.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)

def playMusiqueEcran():
    pygame.mixer.music.load(os.path.join(musique_dir,"menu.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)

def playMusiquePresentation():
    pygame.mixer.music.load(os.path.join(musique_dir,"commentateur.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)

def playMusiqueVictoire():
    pygame.mixer.music.load(os.path.join(musique_dir,"Victory.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)

def playMusiqueVictoireFinale():
    pygame.mixer.music.load(os.path.join(musique_dir,"VictoryFinal.mp3"))
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.05)

playMusiqueEcran()














###################Boucle PV##########################







def PVPkmn1():
    global menu,d,colorpv1,PokemonCombat1,nomatt2,Prio1,numeroechoue2,dgtpdttour2,fantomasque1,compteursash1,compteurmodifatt2
    if d==PokemonCombat1.pv and numeroechoue2 == 1:
        afficherTexte2("Mais cela échoue !      ")
        numeroechoue2 = 0
    if fantomasque1==0:
        fantomasque1 = 99
        afficherTexte2(PokemonCombat1.talent.nom+" de "+PokemonCombat1.nom+" le protège !    ")
    if protect1==True:
        afficherTexte2(PokemonCombat1.nom+" se protège !    ")
    if compteursash1==1 and PokemonCombat1.objet.name=="Focus Sash":
        d=8
        compteursash1=0
        PokemonCombat1.objet=P.NoItem.copy()
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv>d and protect1==False:
            dgtpdttour2-=1
            if PokemonCombat1.pv>d+45 and PokemonCombat1.pv>20:
                PokemonCombat1.pv-=4
            else: PokemonCombat1.pv-=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1)
            canvas.update()
        else :
            if PokemonCombat2.pv>pvapresrecul2:
                afficherTexte2(PokemonCombat2.nom+" se blesse en frappant     ")
            PVPkmn2Recul()
    else:
        if PokemonCombat2.talent.name=="Moxie":
            afficherTexte2(PokemonCombat2.talent.nom+" augmente son attaque      ")
            compteurmodifatt2+=1
        Pokemon1Dead()
        PVPkmn2Recul()
        
                
def FinPVPkmn1():
    if Prio1:
        FinDuTour()
    else:
        if PokemonCombat1.statut=="Appeuré":
                afficherTexte2(PokemonCombat1.nom+" n'a pas pu attaquer     ")
                PokemonCombat1.statut="None"
                FinDuTour()
        elif PokemonCombat1.statut=="Gelé":
                afficherTexte2(PokemonCombat1.nom+" est gelé     ")
                FinDuTour()
        else:
            if not Poke2Mort:
                if PokemonCombat1.statut=="Appeuré":
                    PokemonCombat1.statut="None"
                PVPkmn2()


def PVPkmn1FT():
    global menu,ft1,colorpv1,PokemonCombat1,Prio1
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv>ft1 :
            PokemonCombat1.pv-=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1FT)
            canvas.update()
        else :
            if not Prio1:
                if not Poke2Mort:
                    if PokemonCombat2.statut=="Brûlé" and PokemonCombat2.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat2.nom+" subit des dégats de la brûlure     ")
                    elif (PokemonCombat2.statut=="Empoisonné" or PokemonCombat2.statut=="Gravement Empoisonné") and PokemonCombat2.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat2.nom+" subit des dégats du poison     ")
                    PVPkmn2FT()
            else:
                DgtClimat()
    else: 
        if Poke1Mort != True:
            Pokemon1Dead()
        if not Prio1:
            if not Poke2Mort:
                if PokemonCombat2.statut=="Brûlé" and PokemonCombat2.talent.name!="Magic Guard":
                    afficherTexte2(PokemonCombat2.nom+" subit des dégats de la brûlure     ")
                elif (PokemonCombat2.statut=="Empoisonné" or PokemonCombat2.statut=="Gravement Empoisonné") and PokemonCombat2.talent.name!="Magic Guard":
                    afficherTexte2(PokemonCombat2.nom+" subit des dégats du poison     ")
                PVPkmn2FT()
        else:
            DgtClimat()


def PVPkmn2FT():
    global menu,ft2,colorpv2,PokemonCombat2,Prio1
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv>ft2 :
            PokemonCombat2.pv-=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2FT)
            canvas.update()
        else:
            if Prio1:
                if not Poke1Mort:
                    if PokemonCombat1.statut=="Brûlé" and PokemonCombat1.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat1.nom+" subit des dégats de la brûlure     ")
                        if (PokemonCombat1.statut=="Empoisonné" or PokemonCombat1.statut=="Gravement Empoisonné") and PokemonCombat1.talent.name!="Magic Guard":
                            afficherTexte2(PokemonCombat1.nom+" subit des dégats du poison     ")
                    PVPkmn1FT()
            else:
                DgtClimat()
    else:
        if Poke2Mort != True:
            Pokemon2Dead()
        if Prio1:
            if not Poke1Mort:
                if PokemonCombat1.statut=="Brûlé" and PokemonCombat1.talent.name!="Magic Guard":
                    afficherTexte2(PokemonCombat1.nom+" subit des dégats de la brûlure     ")
                    if (PokemonCombat1.statut=="Empoisonné" or PokemonCombat1.statut=="Gravement Empoisonné") and PokemonCombat1.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat1.nom+" subit des dégats du poison     ")
                PVPkmn1FT()
        else:
            DgtClimat()






def PVPkmn1Obj():
    global menu,ft1,colorpv1,PokemonCombat1,Prio1
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv>ft1:
            PokemonCombat1.pv-=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1Obj)
            canvas.update()
        else :
            if not Prio1:
                if not Poke2Mort:
                    if PokemonCombat2.objet.name=="Life Orb" and compteurattdgt2==2 and dgtpdttour2<100 and PokemonCombat2.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat2.objet.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
                    PVPkmn2Obj()
            else:
                SoinObj()
    else:
        if Poke1Mort != True:
            Pokemon1Dead()
        if not Prio1:
            if not Poke2Mort:
                if PokemonCombat2.objet.name=="Life Orb" and compteurattdgt2==2 and dgtpdttour2<100 and PokemonCombat2.talent.name!="Magic Guard":
                    afficherTexte2(PokemonCombat2.objet.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
                PVPkmn2Obj()
        else:
            SoinObj()



def PVPkmn2Obj():
    global menu,ft2,colorpv2,PokemonCombat2,Prio1
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv>ft2:
            PokemonCombat2.pv-=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2Obj)
            canvas.update()
        else:
            if Prio1:
                if not Poke1Mort:
                    if PokemonCombat1.objet.name=="Life Orb" and compteurattdgt1==2 and dgtpdttour1<100 and PokemonCombat1.talent.name!="Magic Guard":
                        afficherTexte2(PokemonCombat1.objet.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
                    PVPkmn1Obj()
            else:
                SoinObj()
    else: 
        if Poke2Mort != True:
            Pokemon2Dead()
        if Prio1:
            if not Poke1Mort:
                if PokemonCombat1.objet.name=="Life Orb" and compteurattdgt1==2 and dgtpdttour1<100 and PokemonCombat1.talent.name!="Magic Guard":
                    afficherTexte2(PokemonCombat1.objet.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
                PVPkmn1Obj()
        else:
            SoinObj()







def GainPVPkmn1Obj():
    global menu,gainpv1,colorpv1,PokemonCombat1,Prio1
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv<gainpv1:
            PokemonCombat1.pv+=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,GainPVPkmn1Obj)
            canvas.update()
        else :
            if not Prio1:
                if not Poke2Mort:
                    if PokemonCombat2.objet.name=="Leftovers" and PokemonCombat2.pv<PokemonCombat2.pvmax:
                        afficherTexte2(PokemonCombat2.objet.nom+" de " +PokemonCombat2.nom+'\n'+"le soigne    ")
                    GainPVPkmn2Obj()



def GainPVPkmn2Obj():
    global menu,gainpv2,colorpv2,PokemonCombat2,Prio1
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv<gainpv2:
            PokemonCombat2.pv+=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,GainPVPkmn2Obj)
            canvas.update()
        else:
            if Prio1:
                if not Poke1Mort:
                    if PokemonCombat1.objet.name=="Leftovers" and PokemonCombat1.pv<PokemonCombat1.pvmax:
                        afficherTexte2(PokemonCombat1.objet.nom+" de " +PokemonCombat1.nom+'\n'+"le soigne    ")
                    GainPVPkmn1Obj()






def PVPkmn1CD():
    global menu,ft1,colorpv1,PokemonCombat1,Prio1
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv>ft1:
            PokemonCombat1.pv-=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1CD)
            canvas.update()
        else :
            if not Prio1:
                if not Poke2Mort:
                    if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Solar Power":
                        afficherTexte2(PokemonCombat2.talent.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
                    PVPkmn2CD()
            else:
                DgtObj()
    else:
        if Poke1Mort != True:
            Pokemon1Dead()
        if not Prio1:
            if not Poke2Mort:
                if TypeClimat=="Sun" and PokemonCombat2.talent.name=="Solar Power":
                    afficherTexte2(PokemonCombat2.talent.nom+" de " +PokemonCombat2.nom+'\n'+"lui inflige des dégats     ")
                PVPkmn2CD()
        else:
            DgtObj()



def PVPkmn2CD():
    global menu,ft2,colorpv2,PokemonCombat2,Prio1
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv>ft2:
            PokemonCombat2.pv-=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2CD)
            canvas.update()
        else:
            if Prio1:
                if not Poke1Mort:
                    if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Solar Power":
                        afficherTexte2(PokemonCombat1.talent.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
                    PVPkmn1CD()
            else:
                DgtObj()
    else:
        if Poke2Mort != True:
            Pokemon2Dead()
        if Prio1:
            if not Poke1Mort:
                if TypeClimat=="Sun" and PokemonCombat1.talent.name=="Solar Power":
                    afficherTexte2(PokemonCombat1.talent.nom+" de " +PokemonCombat1.nom+'\n'+"lui inflige des dégats     ")
                PVPkmn1CD()
        else:
            DgtObj()








def PVPkmn1Recul():
    global menu,recul,colorpv1,PokemonCombat1,Prio1,pvapresrecul1,soin1,pvapressoin1
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv>pvapresrecul1 :
            PokemonCombat1.pv-=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1Recul)
            canvas.update()
        else:
            pvapressoin1 = PokemonCombat1.pv+soin1
            if pvapressoin1>PokemonCombat1.pvmax:
                pvapressoin1=PokemonCombat1.pvmax
            PVPkmn1SoinAtt()
    else: 
        if Poke1Mort != True:
            Pokemon1Dead()


def PVPkmn1SoinAtt():
    global menu,recul,colorpv1,PokemonCombat1,Prio1,pvapressoin1,Poke2MortCeTour,chgmpkmn1combat
    if PokemonCombat1.pv>5:
        if PokemonCombat1.pv<pvapressoin1 :
            PokemonCombat1.pv+=1
            pcvie1 = (PokemonCombat1.pv/PokemonCombat1.pvmax)*100
            canvas.coords("vieP1",202, 412, 198+pcvie1*2, 423)
            if pcvie1>50: colorpv1 = '#15FC0E'
            elif pcvie1>25: colorpv1 = '#FB7B11'
            else: colorpv1 = '#E50404'
            canvas.itemconfigure("vieP1",fill=colorpv1)
            canvas.after(20,PVPkmn1SoinAtt)
            canvas.update()
        else:
            if chgmpkmn1combat==True:
                    canvas.after(30,ChangementPokemonAttaque)
            else:
                if Poke2MortCeTour == False:
                    canvas.after(30,FinPVPkmn2)
                else:
                    canvas.after(30,FinDuTour)    
                    Poke2MortCeTour = False


def PVPkmn2Recul():
    global menu,recul,colorpv2,PokemonCombat2,Prio1,pvapresrecul2,pvapressoin2,soin2
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv>pvapresrecul2:
            PokemonCombat2.pv-=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2Recul)
            canvas.update()
        else:
            pvapressoin2 = PokemonCombat2.pv+soin2
            if pvapressoin2>PokemonCombat2.pvmax:
                pvapressoin2=PokemonCombat2.pvmax
            PVPkmn2SoinAtt()
    else:
        if Poke2Mort != True: 
            Pokemon2Dead()



def PVPkmn2SoinAtt():
    global menu,soin,colorpv2,PokemonCombat2,Prio1,pvapressoin2,Poke1MortCeTour,chgmpkmn1combat
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv<pvapressoin2:
            PokemonCombat2.pv+=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2SoinAtt)
            canvas.update()
        else:
            if chgmpkmn2combat==True:
                canvas.after(30,ChangementAttaquePokemon2)
            else:
                if Poke1MortCeTour == False:
                    canvas.after(30,FinPVPkmn1)
                else:    
                    canvas.after(30,FinDuTour)






def PVPkmn2():
    global menu,t,colorpv2,PokemonCombat2,nomatt2,Prio1,numeroatt,numeroattbis,numeroechoue1,pvapresrecul1,dgtpdttour1,fantomasque2,compteursash2,compteurmodifatt1
    if numeroatt==1 and numeroattbis == 1:
        numeroattbis = 0
        afficherTexte2(PokemonCombat1.nom+" utilise "+PokemonCombat1.a1.nom+"     ")
    elif numeroatt==2 and numeroattbis == 1:
        numeroattbis = 0
        afficherTexte2(PokemonCombat1.nom+" utilise "+PokemonCombat1.a2.nom+"     ")
    elif numeroatt==3 and numeroattbis == 1:
        numeroattbis = 0
        afficherTexte2(PokemonCombat1.nom+" utilise "+PokemonCombat1.a3.nom+"     ")
    elif numeroatt==4 and numeroattbis == 1:
        numeroattbis = 0
        afficherTexte2(PokemonCombat1.nom+" utilise "+PokemonCombat1.a4.nom+"     ")
    if t==PokemonCombat2.pv and numeroechoue1 == 1:
        afficherTexte2("Mais cela échoue !      ")
    if fantomasque2==0:
        fantomasque2 = 99
        afficherTexte2(PokemonCombat2.talent.nom+" de "+PokemonCombat2.nom+" le protège !    ")
    if protect2==True:
        afficherTexte2(PokemonCombat2.nom+" se protège !    ")
    if compteursash2 == 1 and PokemonCombat2.objet.name=="Focus Sash":
        afficherTexte2(PokemonCombat2.nom+" résiste grâce à sa "+PokemonCombat2.objet.nom+"     ")
        t=6
        compteursash2=0
        PokemonCombat2.objet=P.NoItem.copy()
    if PokemonCombat2.pv>5:
        if PokemonCombat2.pv>t and protect2==False:
            dgtpdttour1-=1
            if PokemonCombat2.pv>t+45 and PokemonCombat2.pv>20:
                PokemonCombat2.pv-=4
            else: PokemonCombat2.pv-=1
            pcvie2 = (PokemonCombat2.pv/PokemonCombat2.pvmax)*100
            canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
            if pcvie2>50: colorpv2 = '#15FC0E'
            elif pcvie2>25: colorpv2 = '#FB7B11'
            else: colorpv2 = '#E50404'
            canvas.itemconfigure("vieP2",fill=colorpv2)
            canvas.after(20,PVPkmn2)
            canvas.update()
        else:
            if numeroatt==1 and numeroechoue1 != 1:
                AppliEffet1(PokemonCombat1.a1,PokemonCombat1.a1.effet)
            elif numeroatt==2 and numeroechoue1 != 1:
                AppliEffet1(PokemonCombat1.a2,PokemonCombat1.a2.effet)
            elif numeroatt==3 and numeroechoue1 != 1:
                AppliEffet1(PokemonCombat1.a3,PokemonCombat1.a3.effet)
            elif numeroatt==4 and numeroechoue1 != 1:
                AppliEffet1(PokemonCombat1.a4,PokemonCombat1.a4.effet)
            if not Poke1Mort:
                if PokemonCombat1.pv>pvapresrecul1:
                    afficherTexte2(PokemonCombat1.nom+" se blesse en frappant     ")
                PVPkmn1Recul()
    else:
        if PokemonCombat1.talent.name=="Moxie":
            afficherTexte2(PokemonCombat1.talent.nom+" augmente son attaque      ")
            compteurmodifatt1+=1
        Pokemon2Dead()
        if not Poke1Mort:
            if PokemonCombat1.pv>pvapresrecul1:
                afficherTexte2(PokemonCombat1.nom+" se blesse en frappant     ")
        PVPkmn1Recul()
    numeroechoue1 = 0

def FinPVPkmn2():
    if Prio1:
        if PokemonCombat2.statut=="Appeuré":
            afficherTexte2(PokemonCombat2.nom+" n'a pas pu attaquer     ")
            PokemonCombat2.statut="None"
            FinDuTour()
        elif PokemonCombat2.statut=="Gelé":
            afficherTexte2(PokemonCombat2.nom+" est gelé     ")
            FinDuTour()
        elif PokemonCombat2.statut=="Paralysé" and random.randint(1,4)==2:
            afficherTexte2(PokemonCombat2.nom+" est paralysé et n'a pas pu attaquer      ")
            FinDuTour()
        else:
            if PokemonCombat2.statut=="Appeuré":
                PokemonCombat2.statut="None"
            IAmoove()
    else:
        FinDuTour()



def AfficherVie(ViePokemon,VieMax,VieDgt):
    if ViePokemon>VieDgt:
        ViePokemon-=1
        pcvie2 = (ViePokemon/VieMax)*100
        canvas.coords("vieP2",577, 157, 573+pcvie2*2, 167)
        canvas.itemconfigure("vieP2",fill=colorpv2)
        canvas.update()
        canvas.after(50,AfficherVie(ViePokemon,VieMax,VieDgt))

def PVPkmn(Att,Pokemon1,Pokemon2):
    global menu,t,colorpv2
    dgt = int(calcdamage(Att,Pokemon1,Pokemon2))
    Vie = Pokemon1.pv-dgt
    AfficherVie(Pokemon1.pv,Pokemon1.pvmax,Vie)
        
#PVPkmn1()
#PVPkmn2()








root.mainloop()  