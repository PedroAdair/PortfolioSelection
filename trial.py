from jinja2 import  Template , Environment, FileSystemLoader
import pdfkit
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import yaml
import logging
from bs4 import BeautifulSoup


# env = Environment(loader=FileSystemLoader('pdfReport'))
# template = env.get_template('ejemplo.html')
with open('ejemplo.html', 'r') as file:
        template = Template(file.read())

usuario = {
    'title': 'Reporte de Compra',
    'Encargado': 'Pedro Adair Avila',
    'constanzaLogo': './chichen_itza.jpg'
}

html = template.render(usuario)

pdfkit.from_string(html, 'report1.pdf')


# f = open('ejemplo.html', 'w')
# f.write(html)
# f.close()

# pdfkit.from_file('ejemplo.html', 'nuevo1.pdf')



pdfkit.from_string(html, 'report1.pdf')

# with open('pdfReport/ejemplo.html', 'r') as file:
#         template = Template(file.read())

# html = template.render(
#         titulo = 'este es un html',
#         mensaje = ' reporte', 
#         imgId = 'firma_id'

# )

# with open("config.yaml", "r") as f:
#             config = yaml.safe_load(f)


# user = 'Constanza'
# msg = MIMEMultipart()
# msg['From']= user
# msg['Subject']= "asd"
# msg['To']=  ', '.join(['pedro.adair.avila@gmail.com'])
# msg.attach(MIMEText(html, 'html'))
# with open('pdfReport/new_logo.png', 'rb') as imagen:
#         firma = MIMEImage

# with smtplib.SMTP('smtp.gmail.com') as server:
#                     server.starttls()
#                     server.login(config['USER_MAIL'], config['pw'])
#                     server.sendmail(config['USER_MAIL'],destinatarios, msg.as_string())

# def message_email(mensaje: str, destinatarios:list, asunto:str):
                
           

            
           
            
            

# message_email(mensaje: str, destinatarios:list, asunto:str)