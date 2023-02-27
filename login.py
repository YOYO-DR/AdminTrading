from tkinter import *
import os
from BD.conexionBD import *
from tkinter import messagebox
from principal import VentanaPrincipal
import hashlib
import random
import re
from enviarCorreo import *

class VentanaLogin:
  def __init__(self):
    #creo la ventana
    self.login = Tk()
    self.login.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.login.geometry("400x520+470+85")
    #bloqueo la modificacion de las posiciones
    self.login.resizable(width=False, height=False)
    #titulo de la ventana
    self.login.title('Administrador de operaciones')
    #ruta de la carpeta Img
    self.carpetaMedia=os.path.join(os.path.join(os.path.dirname(__file__),'media'),'img')
    #logo de la ventana
    self.login.iconbitmap(os.path.join(self.carpetaMedia,'icono.ico'))
#----------------------------------------------------------------#
    #boton para la confirmacion de conexion
    self.confiConexionB=Button(self.login,width=60,height=1,bg='red',command=self.confiConexion)
    self.confiConexionB.place(x=-1,y=500)
    self.confiConexion()

    self.bienvenida=Label(self.login,bg='#a6a6a6', text='¡BIENVENIDO!\nInicia sesión',\
    font=('Leelawadee UI Semilight',20)).place(x=120,y=180)

    #Foto de bienvenida
    self.fotoB=PhotoImage(file=os.path.join(self.carpetaMedia,'imgInicio.png')).subsample(3)
    Label(self.login,image=self.fotoB).place(x=120,y=10)

    #Entry de usuario
    self.nombre=Label(self.login,bg='#a6a6a6', text='Usuario:',\
    font=('Leelawadee UI Semilight',15)).place(x=52,y=274)
    self.ValorUsuario=StringVar()
    self.usuario=Entry(self.login,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorUsuario).place(x=130,y=280)

    #entry de contraseña
    self.contraseña=Label(self.login,bg='#a6a6a6', text='Contraseña:',\
    font=('Leelawadee UI Semilight',15)).place(x=20,y=311)
    self.ValorContraseña=StringVar()
    self.contraseña=Entry(self.login,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorContraseña,show='*').place(x=130,y=316)

    #botones aceptar y cancelar
    self.botonAceptar=Button(self.login,bg='#038554',text='Aceptar',command=self.FAceptar)
    self.botonAceptar.place(x=130,y=355)
    self.botonAceptar.config(width=22)

    self.botonCancelar=Button(self.login,bg='#ac3a3a',text='Cancelar',command=self.FCancelar)
    self.botonCancelar.place(x=130,y=385)
    self.botonCancelar.config(width=22)
   
    #label separador
    self.separador=Canvas(self.login,width=164,height=3,bd=-2,bg='grey40')
    self.separador.place(x=130,y=420)

    #boton registrar
    self.botonRegistrar=Button(self.login,bg='#038554',text='Registrar',command=self.FRegistro)
    self.botonRegistrar.place(x=130,y=430)
    self.botonRegistrar.config(width=22)

    #boton recuperar contraseña
    self.botonOlvidoContra=Button(self.login,bg='#e26a2c',text='¿Olvido su contraseña?',command=self.RContra)
    self.botonOlvidoContra.place(x=130,y=460)
    self.botonOlvidoContra.config(width=22)
    #funcion ultima para que la ventana mantenga activa
    self.login.mainloop()
  
  #verificar usuario valores
  def FAceptar(self):
    usuario=self.ValorUsuario.get()
    usuario=usuario.strip()
    contraseña=self.ValorContraseña.get()
    contraseña=contraseña.strip()
    if usuario=='':
      messagebox.showerror('Usuario', 'Usuario no puede estar vacio.')
      self.ValorContraseña.set('')
    elif usuario!='' and contraseña == '':
      messagebox.showerror('Contraseña', 'Contraseña no puede estar vacio.')
    elif not buscarUsuario(usuario):
      messagebox.showwarning('Inicio se sesión',\
        'No se encontro el usuario, vuelve a intentar. \nSi es nuevo, presiona en registrar para crear un usuario.')
      self.ValorUsuario.set('')
      self.ValorContraseña.set('')
    else:
      valor=verificarUsuario(usuario,contraseña)
      if valor==True:
        self.login.destroy()
        VentanaPrincipal(obtenerIdUsuario(usuario))

      else:
        messagebox.showwarning('Inicio de sesión','Contraseña incorrecta, vuelve a intentar.')
        self.ValorContraseña.set('')

  #registrar usuario
  def FRegistro(self):
    self.login.destroy()
    VentanaRegistro()

  #cancelar inicio
  def FCancelar(self):
    self.login.destroy()

  #confirmar conexion a base de datos
  def confiConexion(self):
    def confirmar():
      try:
        con=conexion()
        return True
      except:
        return False
    
    if confirmar()==True:
      self.confiConexionB.config(bg='green')
    else:
      self.confiConexionB.config(bg='red')
  
  #recuperacion de contraseña
  def RContra(self):
    self.login.destroy()
    RecuperarContra()
