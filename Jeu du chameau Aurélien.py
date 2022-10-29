from random import *

KM_VOYAGE = 300 # Distance a parcourir pour gagner.
AVANCER_NORM_MIN = 10 # Nombre min. de km à la vitesse normale.
AVANCER_NORM_MAX = 15 # Nombre max. de km à la vitesse normale.
AVANCER_RAP_MIN = 20 # Nombre min. de km à toute vitesse.
AVANCER_RAP_MAX = 25 # Nombre max. de km à toute vitesse.
AVANTAGE_VOYAGEUR = 20 # L’avantage initiale du voyageur par rapport aux ennemis.
GOURDE_PLEINE = 12 # La capacité de la gourde en nombre de gorgés.
GOURDE_DEPART = GOURDE_PLEINE // 2 # Nombre de gorgés au départ.
MORT_FATIGUE = 4 # Nombre de tours avant mourir de fatigue.
MORT_SOIF = 4 # Nombre de tours avant mourir de soif.
DIFF_AIDE = 3 # Difficulté pour trouver de l’aide.
AVANCE_ENNEMIS = 4 # La fréquence d’avancement des ennemis : deux fois sur quatre.


def affiche_intro():
    print("JEU DU CHAMEAU !\nVous avez volé un chameau pour traverser le grand désert.\nVos ennemis veulent le récupérer.\nVotre objectif est de survivre à la traversée de 300 km sans être attrapé(e).")
    
def affiche_gagne():
    print("Félicitations ! Vous avez gagné(e) !")
    terminer=True
    
def affiche_perdu():
    print("Vous avez perdu(e)...")
    terminer=True
    
def affiche_options():
    print("OPTIONS :\n1.Boire\n2.Avancer normalement\n3.Avancer à toute allure\n4.Se reposer\n5.Espérer de l'aide\n6.Quitter la partie\n\n")
    
def affiche_gourde(gourde):
    n=int(gourde)
    if n<1:
        print("Votre gourde est vide.")
    elif n==1:
        print("Votre gourde contient 1 gorgée.")
    elif n>=2 and n<=GOURDE_PLEINE:
        print("Votre gourde contient "+str(n)+" gorgées.")
    elif n==GOURDE_PLEINE:
        print("Votre gourde est pleine.")
    return gourde
        
def affiche_km(km_voyageur,km_ennemis):
    a=km_voyageur
    b=km_ennemis
    #distance=a-b
    if "a">"b" and a<KM_VOYAGE:
        print("Vous avez voyagé un total de "+str(a)+"km jusqu'ici.\nVos ennemis sont "+str(a-b)+"km derrière vous.")
    elif "a"<"b":
        print("Vous avez voyagé un total de "+str(a)+"km jusqu'ici.\nVos ennemis vous ont attrapés, vous finissez au cachot.")
        affiche_perdu()
    elif a>=KM_VOYAGE:
        print("Bien joué ! Vous avez traversé le desert !")
        
def affiche_km2(km_voyageur, km_ennemis):
    a=km_voyageur
    b=km_ennemis
    if a<KM_VOYAGE:
        if a<b or a==b :
            print("Vous avez voyagé un total de "+str(a)+"km jusqu'ici.\nVos ennemis vous ont attrapés, vous finissez au cachot.")
            affiche_perdu()
        else:
            print("Vous avez voyagé un total de "+str(a)+"km jusqu'ici.\nVos ennemis sont "+str(a-b)+"km derrière vous.")
    else:
        print("Bien joué ! Vous avez traversé le desert !")
        affiche_gagne()
    return km_voyageur
    return km_ennemis
    
def affiche_fatigue(fatigue):
    if fatigue/MORT_FATIGUE*100<20:
        print("Votre chameau est en bonne forme.")
    elif fatigue/MORT_FATIGUE*100<40 and fatigue/MORT_FATIGUE*100>=20:
        print("Votre chameau est un peu fatigué.")
    elif fatigue/MORT_FATIGUE*100<60 and fatigue/MORT_FATIGUE*100>=40:
        print("Votre chameau est fatigué.")
    elif fatigue/MORT_FATIGUE*100<80 and fatigue/MORT_FATIGUE*100>=60:
        print("Votre chameau est très fatigué !")
    elif fatigue/MORT_FATIGUE*100<=100 and fatigue/MORT_FATIGUE*100>=80:
        print("Votre chameau va mourir de fatigue.. Reposez vous dès que possible !")
    elif fatigue/MORT_FATIGUE*100>100:
        print("Votre chameau est mort de fatigue. Vous auriez du vous reposer.")
        affiche_perdu()
        terminer=True
    return fatigue
        
