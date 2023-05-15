# COMPOSICION DEL PROYECTO

El proyecto se compone de diferentes módulos para su funcionamiento.
El módulo principal es `main.py` el cual mandara a llamar a los otros modulos durante su ejecución.


## wibscan.py
```{code-block}
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

```
1. Importa los módulos necesarios para el funcionamiento del script.

2. Crea un objeto ArgumentParser para procesar los argumentos de línea de comandos. Define los argumentos -ur, -ap y -pl con sus respectivas descripciones.

3. Obtiene el nombre del host y la dirección IP del host.

4. Inicializa variables necesarias para el script, como x, portlist, urlimg y apik.

5. Define la ruta de la carpeta de imágenes.

6. Comienza la ejecución principal del script.

7. Verifica si se proporcionó una URL como argumento. Si no se proporciona, imprime un mensaje indicando que se debe agregar una URL.

8. Si se proporciona una URL pero no se proporciona una API Key de VirusTotal, ejecuta ciertas funciones relacionadas con el scrapping de datos, extracción de metadatos y escaneo de puertos.

9. Si se proporciona una URL y una API Key de VirusTotal, ejecuta todas las funciones mencionadas anteriormente, además de realizar un análisis de la página web utilizando la API de VirusTotal.

10. Finalmente, se realiza un escaneo de puertos para la dirección IP del host utilizando la lista de puertos especificada en portlist.




## scapping.py
```{code-block}
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

    print("El scrapping de: " + url + " ha terminado.\n")  # Imprimir mensaje indicando que se ha completado el scraping para la URL dada
```
El script consta de dos funciones principales:

``imgdownload (urli, dirpath, name)``Esta función toma una URL de imagen (urli), un directorio de destino (dirpath) y un nombre de archivo (name). Descarga la imagen de la URL y la guarda en el directorio especificado con el nombre de archivo dado.

``scrapeo(url, path, x)``Esta función realiza el web scraping de la página web dada por la URL. Toma la URL de la página web (url), la ruta del directorio de destino (path) y un contador (x) utilizado para nombrar las imágenes descargadas. Dentro de la función, se abre la URL de la página web y se crea un objeto BeautifulSoup para analizar su contenido HTML. A continuación, se intenta crear un directorio llamado "Imagenes" (si aún no existe). Después, se busca todas las etiquetas de imagen (<img>) en el contenido HTML de la página y se itera sobre ellas. Para cada imagen, se obtiene la URL de origen (io), se genera un nombre único para la imagen (nombre), se llama a la función imgdownload() para descargar la imagen en el directorio especificado y se incrementa el contador x. Se introduce una pausa de 3 segundos entre cada descarga de imagen. Si ocurre alguna excepción durante la descarga de la imagen, se finaliza el bucle for. Finalmente, se imprime un mensaje indicando que se ha completado el web scraping de la URL dada.




## metadata.py
```{code-block}
from PIL import Image
from PIL.ExifTags import TAGS
import os

def metaextract(path):
    print("Iniciando extraccion de metadatos...")  # Imprime un mensaje de inicio
    contfile = os.listdir(path)  # Obtiene la lista de archivos en el directorio especificado por 'path'
    for imgfile in contfile:  # Itera sobre cada archivo en el directorio
        try:
            mimg = Image.open('../wibscan/Imagenes/' + imgfile)  # Abre la imagen utilizando PIL
            exif_data = mimg.getexif()  # Obtiene los metadatos EXIF de la imagen
            rn = '../wibscan/Imagenes/' + imgfile + ' ' + 'Metadata' + '.txt'  # Construye el nombre del archivo de salida para guardar los metadatos
            with open(rn, 'w') as rfile:  # Abre el archivo de salida en modo de escritura
                for tagId in exif_data:  # Itera sobre cada etiqueta de metadatos en los datos EXIF
                    tag = TAGS.get(tagId, tagId)  # Obtiene el nombre legible de la etiqueta
                    data = exif_data.get(tagId)  # Obtiene el valor de la etiqueta
                    rfile.write(f"{tag:16}:{data}\n")  # Escribe la etiqueta y su valor en el archivo de salida
        except:
            pass  # Si hay algún error al procesar la imagen, se ignora y se continúa con el siguiente archivo
    print("La extraccion de metadata ha terminado.\n")  # Imprime un mensaje de finalización
```

