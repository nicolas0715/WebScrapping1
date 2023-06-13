import time
import os
import csv
import math
import json
#-----------------------------------------------------------------------------#
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

from twilio.rest import Client
#-----------------------------------------------------------------------------#
from do_pdf import *
from enviar_mail import *





#--------------------------------------- Estas lineas pasar al futuro archivo para crear los .txt
from datetime import date
fecha_actual = date.today()
fecha_formateada = 'Fecha ' + fecha_actual.strftime("%d/%m/%Y")
#---------------------------------------------------------------


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
service = ChromeService(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acceder a la página de inicio de sesión
driver.get('https://www.asoprofarma.com.ar/Default.aspx')

# Ingresar credenciales
username_input = driver.find_element(By.NAME, 'Login1$UserName')
username_input.send_keys('totino4541')
password_input = driver.find_element(By.NAME, 'Login1$Password')
password_input.send_keys('farma4542')
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
            'DORIXINA 50 CMP',
            'MEJORAL PED EXHI 30X10CMP',
            'MIGRAL 500 X 100 CMP',
            'NEXT T FTE 50 SOB',
            'PANU DESC ELITE SUA 6X10U',
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
            'UVASAL 30 SOB (15X2)',
        ]
productos4 = [
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

# datos_viejos = [
# {'nombre': 'ACID BORI A SUFA 25G X25S', 'precio': 3334.51, 'unidades': 25, 'precio_unitario': 133.36, 'precio_sugerido': 140}

# precios_dict = {
# 'ACID BORI A SUFA 25G X25S': 3334.51,
for producto in datos_viejos1:
    #Precio en datos_viejos1    =!     Precios en precios_dict
    if str(precios_dict.get(producto['nombre'])) != producto['precio']:
        aumentados.append(producto['nombre'])

# Una vez comparados los datos, ya se pueden guardar en el archivo csv

# Hay que guardar los datos de precios_dict en el archivo csv
# precios_dict = {
# 'ACID BORI A SUFA 25G X25S': 3334.51,                       ACID BORI A SUFA 25G X25S,3334.51,25,133.36,140
if len(aumentados) != 0:
# Leer el contenido actual del archivo CSV y almacenarlos en una lista de diccionarios
    datos_viejos2 = []
    with open('productos.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos_viejos2.append(fila)
#{'nombre': 'ACID BORI A SUFA 25G X25S', 'precio': 3334.51, 'unidades': 25, 'precio_unitario': 133.36, 'precio_sugerido': 140},
    for product in datos_viejos2:
        if product['nombre'] in aumentados:
            #Setear el precio nuevo por el viejo
            product['precio'] = precios_dict.get(product['nombre'])
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
    pdf_ind(l, lista)

#PDF general
pdf_gen()


#Guardar en el drive

#Ruta raiz
ruta_raiz = os.getcwd()
# Credenciales de Google Drive

#ruta_archivo_credenciales = os.path.join(ruta_raiz, 'driven-striker-386616-85af28be82bc.json') 
#credentials = service_account.Credentials.from_service_account_file(ruta_archivo_credenciales, scopes=['https://www.googleapis.com/auth/drive'])
#drive_service = build('drive', 'v3', credentials=credentials)
drive_json = json.loads(os.environ['DRIVE_JSON'])
credentials = service_account.Credentials.from_service_account_info(drive_json, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)


# Obtener la lista de archivos en la carpeta para eliminarlos
carpeta_id = '1vDvnpUTIsC53sAyfBK3BamINb2UQFVnA'
result = drive_service.files().list(q=f"'{carpeta_id}' in parents", fields="files(id)").execute()
archivos = result.get('files', [])
# Eliminar cada archivo de la carpeta
for archivo in archivos:
    drive_service.files().delete(fileId=archivo['id']).execute()


# Subir a Google Drive

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

print('Los productos que aumentaron son: ', aumentados)

# Editar el pdf para poner la fuente un poco mas grande, en negrita, y quizas agregarle padding top y bottom.

# Agregar la logica para que te envie el email SOLAMENTE si hay productos aumentados.

# Agregar la logica para que, si te envia el mail, solamente envie la lista que contiene productos que aumentaron.

# Agregar la logica para que los productos aumentados aparezcan con el fondo rojo en el pdf.


enviar_email()