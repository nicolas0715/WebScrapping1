import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from dotenv import load_dotenv

import os

attachment_files = ['productos1.pdf', 'productos2.pdf', 'productos3.pdf', 'productos4.pdf']

def enviar_email(subject, message):

    load_dotenv()
    
    # Configuración del servidor SMTP y credenciales
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'oteronicolas3@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')

    # Configuración del correo electrónico
    from_addr = 'oteronicolas3@gmail.com'
    to_addr = 'oteronicolas3@gmail.com'#, farmaciatotino@gmail.com'
        
    # Crear objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Adjuntar cuerpo del correo
    msg.attach(MIMEText(message, 'html'))

    # Adjuntar archivos
    for attachment_file in attachment_files:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(open(attachment_file, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_file)
        msg.attach(attachment)

    # Conexión y envío del correo electrónico
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        print('Correo enviado correctamente')