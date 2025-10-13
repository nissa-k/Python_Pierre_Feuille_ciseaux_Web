from flask import Flask, render_template, request
import src.info.info_bot, src.rules.rules_game
from src.gaming.game import etat_jeu, jouer_manche, demarrer_partie # on import car sinon faut remettre le dictionnaire dans le serveur on importe comme ca il a acces a tout 


app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html') 

@app.route('/jouer')
def jouer():
    resultat = None  # Au début, aucune manche jouée donc none dans l'html

    if request.method == 'POST': #on verifie que la requet est un post si c est true on le fait sinon on l ignore 1er chargement ca ignore car get quand on appuie sur commencer la ca execute car post
        action = request.form.get('action') #recupere la valeur du bouton appuyee name="action" dans le html jouer.html donc request.form = {'action': 'demarrer_partie'} contient ca et le .get('action') recupere demarrer_partie donc transforme en variable action

        # Commencer une nouvelle partie
        if action == 'demarrer_partie':   #request.form → contient toutes les données envoyées par le formulaire.
            nom = request.form.get('nom_joueur', 'Annonyme') #get('nom_joueur', 'Annonyme') → récupère la valeur du champ nom_joueur :Si l’utilisateur a écrit “Alice”, nom = "Alice" Si l’utilisateur n’a rien écrit, nom = "Annonyme"
            manches = int(request.form.get('total_manches', 3))  #get('total_manches', 3) → récupère la valeur du champ total_manches : Si l’utilisateur a choisi 5 manches, manches = "5" (string) Si l’utilisateur n’a rien choisi, manches = "3" (string)
            demarrer_partie(nom, manches) # on demarre la partie avec les valeurs recuperees

        # Jouer une manche
        elif action == 'valider':  #valider arrive quand on lance une manche dans le html commencer c est un autre bouton
            choix_joueur = request.form.get('choix_joueur') #quand tu clique sur la manche et que quand tu clique choix joueur recupere la valeur du bouton name="choix_joueur" value="pierre" ou feuille ou ciseaux
            if choix_joueur and etat_jeu['partie_en_cours']: #si choix_joueur n est pas vide et que la partie est en cours
                resultat = jouer_manche(choix_joueur)      #l'ordi choisi leatoire compare met a jour les scores etc.. en gros execute le fichier game

    # Affichage GET ou POST
    return render_template('jouer.html', resultat=resultat)


@app.route('/regles')
def regles():
    regles=src.rules.rules_game
    return render_template('regles.html', reglesJeux=regles)

@app.route('/infos')
def infos():
    info=src.info.info_bot.info_bot()
    return render_template('infos.html', infoRobot=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)