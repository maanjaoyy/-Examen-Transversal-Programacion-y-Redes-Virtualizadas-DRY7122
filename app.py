"""
Script: app.py
Descripción: Sitio web con Flask que valida usuarios contra la base
de datos SQLite, comparando contraseñas mediante hash (puerto 5800).
"""

from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "usuarios.db"

HTML_FORM = """
<!DOCTYPE html>
<html lang="es">
<head><title>Login - Examen DRY7122</title></head>
<body style="font-family: Arial; margin: 50px;">
    <h2>Login de Usuarios - DRY7122</h2>
    <form method="POST">
        <label>Usuario:</label><br>
        <input type="text" name="nombre"><br><br>
        <label>Contraseña:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Ingresar">
    </form>
    {% if mensaje %}
        <p style="color: {{ 'green' if exito else 'red' }};"><b>{{ mensaje }}</b></p>
    {% endif %}
</body>
</html>
"""


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        return False

    hash_ingresado = hash_password(password)
    return hash_ingresado == resultado[0]


@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = None
    exito = False

    if request.method == "POST":
        nombre = request.form.get("nombre")
        password = request.form.get("password")

        if validar_usuario(nombre, password):
            mensaje = f"Bienvenido, {nombre}. Login exitoso."
            exito = True
        else:
            mensaje = "Usuario o contraseña incorrectos."
            exito = False

    return render_template_string(HTML_FORM, mensaje=mensaje, exito=exito)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800, debug=True)
