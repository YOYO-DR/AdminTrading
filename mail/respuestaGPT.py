""" import tkinter as tk
import hashlib
import mysql.connector
import smtplib
import random

# Configurar la conexión a la base de datos MySQL
conexion_mysql = mysql.connector.connect(
    host='localhost',
    user='usuario',
    password='contraseña',
    database='basedatos'
)

# Función para encriptar una contraseña utilizando hashlib
def encriptar_contraseña(contraseña):
    # Convertir la contraseña a bytes
    contraseña_bytes = bytes(contraseña, 'utf-8')
    # Crear un objeto hashlib para utilizar el algoritmo SHA256
    hash_obj = hashlib.sha256(contraseña_bytes)
    # Obtener la representación hexadecimal del hash
    hash_hex = hash_obj.hexdigest()
    return hash_hex

# Función para enviar un correo electrónico con un código de verificación
def enviar_correo(destinatario, codigo):
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    usuario_smtp = 'tu_correo@gmail.com'
    contraseña_smtp = 'tu_contraseña_de_aplicacion'

    mensaje = f'Código de verificación: {codigo}'

    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, contraseña_smtp)

    servidor.sendmail(usuario_smtp, destinatario, mensaje)

    servidor.quit()

# Función para mostrar la ventana de inicio de sesión
def mostrar_ventana_inicio_sesion():
    ventana_inicio_sesion = tk.Toplevel()
    ventana_inicio_sesion.title('Inicio de sesión')

    etiqueta_usuario = tk.Label(ventana_inicio_sesion, text='Usuario:')
    etiqueta_usuario.pack()
    entrada_usuario = tk.Entry(ventana_inicio_sesion)
    entrada_usuario.pack()

    etiqueta_contraseña = tk.Label(ventana_inicio_sesion, text='Contraseña:')
    etiqueta_contraseña.pack()
    entrada_contraseña = tk.Entry(ventana_inicio_sesion, show='*')
    entrada_contraseña.pack()

    def validar_inicio_sesion():
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()
        # Encriptar la contraseña
        contraseña_encriptada = encriptar_contraseña(contraseña)
        # Verificar las credenciales en la base de datos
        cursor_mysql = conexion_mysql.cursor()
        consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
        valores = (usuario, contraseña_encriptada)
        cursor_mysql.execute(consulta, valores)
        resultado = cursor_mysql.fetchone()
        if resultado is not None:
            # Mostrar la ventana principal
            ventana_inicio_sesion.destroy()
            mostrar_ventana_principal()
        else:
            tk.messagebox.showerror('Error', 'Credenciales inválidas')

    boton_iniciar_sesion = tk.Button(ventana_inicio_sesion, text='Iniciar sesión', command=validar_inicio_sesion)
    boton_iniciar_sesion.pack()

# Función para mostrar la ventana de registro
def mostrar_ventana_registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title('Registro')

    etiqueta_correo = tk.Label(ventana_registro, text='Correo') """





""" import tkinter as tk
from tkinter import messagebox
import hashlib
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datos.datos import *
import random

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="prueba_envio"
)
cursor = db.cursor()

def login():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (username, hashed_password))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Inicio de sesión", "Usuario o contraseña incorrectos")
    
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

login_window = tk.Tk()
login_window.title("Inicio de sesión")

username_label = tk.Label(login_window, text="Nombre de usuario")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Contraseña")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Iniciar sesión", command=login)
login_button.pack()

login_window.mainloop()

def enviar_codigo():
    correo_destino = correo_entry.get()

    codigo = str(random.randint(100000, 999999))
    mensaje = MIMEMultipart()
    mensaje['From'] = 'tu_correo@gmail.com'
    mensaje['To'] = correo_destino
    mensaje['Subject'] = 'Código de verificación'

    cuerpo_mensaje = f'Tu código de verificación es {codigo}'
    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    usuario_smtp = 'tu_correo@gmail.com'
    contraseña_smtp = 'tu_contraseña_de_aplicacion'

    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, contraseña_smtp)

    texto = mensaje.as_string()
    servidor.sendmail(usuario_smtp, correo_destino, texto)

    servidor.quit()

 """

