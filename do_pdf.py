from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import csv

def pdf_gen():
    archivo_csv = 'productos.csv'
    archivo_pdf = 'productos.pdf'

    # Leer los datos del archivo CSV y seleccionar las columnas deseadas
    datos = []
    with open(archivo_csv, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            datos.append([row[0], row[1], row[-2], row[-1]])

    # Crear un documento PDF y agregar la tabla
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter)

    # Definir el estilo de la tabla
    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Crear la tabla
    tabla = Table(datos)
    tabla.setStyle(estilo)

    # Crear el contenido del documento y agregar la tabla
    contenido_pdf = [tabla]

    # Generar el archivo PDF
    doc.build(contenido_pdf)

def pdf_ind(l, lista):
    archivo_csv = 'productos.csv'
    datos = []
    
    # Agregar la cabecera de columna a los datos
    cabecera = ['Nombre', 'Precio', 'Precio Unitario', 'Precio Sugerido']
    datos.insert(0, cabecera)
    
    for prod in lista:
        archivo_pdf = 'precios'+str(99)+'.pdf'

        # Leer los datos del archivo CSV y seleccionar las columnas deseadas
        with open(archivo_csv, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == prod:  # Filtrar los productos deseados
                    datos.append([row[0], row[1], row[-2], row[-1]])

        # Crear un documento PDF y agregar la tabla
        doc = SimpleDocTemplate(archivo_pdf, pagesize=letter)

        # Definir el estilo de la tabla
        estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 16),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTWEIGHT', (0, 0), (-1, -1), 'BOLD'),
            ('TOPPADDING', (0, 1), (-1, -1), 4), 
            ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ])

        # Crear la tabla
        tabla = Table(datos)
        tabla.setStyle(estilo)

        # Crear el contenido del documento
        contenido_pdf = [tabla]

        # Generar el archivo PDF
        doc.build(contenido_pdf)