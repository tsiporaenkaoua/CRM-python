from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# on instancie SQLAlchemy
db = SQLAlchemy()

def create_app():
  
    app = Flask(__name__)
    app.config.from_object("config.Config")  # Charge la classe Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    # On "branche" SQLAlchemy sur Flask
    db.init_app(app)

    # Exemple de route basique (tu pourras les déplacer dans routes/)
    @app.route('/')
    def home():
      return render_template("home.html")

    return app
