# Usuarios y canciones

Aplicación sencilla en Flask para crear usuarios y canciones, y asociar canciones favoritas a cada usuario.

## Carpetas

- `flask_app/controllers`: rutas de usuarios y canciones.
- `flask_app/models`: consultas a MySQL.
- `flask_app/config`: conexión a la base de datos.
- `flask_app/bd`: script para crear las tablas.
- `flask_app/templates`: páginas HTML.
- `flask_app/static`: estilos.

## Ejecutar

1. Crea un entorno e instala las dependencias:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. En MySQL Workbench o en la consola de MySQL, ejecuta `flask_app/bd/schema.sql`.
3. Copia `.env.example` a `.env` y ajusta los datos de conexión. Si los valores del ejemplo coinciden con tu MySQL local, puedes dejarlos como están.
4. La app carga automáticamente las variables de `.env`.
5. Inicia la app:

   ```powershell
   py server.py
   ```

6. Abre `http://127.0.0.1:5000`.

Las contraseñas se guardan como hash. No hay inicio de sesión; el campo se incluye al crear el usuario como en el diseño.
