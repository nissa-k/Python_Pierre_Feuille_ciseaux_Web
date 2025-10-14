from flask import Flask, render_template, request, redirect, url_for
import src.info.info_bot, src.rules.rules_game
from src.gaming.game import etat_jeu, jouer_manche, demarrer_partie
import os

base_dir = r"C:/Users/karab/OneDrive/Desktop/ynov/Python_Pierre_Feuille_ciseaux_Web"
templates_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")  # dossier pour tes CSS, images, etc.

# === Initialisation de Flask ===
app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)

print("CHEMIN TEMPLATES UTILISÉ PAR FLASK :", templates_dir)
print("CHEMIN STATIC UTILISÉ PAR FLASK :", static_dir)


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/jouer', methods=['GET', 'POST'])
def jouer():
    resultat = None

    if request.method == 'POST':
        action = request.form.get('action')

        # Démarrer une nouvelle partie
        if action == 'demarrer_partie':
            nom = request.form.get('nom_joueur', 'Anonyme')
            manches = int(request.form.get('total_manches', 3))
            demarrer_partie(nom, manches)
            return redirect(url_for('jouer'))

        # Jouer une manche
        elif action in ['pierre', 'feuille', 'ciseaux'] and etat_jeu['partie_en_cours']:
            resultat = jouer_manche(action)
            resultat['nom_joueur'] = etat_jeu['nom_joueur']

    if etat_jeu['partie_en_cours'] and resultat is None:
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

    return render_template('jouer.html', resultat=resultat, etat_jeu=etat_jeu)


@app.route('/regles')
def regles():
    regles = src.rules.rules_game.regles_jeu()
    return render_template('rules.html', reglesJeux=regles)


@app.route('/infos')
def infos():
    info = src.info.info_bot.info_bot()
    return render_template('infoBot.html', infoRobot=info)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