def affiche_soif(soif):
    if soif/MORT_SOIF*100<20:
        print("Vous n'avez pas soif.")
    elif soif/MORT_SOIF*100<40 and soif/MORT_SOIF*100>=20:
        print("Vous commencez a avoir un peu soif.")
    elif soif/MORT_SOIF*100<60 and soif/MORT_SOIF*100>=40:
        print("Vous avez soif.")
    elif soif/MORT_SOIF*100<80 and soif/MORT_SOIF*100>=60:
        print("Vous avez très soif.")
    elif soif/MORT_SOIF*100<=100 and soif/MORT_SOIF*100>=80:
        print("Vous êtes assoifé(e) ! Buvez dès que possible !")
    elif soif/MORT_SOIF*100>100:
        print("Vous êtes mort de soif. Vous auriez du boire...")
        affiche_perdu()
        terminer=True
    return soif

    
def repose(soif):
    soif=soif+1
    fatigue=0
    print("Votre chameau s'est bien reposé. Il est en pleine forme !")
    print("La fatigue de votre chameau est donc maintenant à 0.")
    print("Votre soif est à "+str(soif)+".")
    return soif
    
def boit(gourde, soif):
    if gourde>=1:
        gourde=gourde-1
        soif=0
        print("Vous avez bu une gorgée d'eau, vous vous sentez mieux.")
        print("Il vous reste "+str(gourde)+" gorgée(s) d'eau dans votre gourde.")
        print("Votre niveau de soif est à 0.")
    else:
        print("Malheureusement votre gourde est vide.. Il est donc impossible pour vous de boire.\nTentez de trouver un oasis afin de la remplir, ou vous mourrez..")
        print("Votre gourde contient 0 gorgée(s) d'eau.")
        print("votre niveau de soif est à "+str(soif)+".")
    return gourde
    return soif
        
def avance_voyageur(km_voyageur, fatigue, soif):
    avance_km_voyageur=randrange(AVANCER_NORM_MIN, AVANCER_NORM_MAX+1)
    km_voyageur=km_voyageur+avance_km_voyageur
    fatigue=fatigue+1
    soif=soif+1
    print("Vous avez parcouru "+str(avance_km_voyageur)+"km de plus, vous avez parcouru "+str(km_voyageur)+"km au total.")
    print("Votre fatigue est à "+str(fatigue)+".")
    print("Votre soif est à "+str(soif)+".")
    return km_voyageur
    return fatigue
    return soif

def avance_voyageur2(km_voyageur, fatigue, soif):
    avance_km_voyageur=randrange(AVANCER_RAP_MIN, AVANCER_RAP_MAX+1)
    km_voyageur=km_voyageur+avance_km_voyageur
    fatigue=fatigue+2
    soif=soif+1
    print("Vous avez parcouru "+str(avance_km_voyageur)+"km de plus, vous avez parcouru "+str(km_voyageur)+"km au total.")
    print("Votre fatigue est à "+str(fatigue)+".")
    print("Votre soif est à "+str(soif)+".")
    return km_voyageur
    return fatigue
    return soif
        
