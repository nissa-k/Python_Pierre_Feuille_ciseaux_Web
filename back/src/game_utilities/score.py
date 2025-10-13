

def score(score_joueur, score_ordi, nom_joueur):

    if score_joueur > score_ordi:
        return f"Félicitations tu as gagné la partie !  {nom_joueur}   :)  {score_joueur} | ordi   :(  {score_ordi}"  #f pour formater la chaine de caractere
    elif score_joueur < score_ordi:
        return  f"Dommage tu as perdu la partie !  {nom_joueur}   :(  {score_joueur} | ordi   :)  {score_ordi}" #plus simple que les +str()
    else:
        return "Égalité ! Retente ta chance !"  #pas besoin de variable ici

  #return {
  #      "score_joueur": score_joueur,  #on renvoie les scores pour affichage en dico
  #      "score_ordi": score_ordi,
  #      "nom_joueur": nom_joueur,
   #     "message": message
    #}
#plus de print donc plus d'affichage console , impossible de les reutiliser en web 