En este script se define una función llamada `metaextract` que toma como argumento el directorio path donde se encuentran las imágenes.

1. Imprime un mensaje indicando que se está iniciando la extracción de metadatos.

2. Obtiene una lista de todos los archivos en el directorio especificado usando os.listdir(path) y la guarda en la variable contfile.

3. Itera sobre cada archivo en la lista contfile utilizando un bucle for.

4. Dentro del bucle, intenta abrir la imagen utilizando Image.open('../wibscan/Imagenes/' + imgfile) y la guarda en la variable mimg.

5. Luego, obtiene los datos EXIF de la imagen utilizando el método getexif() de mimg y los guarda en la variable exif_data.

6. Crea una ruta de archivo para el archivo de texto de salida utilizando el nombre de archivo de la imagen y la extensión ".txt". Por ejemplo, si el nombre de archivo de la imagen es "imagen.jpg", la ruta de archivo será "../wibscan/Imagenes/imagen.jpg Metadata.txt". La ruta de archivo se guarda en la variable rn.

7. Abre el archivo de texto de salida en modo de escritura utilizando open(rn, 'w') y lo guarda en la variable rfile.

8. Itera sobre cada identificador de etiqueta en exif_data utilizando otro bucle for.

9. Para cada identificador de etiqueta, obtiene el nombre de la etiqueta correspondiente utilizando el diccionario TAGS.get(tagId, tagId) y lo guarda en la variable tag.

10. Obtiene el valor de datos correspondiente al identificador de etiqueta utilizando exif_data.get(tagId) y lo guarda en la variable data.

11. Escribe la etiqueta y los datos en el archivo de texto utilizando rfile.write(f"{tag:16}:{data}\n"). Los datos se escriben en el formato "etiqueta: datos".

12. Después de procesar todos los identificadores de etiquetas en exif_data, se cierra el archivo de texto.

13. Si ocurre una excepción durante el proceso de apertura de la imagen o la extracción de metadatos, se captura la excepción utilizando except: y se pasa al siguiente archivo sin generar un error.

14. Después de completar el bucle for principal, se imprime un mensaje indicando que la extracción de metadatos ha terminado.




## portscan.py
```{code-block}
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
                print("El puerto:"+ str(port) +" esta abierto")
            else:
                # Si la conexión falla, el puerto está cerrado
                print("El puerto: " + str(port) +" esta cerrado")
            sockt.close()
    except socket.error as exc:
        # Si ocurre un error durante la conexión, muestra un mensaje de error
        print("No se pudo establecer conexión")
        pass

def techscan(url):
    print("Realizando escaneo de tecnologías de la página...")
    # Abre un archivo en modo escritura para almacenar los resultados del escaneo
    with open("TecnologiaPAG.txt", 'w') as file:
        # Realiza el escaneo de tecnologías utilizando la biblioteca builtwith
        result = builtwith.parse(url)
        # Escribe la información del escaneo en el archivo
        file.write("Detección de tecnologías de: " + url + "\n\n")
        for key,value in result.items():
            file.write(str(key) + '=' + str(value) + "\n")
            
        print("Escaneo de tecnologías de: "+ url + " terminado.\n")
```

El script proporciona dos funciones principales: ``puertoscan(ip, listpuertos)`` y ``techscan(url)``

1. La función ``puertoscan(ip, listpuertos)`` se encarga de escanear los puertos de una dirección IP especificada. Recibe como parámetros la dirección IP (ip) y una lista de puertos (listpuertos) a escanear.

