from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from flask_app.models import usuario


usuarios = Blueprint("usuarios", __name__)


@usuarios.route("/usuarios", methods=["GET", "POST"])
def listar():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not nombre or not email or not password:
            flash("Completa todos los campos.")
        else:
            usuario.crear(nombre, email, generate_password_hash(password))
            flash("Usuario creado.")
            return redirect(url_for("usuarios.listar"))

    return render_template("usuarios.html", usuarios=usuario.listar())


@usuarios.get("/usuarios/<int:user_id>")
def mostrar(user_id):
    persona = usuario.buscar(user_id)
    if persona is None:
        return "Usuario no encontrado.", 404

    canciones = usuario.canciones_favoritas(user_id)
    disponibles = usuario.canciones_disponibles(user_id)
    return render_template(
        "usuario.html",
        usuario=persona,
        canciones=canciones,
        disponibles=disponibles,
    )


@usuarios.post("/usuarios/<int:user_id>/favoritos")
def agregar_favorito(user_id):
    if usuario.buscar(user_id) is None:
        return "Usuario no encontrado.", 404

    cancion_id = request.form.get("cancion_id", type=int)
    if cancion_id is None:
        flash("Selecciona una canción.")
    else:
        usuario.agregar_favorito(user_id, cancion_id)
        flash("Canción agregada a favoritos.")
    return redirect(url_for("usuarios.mostrar", user_id=user_id))
