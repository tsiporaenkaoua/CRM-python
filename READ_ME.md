Création d'un CRM 

ouvrir le projet sur nav :
python app.py (point d'entree)





Commandes pour creer le projet :
python -m venv venv
./venv/scripts/activate
pip install flask flask_sqlalchemy flask_login flask_wtf email_validator
pip freeze > requirements.txt : pour Installer toutes les dépendances en une seule commande et le mettre a jr

Verif :
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

