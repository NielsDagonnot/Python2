import random
mot = ["bonjour", "programme", "python", "cyber" "securite", "ordinateur", "code", "language", "programation"]
mot2 = random.choice(mot)
print(mot2)
chances = 10
nouvel_affichage = ""
lgmot = " ".join(["_"] * len(mot2))
while "_" in lgmot and chances > 0:
    print(lgmot)
    lettre = input("choisir une lettre : ")
    
    if len(lettre) > 1 :
        print("tricheur")
        break
    nouvel_affichage = ""

    if lettre in mot2:
        for i in range(len(mot2)):
            if mot2[i] == lettre:
                nouvel_affichage += lettre
            else:
                nouvel_affichage += lgmot[i] 

        lgmot = nouvel_affichage

        lgmot = nouvel_affichage
        

    else:
        if chances 
        chances -=1
        print("La lettre n'est pas bonne. Il reste", chances, "chances")
    for i in range(len(mot2)):
        if mot2[i] == lettre:
            nouvel_affichage += lettre




