# -*- coding: utf-8 -*-


########################################################################################################
### INFORMATIONS
#########################################################################################################


#Ce programme utilise des symbole spéciaux:
#la lettre grec delta pour le discriminant et le signe de la racine carré,
#il faut donc utiliser le codage utf-8 (installé de base sur python et tout les systèmes d'exploitation)


########################################################################################################
### IMPORTS
########################################################################################################


from math import sqrt
from fractions import Fraction


########################################################################################################
### RESOLUTION DEFINITION
########################################################################################################



def entree_parametre_equation():    
        e = input("Entrer l'équation: \n")
        if "exit" in e:
            exit()
        else:
            e = e.replace("**2", "")
            e = e.replace("+", "")
            e = e.split("x")
            a = Fraction(e[0])
            b = Fraction(e[1])
            c = Fraction(e[2])
            return a, b, c


def resolution(a, b, c):
    delta = b**2 - 4*a*c
    print(f"\nle discriminant de l'équation est(b**2-4ac): {delta}\n")
    if delta < 0:
        print(f"L'équation n'as pas de solution réelle.")
        print("On calcule les deux solution complexe et conjuguée")
        i = 1j
        racine_delta = sqrt(-delta)
        delta_complexe = racine_delta*i
        solution_complexe1 = (-b-delta_complexe)/(2*a)
        solution_complexe2 = (-b+delta_complexe)/(2*a)
        print(f"la premiere solution complexe est(-b-i√Δ/2a):{solution_complexe1}\n")
        print(f"la seconde solution complexe est(-b+i√Δ/2a):{solution_complexe2}\n")

    elif delta == 0:
        solution1 = -b/(2*a)
        print(f"La solution de l'équation est(-b/2*a): {solution1}\n")
    else:
        print("Le discriminant est supérieur a 0 donc l'équation à deux solution")
        racine_de_delta = sqrt(delta)
        solution2 = (-b-racine_de_delta)/(2*a)
        print(f"la première solution de l'équation est(-b-√Δ/2a): {solution2}\n")
        solution4 = (-b+racine_de_delta)/(2*a)
        print(f"la seconde solution est(-b-√Δ/2a): {solution4}\n")


def début():
    print("------------------------------------------------------------------------------------------------------------------------" +
    "\nAvant d'entrer l'équation vérifiez que c'est une équation du " +
    "second degré sous la forme ax**2+bx+c=0.\nSi ce n'est pas le cas, transformez la.\n"+
    "Le carré ce note **2, il ne faut marquer ni les multiplication ni le =0.\n"+
    "Tapez help pour avoir des information sur le programme.\n"+
    "Tapez exit pour quitter le programme.")
    a, b, c = entree_parametre_equation()
    resolution(a, b, c)
    

def aide():
     print("------------------------------------------------------------------------------------------------------------------------" +
     "Voici les commandes d'aide:\n")
     



########################################################################################################
### EXECUTE
########################################################################################################


    
a = input("Voici le programme de résolution d'équation du second degrés main.py.\nAppuyer sur ENTRER pour commencer...\n")
while True:   
    if "" in a.lower():
        début()
    else:
        break
 

