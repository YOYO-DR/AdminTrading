from tkinter import Label,Tk,StringVar,Entry,Button,PhotoImage,messagebox
import tkinter.ttk as ttk
import hashlib
import mysql.connector
import smtplib
import random
import os
def conexion():
  con = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='root',
  port='3306',
  database='prueba_envio',
  auth_plugin='mysql_native_password')
  cursor = con.cursor()
  cursor.close()
  return con

class Inicio():
  def __init__(self):
    self.root = Tk()
    self.root.title("Inicio de sesión")
    self.root.geometry("300x300")
    self.root.resizable(False, False)
    self.root.config(bg="black")

    #Usuario
    self.entrysUsuContra()

    #botones
    self.botonesInicioRegistro()

    self.root.mainloop()
  
  def entrysUsuContra(self):
    #label de usuario
    self.usuarioLabel=Label(self.root,text='Usuario',bg='black',fg='white',font=('Leelawadee UI Semilight',15))
    self.usuarioLabel.pack(anchor='center',pady=10)

    #entry de usuario
    self.usuarioEntryValor=StringVar()
    self.usuarioEntry=Entry(self.root,width=20,font=('Leelawadee UI Semilight',10),textvariable=self.usuarioEntryValor)
    self.usuarioEntry.pack(anchor='center',pady=5)

    #label de contraseña
    self.contraLabel=Label(self.root,text='Contraseña',bg='black',fg='white',font=('Leelawadee UI Semilight',15))
    self.contraLabel.pack(anchor='center',pady=10)

    #entry de contraseña
    self.contraEntryValor=StringVar()
    self.contraEntry=Entry(self.root,width=20,font=('Leelawadee UI Semilight',10),textvariable=self.contraEntryValor,show='*')
    self.contraEntry.pack(anchor='center',pady=5)





    #,font=('Leelawadee UI Semilight',10),height=1,bg='#8c8c8c'

  def botonesInicioRegistro(self):
    #boton iniciar sesion
    def on_enterI(event):
        self.botonIniciarS['background'] = '#92e27a'
        self.botonIniciarS['foreground'] = '#141414'

    def on_leaveI(event):
        self.botonIniciarS['background'] = '#141414'
        self.botonIniciarS['foreground'] = '#92e27a'

    self.botonIniciarS=Button(self.root,
                        width=15,
                        text='Iniciar sesion',
                        fg='#92e27a',
                        bg='#141414',
                        border=0,
                        activeforeground='#141414',
                        activebackground='#92e27a',
                        command=self.iniciarSesion)

    self.botonIniciarS.bind("<Enter>",on_enterI)
    self.botonIniciarS.bind("<Leave>",on_leaveI)

    self.botonIniciarS.pack(anchor='center',pady=5)

    #boton registrar
    def on_enterR(event):
        self.botonRegistrarU['background'] = '#25dae9'
        self.botonRegistrarU['foreground'] = '#141414'

    def on_leaveR(event):
        self.botonRegistrarU['background'] = '#141414'
        self.botonRegistrarU['foreground'] = '#25dae9'

    self.botonRegistrarU=Button(self.root,
                        width=15,
                        text='Registrar',
                        fg='#25dae9',
                        bg='#141414',
                        border=0,
                        activeforeground='#141414',
                        activebackground='#25dae9',
                        command=self.registrarUsuario)

    self.botonRegistrarU.bind("<Enter>",on_enterR)
    self.botonRegistrarU.bind("<Leave>",on_leaveR)

    self.botonRegistrarU.pack(anchor='center',pady=5)
  
  def iniciarSesion(self):
    usuario=self.usuarioEntryValor.get().strip()
    def existeUsuario(usuario):
       conn=conexion()
       cursor=conn.cursor()
       cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}'")
       bus=''
       for i in cursor:
          bus=i
       if len(bus)!=0:
          return True
       else:
          return False
    if existeUsuario(usuario):
      contrasena=self.contraEntryValor.get()
      def idUsuario():
        conn=conexion()
        cursor=conn.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}'")
        for i in cursor:
          id=i[0]
        return id

      conn=conexion()
      cursor=conn.cursor()
      cursor.execute(f"SELECT * FROM usuarios WHERE id={idUsuario()}")
      contra=''
      for i in cursor:
         contra=i[2]
      #verificar contraseña
      #separo el salt y el hash
      salt,hash=contra.split(':')

      #combino el salt y la contraseña ingresada
      hashContraNew=hashlib.sha256((contrasena+salt).encode())

      #obtengo el hash en formato hexadecimal
      hashHexNew=hashContraNew.hexdigest()

      #comparo los hash
      if hash==hashHexNew:
        #si es verdaderi, habro la ventana principal
        self.root.destroy()
        Principal(idUsuario())
      else:
         messagebox.showwarning('Inicio de sesión','Contraseña incorrecta, vuelve a intentar.')
    else:
       messagebox.showwarning('Inicio se sesión',\
        'No se encontro el usuario, vuelve a intentar. \nSi es nuevo, presiona en registrar para crear un usuario.')
  
  def registrarUsuario(self):
     self.root.destroy()
     Registrar()

class Principal():
  def __init__(self, idUsuario):
    self.idUsuario = idUsuario
    self.nomUsuario=self.nombreUsuario(idUsuario)
    self.root = Tk()
    self.root.title(f'Hola, {self.nomUsuario.title()}')
    self.root.geometry("300x300")
    self.root.resizable(False, False)
    self.root.config(bg="black")

    self.botonAjustes()

    self.root.mainloop()
  def nombreUsuario(self,idUsuario):
     conn=conexion()
     cursor=conn.cursor()
     cursor.execute(f"SELECT * FROM usuarios WHERE id={idUsuario}")
     for i in cursor:
        nombre=i[1]
     return nombre
  def botonAjustes(self):
     pass #aqui voy
  
class Registrar():
   def __init__(self):
      print('Te vas a registrar!')

if __name__ == '__main__':
  #Inicio()
  Principal(1)

