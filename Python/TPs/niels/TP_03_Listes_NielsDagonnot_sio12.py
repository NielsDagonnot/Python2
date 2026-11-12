#Exercice 1 : indices et fonction range()

""" liste1 = list(range(10,15))
var = 0
var2 = 10

print(liste1[2]) #le resultat est 12 car c'est la deuxième valeur de la liste
print(liste1[var]) #le resultat est 10 car var = 0 et 10 est la première valeur de la liste (en position 0)
#print(liste1[var2]) #le code indique une erreur car il n'y a pas de 10ème valeur a afficher
print(liste1["var"]) #le code indique une erreur car l'élément entre [] est un string """


#Exercice 2 : Jours de la semaine

""" #1
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

#2
print(semaine[0])
print(semaine[reversed==True])

#3
print(semaine[5:7])
print(semaine[5:])

#4
semaine.reverse()
print(semaine) """

#Exercice 3 : Manipulations sur une liste numérique

""" #1

liste1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #première méthode
liste2 = list(range(0,11)) #deuxième méthode

#2
del liste1[3] #première méthode
liste2.remove(3) #deuxième méthose


#3
liste1.insert(3,3)


#4
liste1.append(11)


#5 #première méthode
liste1.sort(reverse = True)
#deuxième méthode
liste2.reverse()

#6
print(min(liste1))
print(max(liste1))
print(sum(liste1))

#7
print(5 in liste1)

#8
liste1.clear() """

#Exercice 4 : Calendrier

""" #1
Année = ["Janvier",1],["Fevrier",2],["Mars",3],["Avril",4],["Mai",5],["Juin",6],["Juillet"],["Aout",8],["Septembre",9],["Octobre",10],["Novembre",11],["Decembre",12]

#2
print(Année[3])

#3
print(Année[3][0]) """


#Exercice 5 : Transformations

""" lettres = ["a","a","b","d","e","a","c","b","e","d"]

#1
print(lettres.count("a"))

#2
li = ":".join(lettres)
print(li)

#3
print(li.split(":")) """


#Exercice 6 : Les saisons

""" printemps = ["Mars","Avril","Mai"]
ete = ["Juin","Juillet","Aout"]
automne = ["Septembre","Octobre","Novembre"]
hiver = ["Décembre","Javnvier","Février"]
saisons = [printemps, ete, automne, hiver]

#1
print(saisons[2]) # ['Septembre', 'Octobre', 'Novembre']

#2
print(saisons[1][0]) # Juin

#3
print(saisons[1:2]) # [['juin', 'JuilletAout']] 

#4
print(saisons[:][1]) # ['juin', 'Juillet', 'Aout']
#Il affiche ce résultat car il affiche dans la liste saison, la liste qui se trouve en valeur 1 qui est l'été
 """

#Exercice 7 : Table de multiplication par 9

"""print(list(range(9,90,9)))"""


#Exercice 8 : Nombres paires