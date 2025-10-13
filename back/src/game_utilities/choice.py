from colorama import Fore, Style

def choix(choix_user, ordi, score_joueur, score_ordi ):
    if choix_user == ordi:
        print("égalité ! \n")
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi)+ "\n")
    elif (choix_user=="pierre" and ordi=="ciseaux") or (choix_user=="ciseaux" and ordi=="feuille") or (choix_user=="feuille" and ordi=="pierre"):
        score_joueur += 1
        print(str(Fore.GREEN) + "tu as gagné cette manche ! \n" + Style.RESET_ALL)
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))
    else:
        score_ordi += 1
        print(str(Fore.RED) + "tu as perdu cette manche ! \n"+ Style.RESET_ALL)
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))
    return score_joueur, score_ordi