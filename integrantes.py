"""
Script: integrantes.py
Descripción: Imprime en una lista los nombres y apellidos de los
integrantes del grupo - Examen Transversal DRY7122.
"""

integrantes = [
    "Marco Jaramillo",
    "Tomas Arros",
    "Rodolfo Hernandez"
]

print("Integrantes del grupo - Examen Transversal DRY7122:")
print(integrantes)

print("\nListado detallado:")
for nombre in integrantes:
    print(f"- {nombre}")
