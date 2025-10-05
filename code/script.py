import random

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

#Exercice 1.3 : L'urne (version alternative) (string)
def exercice_1_3_alt():
    # Initialisation des chaines de boules
    # ici la première lettre de chaque couleur suffit
    boules_rouges = "R"
    boules_jaunes = "J"
    boules_noires = "N"
    # on multiplie chaque item de boules par leur nombre pour former un tableau
    urne = boules_rouges * 6 + boules_jaunes * 3 + boules_noires * 1
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

#Exercice 1.6 : En attendant la boule noire
def exercice_1_6():
    # !!!!!!!!!!
    # Cette fonction necessite la librairie random importée en ligne 1
    # !!!!!!!!!!
    
    # Initialisation des chaines de boules
    # ici la première lettre de chaque couleur suffit
    boules_rouges = "R"
    boules_jaunes = "J"
    boules_noires = "N"
    # on multiplie chaque item de boules par leur nombre pour former un tableau
    urne = [boules_rouges] * 6 + [boules_jaunes] * 3 + [boules_noires] * 1
    # On initialise un int pour compter le nombre de tirages à 0
    nb_tirages = 0
    # On initialise un bool pour savoir si on a tiré la boule noire à False (pas encore tirée)
    boule_noire_tiree = False
    while not boule_noire_tiree:
        # On tire une boule au hasard dans l'urne en utilisant la methode choice de la librairie random importée en ligne 1
        boule_tiree = random.choice(urne)
        # On incrémente le nombre de tirages
        nb_tirages += 1
        # Si la boule tirée est noire, on change le bool à True pour sortir de la boucle
        if boule_tiree == boules_noires:
            boule_noire_tiree = True
    # Retour du compteur de tirages
    return nb_tirages

# Exercice 1.7 : (Mémoire d'une urne malmenée)
# on réutilise la fonction exercice_1_6
def exercice_1_7():
    boules_rouges = "R"
    boules_jaunes = "J"
    boules_noires = "N"
    # on multiplie chaque item de boules par leur nombre pour former un tableau
    urne = [boules_rouges] * 6 + [boules_jaunes] * 3 + [boules_noires] * 1
    # On initialise la liste des boules tirées à vide
    boules_tirees = []
    # On initialise un bool pour savoir si on a tiré la boule noire à False (pas encore tirée)
    boule_noire_tiree = False
    while not boule_noire_tiree:
        # On tire une boule au hasard dans l'urne en utilisant la methode choice de la librairie random importée en ligne 1
        boule_tiree = random.choice(urne)
        # On ajoute la boule tirée à la liste des boules tirées
        boules_tirees.append(boule_tiree)
        # Si la boule tirée est noire, on change le bool à True pour sortir de la boucle
        if boule_tiree == boules_noires:
            boule_noire_tiree = True
    # Retour de la liste des boules tirées
    return boules_tirees

#Exercice 1.8 : (Les deux pièces)
def exercice_1_8():
    # !!!!!!!!!!
    # Cette fonction necessite la librairie random importée en ligne 1
    # !!!!!!!!!!
    # Initialisation des chaines de pièces
    piece_face = "face"
    piece_pile = "pile"
    # piece sous forme de tableau 
    piece = [piece_face, piece_pile]
    # PREMIERE SERIE : 
    # Initialisation du compteur piles à 0
    compteur_pour_pile = 0
    # On initialise un bool pour savoir si on a tiré Pile à False (pas encore tirée)
    pile_tiree = False
    while not pile_tiree:
        # On tire une pièce au hasard dans le sac en utilisant la methode choice de la librairie random importée en ligne 1
        piece_tiree = random.choice(piece)
        # on incrémente le compteur dans tous les cas
        compteur_pour_pile += 1
        print(f"{piece_face}, a=", compteur_pour_pile)
        # Si la pièce tirée est pile, on change le bool à True pour sortir de la boucle
        if piece_tiree == piece_pile:
            pile_tiree = True
    # Deuxième SERIE :
    # Initialisation du compteur piles à 0
    compteur_pour_face = 0
    # On initialise un bool pour savoir si on a tiré Face à False (pas encore tirée)
    face_tiree = False
    while not face_tiree:
        # On tire une pièce au hasard dans le sac en utilisant la methode choice de la librairie random importée en ligne 1
        piece_tiree = random.choice(piece)
        # Si la pièce tirée est face, on incrémente le compteur
        if piece_tiree == piece_face:
            compteur_pour_face += 1
        # Si la pièce tirée est face, on change le bool à True pour sortir de la boucle
        if piece_tiree == piece_face:
            face_tiree = True
    # Retour de la liste des pièces tirées
    return compteur_pour_face

# Exercice 1.9 : (à la recherche du maximum)
def exercice_1_9():
    # Cette fonction n'utilise pas la méthode max de python
    # Initialisation d'une liste 
    # la méthode randint retourne un entier entre les deux bornes (0 et 10 ici)
    # on en créé 5 avec la liste de compréhension
    nb_aleatoires = [random.randint(0,10) for i in range(5)]
    print ("Liste de nombres aléatoires de départ exercice_1_9 :", nb_aleatoires)
    # on parcoure la liste aléatoire pour trouver le maximum
    # on initialise le maximum avec le premier élément de la liste
    maximum = nb_aleatoires[0]
    # on parcoure la liste à partir du deuxième élément
    for i in range(1,len(nb_aleatoires)):
        # si l'élément courant est plus grand que le maximum, on met à jour le maximum
        if nb_aleatoires[i] > maximum:
            maximum = nb_aleatoires[i]
    # on retourne le maximum trouvé
    return maximum

# Defining main function
def main():
    print("Début des exercices partie 1")
    print("\n")
    print(exercice_1_3())
    print(exercice_1_3_alt())
    print("\n")
    print(exercice_1_4())
    print(exercice_1_4_alt())
    print("\n")
    print("Resultat exercice_1_5 avec n=5 :", exercice_1_5(5))
    print("\n")
    print("Resultat exercice 1_6 compteur de boules tirées avant la noire :", exercice_1_6())
    print("\n")
    print("Resultat exercice 1_7 liste des boules tirées :", exercice_1_7())
    print("\n")
    print("a=", exercice_1_8())
    print("\n")
    print("Resultat exercice_1_9 maximum trouvé :", exercice_1_9())
    print("\n")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
    
