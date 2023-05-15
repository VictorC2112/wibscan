# Se importan los módulos necesarios para el script

import os, socket, metadata, portscan, scapping, argparse
import vt_scan_website, gobuster


# Se crea un objeto ArgumentParser para procesar los argumentos de línea de comandos
# Se definen los argumentos "-ur", "-ap" y "-pl" con sus respectivas descripciones
parser = argparse.ArgumentParser()
parser.add_argument("-ur", dest="url", help="URL del scrapping y escaneo")
parser.add_argument("-ap", dest="ap1", help="Api Key VirusTotal")
parser.add_argument("-pl", dest="portl", help="Lista de puertos a escanear")
args = parser.parse_args()


# Se obtiene el nombre del host y la dirección IP del host
hn = socket.gethostname()
ipa = socket.gethostbyname(hn)


# Se inicializan algunas variables necesarias para el script
x=1
portlist = [80, 84, 243, 135, 445]
urlimg = args.url
apik = args.ap1


# Se define la ruta de la carpeta de imágenes
pathimg = '../wibscan/Imagenes'


if __name__ == "__main__":
    if args.url == None:
        print("Hay que agregar una URL")
    else:
        if args.ap1 == None:
            # Si no se proporciona una API Key de VirusTotal, se ejecutan ciertas funciones
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
            gobuster.dirscan(urlimg)
        else:
            # Si se proporciona una API Key de VirusTotal, se ejecutan todas las funciones
            vt_scan_website.vt_website_analysis(urlimg, args.ap1)
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
            gobuster.dirscan(urlimg)
    portscan.puertoscan(ipa, portlist)

# Se realiza un escaneo de puertos para la dirección IP del host
