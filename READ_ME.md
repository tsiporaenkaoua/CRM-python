CONFIGURATION DU BACK END : 

Création d'un CRM 

*******ouvrir le projet sur nav :
python app.py (point d'entree)/flask run

******Commandes pour creer le projet :
python -m venv venv
./venv/scripts/activate ca active l'enviro virtuel
pip install flask flask_sqlalchemy flask_login flask_wtf email_validator
pip freeze > requirements.txt : pour Installer toutes les dépendances en une seule commande et le mettre a jr

*******Verif :
python -m flask --version

pip = l’outil qui gère les packages Python (un peu comme npm en Node.js ou composer en PHP).
Flask → framework web
Flask-SQLAlchemy → ORM gestion de la base de données
Flask-Login → authentification et sessions
Flask-WTF → formulaires sécurisés (CSRF, validation)
Email-Validator → validation des adresses email


Flask est disponible via le gestionnaire de paquets Python, PyPI 
Avec Flask (microserveur / framework web), il n’y a pas de générateur automatique pour les CRUD ou les pages.
👉 Donc c’est toi qui définis l’architecture et crée les fichiers/dossiers dès le départ.

Ce que tu dois faire avant de coder
Réfléchir à ton architecture (dossiers, séparation routes/models/templates).
Créer les dossiers vides (routes/, templates/, static/…) pour préparer le terrain.
Mettre en place la base (app.py, config.py, __init__.py) → que ton app démarre avec une simple page d’accueil.


Etapes configuration :
-Installer la dépendance si c pas fait
- Remplir ton fichier config.py
- Initialiser SQLAlchemy dans app/__init__.py
- créer un fichier app/models.py avec des classes (User, etc.),
- générer la base app.db,
- insérer et lire des données.


******Creer une bdd :
Config la bdd dans config.py
(Si app.db n’existe pas, il sera créé automatiquement lors du db.create_all() lorsqu'on crée les tables)

******Creer une table :
dans model creer la table en detail (niveau python)

******Faire persister la table niveau bdd et la remplir:
flask shell
from app import db, create_app
from app.models import Essai

app = create_app()

with app.app_context():
    db.create_all()  # crée la table Essai si elle n'existe pas

    # ➕ Ajouter des données
    e1 = Essai(nom="Alice", numero=101)
    e2 = Essai(nom="Bob", numero=202)

    db.session.add_all([e1, e2])
    db.session.commit()

    # ✅ Vérifier le contenu
    print(Essai.query.all())


