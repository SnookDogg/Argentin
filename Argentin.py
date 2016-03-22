couleur=('pique','trefle','carreau','coeur')
valeur=('as','2','3','4','5','6','7','8','9','10','valet','dame','roi')

import random

def permutation(n):
    res=[]
    for i in range(n):
        res+=[i]
    random.shuffle(res)
    return(res)


def permutation_liste(l):
    lcop=[]
    n=len(l)
    liste_permut=permutation(n)
    for i in range(len(liste_permut)):
        lcop+=[l[liste_permut[i]]]
    return(lcop)

## génération du deck
deck=[]
for col in couleur:
    for item in valeur:
        deck+= [(item,col)]


## on fait une permutation du deck
deck=permutation_liste(deck)

## on définit le nombre de joueur
nbre_joueur=4
main=[]
for i in range(4):
    main+=[deck[0:4]]
    deck=deck[4::]


## main du 1er joueur
print("Affichage main premier joueur")
print("")
print(main[0])
print("***********************")


liste_defausse=[]
cont=True
pioche=deck

# un coup quelconque en dehors du tour d'initialisation
def coup_joueur(i,pioche,defausse,main):
    n_main=len(main[i-1])
    n_defausse=len(defausse)
    n_pioche=len(pioche)
    print("main du joueur")
    print(main[i-1])
    print("****************")
    print("carte visible de la défausse")
    print(defausse[n_defausse-1])
    print("*****************")
    choix=int(input("Choix entre pioche et defausse, 0= pioche, 1= defausse"))
    #
    if choix==0:
        # on s'apprête à piocher
        print(pioche[0])
        pioche=pioche[1::]
        choix_bis=int(input("Choix entre garder ou défausser,0=garde,1=défausse"))
        if choix_bis==0:
            # on a gardé la carte, il faut défausser une de nos cartes
            choix_trois=int(input("numéro carte que l'on va défausser, entier compris entre 0 et "+str(len(main[i-1])-1)+" ici"))
            auxiliaire=main[i-1][choix_trois]
            main[i-1][choix_trois]=pioche[0]
            defausse=defausse+[auxiliaire]
        elif choix_bis==1:
            # on défausse directement la carte
            defausse+=[pioche[0]]
            # il faut activer les pouvoirs pas encore implémentés
        else:
            print("tu écris de la merde")
    elif choix==1:
        # on prend la carte de la défausse
        print(defausse[len(defausse)-1])
        carte_defausse=defausse[len(defausse)-1]
        defausse=defausse[0:(len(defausse)-1)]
        choix_quatre=int(input("numéro carte que l'on va défausser, entier compris entre 0 et"+str(len(main[i-1]))+"ici"))
        auxiliaire=main[i-1][choix_quatre]
        main[i-1][choix_quatre]=carte_defausse
        defausse+=[auxiliaire]
    else:
        print("impossible")
    print("Nouvelle main")
    print("************")
    print(main[i-1])



#while cont:
    # si le jeu est terminé on arrête tout
    #if :

    # sinon on s'intéresse à un tour de jeu
    ## le joueur pioche soit dans la défausse, soit une carte dans le deck
carte_test=deck[0]
deck=deck[1::]
defausse=[carte_test]
print("Tentative de premier coup")
print(" ")
print("**************************")
coup_joueur(1,deck,defausse,main)