2. Dentro de la función`` puertoscan()``, se realiza un bucle que itera sobre cada puerto en la lista de puertos proporcionada.

3. Para cada puerto, se crea un objeto de socket utilizando socket.socket(socket.AF_INET, socket.SOCK_STREAM). Se configura un tiempo de espera de 5 segundos para establecer una conexión con ese puerto en la dirección IP especificada.

4. Se utiliza sockt.connect_ex((ip, port)) para intentar establecer la conexión con el puerto. Si el resultado de connect_ex() es 0, significa que la conexión se estableció correctamente y, por lo tanto, el puerto está abierto. Se muestra un mensaje indicando que el puerto está abierto. De lo contrario, se muestra un mensaje indicando que el puerto está cerrado.

5. Después de realizar el escaneo de todos los puertos, se cierra el objeto de socket.

6. La función ``techscan(url)`` se encarga de escanear las tecnologías utilizadas en una página web. Recibe como parámetro la URL de la página (url).

7. Dentro de la función ``techscan()``, se abre un archivo llamado "TecnologiaPAG.txt" en modo escritura para almacenar los resultados del escaneo.

8. Se utiliza la biblioteca builtwith.parse(url) para realizar el escaneo de tecnologías de la página. Los resultados se almacenan en la variable result.

9. A continuación, se escribe en el archivo la información del escaneo, incluyendo la URL y las tecnologías detectadas.

10. Después de escribir en el archivo, se muestra un mensaje indicando que el escaneo de tecnologías ha finalizado.



## gobuster.py

```{code-block}
import subprocess, os

def dirscan(url):
    try:
        os.mkdir("GoBuster")  # Crea un directorio llamado "GoBuster" si no existe
    except Exception:
        pass

    # Construye el comando para ejecutar GoBuster y realiza el escaneo de directorios
    command = "gobuster dir -u " + url + " -w /usr/share/dirb/wordlists/small.txt -o ../wibscan/GoBuster/results.txt"
    subprocess.run(command, shell=True, universal_newlines=True)
    
    print("\nEscaneo de directorios de: " + url + " completado.")  # Imprime un mensaje indicando que el escaneo ha finalizado.

```
1. Intenta crear un directorio llamado "GoBuster". Si el directorio ya existe, se omite este paso sin generar ningún error.

2. Construye un comando de línea de comandos que utiliza la herramienta GoBuster para realizar el escaneo de directorios en la URL proporcionada.

    * El comando utiliza la opción -u para especificar la URL a escanear.

    * La opción -w se utiliza para indicar la ubicación de un archivo de lista de palabras (en este caso, small.txt).
    * La opción -o se utiliza para especificar la ubicación y el nombre del archivo de resultados (results.txt) dentro de la carpeta "GoBuster".

3. Ejecuta el comando utilizando subprocess.run(). Esto permite ejecutar comandos en el sistema operativo desde el script de Python.

4. Imprime un mensaje indicando que el escaneo de directorios para la URL proporcionada ha sido completado.




## vt_scan_website.py

