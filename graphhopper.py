"""
Script: graphhopper.py
Descripción: Calcula distancia y ruta entre una ciudad de Chile y una
ciudad de Argentina utilizando la API de GraphHopper.
"""

import requests

# ==========================================================
# PEGA TU API KEY DE GRAPHHOPPER AQUÍ, ENTRE LAS COMILLAS:
API_KEY = "02643dad-efea-42fb-8a15-061694ea9b60"
# ==========================================================

GEOCODE_URL = "https://graphhopper.com/api/1/geocode"
ROUTE_URL = "https://graphhopper.com/api/1/route"


def obtener_coordenadas(ciudad):
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }
    respuesta = requests.get(GEOCODE_URL, params=params)
    datos = respuesta.json()

    if not datos.get("hits"):
        return None

    punto = datos["hits"][0]["point"]
    return punto["lat"], punto["lng"]


def elegir_medio_transporte():
    print("\nSeleccione el medio de transporte:")
    print("1. Auto (car)")
    print("2. Bicicleta (bike)")
    print("3. A pie (foot)")

    opciones = {"1": "car", "2": "bike", "3": "foot"}
    eleccion = input("Ingrese el número de opción: ")
    return opciones.get(eleccion, "car")


def calcular_ruta(origen_coords, destino_coords, vehiculo):
    params = {
        "point": [f"{origen_coords[0]},{origen_coords[1]}",
                   f"{destino_coords[0]},{destino_coords[1]}"],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }
    respuesta = requests.get(ROUTE_URL, params=params)
    return respuesta.json()


def mostrar_resultado(datos_ruta):
    if "paths" not in datos_ruta:
        print("No se pudo calcular la ruta. Verifique las ciudades ingresadas.")
        return

    ruta = datos_ruta["paths"][0]

    distancia_km = ruta["distance"] / 1000
    distancia_millas = distancia_km * 0.621371
    duracion_ms = ruta["time"]
    duracion_min = duracion_ms / 60000

    print(f"\nDistancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
    print(f"Duración del viaje: {duracion_min:.1f} minutos")

    print("\nNarrativa del viaje:")
    for instruccion in ruta.get("instructions", []):
        print(f"- {instruccion['text']}")


def main():
    print("=== Calculadora de rutas Chile - Argentina (GraphHopper) ===")

    while True:
        origen = input("\nIngrese Ciudad de Origen (o 's' para salir): ")
        if origen.lower() == "s":
            print("Saliendo del programa...")
            break

        destino = input("Ingrese Ciudad de Destino (o 's' para salir): ")
        if destino.lower() == "s":
            print("Saliendo del programa...")
            break

        coords_origen = obtener_coordenadas(origen)
        coords_destino = obtener_coordenadas(destino)

        if not coords_origen or not coords_destino:
            print("No se pudieron encontrar una o ambas ciudades. Intente de nuevo.")
            continue

        vehiculo = elegir_medio_transporte()
        resultado = calcular_ruta(coords_origen, coords_destino, vehiculo)
        mostrar_resultado(resultado)


if __name__ == "__main__":
    main()
