#jeu du plus petit, plus grand
# le joueur tape un chiffre et l'ordinateur compris entre 0 et 100
# lui dit si ce chiffre est plus petit ou plus grand que le sien.
# le jeu s'arrete quand on a trouve le chiffre de l'ordinateur
import random

chiffre_ordi= random.randint(0,100)
fini = False

while fini == False:
    print("Tape un nombre entre 0 et 100")
    chiffre_joueur= int(input("-->"))

    if chiffre_joueur < chiffre_ordi:
        print("ton chiffre est plus petit que le mien")
    elif chiffre_joueur == chiffre_ordi:
        print("gagne!")
        fini = True
    else:
        print("ton chiffre est plus grand que le mien")