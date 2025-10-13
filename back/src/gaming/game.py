import random
from src.game_utilities.choice import choix
from src.game_utilities.score import score   # pour calculer le message final

# État global de la partie
etat_jeu = {                                                     #c est un dico pour stocker l etat du jeu oblige en web car pas de variables globales
    'score_joueur': 0,
    'score_ordi': 0,
    'manche_actuelle': 0,
    'total_manches': 3,
    'nom_joueur': "Annonyme",                                   #mets des valeur par deafaut
    'partie_en_cours': False
}

# Démarrer une nouvelle partie
def demarrer_partie(nom, manches):                               #creer une nouvelle partie defini le nom et manche choisis par le joueur
    etat_jeu['score_joueur'] = 0                                 #remet le score a 0
    etat_jeu['score_ordi'] = 0                                   #on mets les valeurs dans le dico etat_jeu cle value
    etat_jeu['manche_actuelle'] = 0
    etat_jeu['nom_joueur'] = nom
    etat_jeu['total_manches'] = manches
    etat_jeu['partie_en_cours'] = True                           #indique qu une partie est en cours
    return f"Partie démarrée : {nom} - {manches} manches"        #{} pour inserer des variables dans une chaine de caractere avec le formatage f""
#=! message = "Partie démarrée : " + nom + " - " + str(manches) + " manches" c est plus simple que ca 


# Jouer une manche
def jouer_manche(choix_joueur): #joue une manche avec le choix du joueur le input dans l'html name="choix_joueur"
    # Vérifie si une partie est en cours si elle ne l est pas on renvoie une erreur si le demarrer_partie n est pas lancer false de base 
    if not etat_jeu['partie_en_cours']: #si c est pas true 
        return {"erreur": "Démarre une partie d'abord !"}

    # Choix aléatoire de l'ordinateur
    choix_ordi = random.choice(["pierre", "feuille", "ciseaux"])

    # Appelle la fonction choice pour déterminer le gagnant de la manche et mettre à jour les scores
    nouveau_score_j, nouveau_score_o = choix(  #les nouveau return dans l ordre de la fonction choix
        choix_joueur, choix_ordi,
        etat_jeu['score_joueur'], etat_jeu['score_ordi']   #on appelle la fonction et on mets en attribut les choix et les valeurs dans le dico qui update avec les choix donc score joueur et ordi
    )

    # Mise à jour des scores et de la manche actuelle
    etat_jeu['score_joueur'] = nouveau_score_j  #on les renomme pour pas avoir des conflits
    etat_jeu['score_ordi'] = nouveau_score_o
    etat_jeu['manche_actuelle'] += 1  #on fait +1 a la manche manuellement car choix ne traite pas l'attribut manche

    # Vérifie si la partie est terminée
    fini = etat_jeu['manche_actuelle'] >= etat_jeu['total_manches'] #on teste si la values manches actuelle est superieur ou egale a la total entrer par le joueur 
    message_final = ""
    if fini: #si fini est true
        etat_jeu['partie_en_cours'] = False #la partie n est plus en cours

        # On utilise la fonction score pour générer le message final
        message_final = score(
            etat_jeu['score_joueur'],
            etat_jeu['score_ordi'],
            etat_jeu['nom_joueur']          #on envoie les valeurs pour generer le message final via la fonction score
        )

    # Retourne un dictionnaire avec toutes les infos nécessaires pour le front-end
    return {
        'choix_joueur': choix_joueur,
        'choix_ordi': choix_ordi,
        'score_joueur': etat_jeu['score_joueur'],
        'score_ordi': etat_jeu['score_ordi'],
        'manche': etat_jeu['manche_actuelle'],
        'total_manches': etat_jeu['total_manches'],
        'fini': fini,
        'message_final': message_final                  #on renvoie le message final pour l afficher en front si la partie est finie
    }
