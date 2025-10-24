import time 
import numpy as np

import input_space as I

for i in range(30):
    print()

d = {}
k = 0 

with open('words.txt', 'r') as file_read:
    lines = file_read.readlines()
    n = len(lines)
    for line in lines:
        line = line.strip() # strip() pour enlever les éventuels caractères de nouvelle ligne
        d[k] = line
        k+=1
        #print(line) 
    file_read.close()




s = 0
debut = time.time()

# np.random.randint(0,n) va de 0 à n-1 

def isEqual(s1,s2):
    return s1 == s2



compteur_mots = 0 
compteur_caractères = 0
nombre_mots_a_ecrire = 20

while compteur_mots < nombre_mots_a_ecrire:
    P = []
    taille_affichage = 20
    affichage = ""
    for i in range(taille_affichage):
        p = np.random.randint(0,len(d))
        P.append(p)
        affichage += d[p] + " "

    print(affichage)
    for i in range(2):
        print()

    A = []
    for i in range(taille_affichage):
        a = I.new_input(d[P[i]])
        A.append(a)
        print()

    for i in range(taille_affichage):
        s += isEqual(A[i],d[P[i]]) 
        if isEqual(A[i],d[P[i]]): #on ne compte que les caractères pour les mots corrects
            compteur_caractères += len(d[P[i]])

    for i in range(30):
        print()
    compteur_mots += taille_affichage

    
    
temps_ecoule = time.time() - debut
temps_ecoule = int((temps_ecoule*100))/100

frappes = int((compteur_caractères/temps_ecoule)*100)/100

print()
print(str(s) + " mots corrects en " + str(temps_ecoule) + " secondes")
print(str(compteur_caractères) + " caractères corrects en " + str(temps_ecoule) + " secondes")
print("C'est-à-dire " + str(frappes) + " frappes par seconde")


for i in range(3):
    print()

# virer les accents circonflexes de la data base
# ranger la data base dans l'ordre alphabétique
# record 19 mots corrects en 16.91 secondes
# soit 6.38 frappes/seconde