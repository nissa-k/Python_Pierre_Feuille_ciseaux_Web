from flask import Flask, render_template, request, redirect, url_for
import src.info.info_bot, src.rules.rules_game
from src.gaming.game import etat_jeu, jouer_manche, demarrer_partie # on import car sinon faut remettre le dictionnaire dans le serveur on importe comme ca il a acces a tout 
import os

# Spécifie manuellement où se trouve le dossier templates
templates_dir = r"C:\Users\karab\OneDrive\Desktop\ynov\Python_Pierre_Feuille_ciseaux_Web\templates"


app = Flask(__name__, template_folder=templates_dir) # Indique à Flask où se trouvent les templates HTML car le fichier n est pas dans back mais a la racine donc on mets le chemain plus haut 
print("CHEMIN TEMPLATES UTILISÉ PAR FLASK :", templates_dir)

@app.route('/')
def menu():
    return render_template('menu.html') 

@app.route('/jouer', methods=['GET', 'POST']) #permet de dire que cette route accepte les methodes get et post par defaut c est get
def jouer():
    resultat = None  # Au début, aucune manche jouée donc none dans l'html

    if request.method == 'POST': #on verifie que la requet est un post si c est true on le fait sinon on l ignore 1er chargement ca ignore car get quand on appuie sur commencer la ca execute car post
        action = request.form.get('action') #recupere la valeur du bouton appuyee name="action" dans le html jouer.html donc request.form = {'action': 'demarrer_partie'} contient ca et le .get('action') recupere demarrer_partie donc transforme en variable action

        # Commencer une nouvelle partie
        if action == 'demarrer_partie':   #request.form → contient toutes les données envoyées par le formulaire.
            nom = request.form.get('nom_joueur', 'Annonyme') #get('nom_joueur', 'Annonyme') → récupère la valeur du champ nom_joueur :Si l’utilisateur a écrit “Alice”, nom = "Alice" Si l’utilisateur n’a rien écrit, nom = "Annonyme"
            manches = int(request.form.get('total_manches', 3))  #get('total_manches', 3) → récupère la valeur du champ total_manches : Si l’utilisateur a choisi 5 manches, manches = "5" (string) Si l’utilisateur n’a rien choisi, manches = "3" (string)
            demarrer_partie(nom, manches) # on demarre la partie avec les valeurs recuperees
            return redirect(url_for('jouer'))
        

        #return redirect(url_for('jouer'))  # Redirige vers la même page pour éviter le re-post du formulaire
        
        # Jouer une manche
        elif action in ['pierre','feuille','ciseaux'] and etat_jeu['partie_en_cours']: #si action est bien pierre feuille ou ciseaux et qu une partie est en cours:  
            action = request.form.get('action') #quand tu clique sur la manche et que quand tu clique choix joueur recupere la valeur du bouton name="choix_joueur" value="pierre" ou feuille ou ciseaux
            
            # Jouer une manche avec le choix du joueur
            resultat = jouer_manche(action)      #l'ordi choisi leatoire compare met a jour les scores etc.. en gros execute le fichier game
            resultat['nom_joueur'] = etat_jeu['nom_joueur'] #on ajoute le nom du joueur au resultat pour l afficher dans l html
       
    # Si une partie est en cours mais aucune manche jouée encore, on prépare un résultat par défaut pour l'affichage

    if etat_jeu['partie_en_cours'] and resultat is None: #resultat est None au debut car on a pas encore jouer de manche

        #on cree un dico resultat avec les valeurs actuelles de etat_jeu pour l afficher dans l html
        resultat = {
            'choix_joueur': None,
            'choix_ordi': None,
            'score_joueur': etat_jeu['score_joueur'],
            'score_ordi': etat_jeu['score_ordi'],
            'manche': etat_jeu['manche_actuelle'],
            'total_manches': etat_jeu['total_manches'],
            'fini': False,
            'message_final': '',
            'nom_joueur': etat_jeu['nom_joueur']
            }
        
    # Affichage GET ou POST
    return render_template('jouer.html', resultat=resultat, etat_jeu=etat_jeu) #on passe resultat et etat_jeu a l html pour qu il puisse les utiliser


@app.route('/regles')
def regles():
    print("CHEMIN TEMPLATES UTILISÉ PAR FLASK :", templates_dir)
    regles=src.rules.rules_game.regles_jeu()
    return render_template('rules.html', reglesJeux=regles)

@app.route('/infos')
def infos():
    info=src.info.info_bot.info_bot()
    return render_template('infoBot.html', infoRobot=info)

if __name__ == '__main__':
    app.run(port=8080, debug=True)