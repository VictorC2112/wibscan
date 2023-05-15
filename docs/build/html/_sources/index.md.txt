# wibscan

```{note}
Este es un proyecto de programación para ciberseguridad el cual ha sido desarrollado con fines practicos y educativos el cual tiene como objetivo principal el escaneo de paginas web permitiendo a los usuarios comprender mejor la estructura de los directorios en un sitio web y aprender sobre las posibles vulnerabilidades de seguridad asociadas.
```

## Informacion general
En este proyecto creamos un pequeño script multiherramienta para ciberseguridad web el cual se ejecuta desde la linea de comandos recibiendo como argumento una cadena de texto `str` que contendra una `URL` de una pagina especifica a analizar y opcionalmente una `API-KEY` de virus total.

Mediante el uso de un Web_Scrapig y algunas otras herramientas de terceros este proyecto sera capaz de lo siguiente:

* Extraccion de metadata de las imagenes 
* Reconocimiento de las tecnologias utilizadas
* Escaneo de directorios de la pagina
* Escaneo de la URL mediante el uso de una API a [VirusTotal](https://www.virustotal.com/gui/home/upload)
* Escaneo de puertos locales

y posteriormente generara un reporte de los resultados obtenidos.

```{warning}
Queremos dejar claro que el escaneo de directorios web solo debe llevarse a cabo en ambientes controlados, como pruebas de seguridad autorizadas o entornos de investigación legítimos. Si deseas utilizar esta herramienta, te insitamos a obtener el permiso expreso del propietario del sitio web antes de realizar cualquier escaneo.

Te recordamos que el uso no autorizado de esta herramienta para escanear directorios web puede violar las leyes y regulaciones aplicables. No respaldamos ni promovemos cualquier uso indebido o ilegal de esta herramienta, cada individuo es responsable de utilizarla de manera adecuada y en cumplimiento de la legislación vigente.
```
Para más acerca de este proyecto tenemos los siguientes apartados:


```{toctree}
uso
composicion
```