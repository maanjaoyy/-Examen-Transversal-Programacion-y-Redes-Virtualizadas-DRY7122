"""
Script: crear_bd.py
Descripción: Crea la base de datos SQL y almacena usuarios con
contraseñas en hash (gestión de claves con hashlib + sqlite3).
"""

import sqlite3
import hashlib

DB_NAME = "usuarios.db"


def crear_conexion():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def insertar_usuario(nombre, password):
    conn = crear_conexion()
    cursor = conn.cursor()
    password_hash = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)",
            (nombre, password_hash)
        )
        conn.commit()
        print(f"Usuario '{nombre}' agregado correctamente.")
    except sqlite3.IntegrityError:
        print(f"El usuario '{nombre}' ya existe.")
    conn.close()


def main():
    crear_tabla()

    # Integrantes del examen - contraseñas a elección
    usuarios = {
        "Marco Jaramillo": "clave123",
        "Tomas Arros": "clave456",
        "Rodolfo Hernandez": "clave789"
    }

    for nombre, password in usuarios.items():
        insertar_usuario(nombre, password)

    print("\nBase de datos creada y usuarios almacenados con éxito.")


if __name__ == "__main__":
    main()
