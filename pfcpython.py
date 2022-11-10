# Début

# On admet une fonction random() qui retourne un integer aléatoire entre 0 et 2 compris
# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str

# On definit une fonction pfc qui ne prend aucun argument
"""INITIALISATION"""
    # Assigne a choice une liste [0,1,2]
    # Assigne a comPoints la valeur 0
    # Assigne a playerPoints la valeur 0
"""DEBUT BOUCLE"""
    # Tant que playerPoints est inferieure à 3 et comPoints est inferieure à 3
        # Alors
        # Assigne a validAnswer la valeur True
        # Assigne a answer le retour de l'execution de la fonction input
"""ANALYSE REPONSE"""
        # Si answer contient  "P" ou "Pierre"
            # Alors
            # Assigne a playerShot la valeur 0
        # Sinon Si answer contient "F" ou "Feuille"
            # Alors
            # Assigne a playerShot la valeur 1
        # Sinon Si answer contient "C" ou "Ciseaux"
            # Alors
            # Assigne a playerShot la valeur 2
        # Sinon
            # Alors
            # Affiche le message "Réponse invalide"
            # Assigne a validAnswer la valeur False
        #

#Fin