#------------------------------------Ventana recuperar contraseña------------------------------#
class RecuperarContra():
  def __init__(self):
    self.root=Tk()
    self.root.title("Inicio de sesión")
    self.root.geometry("330x200+470+85")
    self.root.resizable(False, False)
    self.root.config(bg='#a6a6a6')
    self.root.title('Cambiar contraseña')

    #label info
    self.infoLabel=Label(self.root,text='¿Olvido su contraseña?',font=('Leelawadee UI Semilight',15),bg='#a6a6a6')
    self.infoLabel.pack(anchor='center')

    #Label correo
    self.correoLabel=Label(self.root,text='Correo:',font=('Leelawadee UI Semilight',15),bg='#a6a6a6')
    self.correoLabel.place(x=45,y=40)

    #Entry correo
    self.valorCorreoEntry=StringVar()
    self.correoEntry=Entry(self.root,width=26,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='black',textvariable=self.valorCorreoEntry)
    self.correoEntry.place(x=50,y=75)

    #boton verificar
    self.botonVerificar=Button(self.root,bg='#038554',text='Verificar',command=self.recuperarContra)
    self.botonVerificar.place(x=50,y=115)

    #boton volver al inicio
    self.botonInicio=Button(self.root,bg='#e26a2c',text='Volver al inicio',command=self.volverInicio)
    self.botonInicio.place(x=120,y=115)

    self.root.mainloop()

  def recuperarContra(self):
    correo=self.valorCorreoEntry.get().strip()
    if correo=='':
      messagebox.showerror('Correo', 'Correo no puede estar vacio.')
    else:
    #verificar el correo en la base de datos
      if not verificarCorreo(correo):
        messagebox.showwarning('Correo','el correo no esta registrado, vuelve a intentar.')
      else:
        #crear funcion para el envio del codigo
        #generar codigo
        letras='abcdefghijklmnopqrstuvwxyz1234567890'
        self.codigoEnvio=''
        for i in range(0,8):
          a=letras[random.randint(0,35)]
          if not a in self.codigoEnvio:
            self.codigoEnvio+=letras[random.randint(0,35)]
          else:
            i-=1

        #asunto del correo a enviar
        self.asunto='Admintrading - Codigo de verificación.'
        #cuerpo del mensaje a enviar
        self.cuerpo=f'''<b>Codigo:</b> <i>{self.codigoEnvio}</i>'''
        confiEnvio=enviarCodigo(correo,self.asunto,self.cuerpo)
        if not confiEnvio:
          messagebox.showinfo('Codigo de verificación','Hubo un error enviando el correo de verificación, intenta nuevamente.')
        else:
          #reacomodar el tamaño de la pantalla
          self.root.geometry('330x280+470+85')

          #desactivar entry del correo y boton
          self.correoEntry.config(state='disabled')
          self.botonVerificar.config(state='disabled')
          
          #Label codigo
          self.codigoLabel=Label(self.root,text='Codigo:',font=('Leelawadee UI Semilight',15),bg='#a6a6a6')
          self.codigoLabel.place(x=45,y=140) 

          #Entry del codigo
          self.valorCodigoEntry=StringVar()
          self.codigoEntry=Entry(self.root,width=26,bg='#8c8c8c',\
          font=('Leelawadee UI Semilight',13),fg='black',textvariable=self.valorCodigoEntry)
          self.codigoEntry.place(x=50,y=180)

          #boton de verificar codigo
          #boton verificar
          self.verificarCodi=Button(self.root,bg='#038554',text='Verificar',command=self.cambiarContra)
          self.verificarCodi.place(x=50,y=215)

          #boton enviar codigo de nuevo
          self.enviarCodeDeNuevo=Button(self.root,bg='#e26a2c',text='Enviar codigo de nuevo',command=self.enviarCode)
          self.enviarCodeDeNuevo.place(x=120,y=215)

  def enviarCode(self):
    confiEnvio=enviarCodigo(self.valorCorreoEntry.get().strip(),self.asunto,self.cuerpo)
    if not confiEnvio:
      messagebox.showinfo('Codigo de verificación','Hubo un error enviando el correo de verificación, intenta nuevamente.')

  def cambiarContra(self):
    #compara codigos
    if not self.valorCodigoEntry.get()==self.codigoEnvio:
      messagebox.showerror('Codigo de verificación', 'El codigo de verificación ingresado no es correcto.')
    else:
      self.verificacionCorrecta()

    #crear ventana de cambiar contraseña
    pass

  def verificacionCorrecta(self):
    #modificar ventana
    self.root.title('Cambiar contraseña')
    self.root.geometry("285x220+470+85")

    #modificar titulo
    self.infoLabel.config(text='Cambiar contraseña')

    #modificar label correo por "contraseña"
    self.correoLabel.config(text='Contraseña:')

    #ocultar botones
    self.botonVerificar.place_forget()
    self.verificarCodi.place_forget()
    self.enviarCodeDeNuevo.place_forget()

    #reposicionar boton de volver al inicio
    self.botonInicio.place(x=145,y=185)

    #ocultar entry correo
    self.correoEntry.place_forget()

    #crear entry contraseña
    self.valorContra=StringVar()
    self.contraEntry=Entry(self.root,width=20,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='black',textvariable=self.valorContra,show='*')
    self.contraEntry.place(x=50,y=75)

    #cambiar label codigo por "confirmar contraseña"
    self.codigoLabel.config(text='Confirmar contraseña:')
    self.codigoLabel.place(x=45,y=110)

    #ocultar entry del codigo
    self.codigoEntry.place_forget()

    #crear entry confiContraseña
    self.valorContraConfi=StringVar()
    self.contraConfiEntry=Entry(self.root,width=20,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='black',textvariable=self.valorContraConfi,show='*')
    self.contraConfiEntry.place(x=50,y=150)

    #boton confirmar cambio
    self.verificarCodi=Button(self.root,bg='#038554',text='Confirmar',command=self.confiCambioContra)
    self.verificarCodi.place(x=50,y=185)

  def confiCambioContra(self):
    #entry contraseña
    contra=self.valorContra.get().strip()

    #entry confiContraseña
    contraConfi=self.valorContraConfi.get().strip()

    if contra=='':
      messagebox.showerror('Contraseña', 'La contraseña no puede estar vacia.')
    elif contraConfi=='':
      messagebox.showerror('Confirmar contraseña', 'La confirmacion de contraseña no puede estar vacia.')
    elif len(contra)<8:
      messagebox.showerror('Contraseña', 'La contraseña debe tener al menos 8 caracteres.')
    elif contra!=contraConfi:
      messagebox.showerror('Contraseña', 'Las contraseñas no coinciden.')
    else:
      contraNueva=self.encriptar(contra)

    #funcion para cambiar contraseña
    try:
      cambioContraseña(contraNueva,self.valorCorreoEntry.get().strip())
      messagebox.showinfo('Cambio contraseña', 'La contraseña se ha cambiado correctamente.')
      self.root.destroy()
      VentanaLogin()
    except Exception as e:
      print(str(e))
      messagebox.showerror('Cambio contraseña', 'Hubo un error al cambiar la contraseña, intenta nuevamente.')

  def encriptar(self,contra):
    #caracteres para generar el salt
    caracteres='qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
    salt=''

    #lleno el salt de forma aleatoria
    for i in range(0,11):
      a=int(random.randint(0,35))
      salt+=caracteres[a]
    
    #junto la contraseña y el sal y luego lo hasheo
    hash_objet=hashlib.sha256((contra+salt).encode())

    #obtengo el has en formato hexadecimal
    hex_dig = hash_objet.hexdigest()

    #cojo el sal y el hash en una cadena de texto separa por ":" y ya eso se guarda en la base de datos
    contraEncrip=salt+":"+hex_dig
    return contraEncrip
  def volverInicio(self):
    self.root.destroy()
    VentanaLogin()
