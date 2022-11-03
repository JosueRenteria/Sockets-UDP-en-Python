# Declaracion de librerias.
from socket import *
import sys

# Funcion para Resivir un Archivos.
def resivir_archivo(file_name, socket: socket):
    # Declaracion del Buffer.
    buffer = 1024
    # Resivir el Nombre del Archivo. 
    data, servidor_addres = socket.recvfrom(buffer)

    # Abrimos y resivimos el archivo.
    print("Received File:",data.strip())
    f = open(file_name,"wb")

    # Resivimos los datos.
    data, servidor_addres = socket.recvfrom(buffer)

    # Funcion para resivir los metadatos del archivo.
    try:
        while(data):
            # Guardamos los Datos, escribimos el archivo creado.
            data, servidor_addres = socket.recvfrom(buffer)
            f.write(data)
            socket.settimeout(2)
    # Salida del proceso while.        
    except timeout:
        f.close()
    
    # Mensaje de que el Archivo se resivio.
    print ("File Downloaded")

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099
buffer = 1024 

# Creamos el servidor con el protocolo UDP
socket_cliente = socket(AF_INET, SOCK_DGRAM)

#Mensaje de entrada, que nos indica que nos conectamos al servidor..
mensaje = "Conectando"

# Enviamos el servidor nuestro mensaje decodificado.
socket_cliente.sendto(mensaje.encode(),(direccion_servidor, puerto_servidor))

# Nombre y ruta del archivo que se creara,
file_name = "imagen2.jpg"

# Mandamos a llamar a la funcion de resivir archivo.
resivir_archivo(file_name, socket_cliente)

# Cerramos nuestro sockets.
socket_cliente.close()