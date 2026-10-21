CREATE DATABASE IF NOT EXISTS canciones
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE canciones;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    email VARCHAR(180) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS canciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(180) NOT NULL,
    artista VARCHAR(180) NOT NULL
);

CREATE TABLE IF NOT EXISTS favoritos (
    usuario_id INT NOT NULL,
    cancion_id INT NOT NULL,
    PRIMARY KEY (usuario_id, cancion_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (cancion_id) REFERENCES canciones(id) ON DELETE CASCADE
);
