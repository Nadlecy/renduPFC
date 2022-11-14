# Début

# On admet une fonction random() retourne un integer aléatoire entre 0 et 2 inclus
# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str

# On definit une fonction pfc qui ne prend aucun argument
    # Assigne a hands une liste [0,1,2]
    # Assigne a comPoints la valeur 0
    # Assigne a playerPoints la valeur 0
    # Tant que playerPoints est inferieure à 3 et comPoints est inferieure à 3
        # Alors
        # Afficher une chaine de caracteres composee de playerPoints, " - ", puis comPoints
        # Assigne a validAnswer la valeur Vrai
        # Assigne a comShot le retour de l'execution de la fonction random()
        # Assigne a answer le retour de l'execution de la fonction input()
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
    # Afficher une chaine de caracteres composee de "Score final: ", playerPoints, " - ", puis comPoints
    # Si comPoints est strictement plus grande que playerPoints
        # Alors renvoyer le message "Vous avez perdu."
    # Sinon
        # Alors renvoyer le message "Vous avez Gagné!"

# Appeler la fonction pfc()

# Fin