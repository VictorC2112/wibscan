import requests, urllib, time
from bs4 import BeautifulSoup as bs
import os

def imgdownload(urli, dirpath, name):
    completepath = dirpath + '/' + name + '.jpg'  # Ruta completa de archivo, incluyendo el nombre y la extensión
    urllib.request.urlretrieve(urli, completepath)  # Descargar la imagen desde la URL y guardarla en el directorio especificado

def scrapeo(url, path, x):
    print("\nIniciando scrapping de: " + url)  # Imprimir mensaje de inicio del scraping para la URL dada
    html = urllib.request.urlopen(url)  # Abrir la URL y obtener su contenido HTML
    soup = bs(html, 'html.parser')  # Crear un objeto BeautifulSoup para analizar el contenido HTML

    try:
        os.mkdir("Imagenes")  # Intentar crear un directorio llamado "Imagenes" (si aún no existe)
    except Exception:
        pass

    imglink = soup.find_all('img')  # Encontrar todas las etiquetas de imagen en el contenido HTML
    for imagen in imglink:
        io = imagen.get('src')  # Obtener la URL de origen de la imagen
        nombre = 'Imagen' + str(x)  # Generar un nombre único para la imagen
        try:
            imgdownload(io, path, nombre)  # Descargar la imagen en el directorio especificado
            x += 1  # Incrementar el contador para el nombre de la siguiente imagen
            time.sleep(3)  # Pausa de 3 segundos entre descargas de imagen (para evitar sobrecargar el servidor)
        except:
            break  # Si ocurre alguna excepción durante la descarga de la imagen, finalizar el bucle

    print("\nEl scrapping de: " + url + " ha terminado.")  # Imprimir mensaje indicando que se ha completado el scraping para la URL dada
