# Declaracion de librerias.
from socket import *
import sys

# Dirreccion Loopback y puerto de Escucha.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099

# Creamos el servidor con el protocolo UDP
socket_servidor= socket(AF_INET, SOCK_DGRAM)

# Establecer la coneccion con el servidor.
socket_servidor.bind((direccion_servidor, puerto_servidor))

# Mensaje de Inicio.
print("El servidor esta listo para resivir.")

while True:

    # Mensaje y el tamaño a resibir.
    mensaje, cliente_addres = socket_servidor.recvfrom(4096)
    print('received {} bytes from {}'.format(len(mensaje), cliente_addres))

    mensaje_modificado = mensaje.upper() # Hace el mensaje en mayusculas

    # Enviamos un mensaje.
    socket_servidor.sendto(mensaje_modificado, cliente_addres)