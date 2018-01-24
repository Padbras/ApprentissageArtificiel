#!/usr/bin/python3

import pandas
import matplotlib.pyplot as plt

#Commentaire
"""
	Docstring décrivant une fonction ou un module. 
"""

for i in [ 1, 2, 3, 4, 5]:
	print(i)
print("toto")

#Creation liste
liste_de_listes = [[1,2,3],[4,5,6],[7,8,9]]

#Chaines car
chaineCar = 'En python les chaines sont idem avec guillements et quotes'
chaineCar2 = "la preuve"

#concat chaines
chaineTest = chaineCar + chaineCar2


print(chaineTest)

#show carac de chaine
print(chaineCar[0])
#show fragment de chaine
print(chaineCar[0:10])

liste = [] #liste vide
#ajout element à liste
liste.append("test")
liste.append(1)
print(liste)

del liste[1]

print(liste)

autre_liste = [1,2,3,4,5,6]

print(autre_liste[2:4])

liste_de_listes = [liste, autre_liste]
print(liste_de_listes)

print(len(liste_de_listes))

print(liste_de_listes[-1])

liste.extend(autre_liste)

print(liste)

# LES TUPLES

def square_and_cubes(x):
	return(x*x,x*x*x)
a,b = square_and_cubes(3)
_,c = square_and_cubes(2)

print(a)
print(b)
print(c) 

#DICO

d = dict()
nombres = { "un" : 0, "deux" : 2, "dix" : 10 }
nombres["un"] = 1 #remplace
nombres["cinq"] = 5 #ajoute
nombres.get("deux") # 2
nombres.keys() #les cles
nombres.values() #les valeurs
nombres.items() # tuples cles/valeurs

for k,v in nombres.items():
	print("La valeur de la clé {} est {}".format(k,v))


# ensembles = listes sans doublons

ens = set([1,2,2,3,4,5])
ens2 = set([1,3,4,7])
ens & ens2 #intersaction
ens | ens2 # union
ens - ens2 #difference
ens ^ ens2 #difference symetrique

temps = 10
if temps > 25:
	print("coucou")
elif temps < 10:
	print ("toto")
else:
	print ("tata")

x = 0
while x < 10:
	print(x)
	x+=1

for x in range(10):
	print(x)

for i in range(2,4):
	print(i)

for couleur in ["rouge","vert","bleu","jaune"]:
	print("{} est une couleur".format(couleur))

def somme(a,b):
	print("{} + {} = {}".format(a,b,a+b))
	return a+b

somme(3,4)
somme(a=3,b=4)
somme(b=4,a=3)

#portée des var

x = 42

def set_x(a):
	x = a # ici nvelle var locale
	x+=1
	print(x)

def set_global_x(a):
	global x
	x = a # ici var globale (à éviter)
	x+=1
	print(x)
