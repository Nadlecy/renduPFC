# Début

# On admet une fonction random() retourne un integer aléatoire entre 0 et 2 inclus
# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str

# On definit une fonction pfc qui ne prend aucun argument
"""INITIALISATION"""
    # Assigne a hands une liste [0,1,2]
    # Assigne a comPoints la valeur 0
    # Assigne a playerPoints la valeur 0
"""DEBUT BOUCLE"""
    # Tant que playerPoints est inferieure à 3 et comPoints est inferieure à 3
        # Alors
        # Assigne a validAnswer la valeur Vrai
"""CHOIX DE L'ORDI"""
        # Assigne a comShot le retour de l'execution de la fonction random()
"""ANALYSE REPONSE JOUEUR"""
        # Assigne a answer le retour de l'execution de la fonction input
        # Si answer est egale a "P" ou "Pierre"
            # Alors
            # Assigne a playerShot la valeur 0
        # Sinon Si answer est egale a "F" ou "Feuille"
            # Alors
            # Assigne a playerShot la valeur 1
        # Sinon Si answer est egale a "C" ou "Ciseaux"
            # Alors
            # Assigne a playerShot la valeur 2
        # Sinon
            # Alors
            # Affiche le message "Réponse invalide"
            # Assigne a validAnswer la valeur Faux
"""COMPARAISON RESULTATS"""
        # Si validAnswer est egale a Vrai
            # Alors
            # Si comShot est egale a la valeur dans la liste hands a l'index de valeur playerShot moins un
                # Alors
                # Afficher le message "Victoire!"
                # Incrementer playerPoints de 1
            # Sinon Si comShot est egale a la valeur dans la liste hands a l'index de valeur playerShot moins deux
                # Alors
                # Afficher le message "Défaite!"
                # Incrementer comPoints de 1
            # Sinon
                # Alors
                # Afficher le message "Egalité!"
"""SORTIE DE BOUCLE ET ANNONCE DU SCORE/VAINQUEUR"""
    #
#Fin