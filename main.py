
import os, socket, metadata, portscan, scapping, argparse
import vt_scan_website

parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url", help="url del scrapping y escaneo")
parser.add_argument("-ap", dest="ap1", help="Api Key VirusTotal")
parser.add_argument("-pl", dest="portl", help="Lista de puertos a escanear")
args = parser.parse_args()

hn = socket.gethostname()
ipa = socket.gethostbyname(hn)

x=1
portlist = [80, 84, 243]
urlimg = args.url
apik = args.ap1


pathimg = '../PIA/Imagenes'

if __name__ == "__main__":
    if args.url == None:
        print("Hay que agregar una url")
    else:
        if args.ap1 == None:    
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
        else:
            vt_scan_website.vt_website_analysis(urlimg, args.ap1)
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
    portscan.puertoscan(ipa, portlist)
