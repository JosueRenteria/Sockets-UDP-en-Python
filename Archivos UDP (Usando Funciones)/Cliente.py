# Declaracion de librerias.
from socket import *
import sys

# Funcion para enviar Archivos.
def envio_archivo(file_name, socket_cliente: socket, direccion_servidor, puerto_servidor):
    # Manejar el Archivo y ponerlo en modo lectura.
    buffer = 1024 
    f = open(file_name,"rb")
    data = f.read(buffer)

    # Enviar el Nombre del Archivo y si el archivo esta vacio o no.
    socket_cliente.sendto(file_name.encode(), (direccion_servidor, puerto_servidor))
    socket_cliente.sendto(data, (direccion_servidor, puerto_servidor))

    # Enviado de nuestro Archivo en porciones del tamaño del buffer
    while (data):
        if(socket_cliente.sendto(data,(direccion_servidor, puerto_servidor))):
            print ("Enviando Archivo...")
            data = f.read(buffer)
    
    #  Cierre de nuestro Archivo.
    f.close()

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099

# Creamos el servidor con el protocolo UDP.
socket_cliente = socket(AF_INET, SOCK_DGRAM)

# Nombre de nuestro archivo y llamado a la funcion de resivir archivo.
file_name="imagen.jpg"
envio_archivo(file_name, socket_cliente, direccion_servidor, puerto_servidor)

# Cierre de nuestro socket.
socket_cliente.close()