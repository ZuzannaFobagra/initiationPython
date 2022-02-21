# Importer nos librairies
# On nous affiche :
# Entrez un caractere de a->z
# On tape une lettre
# On retrouve la postion de la lettre dans l'alphabet
# On affiche le code morse correspondant a l'index trouve
# Le programme nous retourne les symboles correspodants

import liste_morse

print ("entrez un caractere de a->z")
lettre= input(">>>")

index = liste_morse.alphabet.index(lettre)
print(liste_morse.morse[index])


