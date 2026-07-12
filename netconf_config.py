"""
Script: netconf_config.py
Descripción: Se conecta al router CSR1000v vía NETCONF, cambia el
hostname usando los apellidos del equipo y crea la interfaz loopback 11
con dirección IPv4 11.11.11.11/32.
"""

from ncclient import manager

# Datos de conexión al router
HOST = "10.0.2.5"
PORT = 830
USER = "admin"
PASSWORD = "admin123"

NUEVO_HOSTNAME = "Jaramillo-Arros-Hernandez"

# Payload NETCONF para cambiar el hostname
CONFIG_HOSTNAME = f"""
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>{NUEVO_HOSTNAME}</hostname>
  </native>
</config>
"""

# Payload NETCONF para crear la interfaz Loopback 11
CONFIG_LOOPBACK = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""


def main():
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USER,
        password=PASSWORD,
        hostkey_verify=False,
        device_params={"name": "csr"},
        allow_agent=False,
        look_for_keys=False
    ) as m:
        print("Conexión NETCONF establecida con éxito.\n")

        # Cambiar hostname
        print(f"Cambiando el hostname del router a '{NUEVO_HOSTNAME}'...")
        respuesta_hostname = m.edit_config(target="running", config=CONFIG_HOSTNAME)
        print("Resultado:", respuesta_hostname)

        # Crear loopback 11
        print("\nCreando interfaz Loopback 11 con IP 11.11.11.11/32...")
        respuesta_loopback = m.edit_config(target="running", config=CONFIG_LOOPBACK)
        print("Resultado:", respuesta_loopback)

        print("\nConfiguración aplicada correctamente.")


if __name__ == "__main__":
    main()
