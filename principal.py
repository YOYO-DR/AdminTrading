from tkinter import *
import os
from tkinter import ttk
from BD.conexionBD import *
import time
from tkinter import messagebox

class VentanaPrincipal:
  def __init__(self,id):
    self.root=Tk()
    self.root.geometry('1050x600+1500+50')
    self.root.title('AdminTrading')
    self.IDusuario=id
    #---------------------------------carpeta media---------------------------------#
    self.carpetaMedia=os.path.join(os.path.dirname(__file__),'media')

    #------------------------------carpeta de imagenes------------------------------#
    self.carpetaImg=os.path.join(self.carpetaMedia,'img')
    
    #------------------------icono ventana y barra de inicio------------------------#
    self.iconoVentana=PhotoImage(file=os.path.join(self.carpetaImg,'icono.png'))
    self.root.iconphoto(False, self.iconoVentana,self.iconoVentana)

    #-----------------------elementos del apartado de la barra-----------------------#
    #apartado de barra de logo y titulo
    self.operacionesC=Canvas(self.root,width=1050,height=40,bg='grey90')
    self.operacionesC.place(x=0,y=0)

    #logo
    self.logoB=PhotoImage(file=os.path.join(self.carpetaImg,'logoAdmin.png')).subsample(15)
    Label(self.root,image=self.logoB,bg='grey90').place(x=0,y=2)

    #label del titulo en barra
    self.tituloB=Label(self.root,text='Administrador',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloB.place(x=35,y=5)

    #apartado de barra del valor de inicio
    #obtengo valor de inicio
    self.valorInicioMostrar=obtenerValorInicio(self.IDusuario)

    self.valorInicioB=Canvas(self.root,width=300,height=40,bg='grey90')
    self.valorInicioB.place(x=240,y=0)

    #label del valor de inicio
    actualizarValorActual(self.IDusuario)
    self.MValorActual=obtenerValorActual(self.IDusuario)
    self.tituloB=Label(self.root,text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloB.place(x=285,y=5)


    #botones modificar inicio
    self.imgActualizar=PhotoImage(file=os.path.join(self.carpetaImg,'botonActualizar.png')).subsample(21)
    self.modificarI=Button(self.root,image=self.imgActualizar,bg='#9acef8',font=('Leelawadee UI Semilight',8,'bold'),command=self.actuaInicio)
    self.modificarI.place(x=250,y=7)

    #----------------------elementos del apartado de operaciones----------------------#
    #apartado de ingresar operaciones
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=50)

    #Label del titulo de operaciones
    self.tituloIngresar=Label(self.root,text='Ingresar operacion',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=20,y=55)

    #label activo
    self.activoL=Label(self.root,text='Activo',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.activoL.place(x=20,y=85)

    #combobox de activo
    self.activoSelect=StringVar()
    self.activoOpciones=obtenActivos()
    self.selectA=ttk.Combobox(self.root,state='readonly',width=10,font=('Leelawadee UI Semilight',10),textvariable=self.activoSelect,values=self.activoOpciones)
    self.selectA.place(x=20,y=110)

    #label Valor usd
    self.valorUsdL=Label(self.root,text='Valor USD',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.valorUsdL.place(x=20,y=135)

    #entry de Valor usd
    self.valorUsdS=StringVar()
    self.valorUsdS.set('0')
    self.valorUsdE=Entry(self.root,textvariable=self.valorUsdS)
    self.valorUsdE.config(font=('Leelawadee UI Semilight',11))
    self.valorUsdE.place(x=20,y=160)

    #boton de vista previa
    self.botonGuardarOpe=Button(self.root,text='Vista previa',bg='#92e27a',font=('Leelawadee UI Semilight',9,'bold'),command=self.verVistaP)
    self.botonGuardarOpe.place(x=20,y=187)
    self.confirmarVista=False

    #boton guardar
    self.botonGuardarOpe=Button(self.root,text='Guardar',bg='#92e27a',font=('Leelawadee UI Semilight',9,'bold'),command=self.guardar,width=19)
    self.botonGuardarOpe.place(x=21,y=217)

    #boton limpiar
    self.botonLimpiarOpe=Button(self.root,text='Limpiar',bg='#ff7676',font=('Leelawadee UI Semilight',9,'bold'),command=self.limpiarOpe,width=8)
    self.botonLimpiarOpe.place(x=110,y=187)

    #label fecha
    self.fechaL=Label(self.root,text='Fecha (AAAA-MM-DD)',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.fechaL.place(x=195,y=85)

    #entry de fecha
    self.valorFecha=StringVar()
    self.fechaE=Entry(self.root,textvariable=self.valorFecha)
    self.fechaE.config(font=('Leelawadee UI Semilight',11))
    self.fechaE.place(x=195,y=110)

    #boton de fecha 'hoy'
    self.fechaHoy=Button(self.root,text='Hoy',bg='#92e27a',font=('Leelawadee UI Semilight',8,'bold'),command=self.fechaHoyB)
    self.fechaHoy.place(x=365,y=110)

    #apartado de salida de vista previa de la operacion ingresada
    self.vistaP=Canvas(self.root,width=315,height=80,bg='grey90')
    self.vistaP.place(x=195,y=165)

    #label vista previa
    self.fechaL=Label(self.root,text='Vista previa',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.fechaL.place(x=195,y=135)

    #text para vista previa
    self.vistaPrevia=Text(self.root,font=('Leelawadee UI Semilight',10,'bold'),padx=0,pady=0,width=38,height=4,bg='grey85')
    self.vistaPrevia.place(x=201,y=171.5)
    self.vistaPrevia.insert(END,' ')
    self.vistaPrevia.config(state=DISABLED)

    #----------------------elementos del apartado de calculadora----------------------#
    #apartado de calculadora
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=255)

    #Label del titulo de calculadora
    self.tituloIngresar=Label(self.root,text='Calculadora',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=20,y=260)

    #--------------------elementos del apartado de ganancias/perdidas--------------------#
    #apartado de ganancias/perdidas
    self.operacionesC=Canvas(self.root,width=500,height=130,bg='grey90')
    self.operacionesC.place(x=10,y=460)

    #Label del titulo de ganancias/perdidas
    self.tituloIngresar=Label(self.root,text='Ganancias/perdidas',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=20,y=465)

    #canvas total
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=16,y=500)

    #canvas mes
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=183,y=500)

    #canvas semana
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=350,y=500)

    #--------------------elementos del apartado de buscaroperaciones--------------------#
    #apartado de ganancias/perdidas
    self.operacionesC=Canvas(self.root,width=510,height=350,bg='grey90')
    self.operacionesC.place(x=525,y=50)

    #Label del titulo de buscar operaciones
    self.tituloIngresar=Label(self.root,text='Buscar operaciones',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=530,y=55)

    #--------------------elementos del apartado de actualizar/borrar/logo--------------------#
    
    #apartado de actualizar/borrar/logo
    self.operacionesC=Canvas(self.root,width=510,height=180,bg='grey90')
    self.operacionesC.place(x=525,y=410)

    #logo
    self.logoVelas=PhotoImage(file=os.path.join(self.carpetaImg,'velas_japonesas.png')).subsample(3)
    Label(self.root,image=self.logoVelas,bg='grey90').place(x=660,y=430)

    """ #label actualizar
    self.actualizarL=Label(self.root,text='¿Desea actualizar la operacion n° ?',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.actualizarL.place(x=535,y=415) """
    
    #label borrar
    self.actualizarL=Label(self.root,text='¿Desea borrar la operacion n° ?',bg='grey90',font=('Leelawadee UI Semilight',14,'bold'))
    self.actualizarL.place(x=535,y=415)

    self.root.mainloop()

  def guardar(self):
    if self.confirmarVista==True:
      try:
        guardarValores(self.valoresGuardar)
        sumarOperacion((float(self.valorUsdS.get())),self.IDusuario)
        messagebox.showinfo('Operacion','La operacion se guardo correctamente')
        actualizarValorActual(self.IDusuario)
        self.MValorActual=obtenerValorActual(self.IDusuario)
        self.tituloB.config(text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}')
      except:
        messagebox.showerror('Error','Hubo un error, vuelve a intentarlo.')
    elif self.confirmarVista==False:
      messagebox.showwarning('Vista previa','No has realizado la vista previa.')

  def verVistaP(self):
    activo=self.activoSelect.get().lower()
    try:
      valor=float(self.valorUsdS.get())

    except:
      messagebox.showwarning('Valor USD','El valor no es un numero, el formato debe ser (0.0)')
    fecha=self.valorFecha.get()
    id=siguienteID()
    valorPor=round(((valor/(float(obtenerValorActual(self.IDusuario))))*100),2)
    
    posOneg=''
    if valor>0:
      posOneg='+'
    #Verificar todos los campos antes de mostrar la vista previa
    if activo=='':
      messagebox.showwarning('Activo','No has seleccionado un activo')
    elif valor==0:
      messagebox.showwarning('Valor USD','No has puesto un valor a guardar')
    elif fecha=='':
      messagebox.showwarning('Fecha','No has introducido la fecha')

    else:
      self.confirmarVista=True
      self.vistaPrevia.config(state=NORMAL)
      self.vistaPrevia.delete('1.0',END)
      insertar=f'''Activo: {activo}
Valor: {posOneg}{valor}  Valor %: {posOneg}{valorPor}%
Fecha: {fecha}
ID: {id}'''
      self.vistaPrevia.insert('1.0',insertar)
      self.vistaPrevia.config(state=DISABLED)
      self.valoresGuardar=[self.IDusuario,activo,valor,valorPor,fecha]
      
  def limpiarOpe(self):
    self.valoresGuardar=[self.IDusuario]
    self.confirmarVista=False
    self.activoSelect.set(' ')
    self.valorUsdS.set('0')
    self.valorFecha.set('')
    self.vistaPrevia.config(state=NORMAL)
    self.vistaPrevia.delete('1.0',END)
    self.vistaPrevia.config(state=DISABLED)

  def fechaHoyB(self):
    if self.valorFecha=='':
      hoy=time.localtime()
      self.fechaE.insert(0,f'{hoy.tm_year}-{hoy.tm_mon}-{hoy.tm_mday}')
    else:
      self.fechaE.delete(0,END)
      hoy=time.localtime()
      self.fechaE.insert(0,f'{hoy.tm_year}-{hoy.tm_mon}-{hoy.tm_mday}')

  def actuaInicio(self):
    self.tituloB.config(text='Inicio:')
    #entry del listo
    self.entryValorNVari=StringVar()
    self.entryValorN=Entry(self.root,textvariable=self.entryValorNVari,font=('Leelawadee UI Semilight',11),width=5)
    self.entryValorN.place(x=350,y=10)

    #boton listo
    self.imgBotonListo=PhotoImage(file=os.path.join(self.carpetaImg,'check.png')).subsample(20)
    self.botonListoO=Button(self.root,image=self.imgBotonListo,bg='#92e27a',command=self.botonListoOpe)
    self.botonListoO.place(x=402,y=5)


    #boton cancelar
    self.imgBotonCancelar=PhotoImage(file=os.path.join(self.carpetaImg,'cancel.png')).subsample(20)
    self.botonCancelarO=Button(self.root,image=self.imgBotonCancelar,bg='#ff7676',command=self.botonCancelarOpe)
    self.botonCancelarO.place(x=442,y=5)

  def botonCancelarOpe(self):
    self.tituloB.config(text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}')
    self.botonCancelarO.place_forget()
    self.botonListoO.place_forget()
    self.entryValorN.place_forget()

  def botonListoOpe(self):
    control=False
    valorActual=obtenerValorInicio(self.IDusuario)
    try:
      valor=float(self.entryValorNVari.get())
      control=True
      if control==True:
        try:
          actualizarInicio(self.IDusuario,valor)
          self.botonCancelarOpe()
          messagebox.showinfo('Actualizado',f'Valor inicio: {valorActual} \nActualizado a: {valor}.')
          actualizarValorActual(self.IDusuario)
          self.MValorActual=obtenerValorActual(self.IDusuario)
          self.valorInicioMostrar=obtenerValorInicio(self.IDusuario)
          self.tituloB.config(text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}')
        except:
          messagebox.showerror('Error','Error al actualizar el valor, vuelve a intentar')
          self.botonCancelarOpe()
    except:
      messagebox.showwarning('Error','No es un numero lo que ingresaste, formato (0.00)')
      self.botonCancelarOpe()
    

    



VentanaPrincipal(1)