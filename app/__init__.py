from flask import Flask

def create_app():
    app = Flask(__name__)

    # Exemple de route basique (tu pourras les déplacer dans routes/)
    @app.route('/')
    def index():
        return "Hello world !"

    return app
