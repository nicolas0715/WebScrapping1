import time
import os
import csv
import math
import json
#-----------------------------------------------------------------------------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
#-----------------------------------------------------------------------------------------------------------------------------#
from do_pdf import *
from enviar_mail import *
from pusheo import push

#--------------------------------------- Obtener Valores Viejos -----------------------------------------------------#

archivo_csv = 'productos.csv' # Nombre del archivo CSV
# Leer el archivo CSV y almacenar su contenido en una lista de diccionarios
datos_viejos1 = []
with open(archivo_csv, 'r') as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        datos_viejos1.append(fila)
#--------------------------------------------------------------------------------------------------------------------#

# Configurar el servicio y el controlador de Selenium
desired_version = "114.0.5735.90"
service = ChromeService(ChromeDriverManager(version=desired_version).install())
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acceder a la página de inicio de sesión
driver.get('https://www.asoprofarma.com.ar/Default.aspx')

# Ingresar credenciales
username_input = driver.find_element(By.NAME, 'Login1$UserName')
asopro_user = os.getenv('ASOPRO_USER')
password_input = driver.find_element(By.NAME, 'Login1$Password')
asopro_psw = os.getenv('ASOPRO_PSW')
password_input.send_keys(Keys.ENTER)
try:
# Hacer clic en el elemento <span>
    span_element = driver.find_element(By.CSS_SELECTOR, 'span.ui-button-icon-primary.ui-icon-closethick')
    span_element.click()
except:
    pass

# Hacer clic en el elemento <a>
a_element = driver.find_element(By.ID, 'ctl00_Lnkeshop')
a_element.click()

time.sleep(3)

productos1 = [
            'ACID BORI A SUFA 25G X25S',
            'AGUA OXI A SUFA 10 X 1L',
            'AGUA OXI A SUFA 10 X100ML',
            'AGUA OXI A SUFA 10 X250ML',
            'AGUA OXI A SUFA 10 X500ML',
            'BICARB SODIO A SUFA 100GR',
            'BICARB SODIO A SUFA 25X25',
            'BICARB SODIO A SUFA X250',
            'BORATO SODIO SANA 25X25S',
            'CLORURO MAGNES A SUFA 33G',
            'ENV ESTE GASANA CAJA X125',
            'ENV ESTE GASANA CAJA X300',
            'GASA A SUFA 5 10X10 CAJA',
            'GASA A SUFA 5 20X20 CAJA',
            'GASA A SUFA 5 30X30 CAJA',
            'VASE A SUFA LIQ X 125 ML',
            'VASE A SUFA LIQ X 250 ML',
            'VASE A SUFA LIQ X 500 ML',
            'VASE A SUFA SDA BLA X 60',
            ]
productos2 = [
            'ACTRON 20 CAP', 
            'ACTRON 600 A/RAP 20 CAP', 
            'ALCANFOR CAJA 128 TAB', 
            'ASPIRINETAS X 98 CMP', 
            'BAYASPIRINA x 30 CMP', 
            'BAYASPIRINA FTE x 20 CMP', 
            'BAYASPIRINA C LIMON 24SOB', 
            'BAYASPIRINA C CALIE 24SOB', 
            'BUSCAPINA 50 PERL',
            'BUSCAPINA DUO 60 CMP',
            'BUSCAPINA COMPO 60 CMP',
            'CAFIASPIRINA 30 CMP', 
            'CAFIASPIRINA PLUS x 20CMP',
            'CURITAS APO ELASTICA`24X8',
            'DORIXINA PACK 10 X 10C VL',
            'MEJORAL PED EXHI 30X10CMP',
            'MIGRAL 500 X 100 CMP',
            'NEXT T FTE 50 SOB',
            'PANU DESC ELITE SUA 6X10U',
            'RENNIE 12 CMP',
            'SERTAL CTO 50 CMP',
            'SOLU FISI PARA X 100 ML',
            'VICK VITAPYRENA 50 SOB',
            'VICK VITAPYRENA FTE 50SOB',
            ]
