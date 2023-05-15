# GUIA DE USO

Para ejecutar el script, debes abrir una terminal y usar el intérprete de Python junto con el nombre del archivo del script y los argumentos requeridos. 

El archivo del script principal se llama `wibscan.py`

El script ejecutará las acciones correspondientes según los argumentos proporcionados. Realizará el scrapping, extraerá metadatos de las imágenes, reconocimiento de las tecnologias utilizadas, escaneo de directorios de la URL, realizará un análisis de la URL en [VirusTotal](https://www.virustotal.com/gui/home/upload) (si se proporciona una clave de API) y finalmente escaneará los puertos locales especificados en la lista personalizada.

```{note}
Recuerda asegúrate de tener instalados todos los módulos y dependencias necesarios antes de ejecutar el script.
```

A continuación, se muestran algunos ejemplos de ejecución con diferentes argumentos:

**Ejemplo sin URL:**
```{code-block}
python wibscan.py
```
**Salida esperada:** "Hay que agregar una URL" y realiza escaneo de puertos locales
```{code-block}
Hay que agregar una URL
El puerto: 80 esta cerrado
El puerto: 84 esta cerrado
El puerto: 243 esta cerrado
El puerto:135 esta abierto
El puerto:445 esta abierto
```



**Ejemplo con URL y sin clave API de VirusTotal:**
```{code-block}
python wibscan.py -ur http://example.com
```
**Salida esperada:** Realizará el scrapping, extraerá metadatos de las imágenes, reconocimiento de las tecnologias utilizadas, escaneo de directorios de la URL y finalmente escaneará los puertos locales especificados en la lista personalizada.
```{code-block}
Iniciando scrapping de: http://example.com

El scrapping de: http://example.com ha terminado.

Iniciando extraccion de metadatos...

La extraccion de metadata ha terminado.

Realizando escaneo de tecnologías de la página...

Escaneo de tecnologías de: http://example.com terminado.

===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://example.com
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/05/15 02:37:02 Starting gobuster in directory enumeration mode
===============================================================
/123                  (Status: 200) [Size: 333827]
/00                   (Status: 200) [Size: 333827]
/20                   (Status: 200) [Size: 333827]
/1                    (Status: 200) [Size: 333827]
/10                   (Status: 200) [Size: 333827]
/03                   (Status: 200) [Size: 333827]
/1000                 (Status: 200) [Size: 333827]
/2                    (Status: 200) [Size: 333827]
/200                  (Status: 200) [Size: 333827]
/2004                 (Status: 200) [Size: 333827]
/2003                 (Status: 200) [Size: 333827]
/01                   (Status: 200) [Size: 333827]
                        .
                        .
                        .
/~operator            (Status: 429) [Size: 5]
/~mail                (Status: 429) [Size: 5]
/~root                (Status: 429) [Size: 5]
/~test                (Status: 429) [Size: 5]
/~sysadm              (Status: 429) [Size: 5]
/~user                (Status: 429) [Size: 5]
/~sys                 (Status: 429) [Size: 5]
/~sysadmin            (Status: 429) [Size: 5]
/~webmaster           (Status: 429) [Size: 5]

/~www                 (Status: 429) [Size: 5]
===============================================================
2023/05/15 02:37:47 Finished
===============================================================

Escaneo de directorios de: http://example.com completado.

El puerto: 80 esta cerrado

El puerto: 84 esta cerrado

El puerto: 243 esta cerrado

El puerto: 135 esta cerrado

El puerto: 445 esta cerrado

```



**Ejemplo con URL y clave API de VirusTotal:**
```{code-block}
python wibscan.py -ur http://example.com -ap YOUR_API_KEY
```
**Salida esperada:** Realizará el análisis de la URL en [VirusTotal](https://www.virustotal.com/gui/home/upload), el scrapping, extraerá metadatos de las imágenes, reconocimiento de las tecnologias utilizadas, escaneo de directorios de la URL y finalmente escaneará los puertos locales especificados en la lista personalizada.

El resultado de salida será igual que el ejemplo anterior a excepcion que al inicio de su ejecucion mostrara el siguiente mensaje:
```{code-block}
Realizando escaneo de la pagina...

Escaneo realizado completo al: 2023-05-15T01:30 (dependiendo la fecha y hora de ejecución)
```

```{note}
Al final de la ejecución del script podras encontrar la documentacion de tu busqueda dentro de la carpeta `wibscan` que es la carpeta principal donde se encuentra alojado este proyecto.
```