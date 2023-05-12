import socket, sys, builtwith, csv

def puertoscan(ip, listpuertos):
    try:
        for port in listpuertos: 
            sockt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sockt.settimeout(5)
            result = sockt.connect_ex((ip,port))
            if result == 0:
                print("El puerto:"+ str(port) +" esta abierto")
            else:
                print("El puerto: " + str(port) +" esta cerrado")
            sockt.close()
    except socket.error as exc:
        print("No se pudo establecer conexion")
        pass

def techscan(url):
    print("Realizando escaneo de tecnologias de la pagina...")
    with open("TecnologiaPAG.txt", 'w') as file:
        result = builtwith.parse(url)
        file.write("Deteccion de tecnologias de: " + url + "\n")
        for key,value in result.items():
            file.write(str(key) + '=' + str(value) + "\n")
            
        print("Escaneo de tecnologias de: "+ url + "terminado.")