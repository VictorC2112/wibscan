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

