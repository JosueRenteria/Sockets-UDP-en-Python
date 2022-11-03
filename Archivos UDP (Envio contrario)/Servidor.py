# Declaracion de librerias.
from socket import *
import sys
import select

# Dirreccion Loopback y puerto de Escucha.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099
buffer = 1024

# Creamos el servidor con el protocolo UDP
socket_servidor= socket(AF_INET, SOCK_DGRAM)

# Establecer la coneccion con el servidor.
socket_servidor.bind((direccion_servidor, puerto_servidor))

mensaje, cliente_addres = socket_servidor.recvfrom(4096)

file_name="imagen.jpg"

# Manejar el Archivo.
f = open(file_name,"rb")
data = f.read(buffer)

# Enviar el archivo.
socket_servidor.sendto(file_name.encode(), cliente_addres)
socket_servidor.sendto(data, cliente_addres)

while (data):
    if(socket_servidor.sendto(data,cliente_addres)):
        print ("sending ...")
        data = f.read(buffer)
socket_servidor.close()
f.close()

