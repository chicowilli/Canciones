from flask_app.config.mysqlconnection import get_connection


def listar():
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, titulo, artista FROM canciones ORDER BY titulo")
        return cursor.fetchall()
    finally:
        connection.close()


def crear(titulo, artista):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO canciones (titulo, artista) VALUES (%s, %s)",
            (titulo, artista),
        )
        connection.commit()
    finally:
        connection.close()


def buscar(song_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, titulo, artista FROM canciones WHERE id = %s", (song_id,)
        )
        return cursor.fetchone()
    finally:
        connection.close()


def usuarios_favoritos(song_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT u.id, u.nombre
            FROM usuarios u
            JOIN favoritos f ON f.usuario_id = u.id
            WHERE f.cancion_id = %s
            ORDER BY u.nombre
            """,
            (song_id,),
        )
        return cursor.fetchall()
    finally:
        connection.close()


def usuarios_disponibles(song_id):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT u.id, u.nombre
            FROM usuarios u
            WHERE NOT EXISTS (
                SELECT 1 FROM favoritos f
                WHERE f.usuario_id = u.id AND f.cancion_id = %s
            )
            ORDER BY u.nombre
            """,
            (song_id,),
        )
        return cursor.fetchall()
    finally:
        connection.close()


def agregar_favorito(song_id, user_id):
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