def cherche_aide(gourde, fatigue, soif):
    x=randrange(0,DIFF_AIDE+1)
    fatigue=fatigue+1
    soif=soif+1
    if x==0:
        print("Vous avez trouver de l'aide, quelle chance !")
        if gourde<=8:
            gourde=gourde+3
            print("Votre gourde a récupéré 3 gorgées d'eau, bonne chance pour le reste du voyage.")
            print("Votre gourde dispose dès à présent de "+str(gourde)+" gorgées d'eau.")
            print("Votre fatigue est à "+str(fatigue)+".")
            print("Votre soif est à "+str(soif)+".")
        elif gourde==9:
            gourde=gourde+3
            print("Votre gourde a été remplie, bonne chance pour le reste du voyage.")
            print("Votre gourde dispose dès à présent de "+str(gourde)+" gorgées d'eau.")
            print("Votre fatigue est à "+str(fatigue)+".")
            print("Votre soif est à "+str(soif)+".")
        elif gourde==10:
            gourde=gourde+2
            print("Votre gourde a été remplie, bonne chance pour le reste du voyage.")
            print("Votre gourde dispose dès à présent de "+str(gourde)+" gorgées d'eau.")
            print("Votre fatigue est à "+str(fatigue)+".")
            print("Votre soif est à "+str(soif)+".")
        elif gourde==11:
            gourde=gourde+1
            print("Votre gourde à été remplie, bonne chance pour le reste du voyage.")
            print("Votre gourde dispose dès à présent de "+str(gourde)+" gorgées d'eau.")
            print("Votre fatigue est à "+str(fatigue)+".")
            print("Votre soif est à "+str(soif)+".")
        elif gourde==12:
            print("Malheureusement (dans ce cas) votre gourde est pleine.. Il est donc inutile d'essayer de la remplir.\nVous aurez sûrement plus de chance la prochaine fois, bonne chance pour le reste du voyage.")
            print("Votre gourde dispose de "+str(gourde)+" gorgées d'eau.")
            print("Votre fatigue est à "+str(fatigue)+".")
            print("Votre soif est à "+str(soif)+".")
    else:
        print("Vous n'avez pas trouvé d'aide.. Vous aurez sans doute plus de chance la prochaine fois.")
        print("Votre gourde contient "+str(gourde)+" gorgée(s) d'eau.")
        print("Votre fatigue est à "+str(fatigue)+".")
        print("Votre soif est à "+str(soif)+".")
    return gourde
    return fatigue
    return soif
        
def avance_ennemis(km_ennemis):
    x=randrange(0, AVANCE_ENNEMIS)
    if x==0:
        y=randrange(AVANCER_NORM_MIN, AVANCER_NORM_MAX)
        km_ennemis=km_ennemis+y
        print("Vos ennemis ont avancé de "+str(y)+"km.\nIls ont dèjà parcourus "+str(km_ennemis)+"km au total, dépêchez vous !")
    elif x==1:
        y=randrange(AVANCER_RAP_MIN, AVANCER_RAP_MAX)
        km_ennemis=km_ennemis+y
        print("Vos ennemis ont avancé de "+str(y)+"km.\nIls ont dèjà parcourus "+str(km_ennemis)+"km au total, dépêchez vous !")
    else:
        print("Vos ennemis n'ont pas avancé, vous avez de la chance. Ils doivent être fatigués.")
        print("ils n'ont parcourus que "+str(km_ennemis)+"km au total.")
    return km_ennemis
        
def input_options2():

    option_valide=False
    while not option_valide:
        affiche_options()
        op=input("Que voulez vous faire?\n")
        if op != '1' and op != '2' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6':
            print('Option Invalide!')
            input()
        else:
            return op
        
def joue_partie():
    km_voyageur = 0 # Distance parcourue.
    km_ennemis = km_voyageur - AVANTAGE_VOYAGEUR # Distance parcourue par les ennemis.
    gourde = GOURDE_DEPART # Nombre de gorgés dans la gourde.
    soif = 0 # Niveau de soif du voyageur.
    fatigue = 0 # Niveau de fatigue du chameau.
    terminer = False # Le jeu est terminé.
    tour = 0 # Tour du jeu.

    affiche_intro()
    
while terminer==False:
    
    op = input_options2()

    # Quitter?
    if op == '6':
        terminer = True
    
    else:
        if op == '1':
            #gourde, soif = boit(gourde,soif)
            boit(gourde,soif)
        elif op == '2':
            #fatigue, km_voyageur, soif = avance_voyageur(fatigue, km_voyageur, soif)
            avance_voyageur(km_voyageur, fatigue, soif)
        elif op == '3':
            #fatigue, km_voyageur, soif = avance_voyageur2(fatigue, km_voyageur, soif)
            avance_voyageur2(km_voyageur, fatigue, soif)        
        elif op == '4':
            #fatigue, soif = repose(soif)
            repose(soif)
        elif op == '5':
            #gourde, fatigue, soif = cherche_aide(gourde, fatigue, soif)
            cherche_aide(gourde,fatigue,soif)
        
        # Jeu
        
        #Avance du tour du jeu
        tour=tour+1
        #Avance des ennemis
        km_ennemis = avance_ennemis(km_ennemis)
        
        #Affichage
        affiche_km2(km_voyageur, km_ennemis)
        affiche_soif(soif)
        affiche_gourde(gourde)
        affiche_fatigue(fatigue)
        
    
        #Voir si le jeu se fini ou non
        
        #Vérification des kms parcourus
        if km_voyageur >= KM_VOYAGE:
            affiche_gagne()
            
else if terminer==false:
    tour=tour+1
            

    