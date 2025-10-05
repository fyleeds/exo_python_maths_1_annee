#Exercice 1.3 : L'urne
def exercice_1_3():
    # Initialisation des chaines de boules
    # ici la première lettre de chaque couleur suffit
    boules_rouges = "R"
    boules_jaunes = "J"
    boules_noires = "N"
    # on multiplie chaque item de boules par leur nombre pour former un tableau
    urne = [boules_rouges] * 6 + [boules_jaunes] * 3 + [boules_noires] * 1
    # Retour de la fonction
    return urne

#Exercice 1.3 : L'urne
def exercice_1_3_alt():
    # Initialisation des chaines de boules
    # ici la première lettre de chaque couleur suffit
    boules_rouges = "R"
    boules_jaunes = "J"
    boules_noires = "N"
    # on multiplie chaque item de boules par leur nombre pour former un tableau
    urne = [boules_rouges] * 6 + [boules_jaunes] * 3 + [boules_noires] * 1
    # Retour de la fonction
    return urne

#Exercice 1.4 : Le graphe (tableau deux dimensions)
def exercice_1_4():
    # Initialisation lettress
    lettre_a = "A"
    lettre_b = "B"
    lettre_c = "C"
    lettre_d = "D"
    # Initialisation premiere ligne du graphe
    premiere_ligne = [lettre_a,lettre_b]
    # Initialisation deuxieme ligne du graphe
    deuxieme_ligne = [lettre_d,lettre_c]
    # Initialisation graphe complet (tableau deux dimensions avec un tableau global et deux tableaux internes)
    graphe = [premiere_ligne,deuxieme_ligne]
    # Retour de la fonction
    return graphe

#Exercice 1.4 : Le graphe (version alternative) (tableau une dimension)
def exercice_1_4_alt():
    # Initialisation lettress
    lettre_a = "A"
    lettre_b = "B"
    lettre_c = "C"
    lettre_d = "D"
    # Initialisation graphe complet (tableau une dimension)
    graphe = [lettre_a,lettre_b,lettre_d,lettre_c ]
    # Retour de la fonction
    return graphe


# Exercice 1.5 : un calcul de somme
def exercice_1_5(n):
    total = 0
    for k in range(1,n+1):
        term = (1/k**2)
        total += term
    return total


# Defining main function
def main():
    print(exercice_1_3())
    print(exercice_1_4())
    print("Resultat exercice_1_5 avec n=5 :", exercice_1_5(5))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
    
