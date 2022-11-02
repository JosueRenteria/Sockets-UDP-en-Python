# Declaracion de librerias.
from socket import *
import sys

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099
buffer = 1024 

# Creamos el servidor con el protocolo UDP
socket_cliente = socket(AF_INET, SOCK_DGRAM)

file_name="imagen.jpg"

# Manejar el Archivo.
f = open(file_name,"rb")
data = f.read(buffer)

# Enviar el archivo.
socket_cliente.sendto(file_name.encode(), (direccion_servidor, puerto_servidor))
socket_cliente.sendto(data, (direccion_servidor, puerto_servidor))

while (data):
    if(socket_cliente.sendto(data,(direccion_servidor, puerto_servidor))):
        print ("sending ...")
        data = f.read(buffer)
socket_cliente.close()
f.close()

