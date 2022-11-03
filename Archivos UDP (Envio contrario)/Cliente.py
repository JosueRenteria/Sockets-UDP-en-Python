# Declaracion de librerias.
from socket import *
import sys

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099
buffer = 1024 

# Creamos el servidor con el protocolo UDP
socket_cliente = socket(AF_INET, SOCK_DGRAM)

#Mensaje de entrada.
mensaje = "Conectando"

# Enviamos el servidor nuestro mensaje decodificado.
socket_cliente.sendto(mensaje.encode(),(direccion_servidor, puerto_servidor))

#Resivir el Nombre del Archivo.
data, servidor_addres = socket_cliente.recvfrom(buffer)

print("Received File:",data.strip())
f = open("imagen2.jpg","wb")

# Resivimos los datos.
data, servidor_addres = socket_cliente.recvfrom(buffer)

try:
    while(data):
        data, servidor_addres = socket_cliente.recvfrom(buffer)
        f.write(data)
        socket_cliente.settimeout(2)
        
except timeout:
    f.close()

socket_cliente.close()
print ("File Downloaded")