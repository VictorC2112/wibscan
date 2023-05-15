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
        print('\nERROR. No se pudo escanear: ' + url)
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
            print('\nRealizando escaneo de la pagina...')
            threats_list = vt_data['data']['attributes']['threat_names']
            if len(threats_list) != 0:
                file.write("Posibles amenazas: \n")
                for threat in threats_list:
                    file.write(threat + "\n")  # Escribe las amenazas encontradas en el archivo
            else:
                file.write("No existen amenazas \n")  # Escribe un mensaje si no se encontraron amenazas
            last_time_checked = datetime_object = datetime.datetime.fromtimestamp(vt_data['data']['attributes']['last_submission_date'])
            last_time_checked = datetime_object.strftime('%Y-%m-%dT%H:%M')
            print('\nEscaneo realizado completo al:', last_time_checked)
            file.write("Estadisticas del ultimo analisis: \n")
            last_analysis_stats = vt_data['data']['attributes']['last_analysis_stats']
            for risk, risk_result in last_analysis_stats.items():
                file.write(f'{risk}: {risk_result}\n')  # Escribe las estadísticas del análisis en el archivo
        else:
            pass  # Si la respuesta no es exitosa, no se hace nada
