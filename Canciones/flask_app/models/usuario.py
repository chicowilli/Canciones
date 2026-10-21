from flask_app.config.mysqlconnection import get_connection


def listar():
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, email FROM usuarios ORDER BY nombre")
        return cursor.fetchall()
    finally:
        connection.close()


def crear(nombre, email, password_hash):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)",
            (nombre, email, password_hash),
        )
        connection.commit()
    finally:
        connection.close()


def buscar(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, nombre, email FROM usuarios WHERE id = %s", (user_id,)
        )
        return cursor.fetchone()
    finally:
        connection.close()


def canciones_favoritas(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT c.id, c.titulo, c.artista
            FROM canciones c
            JOIN favoritos f ON f.cancion_id = c.id
            WHERE f.usuario_id = %s
            ORDER BY c.titulo
            """,
            (user_id,),
        )
        return cursor.fetchall()
    finally:
        connection.close()


def canciones_disponibles(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT c.id, c.titulo, c.artista
            FROM canciones c
            WHERE NOT EXISTS (
                SELECT 1 FROM favoritos f
                WHERE f.cancion_id = c.id AND f.usuario_id = %s
            )
            ORDER BY c.titulo
            """,
            (user_id,),
        )
        return cursor.fetchall()
    finally:
        connection.close()


def agregar_favorito(user_id, song_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT IGNORE INTO favoritos (usuario_id, cancion_id) VALUES (%s, %s)",
            (user_id, song_id),
        )
        connection.commit()
    finally:
        connection.close()
