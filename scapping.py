import requests, urllib, time
from bs4 import BeautifulSoup as bs
import os

def imgdownload(urli, dirpath, name):
    completepath = dirpath + '/' + name + '.jpg'
    urllib.request.urlretrieve(urli,completepath)

def scrapeo(url, path, x):
    print("Iniciando scrapping de: " + url)
    html = urllib.request.urlopen(url)
    soup = bs(html, 'html.parser')
    try:
        os.mkdir("Imagenes")
    except Exception:
        pass

    imglink = soup.find_all('img')
    for imagen in imglink:
        io = imagen.get('src')
        nombre = 'Imagen' + str(x)
        try:
            imgdownload(io, path, nombre)
            x += 1
            time.sleep(3)
        except:
            break
    print("El scrapping de: " + url + " ha terminado\n")