#------------------------------------Ventana registro--------------------------------#
class VentanaRegistro:
  def __init__(self):
    self.registro = Tk()
    self.registro.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.registro.geometry("400x540+470+65")
    #bloqueo la modificacion de las posiciones
    self.registro.resizable(width=False, height=False)
    #titulo de la ventana
    self.registro.title('Administrador de operaciones')
    #ruta de la carpeta Img
    self.carpetaMedia=os.path.join(os.path.join(os.path.dirname(__file__),'media'),'img')
    self.carpetaLogin=os.path.join(self.carpetaMedia,'login')
    #logo de la ventana
    self.registro.iconbitmap(os.path.join(self.carpetaMedia,'icono.ico'))
#----------------------------------------------------------------#
    self.bienvenida=Label(self.registro,bg='#a6a6a6', text='Registro',\
    font=('Leelawadee UI Semilight',20)).place(x=160,y=180)

    #Foto de bienvenida
    self.fotoB=PhotoImage(file=os.path.join(self.carpetaLogin,'signup_100_2.png')).zoom(2)
    Label(self.registro,image=self.fotoB,bd=0).place(x=105,y=-10)

    #Entry de usuario
    self.nombre=Label(self.registro,bg='#a6a6a6', text='Usuario:',\
    font=('Leelawadee UI Semilight',15)).place(x=117,y=234)
    self.ValorUsuario=StringVar()
    self.usuario=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorUsuario)
    self.usuario.place(x=195,y=240)

    #entry de contraseña
    self.contraseña=Label(self.registro,bg='#a6a6a6', text='Contraseña:',\
    font=('Leelawadee UI Semilight',15)).place(x=85,y=271)
    self.ValorContraseña=StringVar()
    self.contraseña=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorContraseña,show='*').place(x=195,y=276)
   
   #entry de confirmacion de contraseña
    self.confiContra=Label(self.registro,bg='#a6a6a6', text='Confirmar contraseña:',\
    font=('Leelawadee UI Semilight',15)).place(x=1,y=306)
    self.ValorConfiContra=StringVar()
    self.confiContra=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorConfiContra,show='*').place(x=195,y=311)

    #entry de correo
    self.correo=Label(self.registro,bg='#a6a6a6', text='Correo:',\
    font=('Leelawadee UI Semilight',15)).place(x=125,y=345)
    self.ValorCorreo=StringVar()
    self.correo=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorCorreo).place(x=195,y=351)

    #entry de valor inicial de la cuenta
    self.valorInicial=Label(self.registro,bg='#a6a6a6', text='Valor de la cuenta:',\
    font=('Leelawadee UI Semilight',15)).place(x=30,y=385)
    self.ValorInicialC=StringVar()
    self.valorInicial=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorInicialC).place(x=195,y=391)
    self.ValorInicialC.set('0')

    #boton registrar
    self.botonAceptar=Button(self.registro,bg='#038554',text='Registrar',command=self.FRegistro)
    self.botonAceptar.place(x=125,y=430)
    self.botonAceptar.config(width=22)

    #boton volver login
    self.botonVLogin=Button(self.registro,bg='#8c8c8c',text='Volver al inicio',command=self.volverLogin)
    self.botonVLogin.place(x=125,y=460)
    self.botonVLogin.config(width=22)

    #label separador
    self.separador=Canvas(self.registro,width=164,height=3,bd=-2,bg='grey40')
    self.separador.place(x=125,y=492)

    #boton cancelar
    self.botonCancelar=Button(self.registro,bg='#ac3a3a',text='Cancelar',command=self.FCancelar)
    self.botonCancelar.place(x=125,y=500)
    self.botonCancelar.config(width=22)


    self.registro.mainloop()

  def volverLogin(self):
    self.registro.destroy()
    VentanaLogin()

  def FCancelar(self):
      self.registro.destroy()
      
  def FRegistro(self):
    #Usuario
    usuario=self.ValorUsuario.get()
    usuario=usuario.strip()
    verificar=buscarUsuario(usuario)

    #contraseña
    contrasena=self.ValorContraseña.get()
    contrasena=contrasena.strip()

    #confiramcion de contraseña
    confi=self.ValorConfiContra.get()
    confi=confi.strip()

    #correo
    correo=self.ValorCorreo.get()
    correo=correo.strip().lower()


    if verificar==True:
      messagebox.showwarning('Usuario','El nombre de usuario ya existe, elige otro.')
      self.ValorUsuario.set('')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif usuario=='':
      messagebox.showwarning('Usuario','Usuario no puede estar vacio.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif contrasena=='':
      messagebox.showwarning('Contraseña','La contraseña no puede estar vacio.')
    elif confi=='':
      messagebox.showwarning('Confirmacion','La confirmacion, no puede estar vacio.')
    elif correo=='':
      messagebox.showwarning('Correo','Debe ingresar un correo')
    elif len(contrasena)<8 or len(contrasena)>12:
      messagebox.showerror('Tamaño contraseña',\
        'La contraseña debe ser de minimo 8 y maximo de 12 caracteres.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif contrasena!=confi:
      messagebox.showerror('Confirmacion contraseña','La confirmacion no es igual a la contraseña.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    else:
      if self.validarCorreo(correo):
        try:
          valorInicial=float(self.ValorInicialC.get())
          valorInicial=round(valorInicial,2)
          if valorInicial==0:
            messagebox.showinfo('Valor inicial','El valor inicial no puede estar vacio o ser igual a "0".')
          else:
            try:
              #encriptamiento de la contrasena
              contrasena=self.encriptar(contrasena)
              registrar(usuario,contrasena,valorInicial,correo)
              messagebox.showinfo('Registro','Usuario registrado')
              self.registro.destroy()
              VentanaLogin()
            except Exception as e:
              print(str(e))
              messagebox.showerror('Error','Hubo un problema al registrar al usuario, vuelve a intentar.')
        except:
          messagebox.showerror('Error','El valor debe ser un numero, formato: 0.00')
          self.ValorInicialC.set('0')
      else:
        messagebox.showerror('Correo','Debe ingresar un correo valido')
  
  def validarCorreo(self,correo):
    expresion_regular=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(expresion_regular,correo):
      return True
    else:
      return False

  def encriptar(self,contra):
    #caracteres para generar el salt
    caracteres='qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
    salt=''
    #lleno el salt de forma aleatoria
    for i in range(0,11):
      a=int(random.randint(0,35))
      salt+=caracteres[a]
    #junto la contraseña y el sal y luego lo hasheo
    hash_objet=hashlib.sha256((contra+salt).encode())
    
    #obtengo el has en formato hexadecimal
    hex_dig = hash_objet.hexdigest()

    #cojo el sal y el hash en una cadena de texto separa por ":" y ya eso se guarda en la base de datos
    contraEncrip=salt+":"+hex_dig
    return contraEncrip

if __name__ == '__main__':
  VentanaLogin()