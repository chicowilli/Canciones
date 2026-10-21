import os

from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "clave-local-para-desarrollo")

    from flask_app.controllers.canciones import canciones
    from flask_app.controllers.usuarios import usuarios

    app.register_blueprint(usuarios)
    app.register_blueprint(canciones)

    @app.get("/")
    def inicio():
        return redirect(url_for("usuarios.listar"))

    return app
