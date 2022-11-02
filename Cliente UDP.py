# Declaracion de librerias.
from socket import *
import sys

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099 

# Creamos el servidor con el protocolo UDP
socket_cliente = socket(AF_INET, SOCK_DGRAM)

#Mensaje de entrada.
mensaje = input("Ingresa un mensaje de Texto en Minusculas:")    

# Enviamos el servidor nuestro mensaje decodificado.
socket_cliente.sendto(mensaje.encode(),(direccion_servidor, puerto_servidor))

# Mensaje resibido de nuestro Servidor.
mensaje_modificado, servidor_addres = socket_cliente.recvfrom(4096)
print(mensaje_modificado).decode()

print("Socket Cerrado")
socket_cliente.close()

