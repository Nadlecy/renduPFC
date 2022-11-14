# Début

# On admet une fonction random() retourne un integer aléatoire entre 0 et 2 inclus
import random
# On admet une fonction input() qui enregistre l'entree d'un joueur sous forme de str

# On definit une fonction pfc qui ne prend aucun argument
def pfc():
    # Assigne a hands une liste [0,1,2]
    hands=[0,1,2]
    # Assigne a comPoints la valeur 0
    comPoints=0
    # Assigne a playerPoints la valeur 0
    playerPoints=0
    # Tant que playerPoints est inferieure à 3 et comPoints est inferieure à 3
    while playerPoints < 3 and comPoints < 3:
        # Alors
        # Afficher une chaine de caracteres composee de playerPoints, " - ", puis comPoints
        print(str(playerPoints) + " - " + str(comPoints))
        # Assigne a validAnswer la valeur Vrai
        validAnswer = True
        # Assigne a comShot le retour de l'execution de la fonction random()
        comShot = random.randint(0,2)
        # Assigne a answer le retour de l'execution de la fonction input()
        answer = input("P / F / C ? \n")
        # Si answer est egale a "P" ou "Pierre"
        if answer == "P" or answer == "Pierre":
            # Alors
            # Assigne a playerShot la valeur 0
            playerShot=0
        # Sinon Si answer est egale a "F" ou "Feuille"
        elif answer == "F" or answer == "Feuille":
            # Alors
            # Assigne a playerShot la valeur 1
            playerShot=1
        # Sinon Si answer est egale a "C" ou "Ciseaux"
        elif answer == "C" or answer == "Ciseaux":
            # Alors
            # Assigne a playerShot la valeur 2
            playerShot = 2
        # Sinon
        else:
            # Alors
            # Affiche le message "Réponse invalide"
            print("Réponse Invalide")
            # Assigne a validAnswer la valeur Faux
            validAnswer=False
        # Si validAnswer est egale a Vrai
        if validAnswer == True:
            # Alors
            # Si comShot est egale a la valeur dans la liste hands a l'index de valeur playerShot moins un
            if comShot == hands[(playerShot-1)]:
                # Alors
                # Afficher le message "Victoire !"
                print("Victoire ! \n______________________")
                # Incrementer playerPoints de 1
                playerPoints+=1
            # Sinon Si comShot est egale a la valeur dans la liste hands a l'index de valeur playerShot moins deux
            elif comShot == hands[(playerShot-2)]:
                # Alors
                # Afficher le message "Défaite !"
                print("Défaite ! \n______________________")
                # Incrementer comPoints de 1
                comPoints += 1
            # Sinon
            else:
                # Alors
                # Afficher le message "Egalité !"
                print("Egalité ! \n______________________")
    # Afficher une chaine de caracteres composee de "Score final: ", playerPoints, " - ", puis comPoints
    print("Score final : " + str(playerPoints) + " - " + str(comPoints))
    # Si comPoints est strictement plus grande que playerPoints
    if comPoints > playerPoints:
        # Alors renvoyer le message "Vous avez perdu."
        return print("Vous avez perdu !")
    # Sinon
    else:
        # Alors renvoyer le message "Vous avez Gagné!"
        return print("Vous avez Gagné !")

# Appeler la fonction pfc()
pfc()

# Fin