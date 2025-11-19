import random 
print("Bienvenue dans le jeu de devinette de lettres consécutives !")
print("---------------------------------------------------")
lettres = ("kk","ll","mm") 
lettres_secretes = random.choice(lettres)
deviner = input("Entrez les deux lettres consécutives à deviner :").strip().lower()
if deviner == lettres_secretes:
    print("Bien joué :)")
else : 
    print("Dommage,la lettre était",lettres_secretes)
