""" code = int(input("Enter le code PIN : "))
if code == 4567 :
    print("code correct")

else :
    print("code incorrect") """

   
    #exercice 2 signe d'un nombre

""" nombre = int(input("Saisir un nombre entier : "))
if nombre == 0:
    print("nul")
elif nombre<0 :
    print("negatif")

elif nombre>0 :
    print("Positif") """

    
    #exercice 3 parité
""" 
nombre2 = int(input("saisir un nombre entier : "))
if nombre2 % 2 == 0 :
    print("Le nombre est pair")
else : 
    print("Le nombre est impair.") """


#exercice 3 age

""" age = int(input("Entrer votre age : "))
if age <12 :
    print("A", age , " ans, vous enfant")
elif age >=12 and age <18 :
    print("A", age ,"vous êtes un adolescent")
else :
    print("A",age, "vous êtes un adulte") """


#exercice 4 perte ou profit

""" fabrication = float(input("Prix de fabrication : "))
vente = float(input("Prix de vente"))
if fabrication<vente :
    print("profit")
else :
    print("perte") """

    
    #exercice 5 maximum

""" premier = float(input("Saisir le premier nombre : "))
second = float(input("Saisir le second nombre : "))
troisieme = float(input("Sairir le troisieme nombre : "))
if premier>second and premier>troisieme :
    print("le maximum est le premier nombre :", premier)
elif second>premier and second>troisieme :
     print("le maximum est le deuxieme nombre :", second)
elif troisieme>premier and troisieme>second :
     print("le maximum est le troisieme nombre :", troisieme) """



#Exercice triangle rectangle
""" bc = int(input("entrer la lonueur du premier côté : "))
ac = int(input("entrer la longueur du deuxième coté : "))
ab = int(input("entrer la longueur du troisième coté : "))

if bc>ac and ac>ab and bc>ab :
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")

elif ab**2 == ac**2 + bc**2 :
    print("triangle rectangle")

elif ab**2  !=  ac**2 + bc**2 :
    print("triangle non rectangle") """


#Exercice Année bissextile

""" annee = int(input("entrer une année : "))

if  (annee%4) == 0 or (annee%400) == 0 and annee%100 != 0  :
    print("année bissextile")
else :
    print("année non bissextile") """


#Exercice société de transport

""" age = int(input("Saisir votre âge : "))

if age<=5  :
    print("Le voyage est gratuit") 

elif age<16 :
    print("Le prix du transport est de 5 euros.")

elif age<21 :
    print("Le prix du transport est de 6 euros. ")
    
elif age<51 :
    print("Le prix du transport est de 10 euros. ")

elif age>51 :
    print("Le prix du transport est de 9 euros. ") """


#Exercice voyage scolaire
 
""" eleve = int(input("Nombre d'élèves : "))
duree = int(input("Durée du voyage en jours : "))
repas = duree*3.50
if eleve<25 :
    transport = 110
else :
    transport = 100


if eleve<20 :
    heberg = duree*4.20

elif eleve<35 :
    heberg =  duree*3.80
else : 
    heberg = duree*4

total = transport + repas + heberg
print("Le prix du voyage revient à",total ,"euros à par élève.") """


#Exercice Vinci location

""" type_vehicule = input("Type du véhicule : ")
carburant = input("carburant : ")
duree = int(input("Durée de location en jours : "))
distance = int(input("distance en km : "))
offre = bool(input("Offre comerciale : "))


if type_vehicule == "citadine" : 
    perj = 80*duree

elif type_vehicule == "berline" :
    perj = 100*duree

elif type_vehicule == "sportive" :
    perj = 130*duree


if carburant == "essence" :
    caburant = 1.93*distance

elif carburant == "diesel" :
    carburant = 1.89*distance


total = perj + carburant

if offre : 
    total2 = (total*0.9)+30
else :
#elif offre == "false":
    total2 = total



print("Le prix total de la location est de ", total2, "euros.") """


#Exercice natation

sceance = int(input("Nombre de scéance : "))
tarifA = (sceance*1.50)+145
tarifB = sceance*15.50
detail = (input("Detail? (yes/no)")

if tarifA<tarifB :
    print("Pour", sceance, "séances, le tarif B est le plus avantageux.")

elif tarifB<tarifA :
    print("Pour", sceance, "séances, le tarif B est le plus avantageux.")

elif tarifA==tarifB :
    print("Pour",sceance ,"séances, aucun tarif n'est plus avantageux que l'autre.")

if detail == yes : 
    print("Tarif A : " tarifA)
    print("Tarif B : " tarifb)

elif detail == no :