productos3 = [
            'ALIKAL C/PROS 30 SOB',
            'ARTROSTOP CALAMB S/AZU X4',
            'ARTROSTOP CALAMBRE X25SOB',
            'ARTROSTOP COLAGENO X25SOB',
            'ARTROSTOP ENERGY X 25 SOB',
            'ARTROSTOP MEMORY x 25 SOB',
            'ARTROSTOP T CALIE 24 SOB',
            'AZUF A SUFA BARR 20X5 BLI',
            'FEEN A MINT EXHI 20X6CHIC',
            'MANTE CACAO LISFAR EXH 20',
            'MYLANTA EXTRA EXH 96CM MA',
            'MYLANTA MENTA FRES 96 CMP',
            'PRES PRIME ANAT VERD 3UNI',
            'PRES PRIME ESPE BLAN 3UNI',
            'PRES PRIME LUBR AZUL 3UNI',
            'PRES PRIME MEGA/LARGE X 3',
            'PRES PRIME RETARD CELE 3U',
            'PRES PRIME S/FINO GRIS 3U',
            'PRES PRIME SKYN NEGRO X 3',
            'PRES PRIME STRONGER x3',
            'PRES PRIME TACHAS X 3 UNI',
            'PRES PRIME TEXT ROJO 3UNI',
            'PRES PRIME U/FINO NAR X3U',
            'PRES PRIME WARM VIOL 3UNI',
            'PRES TULIP CLAS 16X3',
            'TELA ADH HIPO POR25x9m12U',
            'TELA ADH HIPO POR5x9m 6U',
            'UVASAL 30 SOB (15X2)',
        ]
productos4 = [
            'CARBON ACT 250 X 100 CMP',
            'GENIOL 500 X 16 CMP',
            'GENIOL 650 X 16 CMP',
            'GENIOL 1 X 8 CMP',
            'GENIOL PLUS R/A 12 CAP',
            'PARACET ISA 30 CMP',
            'PARACET ISA EXH 1G 50X8CM',
            'PARACET ISA FTE EXHI X500',
            'PARACET LAZ VL 20 CMP',
            'TAFIROL EXHI 40 X 10 CMP',
            'TAFIROL FTE EXHI 30X10CMP',
            'TAFIROL 1 X 80 CMP',
            'TAFIROL PLUS A/RAP 8 CAP',
            'TAFIROLITO 80X20 CMP MAST',
            'TAFIROLITO MAST 20 CMP',
        ]

precios_dict = dict()

for lista in (productos1, productos2, productos3, productos4):
    for producto in lista:
        search_input = driver.find_element(By.CSS_SELECTOR, 'input#TextoBusqueda')
        search_input.clear()
        search_input.send_keys(producto)
        search_input.send_keys(Keys.ENTER)
        
        time.sleep(3)
        
        # Obtener el HTML de la página actual
        html = driver.page_source

        # Utilizar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Encontrar la etiqueta tr con la clase "handcursor gridviewProductosIsImpar"
        tr_element = soup.find('tr', class_='handcursor gridviewProductosIsImpar')

        # Encontrar todas las etiquetas td dentro de la etiqueta tr
        td_elements = tr_element.find_all('td')

        nombre__s = BeautifulSoup(str(td_elements[0]), 'html.parser')
        nombre = nombre__s.td.text.strip()
        
        valor_s = BeautifulSoup(str(td_elements[2]), 'html.parser')
        valor = valor_s.td.text.strip()
        valor = float(valor.replace(',', '.')) 
        valor = round(valor, 2)
        if valor == 0.0:
            valor_s = BeautifulSoup(str(td_elements[1]), 'html.parser')
            valor = (valor_s.td.text.strip()).replace('*', '')
            valor = (float(valor.replace(',', '.')) * 1.6)
            valor = round(valor, 2)
            
        precios_dict[nombre] = valor
                
# Cerrar el navegador
driver.quit()

#Conocer los productos que aumentaron
aumentados = []

for producto in datos_viejos1:
    if str(precios_dict.get(producto['nombre'])) != producto['precio']:
        aumentados.append(producto['nombre'])

