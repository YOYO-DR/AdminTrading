from BD.datos import correo,contra
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviarCodigo(enviar,asunto,cuerpo):
  try:
    # Configurar los parámetros del servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    usuario_smtp = correo
    contraseña_smtp = contra

    # Crear el objeto mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_smtp
    mensaje['To'] = enviar
    mensaje['Subject'] = asunto

    # Añadir el cuerpo del mensaje
    cuerpo_mensaje = cuerpo
    mensaje.attach(MIMEText(cuerpo_mensaje, 'html'))

    # Crear la conexión al servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, contraseña_smtp)

    # Enviar el correo electrónico
    texto = mensaje.as_string()
    servidor.sendmail(usuario_smtp, enviar, texto)

    # Cerrar la conexión al servidor SMTP
    servidor.quit()
    return True
  except Exception as e:
    print(str(e))
    return False

#b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials v10-20020a25c50a000000b00bcdb7d2a03bsm760170ybe.17 - gsmtp'