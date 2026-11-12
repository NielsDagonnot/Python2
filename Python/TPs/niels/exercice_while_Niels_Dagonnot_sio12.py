import random

#Exercice 1
#question 1 
"""n = int(input("entrer un nombre entier : "))
x = 1
while x <= n:
    print(x)
    x = x+1 """

#question 2
"""n = int(input("entrer un nombre entier : "))
x = 1
while x <= n :
    print(n)
    n = n-1"""

#Exercice 2
"""mdp = "python123"
tentatives = 3

while tentatives>0:
    essaie = input("entrer le mot de passe : ")
    if mdp == essaie:
        truc = True
    else:
        truc = False
    
    if essaie != mdp:
        tentatives = tentatives-1
        print("mot de passe incorrect. Il vous reste", tentatives,"tentative(s)" )
    else:
        print("Accès accordé")
        print(truc)
        break
if tentatives == 0:
    print("accès bloqué après 3 tentatives")
    print(truc)"""

#exercice 3
"""nb_secret = random.randint(1, 100)
print(nb_secret)
t = int(input("devine le nombre entre 1 et 100 : "))
nbt = 1
if nb_secret>t:
        print("c'est plus petit")
        nbt = nbt+1
elif nb_secret<t:
        print("c'est plus grand")
        nbt = nbt+1
else:
        print("félicitation, tu as trouvé en", nbt,"tentative(s)")
while t != nb_secret:
    t = int(input("devine le nombre entre 1 et 100 : "))
    if nb_secret>t:
        print("c'est plus petit")
        nbt = nbt+1
    elif nb_secret<t:
        print("c'est plus grand")
        nbt = nbt+1
    else:
        print("félicitation, tu as trouvé en", nbt,"tentative(s)")"""

#Exercice 4
""" n = int(input("entrer un nombre entier positif : "))
i = 0
t = 0
while i < n :
    i += 1
    t = t + i
print("Pour n = ", n, "La somme est :", t) """

#Exercice 5
"""nb = int(input("entrer une valeur positive ou nulle : "))
lg = len(str(nb))
lg2 = 0
while lg2 != lg :
    lg2 +=1
print("Ce nombre contient", lg2, "chiffres.")"""

#Exercice 6
"""premier = int(input("Saisir un nombre entier positif : "))
while premier >= 0 :
    if premier/1 == premier and premier/premier == 1 and premier %2 != 0 :
        print("Le nombre", premier, "est un nombre premier")
    else :
        print("Le nombre", premier, "n'est pas un nombre premier")
    break"""

#Exercice 7
""" euro1 = int(input("Ecrire une valeur entière positive : "))
euro = euro1
while euro >= 0 :
    prix1 = euro//20
    euro -= prix1*20
    print(prix1, "billet de 20$")
    prix2 = euro//10
    euro -= prix2*10
    print(prix2, "billet de 10$")

    prix3 = euro//5
    euro -= prix3*5
    print(prix3, "billet de 5$")

    prix4 = euro//1
    euro -= prix4*1
    print(prix4, "billet de 1$")
    break  """


    
