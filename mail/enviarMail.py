
from datos.datos import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Configurar los parámetros del servidor SMTP
servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587
usuario_smtp = correo
contraseña_smtp = contra

# Crear el objeto mensaje
mensaje = MIMEMultipart()
mensaje['From'] = usuario_smtp
mensaje['To'] = 'duranyoiner86@gmail.com'
mensaje['Subject'] = 'Prueba con Python'

# Añadir el cuerpo del mensaje
cuerpo_mensaje = '''Hola
socio
enviando
correo
desde python
te amo lindo
:3'''
mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

# Crear la conexión al servidor SMTP
servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
servidor.starttls()
servidor.login(usuario_smtp, contraseña_smtp)

# Enviar el correo electrónico
texto = mensaje.as_string()
servidor.sendmail(usuario_smtp, 'duranyoiner86@gmail.com', texto)

# Cerrar la conexión al servidor SMTP
servidor.quit()

print('Correo electrónico enviado con éxito')

