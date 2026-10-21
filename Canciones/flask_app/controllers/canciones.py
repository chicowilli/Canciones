from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_app.models import cancion


canciones = Blueprint("canciones", __name__)


@canciones.route("/canciones", methods=["GET", "POST"])
def listar():
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        artista = request.form.get("artista", "").strip()

        if not titulo or not artista:
            flash("Completa el título y el artista.")
        else:
            cancion.crear(titulo, artista)
            flash("Canción creada.")
            return redirect(url_for("canciones.listar"))

    return render_template("canciones.html", canciones=cancion.listar())


@canciones.get("/canciones/<int:song_id>")
def mostrar(song_id):
    tema = cancion.buscar(song_id)
    if tema is None:
        return "Canción no encontrada.", 404

    usuarios = cancion.usuarios_favoritos(song_id)
    disponibles = cancion.usuarios_disponibles(song_id)
    return render_template(
        "cancion.html",
        cancion=tema,
        usuarios=usuarios,
        disponibles=disponibles,
    )


@canciones.post("/canciones/<int:song_id>/favoritos")
def agregar_favorito(song_id):
    if cancion.buscar(song_id) is None:
        return "Canción no encontrada.", 404

    user_id = request.form.get("usuario_id", type=int)
    if user_id is None:
        flash("Selecciona un usuario.")
    else:
        cancion.agregar_favorito(song_id, user_id)
        flash("Canción agregada a favoritos.")
    return redirect(url_for("canciones.mostrar", song_id=song_id))
