from PIL import Image
from PIL.ExifTags import TAGS
import os

def metaextract(path):
    print("\nIniciando extraccion de metadatos...")  # Imprime un mensaje de inicio
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
    print("\nLa extraccion de metadata ha terminado.")  # Imprime un mensaje de finalización
