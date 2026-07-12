"""
Script: vlan.py
Descripción: Solicita al usuario un número de VLAN e indica si
corresponde al rango normal (1-1005) o al rango extendido (1006-4094).
"""

def clasificar_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1005:
        return "rango NORMAL (1 - 1005)"
    elif 1006 <= numero_vlan <= 4094:
        return "rango EXTENDIDO (1006 - 4094)"
    else:
        return None


def main():
    entrada = input("Ingrese el número de VLAN: ")

    if not entrada.isdigit():
        print("Error: debe ingresar solo números.")
        return

    numero_vlan = int(entrada)
    resultado = clasificar_vlan(numero_vlan)

    if resultado is None:
        print(f"La VLAN {numero_vlan} no es válida. "
              f"Debe estar entre 1 y 4094.")
    else:
        print(f"La VLAN {numero_vlan} corresponde al {resultado}.")


if __name__ == "__main__":
    main()
