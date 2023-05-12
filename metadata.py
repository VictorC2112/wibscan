from PIL import Image
from PIL.ExifTags import TAGS
import os

def metaextract(path):
    print("Iniciando extraccion de metadatos...")
    contfile = os.listdir(path)
    for imgfile in contfile:
        try:
            mimg = Image.open('../PIA/Imagenes/' + imgfile)
            exif_data = mimg.getexif()
            rn = '../PIA/Imagenes/' + imgfile + ' ' + 'Metadata' + '.txt'
            with open(rn, 'w') as rfile:
                for tagId in exif_data:
                    tag = TAGS.get(tagId, tagId)
                    data = exif_data.get(tagId)
                    rfile.write(f"{tag:16}:{data}\n")
        except:
            pass
    print("La extraccion de metadata ha terminado.\n")