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

#Resivir el Nombre del Archivo.
data, cliente_addres = socket_servidor.recvfrom(buffer)

print("Received File:",data.strip())
f = open("imagen2.jpg","wb")

# Resivimos los datos.
data, cliente_addres = socket_servidor.recvfrom(buffer)

try:
    while(data):
        data, cliente_addresr = socket_servidor.recvfrom(buffer)
        f.write(data)
        socket_servidor.settimeout(2)
        
except timeout:
    f.close()

socket_servidor.close()
print ("File Downloaded")

