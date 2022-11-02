# Declaracion de librerias.
from socket import *
import sys
import select

# Funcion que resive Archivos.
def resivir_archivo(socket_servidor: socket):
    # Resivir el Nombre del Archivo y declaracion del buffer.
    buffer = 1024
    data, cliente_addres = socket_servidor.recvfrom(buffer)

    # Abrir y mostrar el nombre del archivo resivido.
    print("Received File:",data.strip().decode())
    f = open("imagen2.jpg","wb")

    # Resivimos los datos.
    data, cliente_addres = socket_servidor.recvfrom(buffer)

    # Abrimos el proceso para copiar el archivo.
    try:
        # Creamos un nuevo archivo con los datos del anterior.
        while(data):
            data, cliente_addres = socket_servidor.recvfrom(buffer)
            f.write(data)
            socket_servidor.settimeout(2)
    # Cerramos el archivo.    
    except timeout:
        f.close()
    
    print ("File Downloaded")

# Dirreccion Loopback y puerto de Escucha.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099

# Creamos el servidor con el protocolo UDP
socket_servidor= socket(AF_INET, SOCK_DGRAM)

# Establecer la coneccion con el servidor.
socket_servidor.bind((direccion_servidor, puerto_servidor))

# Llamos a la funcion resivir archivo. 
resivir_archivo(socket_servidor)

# Cerramos el Servidor (Normalmente siempre esta abierto, pero, para esta practica lo cerramos).
socket_servidor.close()
