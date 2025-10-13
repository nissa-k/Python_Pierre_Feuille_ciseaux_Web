from colorama import Fore, Style

def score(score_joueur, score_ordi, nom_joueur):

    if score_joueur > score_ordi:
        message = f"Félicitations tu as gagné la partie ! {Fore.GREEN}{nom_joueur} :) {score_joueur} | {Fore.RED}ordi :( {score_ordi}{Style.RESET_ALL}"
    elif score_joueur < score_ordi:
        message = f"Dommage tu as perdu la partie ! {Fore.RED}{nom_joueur} :( {score_joueur} | {Fore.GREEN}ordi :) {score_ordi}{Style.RESET_ALL}" #plus simple que les +str()
    else:
        message = "Égalité !"

    return {
        "score_joueur": score_joueur,  #on renvoie les scores pour affichage en dico
        "score_ordi": score_ordi,
        "nom_joueur": nom_joueur,
        "message": message
    }
#plus de print donc plus d'affichage console , impossible de les reutiliser en web 