#lettre = "o"
#mot= "bonjour"

#for element in mot:
#    if lettre == element:
#        print(lettre,"et ", element,"sont bien egaux")
#    else:
#        print(lettre, "et ",element,"sont pas egaux")

# chiffre = 0
# flag= True
# while flag == True:
#     print(chiffre)
#     chiffre = chiffre + 1
#     if chiffre == 100:
#         flag= False

phrase = "bientot la pause"

for lettre in phrase:
    if lettre in "aeiouy":
        print(lettre, "est une voyelle")
    else:
        print(lettre,"est une consonne")


