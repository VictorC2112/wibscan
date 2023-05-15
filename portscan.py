import socket, sys, builtwith, csv

def puertoscan(ip, listpuertos):
    try:
        for port in listpuertos:
            # Crea un objeto de socket
            sockt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sockt.settimeout(5)
            # Intenta establecer una conexión con el puerto especificado en la dirección IP dada
            result = sockt.connect_ex((ip,port))
            if result == 0:
                # Si la conexión se establece correctamente, el puerto está abierto
                print("\nEl puerto:"+ str(port) +" esta abierto")
            else:
                # Si la conexión falla, el puerto está cerrado
                print("\nEl puerto: " + str(port) +" esta cerrado")
            sockt.close()
    except socket.error as exc:
        # Si ocurre un error durante la conexión, muestra un mensaje de error
        print("\nNo se pudo establecer conexión")
        pass

def techscan(url):
    print("\nRealizando escaneo de tecnologías de la página...")
    # Abre un archivo en modo escritura para almacenar los resultados del escaneo
    with open("TecnologiaPAG.txt", 'w') as file:
        # Realiza el escaneo de tecnologías utilizando la biblioteca builtwith
        result = builtwith.parse(url)
        # Escribe la información del escaneo en el archivo
        file.write("Detección de tecnologías de: " + url + "\n\n")
        for key,value in result.items():
            file.write(str(key) + '=' + str(value) + "\n")
            
        print("\nEscaneo de tecnologías de: "+ url + " terminado.\n")