print('Aumentaron ', len(aumentados), '\n')
if len(aumentados) != 0:
# Leer el contenido actual del archivo CSV y almacenarlos en una lista de diccionarios
    datos_viejos2 = []
    with open('productos.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos_viejos2.append(fila)

    for product in datos_viejos2:
        if product['nombre'] in aumentados:
            #Setear el precio nuevo por el viejo
            product['precio'] = precios_dict.get(product['nombre'])
            print('Precios_dict ==> ', precios_dict)
            print(product['nombre'])
            print(precios_dict.get(product['nombre']))
            product['precio_unitario'] = round((precios_dict.get(product['nombre'])) / int(product['unidades']), 2)
            product['precio_sugerido'] = math.ceil(product['precio_unitario'] / 10) * 10
            

    #Escribir los datos actualizados en el archivo
    campos = ['nombre', 'precio', 'unidades', 'precio_unitario', 'precio_sugerido']
    with open('productos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos_viejos2)

#Llamar a la funcion que genera un pdf por lista de productos
listas = productos1, productos2, productos3, productos4
for l, lista in enumerate(listas):
    #Hacer los pdfs individuales
    pdf_ind(int(l) + 1, lista)

#PDF general
pdf_gen()

productos_html = dict()
for l, producto in enumerate(aumentados):
    lista = []
    for producto_list in datos_viejos1:
        if str(producto) == producto_list['nombre']:
            precio_viejo = producto_list['precio']
            lista.append(str(producto))
            lista.append(precio_viejo)
    for producto_dict, precio in precios_dict.items():
        if str(producto) == str(producto_dict):
            lista.append(precio)
    productos_html[f'Producto{l+1}'] = lista

html_mail1 = f'''
<h3 style='margin:10px auto; color:green; font-size: 25px;'>Estos son los productos que aumentaros:</h3>
<div style="display: flex; justify-content: center;"> 
    <table style="margin: 10px 20px; background-color: gray; border: 2px solid black; border-radius: 10px; padding: 0px 8px;">
        <th style="padding:10px 8px; border-bottom: 2px solid black; font-size: 20px; margin: 4px 15px;">Producto</th>
        <th style="padding:10px 8px; border-bottom: 2px solid black; font-size: 20px; margin: 4px 15px;">Precio Anterior</th>
        <th style="padding:10px 8px; border-bottom: 2px solid black; font-size: 20px; margin: 4px 15px;">Precio Actual</th>
        <th style="padding:10px 8px; border-bottom: 2px solid black; font-size: 20px; margin: 4px 15px;">Variacion</th>
'''
for producto, valores in productos_html.items():
    html_mail1 += f'<tr><td style="text-align:center;padding:5px 10px 5px 0px; border-right: 2px solid black;">{valores[0]}</td>'
    html_mail1 += f'<td style="text-align:center;padding:5px 10px 5px 0px; border-right: 2px solid black;">{valores[1]}</td>'
    html_mail1 += f'<td style="text-align:center;padding:5px 10px 5px 0px; border-right: 2px solid black;">{valores[2]}</td>'
    variacion = round((100 * float(valores[2])) / float(valores[1]) - 100, 2)
    html_mail1 += f'<td style="text-align:center;padding:5px 10px 5px 0px">% {variacion}</td></tr>'

html_mail1 += '''
</table>
</div>
</body>
</html>
'''

listas = []
if len(aumentados) != 0:
    # Detectar en que archivo pdf estan los productos aumentados
    for lista, nombre in zip((productos1,productos2,productos3,productos4),('productos1','productos2','productos3','productos4',)):
        for p in lista:
            for pr in aumentados:
                if p == pr:
                    if nombre not in listas:
                        listas.append(nombre)
    # Enviar email
    msj1 = f'Tendrias que imprimir {[l for l in listas]}, porque aumentaron estos productos: {[n for n in aumentados]}'
    enviar_email(f'Aumentaron {len(aumentados)} productos, tendrias que imprimir {[l for l in listas]} ', html_mail1)
else:
    enviar_email('No hay aumentos por ahora.', 'No ha aumentado nada, pero aca estan las listas de precios por las dudas!')


for prod in aumentados:
    for n in datos_viejos1:
        if n['nombre'] == prod:
            print('El precio viejo era: ' + str(n['precio']))
            
#--------------------------------------------------- Subir a Google Drive --------------------------------------------------- #
'''
#Ruta raiz
ruta_raiz = os.getcwd()
# Credenciales de Google Drive
drive_json = json.loads(os.environ['DRIVE_JSON'])
credentials = service_account.Credentials.from_service_account_info(drive_json, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)


# Obtener la lista de archivos en la carpeta
carpeta_id = '1vDvnpUTIsC53sAyfBK3BamINb2UQFVnA'
result = drive_service.files().list(q=f"'{carpeta_id}' in parents", fields="files(id)").execute()
archivos = result.get('files', [])

# Eliminar cada archivo de la carpeta
for archivo in archivos:
    drive_service.files().delete(fileId=archivo['id']).execute()

# Subir archivos pdfs
contenido = os.listdir(ruta_raiz)

archivos_subir = []
for pdf in contenido:
    if pdf.endswith('.pdf'):
        ruta_a = os.path.join(ruta_raiz, pdf)
        archivos_subir.append(pdf)
        media_body = MediaFileUpload(pdf, mimetype='application/pdf', resumable=True)
        archivo_metadata = {'name': pdf, 'parents': [carpeta_id]}
        archivo = drive_service.files().create(body=archivo_metadata, media_body=media_body).execute()


#Link de la carpeta del drive
carpeta_drive = 'https://drive.google.com/drive/folders/1vDvnpUTIsC53sAyfBK3BamINb2UQFVnA?usp=sharing'
'''
#-------------------------------------------------- Pushear al repositorio -------------------------------------------------- #
push()