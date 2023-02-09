from tkinter import *
import os
from BD.conexionBD import *
from tkinter import messagebox
from principal import VentanaPrincipal

class VentanaLogin:
  def __init__(self):
    #creo la ventana
    self.login = Tk()
    self.login.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.login.geometry("400x500+470+85")
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
    self.confiConexionB.place(x=-1,y=480)
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
    self.botonAceptar=Button(self.login,bg='#8c8c8c',text='Aceptar',command=self.FAceptar)
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
    #funcion ultima para que la ventana mantenga activa
    self.login.mainloop()
  
  #verificar usuario valores
  def FAceptar(self):
    usuario=self.ValorUsuario.get()
    usuario=usuario.lower().strip()
    contraseña=self.ValorContraseña.get()
    contraseña=contraseña.lower().strip()
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

#------------------------------------Ventana registro--------------------------------

class VentanaRegistro:
  def __init__(self):
    self.registro = Tk()
    self.registro.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.registro.geometry("400x500+470+85")
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

    #entry de valor inicial de la cuenta
    self.valorInicial=Label(self.registro,bg='#a6a6a6', text='Valor de la cuenta:',\
    font=('Leelawadee UI Semilight',15)).place(x=30,y=345)
    self.ValorInicialC=StringVar()
    self.valorInicial=Entry(self.registro,width=18,bg='#8c8c8c',\
    font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorInicialC).place(x=195,y=351)
    self.ValorInicialC.set('0')

    #boton registrar
    self.botonAceptar=Button(self.registro,bg='#038554',text='Registrar',command=self.FRegistro)
    self.botonAceptar.place(x=125,y=390)
    self.botonAceptar.config(width=22)

    #boton volver login
    self.botonVLogin=Button(self.registro,bg='#8c8c8c',text='Volver al inicio',command=self.volverLogin)
    self.botonVLogin.place(x=125,y=420)
    self.botonVLogin.config(width=22)

    #label separador
    self.separador=Canvas(self.registro,width=164,height=3,bd=-2,bg='grey40')
    self.separador.place(x=125,y=452)

    #boton cancelar
    self.botonCancelar=Button(self.registro,bg='#ac3a3a',text='Cancelar',command=self.FCancelar)
    self.botonCancelar.place(x=125,y=460)
    self.botonCancelar.config(width=22)


    self.registro.mainloop()

  def volverLogin(self):
    self.registro.destroy()
    VentanaLogin()

  def FCancelar(self):
      self.registro.destroy()
      
  def FRegistro(self):
    usuario=self.ValorUsuario.get()
    usuario=usuario.strip()
    verificar=buscarUsuario(usuario)

    contraseña=self.ValorContraseña.get()
    contraseña=contraseña.strip()

    confi=self.ValorConfiContra.get()
    confi=confi.strip()

    if verificar==True:
      messagebox.showwarning('Usuario','El nombre de usuario ya existe, elige otro.')
      self.ValorUsuario.set('')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif usuario=='':
      messagebox.showwarning('Usuario','Usuario no puede estar vacio.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif contraseña=='':
      messagebox.showwarning('Contraseña','La contraseña no puede estar vacio.')
    elif confi=='':
      messagebox.showwarning('Confirmacion','La confirmacion, no puede estar vacio.')
      #Terminar ventana de registro
    elif len(contraseña)<8 or len(contraseña)>12:
      messagebox.showerror('Tamaño contraseña',\
        'La contraseña debe ser de minimo 8 y maximo de 12 caracteres.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    elif contraseña!=confi:
      messagebox.showerror('Confirmacion contraseña','La confirmacion no es igual a la contraseña.')
      self.ValorContraseña.set('')
      self.ValorConfiContra.set('')
    else:
      try:
        valorInicial=float(self.ValorInicialC.get())
        valorInicial=round(valorInicial,2)
        if valorInicial==0:
          messagebox.showinfo('Valor inicial','El valor inicial no puede estar vacio o ser igual a "0".')
        else:
          try:
            registrar(usuario,contraseña,valorInicial)
            messagebox.showinfo('Registro','Usuario registrado')
            self.registro.destroy()
            VentanaLogin()
          except:
            messagebox.showerror('Error','Hubo un problema al registrar al usuario, vuelve a intentar.')
      except:
        messagebox.showerror('Error','El valor debe ser un numero, formato: 0.00')
        self.ValorInicialC.set('0')

if __name__ == '__main__':
  VentanaLogin()