```{code-block}
import requests, base64, datetime, json, csv
from urllib.parse import quote

def vt_scan_website(url, apikey):
    headers = {
    "accept": "application/json",
    "x-apikey": apikey,
    "content-type": "application/x-www-form-urlencoded"
    }
    payload = 'url=' + quote(url)
    vt_scan_url = 'https://www.virustotal.com/api/v3/urls'
    vt_scan_response = requests.post(vt_scan_url,data=payload,headers=headers)
    if vt_scan_response.status_code == 200:
        return 1  # Retorna 1 si el escaneo es exitoso
    else:
        return 0  # Retorna 0 si el escaneo falla


def vt_website_analysis(url, apikey):
    vtheader = {'x-apikey':apikey}
    if vt_scan_website(url, apikey) == 0:  # Verifica si el escaneo falló
        print('ERROR. No se pudo escanear la URL')
        return
    else:
        pass  # Si el escaneo fue exitoso, continúa con el análisis
    with open("Pagescan.txt", 'w') as file:  # Abre el archivo de texto para escribir los resultados
        file.write("Escaneo de: " + url + "\n\n")
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")  # Codifica la URL para su uso en la API
        vt_analysis_url = f'https://www.virustotal.com/api/v3/urls/{url_id}'
        vt_analysis_response = requests.get(url=vt_analysis_url,headers=vtheader)
        if vt_analysis_response.status_code == 200:
            vt_data = json.loads(vt_analysis_response.text)
            print('Realizando escaneo de la pagina...')
            threats_list = vt_data['data']['attributes']['threat_names']
            if len(threats_list) != 0:
                file.write("Posibles amenazas: \n")
                for threat in threats_list:
                    file.write(threat + "\n")  # Escribe las amenazas encontradas en el archivo
            else:
                file.write("No existen amenazas \n")  # Escribe un mensaje si no se encontraron amenazas
            last_time_checked = datetime_object = datetime.datetime.fromtimestamp(vt_data['data']['attributes']['last_submission_date'])
            last_time_checked = datetime_object.strftime('%Y-%m-%dT%H:%M')
            print('Escaneo realizado completo al:', last_time_checked)
            file.write("Estadisticas del ultimo analisis: \n")
            last_analysis_stats = vt_data['data']['attributes']['last_analysis_stats']
            for risk, risk_result in last_analysis_stats.items():
                file.write(f'{risk}: {risk_result}\n')  # Escribe las estadísticas del análisis en el archivo
        else:
            pass  # Si la respuesta no es exitosa, no se hace nada

```

El script proporciona funciones para escanear y analizar un sitio web utilizando la API de VirusTotal.

1. La función ``vt_scan_website(url, apikey)`` realiza un escaneo del sitio web especificado utilizando la API de VirusTotal. Toma la URL del sitio web y la clave de la API como argumentos. Envía una solicitud POST a la URL de escaneo de VirusTotal con la URL del sitio web y la clave de la API como datos y encabezados. Si la respuesta tiene un código de estado 200, se considera que el escaneo fue exitoso y la función devuelve 1. De lo contrario, devuelve 0.

2. La función ``vt_website_analysis(url, apikey)`` realiza un análisis detallado de un sitio web utilizando la API de VirusTotal. Toma la URL del sitio web y la clave de la API como argumentos. Primero, verifica si el escaneo del sitio web es exitoso utilizando la función ``vt_scan_website()``. Si el escaneo falla, muestra un mensaje de error y finaliza la función. Si el escaneo es exitoso, continúa con el análisis.

3. La función abre un archivo de texto llamado "Pagescan.txt" en modo escritura para almacenar los resultados del análisis.

4. Codifica la URL del sitio web utilizando base64 para su uso en la API de VirusTotal.

5. Realiza una solicitud GET a la URL de análisis de VirusTotal con la URL codificada y la clave de la API como encabezados. Obtiene los datos de análisis de la respuesta y los convierte en formato JSON.

6. Muestra un mensaje indicando que se está realizando el escaneo de la página.

7. Obtiene la lista de posibles amenazas del atributo 'threat_names' de los datos de análisis. Si la lista no está vacía, escribe las amenazas encontradas en el archivo de texto.

8. Si no se encuentran amenazas, escribe un mensaje en el archivo de texto indicando que no hay amenazas.

9. Obtiene la fecha y hora del último análisis del atributo 'last_submission_date' y la formatea como una cadena legible.

10. Muestra un mensaje indicando que el escaneo se ha completado y muestra la fecha y hora del último análisis.

11. Escribe las estadísticas del último análisis en el archivo de texto, donde cada estadística se muestra como "riesgo: resultado".