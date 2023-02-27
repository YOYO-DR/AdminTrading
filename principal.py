from tkinter import *
import os
from tkinter import ttk,filedialog
from BD.conexionBD import *
import time
from tkinter import messagebox
from threading import Thread
from time import sleep
from LeerarchivosCSV.leerCSV import *

class VentanaPrincipal:
  def __init__(self,id):
    self.root=Tk()
    self.root.geometry('1050x600+100+50')
    #self.root.geometry('1050x600+1500+50')
    self.root.resizable(width=False,height=False)
    self.root.title('AdminTrading')
    self.IDusuario=id
    #-------------------------------------------------------------------------------#
    #---------------------------------carpeta media---------------------------------#
    #-------------------------------------------------------------------------------#
    self.carpetaMedia=os.path.join(os.path.dirname(__file__),'media')

    #-------------------------------------------------------------------------------#
    #------------------------------carpeta de imagenes------------------------------#
    #-------------------------------------------------------------------------------#
    self.carpetaImg=os.path.join(self.carpetaMedia,'img')
    
    #-------------------------------------------------------------------------------#
    #------------------------icono ventana y barra de inicio------------------------#
    #-------------------------------------------------------------------------------#

    self.iconoVentana=PhotoImage(file=os.path.join(self.carpetaImg,'icono.png'))
    self.root.iconphoto(False, self.iconoVentana,self.iconoVentana)

    #--------------------------------------------------------------------------------#
    #-----------------------elementos del apartado de la barra-----------------------#
    #--------------------------------------------------------------------------------#
    #apartado de barra de logo y titulo
    self.operacionesC=Canvas(self.root,width=1050,height=40,bg='grey90')
    self.operacionesC.place(x=0,y=0)

    #logo
    self.logoB=PhotoImage(file=os.path.join(self.carpetaImg,'logoAdmin.png')).subsample(15)
    Label(self.root,image=self.logoB,bg='grey90').place(x=0,y=2)

    #label del titulo en barra
    self.tituloB=Label(self.root,text='Administrador',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloB.place(x=35,y=5)

    #apartado de barra del valor de inicio
    #obtengo valor de inicio
    self.valorInicioMostrar=obtenerValorInicio(self.IDusuario)

    self.valorInicioB=Canvas(self.root,width=300,height=40,bg='grey90')
    self.valorInicioB.place(x=240,y=0)

    #label del valor de inicio
    actualizarValorActual(self.IDusuario)
    self.MValorActual=obtenerValorActual(self.IDusuario)
    self.tituloB=Label(self.root,\
      text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloB.place(x=285,y=5)


    #botones modificar inicio
    self.imgActualizar=PhotoImage(file=os.path.join(self.carpetaImg,'botonActualizar.png')).subsample(21)
    self.modificarI=Button(self.root,image=self.imgActualizar,bg='#9acef8',\
    font=('Leelawadee UI Semilight',8,'bold'),command=self.actuaInicio)
    self.modificarI.place(x=250,y=7)

    #boton para base de datos
    self.botonVeri=Button(text='Verificar conexion',width=14,height=1,\
    font=('Leelawadee UI Semilight',10),command=self.conexionABD)
    self.conexionABD()
    self.botonVeri.place(x=900,y=7)

    #----------------------------------------------------------------------------------#
    #------------------elementos del apartado de ingresar operaciones------------------#
    #----------------------------------------------------------------------------------#
    #apartado de ingresar operaciones
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=50)

    #Label del titulo de operaciones
    self.tituloIngresar=Label(self.root,text='Ingresar operacion',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=20,y=55)

    #label activo
    self.activoL=Label(self.root,text='Activo',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.activoL.place(x=20,y=85)

    #combobox de activo
    self.activoSelect=StringVar()
    self.activoOpciones=obtenActivos()
    self.selectA=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelect,values=self.activoOpciones)
    self.selectA.place(x=20,y=110)
    

    #label Valor usd
    self.valorUsdL=Label(self.root,text='Valor USD',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.valorUsdL.place(x=20,y=135)

    #entry de Valor usd
    self.valorUsdS=StringVar()
    self.valorUsdE=Entry(self.root,textvariable=self.valorUsdS)
    self.valorUsdE.config(font=('Leelawadee UI Semilight',11))
    self.valorUsdE.place(x=20,y=160)

    #boton de vista previa
    self.botonGuardarOpeV=Button(self.root,text='Vista previa',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.verVistaP)
    self.botonGuardarOpeV.place(x=20,y=187)
    self.confirmarVista=False

    #boton guardar
    self.botonGuardarOpe=Button(self.root,text='Guardar',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.guardar,width=19)
    self.botonGuardarOpe.place(x=21,y=217)

    #boton limpiar
    self.botonLimpiarOpe=Button(self.root,text='Limpiar',bg='#ff7676',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.limpiarOpe,width=8)
    self.botonLimpiarOpe.place(x=110,y=187)

    #label de ID operacion
    self.idOpeL=Label(self.root,text='ID operación',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.idOpeL.place(x=140,y=85)

    #entry de ID operacion
    self.valorIdOpe=StringVar()
    self.idOpeE=Entry(self.root,textvariable=self.valorIdOpe)
    self.idOpeE.config(font=('Leelawadee UI Semilight',11),width=10)
    self.idOpeE.place(x=140,y=110)

    #label fecha
    self.fechaL=Label(self.root,text='Fecha (AAAA-MM-DD)',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.fechaL.place(x=255,y=85)

    #entry de fecha
    self.valorFecha=StringVar()
    self.fechaE=Entry(self.root,textvariable=self.valorFecha)
    self.fechaE.config(font=('Leelawadee UI Semilight',11))
    self.fechaE.place(x=255,y=110)

    #boton de fecha 'hoy'
    self.fechaHoy=Button(self.root,text='Hoy',bg='#92e27a',\
    font=('Leelawadee UI Semilight',8,'bold'),command=self.fechaHoyB)
    self.fechaHoy.place(x=425,y=110)

    #apartado de salida de vista previa de la operacion ingresada
    self.vistaP=Canvas(self.root,width=315,height=80,bg='grey90')
    self.vistaP.place(x=195,y=165)

    #label vista previa
    self.fechaL=Label(self.root,text='Vista previa',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.fechaL.place(x=195,y=135)

    #text para vista previa
    self.vistaPrevia=Text(self.root,font=('Leelawadee UI Semilight',10,'bold'),\
      padx=0,pady=0,width=38,height=4,bg='grey85')
    self.vistaPrevia.place(x=201,y=171.5)
    self.vistaPrevia.insert(END,' ')
    self.vistaPrevia.config(state=DISABLED)

    #boton para subir CSV
    self.botonSiburCSV=Button(self.root,text='Subir CSV',font=('Leelawadee UI Semilight',10,'bold'),bg='#6eb8f5',command=self.ingresarCSV)
    self.botonSiburCSV.place(x=425,y=60)

    #---------------------------------------------------------------------------------#
    #----------------------elementos del apartado de calculadora----------------------#
    #---------------------------------------------------------------------------------#
    #apartado de calculadora
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=255)

    #Label del titulo de calculadora
    self.tituloIngresar=Label(self.root,text='Calculadora',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=20,y=260)

    #Label de 2% y 6%
    self.valorPor=[float(obtenerValorActual(self.IDusuario))*2/100,float(obtenerValorActual(self.IDusuario))*6/100]
    self.dosPor=Label(self.root,text=f'2%: {round(self.valorPor[0],2)} USD  --  6%: {round(self.valorPor[1],2)} USD',bg='grey90',\
                      font=('Leelawadee UI Semilight',12,'bold'))
    self.dosPor.place(x=190,y=260)

    #label de valor SL
    self.valorSL=Label(self.root,text='Valor SL',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.valorSL.place(x=20,y=285)

    #boton porcentaje
    self.botonPorCal=Button(self.root,text='%',bg='#92e27a',\
    font=('Leelawadee UI Semilight',7),width=3,command=self.porcentajeCal)
    self.botonPorCal.place(x=85,y=287)

    #boton usd
    self.botonUsdCal=Button(self.root,text='USD',bg='#ff7676',\
    font=('Leelawadee UI Semilight',7),command=self.usdCal)
    self.botonUsdCal.place(x=115,y=287)

    #saber que boton esta seleccionado
    #1 = %
    #0 = USD
    self.seleccionPorUsd=1

    #entry de Valor SL
    self.striValorSL=StringVar()
    self.eValorSL=Entry(self.root,textvariable=self.striValorSL)
    self.eValorSL.config(font=('Leelawadee UI Semilight',11))
    self.eValorSL.place(x=20,y=315)

    #label pips SL
    self.pipsSL=Label(self.root,text='Pips SL',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.pipsSL.place(x=20,y=350)

    #entry de pips SL
    self.striPipSL=StringVar()
    self.ePipSL=Entry(self.root,textvariable=self.striPipSL)
    self.ePipSL.config(font=('Leelawadee UI Semilight',11))
    self.ePipSL.place(x=20,y=375)
    
    #labels multiplicador
    #variable del valor multiplicador
    self.multiplicadorValor=0
    self.multiL=Label(self.root,text=f'Multiplicador X',bg='grey90',font=('Leelawadee UI Semilight',15))
    self.multiL.place(x=115,y=405)

    #resultado multiplicador
    self.multiplicadorValor=0
    self.resMultiL=Label(self.root,text=f'{self.multiplicadorValor}',bg='grey90',\
      font=('Leelawadee UI Semilight',15,'bold'))
    self.resMultiL.place(x=243,y=405)

    #label importe
    self.importeL=Label(self.root,text=f'Importe',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.importeL.place(x=190,y=285)

    #entry Importe
    self.striImporte=StringVar()
    self.eImporte=Entry(self.root,textvariable=self.striImporte)
    self.eImporte.config(font=('Leelawadee UI Semilight',11))
    self.eImporte.place(x=190,y=315)

    #label precio Actual del activo en el mercado
    self.precioActuL=Label(self.root,text=f'Precio actual',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    self.precioActuL.place(x=190,y=350)

    #entry precio actual
    self.striPrecioActu=StringVar()
    self.ePrecioActu=Entry(self.root,textvariable=self.striPrecioActu)
    self.ePrecioActu.config(font=('Leelawadee UI Semilight',11))
    self.ePrecioActu.place(x=190,y=375)

    #boton calcular
    self.botonCompra=Button(self.root,text='Calcular',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),width=14,command=self.calcular)
    self.botonCompra.place(x=370,y=375)

    #boton limpiar calculadora
    self.botonCompra=Button(self.root,text='Limpiar',bg='#ff7676',\
    font=('Leelawadee UI Semilight',9,'bold'),width=14,command=self.limpiarCal)
    self.botonCompra.place(x=370,y=420)

    #label activo
    self.precioActuL=Label(self.root,text=f'Activo',bg='grey90',font=('Leelawadee UI Semilight',12))
    self.precioActuL.place(x=370,y=285)

    #combobox de tipo moneda
    self.activoSelectCal=StringVar()
    self.activoOpcionesC=['CRIPTO','FOREX']
    self.selectA=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectCal,values=self.activoOpcionesC)
    self.selectA.place(x=370,y=315)

    #------------------------------------------------------------------------------------#
    #--------------------elementos del apartado de ganancias/perdidas--------------------#
    #------------------------------------------------------------------------------------#
    #apartado de ganancias/perdidas
    self.operacionesC=Canvas(self.root,width=500,height=130,bg='grey90')
    self.operacionesC.place(x=10,y=460)

    #Label del titulo de ganancias/perdidas
    self.tituloGanPer=Label(self.root,text='Ganancias/perdidas',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloGanPer.place(x=20,y=465)

    #canvas total
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=16,y=500)

    #valor actual total
    self.valorTotalActuL=Label(self.root,text=f'0 USD / 0%',bg='grey90',\
      font=('Bahnschrift',12,'bold'),fg='#009929')
    self.valorTotalActuL.place(x=25,y=525)

    #label total
    self.tituloTotal=Label(self.root,text='Total',bg='grey90',font=('Leelawadee UI Semilight',12,'bold'))
    self.tituloTotal.place(x=70,y=550)

    #canvas mes
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=183,y=500)
    

    #valor actual ultimo mes
    self.valorMesActuL=Label(self.root,text=f'0 USD / 0%',bg='grey90',\
      font=('Bahnschrift',12,'bold'),fg='#009929')
    self.valorMesActuL.place(x=190,y=525)

    #label mes
    self.tituloTotalMes=Label(self.root,text='Total mes',bg='grey90',\
      font=('Leelawadee UI Semilight',12,'bold'))
    self.tituloTotalMes.place(x=220,y=550)

    #canvas semana
    self.CTotal=Canvas(self.root,width=150,height=80,bg='grey90',bd=2)
    self.CTotal.place(x=350,y=500)

    #valor actual ultima semana
    self.valorSemActuL=Label(self.root,text=f'0 USD / %0',bg='grey90',\
      font=('Bahnschrift',12,'bold'),fg='#009929')
    self.valorSemActuL.place(x=360,y=525)

    #label total semana
    self.tituloSemana=Label(self.root,text='Total semana',bg='grey90',\
      font=('Leelawadee UI Semilight',12,'bold'))
    self.tituloSemana.place(x=365,y=550)
    self.ganPerValores()

    #------------------------------------------------------------------------------------#
    #--------------------elementos del apartado de buscar operaciones--------------------#
    #------------------------------------------------------------------------------------#
    #apartado de ganancias/perdidas
    self.operacionesC=Canvas(self.root,width=510,height=350,bg='grey90')
    self.operacionesC.place(x=525,y=50)

    #Label del titulo de buscar operaciones
    self.tituloIngresar=Label(self.root,text='Buscar operaciones',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))
    self.tituloIngresar.place(x=530,y=55)

    #label de seleccionar forma de busqueda
    self.precioActuL=Label(self.root,text=f'Selecciona como buscar',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    self.precioActuL.place(x=540,y=85)

    #combobox de la seleccion
    self.activoSelectBus=StringVar()
    self.activoOpcionesBus=['ID','DIA','MES','ACTIVO','TODO']
    self.selectFormaBus=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectBus,values=self.activoOpcionesBus)
    self.selectFormaBus.place(x=540,y=110)
    self.activoSelectBus.set('ID')

    #Le digo el evento de seleccionar y que hacer al seleccionarlo
    self.selectFormaBus.bind("<<ComboboxSelected>>",self.seleccionBus)
    
    #boton buscar
    self.botonBuscar=Button(self.root,text='Buscar',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.buscar)
    self.botonBuscar.place(x=535,y=145)

    #checkbox de + y/o -
    self.valorCheckPos=IntVar()
    self.chekPositivo=Checkbutton(self.root,text='+',\
      font=('Bahnschrift',10),bg='grey90',variable=self.valorCheckPos,onvalue=1,offvalue=0)
    self.chekPositivo.place(x=633,y=107)
    self.valorCheckPos.set(1)

    self.valorCheckNeg=IntVar()
    self.chekNegativo=Checkbutton(self.root,text='-',\
      font=('Bahnschrift',10),bg='grey90',variable=self.valorCheckNeg,onvalue=1,offvalue=0)
    self.chekNegativo.place(x=665,y=107)
    self.valorCheckNeg.set(1)

    

#-----------------------------------------------------------
    #Seleccion ID

    #label ID de hasta
    self.IDDeHas=Label(self.root,text=f'ID                     De            Hasta',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    self.IDDeHas.place(x=700,y=105)

    #Entry ID
    self.IDBus=StringVar()
    self.eIDBus=Entry(self.root,textvariable=self.IDBus,width=4)
    self.eIDBus.config(font=('Leelawadee UI Semilight',11))
    self.eIDBus.place(x=720,y=107)

    #entry primer ID
    self.primerID=StringVar()
    self.ePrimerIDBus=Entry(self.root,textvariable=self.primerID,width=4,bg='grey70')
    self.ePrimerIDBus.config(font=('Leelawadee UI Semilight',11))
    self.ePrimerIDBus.place(x=825,y=107)

    #entry segundo ID
    self.segunID=StringVar()
    self.eSegunIDBus=Entry(self.root,textvariable=self.segunID,width=4,bg='grey70')
    self.eSegunIDBus.config(font=('Leelawadee UI Semilight',11))
    self.eSegunIDBus.place(x=910,y=107)

#-----------------------------------------------
    #Seleccion DIA

    #label activo seleccion
    self.activoLBus=Label(self.root,text=f'Activo',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    self.activoOpciones=obtenActivos()

    #combobox de activo
    self.activoSelectDia=StringVar()
    self.activoOpcionesDia=obtenActivos()
    self.selectActivoDia=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectDia,\
        values=self.activoOpcionesDia)

    #label de poner dia
    self.ponerDia=Label(self.root,text=f'Ingresa el dia',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
 

    #entry de poner el dia
    self.ponerDiaE=StringVar()
    self.ePonerDia=Entry(self.root,textvariable=self.ponerDiaE,width=11)
    self.ePonerDia.config(font=('Leelawadee UI Semilight',11))

    #---------------------------------------------------
    #Seleccion mes

    #label activo seleccion
    self.activoLBusMes=Label(self.root,text=f'Activo',bg='grey90',\
      font=('Leelawadee UI Semilight',12))

    #combobox de activo
    self.activoSelectMes=StringVar()
    self.activoOpcionesMes=obtenActivos()
    self.selectActivoMes=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectMes,\
        values=self.activoOpcionesMes)

      #label de poner Mes
    self.ponerMes=Label(self.root,text=f'Ingresa el mes',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    
    #entry de poner el Mes
    self.ponerMesE=StringVar()
    self.ePonerMes=Entry(self.root,textvariable=self.ponerMesE,width=11)
    self.ePonerMes.config(font=('Leelawadee UI Semilight',11))

#---------------------------------------------------
    #Seleccion activo

    #label activo seleccion
    self.activoLBusActi=Label(self.root,text=f'Activo',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    #combobox de activo
    self.activoSelectOp=StringVar()
    self.activoOpcionesOp=obtenActivos()
    self.selectActivoOp=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectOp,\
        values=self.activoOpcionesOp)
    

    #-----------------------------------------
     #canvas de resultado
    self.resBuscar=Canvas(self.root,width=465,height=170,bg='grey90',bd=2)
    self.resBuscar.place(x=550,y=190)


    #creo un frame parap posicionar con pack()
    self.p_aux=Frame(self.root)
    #lo posiciono
    self.p_aux.place(x=556,y=196)

    #creo el scroll dentro del frame
    self.scroll=Scrollbar(self.p_aux)
    #Lo posiciono a la derecha del frame
    self.scroll.pack(side=RIGHT,fill=Y)

    #creo list box para los resultados
    self.resBus=Listbox(self.p_aux,font=\
      ('Leelawadee UI Semilight',10,'bold'),width=55,height=9,yscrollcommand=self.scroll.set)
    self.resBus.pack(side=LEFT)
    
    #enlazar scroll al listbox
    self.scroll.config(command=self.resBus.yview)

    #indico el evento de seleccion
    # <<ListboxSelect>> evento de seleccion
    self.resBus.bind('<<ListboxSelect>>',self.opeSeleccionado)

    #boton actualizar
    self.actuOpeB=Button(self.root,text='Actualizar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#92e27a',command=self.actualizarOpe)
    #boton borrar
    self.borrarOpeB=Button(self.root,text='Borrar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#ff7676',command=self.borrarOpe)
    
    #suma de todas las operaciones
    self.sumaOpeL=Label(self.root,text=f'Suma: 0 USD',bg='grey90',\
      font=('Leelawadee UI Semilight',12,'bold'))
    


    #----------------------------------------------------------------------------------------#
    #--------------------elementos del apartado de actualizar/borrar/logo--------------------#
    #----------------------------------------------------------------------------------------#
    
    #apartado de actualizar/borrar/logo
    self.operacionesC=Canvas(self.root,width=510,height=180,bg='grey90')
    self.operacionesC.place(x=525,y=410)

    #logo
    self.logoVelas=PhotoImage(file=os.path.join(self.carpetaImg,'velas_japonesas.png')).subsample(3)
    self.logoLabel=Label(self.root,image=self.logoVelas,bg='grey90')
    self.logoLabel.place(x=660,y=430)

    #label actualizar
    self.actualizarL=Label(self.root,text='¿Desea actualizar la operacion n°?',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))

    #label borrar
    self.borrarL=Label(self.root,text='¿Desea borrar la operacion n°?',bg='grey90',\
      font=('Leelawadee UI Semilight',14,'bold'))

    #cosas del boton actualizar
    #label activo
    self.activoLActu=Label(self.root,text=f'Activo',bg='grey90',\
      font=('Leelawadee UI Semilight',12))

    #combobox de activo
    self.activoSelectActu=StringVar()
    self.activoOpcionesActu=obtenActivos()
    self.selectActu=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectActu,\
        values=self.activoOpcionesActu)
    
    #label valor
    self.valorLActu=Label(self.root,text=f'Valor',bg='grey90',\
      font=('Leelawadee UI Semilight',12))

    #entry del valor
    self.striValor=StringVar()
    self.eValorActu=Entry(self.root,textvariable=self.striValor,
    width=12,font=('Leelawadee UI Semilight',11))

    #label fecha
    self.fechaLActu=Label(self.root,text=f'Fecha (AAAA-MM-DD)',bg='grey90',\
      font=('Leelawadee UI Semilight',12))
    
    
    #entry de la fecha
    self.striFecha=StringVar()
    self.eFechaActu=Entry(self.root,textvariable=self.striFecha,
    width=12,font=('Leelawadee UI Semilight',11))
    

    #boton actualizar confirmacion
    self.actuOpeActu=Button(self.root,text='Actualizar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#92e27a',command=self.actualizarOpeConfi)

    #boton cancelar confirmacion
    self.cancelarOpeActu=Button(self.root,text='Cancelar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#ff7676',command=self.cancelarConfir)

    #cosas del boton borrar

    #boton borrar confirmacion
    self.borrarOpeBor=Button(self.root,text='Borrar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#92e27a',width=10,command=self.borrarOpeConfi)

    #boton cancelar borrado confirmacion
    self.cancelarOpeBor=Button(self.root,text='Cancelar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#ff7676',width=10,command=self.cancelarConfir)
    
    #label muestreo de operacion
    self.mostrarOpeBor=Label(self.root,bg='grey90',\
      font=('Leelawadee UI Semilight',12))

    #label de N° de operaciones buscadas
    self.mostrarNoOper=Label(self.root,text='N° de operaciones: 20',bg='grey90',\
      font=('Leelawadee UI Semilight',12))

    self.root.mainloop()

#-----------------------funciones del apartado de la barra-----------------------#
  def actuaInicio(self):
    self.tituloB.config(text='Inicio:')
    #entry del listo
    self.entryValorNVari=StringVar()
    self.entryValorN=Entry(self.root,textvariable=self.entryValorNVari,\
      font=('Leelawadee UI Semilight',11),width=5)
    self.entryValorN.place(x=350,y=10)

    #boton listo
    self.imgBotonListo=PhotoImage(file=os.path.join(self.carpetaImg,'check.png')).subsample(20)
    self.botonListoO=Button(self.root,image=self.imgBotonListo,bg='#92e27a',command=self.botonListoOpe)
    self.botonListoO.place(x=402,y=5)


    #boton cancelar
    self.imgBotonCancelar=PhotoImage(file=os.path.join(self.carpetaImg,'cancel.png')).subsample(20)
    self.botonCancelarO=Button(self.root,image=self.imgBotonCancelar,bg='#ff7676',\
    command=self.botonCancelarOpe)
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
      messagebox.showwarning('Error','No es un número lo que ingresaste, formato (0.00)')
      self.botonCancelarOpe()

#------------------------------funciones de la barra------------------------------#
  def conexionABD(self):
      try:
        conexion()
        confi=True
      except:
        confi=False
      if confi==True:
        self.botonVeri.config(bg='#92e27a')
      else:
        self.botonVeri.config(bg='#ff7676')

#----------------------funciones del apartado de ingresar operaciones----------------------#
  def actuActualGanPer(self):
    self.MValorActual=obtenerValorActual(self.IDusuario)
    self.tituloB.config(text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}')
    #actualizar porcentajes de SL y TP
    self.valorPor=[float(obtenerValorActual(self.IDusuario))*2/100,float(obtenerValorActual(self.IDusuario))*6/100]
    self.dosPor=Label(self.root,text=f'2%: {round(self.valorPor[0],2)} USD  --  6%: {round(self.valorPor[1],2)} USD',bg='grey90',\
                      font=('Leelawadee UI Semilight',12,'bold'))
    self.dosPor.place(x=190,y=260)
    self.ganPerValores()

  def guardar(self):
    self.hiloG=Thread(target=self.guardarEspera)
    self.hiloG.start()

  def guardarEspera(self):
    if self.confirmarVista==True:
        sleep(0.15)
        self.desaIngre(True) #las movi al frente
      #try:
        sumarOperacion(round((float(self.valorUsdS.get())),2),self.IDusuario)
        id_activo=buscarActivoConfi(self.valoresGuardar[1])
        self.valoresGuardar[1]=id_activo
        guardarValores(self.IDusuario,dato=self.valoresGuardar)
        #actualizar los activos despues de guardar
        self.actuComboboxActivos()
        messagebox.showinfo('Operacion','La operacion se guardo correctamente')

        self.limpiarOpe()
        self.actuActualGanPer()
        self.desaIngre(False)

        

        try:
          self.hiloG.join()
        except:
          pass
      #except Exception as e:
        #print(e)
        #messagebox.showerror('Error','Hubo un error, vuelve a intentarlo.')
        #self.desaIngre(False)
        try:
          self.hiloG.join()
        except:
          pass
    elif self.confirmarVista==False:
      messagebox.showwarning('Vista previa','No has realizado la vista previa.')
      self.desaIngre(False)
      try:
        self.hiloG.join()
      except:
        pass
  
  def desaIngre(self,confi):
    if confi==True:
      #desactivar guardar
      self.botonGuardarOpe.config(state='disabled',text='Guardando...',fg='white',bg='black')
      #desactivar vista previa
      self.botonGuardarOpeV.config(state='disabled')
      #desactivar limpiar
      self.botonLimpiarOpe.config(state='disabled')

    else:
      #activar guardar
      self.botonGuardarOpe.config(state='normal',text='Guardar',bg='#92e27a',fg='black')
      #activar vista previa
      self.botonGuardarOpeV.config(state='normal')
      #activar limpiar
      self.botonLimpiarOpe.config(state='normal')

  def verVistaP(self):
    activo=self.activoSelect.get().lower()
    fecha=self.valorFecha.get()
    id=siguienteID()
    valor=self.valorUsdS.get()
    idOpe=self.valorIdOpe.get()
    posOneg=''
    #Verificar todos los campos antes de mostrar la vista previa
    if activo=='':
      messagebox.showwarning('Activo','No has seleccionado un activo')
    elif valor=='':
      messagebox.showwarning('Valor USD','No has puesto un valor a guardar')
    elif fecha=='':
      messagebox.showwarning('Fecha','No has introducido la fecha')
    elif idOpe=='':
      messagebox.showwarning('ID','No has introducido el ID')
  
    else:
      try:
        idOpe=int(self.valorIdOpe.get())
      except:
        messagebox.showwarning('ID operación','El valor no es un número entero')
      try:
        valor=float(self.valorUsdS.get())
        if valor>0:
          posOneg='+'
      except:
        messagebox.showwarning('Valor USD','El valor no es un número, el formato debe ser (0.0)')
      valorPor=round(((valor/(float(obtenerValorActual(self.IDusuario))))*100),2)
      self.confirmarVista=True
      self.vistaPrevia.config(state=NORMAL)
      self.vistaPrevia.delete('1.0',END)
      insertar=f'''Activo: {activo}
Valor: {posOneg}{valor}  Valor %: {posOneg}{valorPor}%
Fecha: {fecha}  ID operación: {idOpe}
ID: {id}'''
      self.vistaPrevia.insert('1.0',insertar)
      self.vistaPrevia.config(state=DISABLED)
      self.valoresGuardar=[self.IDusuario,activo,valor,valorPor,fecha,idOpe]
      
  def limpiarOpe(self):
    self.valoresGuardar=[self.IDusuario]
    self.confirmarVista=False
    self.activoSelect.set('')
    self.valorUsdS.set('')
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

  def actiDesaTodo(self,confi):
    if confi == True:
      self.botonSiburCSV.config(state='normal')
      self.botonGuardarOpeV.config(state='normal')
      self.botonGuardarOpe.config(state='normal')
      self.botonLimpiarOpe.config(state='normal')
      self.botonBuscar.config(state='normal')
      self.modificarI.config(state='normal')
      self.botonVeri.config(state='normal')
    if confi == False:
      self.botonSiburCSV.config(state='disabled')
      self.botonGuardarOpeV.config(state='disabled')
      self.botonGuardarOpe.config(state='disabled')
      self.botonLimpiarOpe.config(state='disabled')
      self.botonBuscar.config(state='disabled')
      self.modificarI.config(state='disabled')
      self.botonVeri.config(state='disabled')

  def guardando(self):
    self.actiDesaTodo(False)
    self.botonSiburCSV.place(x=410,y=58)
    self.botonSiburCSV.config(text='Guardando...')

    valorActual=obtenerValorActual(self.IDusuario)
    activosActuales=obtenerActivoYId()
    operaciones=[]
    con=0

    for i in range(len(self.ope),0,-1):
      activo=str(self.ope[i-1]['activo']).lower()
      #verificar si el activo esta y si no esta agregarlo a la base de datos
      if activo not in activosActuales:
        idActivo=buscarActivoConfi(activo)
      else:
        idActivo=activosActuales[activo]
      valor=float(self.ope[i-1]['valor'])
      valorPor=round(((valor/(float(valorActual)))*100),2)
      fecha=self.ope[i-1]['fecha']
      idOpe=self.ope[i-1]['id']
      b=[self.IDusuario,idActivo,valor,valorPor,fecha,idOpe]
      operaciones.append(tuple(b))
      con+=1
    opeGuardados=guardarValores(self.IDusuario,datos=operaciones)
    if opeGuardados[0]>0:
      messagebox.showwarning('Operaciones guardadas',f'Se guardaron {opeGuardados[0]} operaciones')
      sumarOperacion(opeGuardados[1],self.IDusuario)
      self.actuActualGanPer()
      self.actuComboboxActivos()
    elif opeGuardados==0:
      messagebox.showwarning('Operaciones guardadas',f'No hay nuevas operaciones para guardar')
    self.botonSiburCSV.config(text='Guardado')
    self.actiDesaTodo(True)
    self.botonSiburCSV.config(text='Subir CSV')
    self.botonSiburCSV.place(x=430,y=58)
    
    try:
      self.hiloGuardarCSV.join()
    except:
      pass
  
  def actuComboboxActivos(self):
    #para actualizar un combobox toca como "recrearlo" para que se aplique los valores dinamicamente
    #actualizar los activos despues de guardar 
    #ingresar operaciones
    self.activoSelect=StringVar()
    self.activoOpciones=obtenActivos()
    self.selectA=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelect,values=self.activoOpciones)
    self.selectA.place(x=20,y=110)

    #buscar operaciones - dia
    self.activoSelectDia=StringVar()
    self.activoOpcionesDia=obtenActivos()
    self.selectActivoDia=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectDia,\
        values=self.activoOpcionesDia)
    
    #buscar operaciones - mes
    self.activoSelectMes=StringVar()
    self.activoOpcionesMes=obtenActivos()
    self.selectActivoMes=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectMes,\
        values=self.activoOpcionesMes)
    
    #buscar operaciones - activo
    self.activoSelectOp=StringVar()
    self.activoOpcionesOp=obtenActivos()
    self.selectActivoOp=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectOp,\
        values=self.activoOpcionesOp)

  def ingresarCSV(self):
    file=filedialog.askopenfile(initialdir='C',filetypes=(('Fichero csv','*csv'),('Todos los archivos','*.*')))
    archivo=file
    self.ope=leerArchivoCSV(archivo)
    can=len(self.ope)
    if self.ope=='No es de Libertex':
      messagebox.showerror('Archivo','El archivo no es un archivo de operaciones de Libertex')
    elif not self.ope==False:
      alert=messagebox.askokcancel('Operaciones',f'Se han encontrado {can} operaciones, ¿Desea ingresarlas?')
      if alert==True:
        self.hiloGuardarCSV=Thread(target=self.guardando)
        self.hiloGuardarCSV.start()

#----------------------funciones del apartado de calculadora----------------------#
  def porcentajeCal(self):
    self.botonPorCal.config(bg='#92e27a') #verde
    self.botonUsdCal.config(bg='#ff7676')#rojo
    self.seleccionPorUsd=1

  def usdCal(self):
    self.botonUsdCal.config(bg='#92e27a')
    self.botonPorCal.config(bg='#ff7676')
    self.seleccionPorUsd=0
    
  def calcular(self):
    if self.striValorSL.get().strip()=='':
      messagebox.showwarning('Valor SL','No has ingresado el valor del SL.')
    elif self.striPipSL.get().strip()=='':
      messagebox.showwarning('Pips SL','No has ingresado la cantidad de pips del SL.')
    elif self.striImporte.get().strip()=='':
      messagebox.showwarning('Importe','No has ingresado el importe.')
    elif self.striPrecioActu.get().strip()=='':
      messagebox.showwarning('Precio actual','No has ingresado el precio actual del activo')
    elif not self.activoSelectCal.get():
      messagebox.showwarning('Activo','No has seleccionado el tipo de activo.')
    else:
      try:
        valorActualActivo=float(self.striPrecioActu.get())
        try:
          pips=float(self.striPipSL.get())
          try:
            importe=float(self.striImporte.get())
            try:
              valorSLUsd=float(self.striValorSL.get())
              confi=True
            except:
              messagebox.showerror('Valor SL','El valor del SL debe ser un número.')
              confi=False
          except:
            messagebox.showerror('Importe','El valor del importe debe ser un número.')
            confi=False
        except:
            messagebox.showerror('Pips SL','El valor de los pips debe ser un número.')
            confi=False
      except:
        messagebox.showerror('Precio actual','El precio actual debe ser un número.')
        confi=False
      #1 = %
      #0 = USD
      if confi==True:
        if self.seleccionPorUsd==1:
          valorSLUsd=float(obtenerValorActual(self.IDusuario))*(valorSLUsd/100)
        movimiento=(pips/valorActualActivo)*100
        porcentaje=valorSLUsd/importe
        calculo=0
        if self.activoSelectCal.get()=='CRIPTO':
          calculo=int(abs((porcentaje*100)/movimiento))
        elif self.activoSelectCal.get()=='FOREX':
          calculo=int(abs(((porcentaje*100)/movimiento)*10000))
        self.resMultiL.config(text=f'{calculo}')

  def limpiarCal(self):
    self.striValorSL.set('')
    self.striPipSL.set('')
    self.striImporte.set('')
    self.striPrecioActu.set('')
    self.activoSelectCal.set('')

    self.resMultiL.config(text='0')

#--------------------funciones del apartado de ganancias/perdidas--------------------#
  def ganPerValores(self):
    #actualizar valor actual
    actualizarValorActual(self.IDusuario)
    #Label de los valores total(0 USD / 0 %)
    #USD
    valorActual=float(obtenerValorActual(self.IDusuario))
    valorInicial=float(obtenerValorInicio(self.IDusuario))
    valorUSD=valorActual-valorInicial
    #%
    valorPor=(valorUSD/valorInicial)*100
    if valorUSD>0:
      self.valorTotalActuL.config(text=f'{round(valorUSD,2)} USD / {round(valorPor,2)}%,',fg='#009929')
    elif valorUSD<0:
      self.valorTotalActuL.config(text=f'{round(valorUSD,2)} USD / {round(valorPor,2)}%',fg='#ff7676')
    
    #Label de los valores mes(0 USD / 0 %)
    #USD
    #%
    valorMes=sumaOperMes(self.IDusuario)[0]
    porMes=sumaOperMes(self.IDusuario)[1]
    if valorMes>0:
      self.valorMesActuL.config(text=f'{round(valorMes,2)} USD / {round(porMes,2)}%',fg='#009929')
    elif valorMes<0:
      self.valorMesActuL.config(text=f'{round(valorMes,2)} USD / {round(porMes,2)}%',fg='#ff7676')

    #Label de los valores semana(0 USD / 0 %)
    #USD
    #%
    valorSemana=sumaOperSemana(self.IDusuario)[0]
    porSemana=sumaOperSemana(self.IDusuario)[1]
    if valorSemana>0:
      self.valorSemActuL.config(text=f'{round(valorSemana,2)} USD / {round(porSemana,2)}%',fg='#009929')
    elif valorSemana<0:
      self.valorSemActuL.config(text=f'{round(valorSemana,2)} USD / {round(porSemana,2)}%',fg='#ff7676')

#--------------------funciones del apartado de buscar operaciones--------------------#
  def limpiarBuscarOpe(self):
    if self.activoSelectBus.get()=='ID':
      self.limpiarBus('ID')
      self.limpiarOpcionesActuBor()

      self.IDDeHas.place(x=700,y=105)
      self.eIDBus.place(x=720,y=107)
      self.ePrimerIDBus.place(x=825,y=107)
      self.eSegunIDBus.place(x=910,y=107)

    elif self.activoSelectBus.get()=='DIA':
      self.activoSelectDia.set('')
      self.ponerDiaE.set('')
      self.limpiarBus('DIA')
      self.limpiarOpcionesActuBor()
      self.activoLBus.place(x=865,y=85)
      self.selectActivoDia.place(x=865,y=110)
      self.ponerDia.place(x=730,y=85)
      self.ePonerDia.place(x=730,y=110)
    
    elif self.activoSelectBus.get()=='MES':
      self.limpiarBus('MES')
      self.limpiarOpcionesActuBor()
      self.activoLBusMes.place(x=865,y=85)
      self.selectActivoMes.place(x=865,y=110)
      self.ponerMes.place(x=730,y=85)
      self.ePonerMes.place(x=730,y=110)

    elif self.activoSelectBus.get()=='ACTIVO':
      self.limpiarBus('ACTIVO')
      self.limpiarOpcionesActuBor()
      self.selectActivoOp.place(x=730,y=110)
      self.activoLBusActi.place(x=730,y=85)
    
    elif self.activoSelectBus.get()=='TODO':
      self.limpiarBus('TODO')
      self.limpiarOpcionesActuBor()
    
    self.actuOpeB.place_forget()
    self.borrarOpeB.place_forget()
    self.resBus.delete(0,END)

    #ocultar suma y cantidad
    self.sumaOpeL.place_forget() 
    self.mostrarNoOper.place_forget()

  def seleccionBus(self,event):
    self.limpiarBuscarOpe()
    
  def limpiarBus(self,seleccion):
    if seleccion=='ID':
      #cosas DIA
      self.activoLBus.place_forget()
      self.selectActivoDia.place_forget()
      self.ponerDia.place_forget()
      self.ePonerDia.place_forget()
      
      #cosas mes
      self.activoLBusMes.place_forget()
      self.ponerMes.place_forget()
      self.ePonerMes.place_forget()
      self.selectActivoMes.place_forget()

      #cosas activo
      self.selectActivoOp.place_forget()
      self.activoLBusActi.place_forget()


    elif seleccion=='DIA':
      #cosas ID
      self.IDDeHas.place_forget()
      self.eIDBus.place_forget()
      self.ePrimerIDBus.place_forget()
      self.eSegunIDBus.place_forget()

      #cosas mes
      self.activoLBusMes.place_forget()
      self.ponerMes.place_forget()
      self.ePonerMes.place_forget()

      #cosas activo
      self.selectActivoOp.place_forget()
      self.activoLBusActi.place_forget()
    
    elif seleccion=='MES':
      #cosas ID
      self.IDDeHas.place_forget()
      self.eIDBus.place_forget()
      self.ePrimerIDBus.place_forget()
      self.eSegunIDBus.place_forget()
      self.selectActivoMes.place_forget()

      #cosas DIA
      self.activoLBus.place_forget()
      self.selectActivoDia.place_forget()
      self.ponerDia.place_forget()
      self.ePonerDia.place_forget()

      #cosas activo
      self.selectActivoOp.place_forget()
      self.activoLBusActi.place_forget()
    elif seleccion=='ACTIVO':
      #cosas ID
      self.IDDeHas.place_forget()
      self.eIDBus.place_forget()
      self.ePrimerIDBus.place_forget()
      self.eSegunIDBus.place_forget()
      self.selectActivoMes.place_forget()

      #cosas DIA
      self.activoLBus.place_forget()
      self.selectActivoDia.place_forget()
      self.ponerDia.place_forget()
      self.ePonerDia.place_forget()
      
      #cosas mes
      self.activoLBusMes.place_forget()
      self.ponerMes.place_forget()
      self.ePonerMes.place_forget()
      self.selectActivoMes.place_forget()
    
    elif seleccion=='TODO':

      #cosas ID
      self.IDDeHas.place_forget()
      self.eIDBus.place_forget()
      self.ePrimerIDBus.place_forget()
      self.eSegunIDBus.place_forget()
      self.selectActivoMes.place_forget()

      #cosas DIA
      self.activoLBus.place_forget()
      self.selectActivoDia.place_forget()
      self.ponerDia.place_forget()
      self.ePonerDia.place_forget()
      
      #cosas mes
      self.activoLBusMes.place_forget()
      self.ponerMes.place_forget()
      self.ePonerMes.place_forget()
      self.selectActivoMes.place_forget()

      #cosas activo
      self.selectActivoOp.place_forget()
      self.activoLBusActi.place_forget()
  
  def buscar(self):
    self.hiloB=Thread(target=self.buscarEspera)
    self.hiloB.start()

  def buscarEspera(self):
    self.botonBuscar.config(state='disabled')
    #limpio la lista
    self.resBus.delete(0,END)
    self.logoLabel.place(x=660,y=430)
    
    #limpiar abajo
    self.limpiarOpcionesActuBor()
    #verifico que modo de buscar esta seleccionado
    if self.activoSelectBus.get()=='ID': 
        try: #Verifico que sea un numero entero

          id1=self.primerID.get().strip()
          id2=self.segunID.get().strip()

          if self.IDBus.get().strip()=='' and id1=='' and id2=='':
            messagebox.showwarning('ID','El ID no debe estar vacio.')
            self.sumaOpeL.place_forget() 
            self.mostrarNoOper.place_forget()

          elif self.IDBus.get().strip()!='' and id1=='' and id2=='':
            self.primerID.set('')
            self.segunID.set('')
            try: #verificar que sea un numero y no otro caracter
              id=int(self.IDBus.get())
              #busco la operacion
              datosOpe=buscarOperacionID(self.IDusuario,id) 
              if datosOpe==False:
                self.resBus.insert(0,f'La operacion con el ID: {id} no existe.')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
              else:
                #hago el mensaje a mostrar
                resultado=f'ID: {datosOpe[0]} - Activo: {str(saberActivoID(datosOpe[1])).upper()}'\
                +f' - Valor: {datosOpe[2]} USD - Fecha: {datosOpe[4]}'

                #inserto el dato
                self.resBus.insert(0,resultado)
                #limpio el entry del ID
                self.IDBus.set('')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
            except:
              messagebox.showwarning('ID','El ID debe ser un número entero.')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()
          elif (id1!='' and id2=='') or (id1=='' and id2!=''):
            messagebox.showwarning('ID','Falta un ID.')
            self.sumaOpeL.place_forget() 
            self.mostrarNoOper.place_forget()
          else:
            try:
              id1=int(id1)
              id2=int(id2)
              if id1>id2:
                messagebox.showerror('ID','El primer ID no puede ser mayor al segundo.')
                self.primerID.set('')
                self.segunID.set('')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
                
              else:
                if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
                  messagebox.showwarning('Positivo y Negativo',\
                    'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
                  self.sumaOpeL.place_forget() 
                  self.mostrarNoOper.place_forget()
                else:
                  if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==1:
                    pos=2
                  elif self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                    pos=False
                  elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                    pos=True
                  self.operaciones=buscarOperacionesID(self.IDusuario,id1,id2,pos)

                  for i in range(0,len(self.operaciones)):
                    a=self.operaciones[i]
                    b=f'ID: {a[0]} - Activo: {str(a[1]).upper()} - Valor: {a[2]} USD - Fecha: {a[4]}'
                    self.resBus.insert(0,b)

                  if self.resBus.get(0)=='':
                    self.resBus.insert(0,'No se encontraron resultados.')
                    self.sumaOpeL.place_forget() 
                    self.mostrarNoOper.place_forget()
                  else:
                    #muestro la suma
                    self.sumaOpeMos()
                  self.primerID.set('')
                  self.segunID.set('')
                  self.IDBus.set('')
            except:
              messagebox.showwarning('ID','Los ID no deben ser letras o estar vacios.')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()

        except:
          messagebox.showwarning('ID','El ID debe ser un número entero.')
          self.IDBus.set('')
          self.sumaOpeL.place_forget() 
          self.mostrarNoOper.place_forget()

    elif self.activoSelectBus.get()=='DIA':

      #verifivar checkbox
      if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
        messagebox.showwarning('Positivo y Negativo',\
                                'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
        self.sumaOpeL.place_forget() 
        self.mostrarNoOper.place_forget()
      else:

        diaPuesto=self.ponerDiaE.get().strip() #dia escrito por la persona
        if diaPuesto=='':
          messagebox.showwarning('Fecha','Debe ingresar la fecha del dia a buscar')
          self.sumaOpeL.place_forget() 
          self.mostrarNoOper.place_forget()
        else:
        #validar fecha escrita
          try:
            datetime.strptime(diaPuesto, '%Y-%m-%d')
            self.operaciones=[]
            if self.activoSelectDia.get()=='': #activo que selecciona la persona que es opcional
              
              if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto,pos=False)
              elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto,pos=True)
              else:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto)
              for i in self.operaciones:
                resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
                #inserto el dato
                self.resBus.insert(0,resultado)
              
              if self.resBus.get(0).strip()=='':
                self.resBus.insert(0,'No se encontraron resultados.')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
              else:
                #muestro la suma
                self.sumaOpeMos()
            elif self.activoSelectDia.get()!='':
              activo=self.activoSelectDia.get().strip()

              if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto,activo,False)
              elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto,activo,True)
              else:
                self.operaciones=buscarOpeDia(self.IDusuario,diaPuesto,activo)

              for i in self.operaciones:
                resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
                #inserto el dato
                self.resBus.insert(0,resultado)
              if self.resBus.get(0)=='':
                self.resBus.insert(0,'No se encontraron resultados.')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
              else:
                #muestro la suma
                self.sumaOpeMos()

          except Exception as e:
            a=str(e)
            if 'unconverted' in a:
              messagebox.showwarning('Ingreso dia','La fecha no existe')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()
            elif 'time data' in a:
              messagebox.showerror('Ingreso dia','Fecha invalida')
              self.ponerDiaE.set('')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()

    elif self.activoSelectBus.get()=='MES':
      #verifivar checkbox
      if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
        messagebox.showwarning('Positivo y Negativo',\
                                'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
        self.sumaOpeL.place_forget() 
        self.mostrarNoOper.place_forget()
      else:

        diaPuesto=self.ponerMesE.get().strip() #dia escrito por la persona
        if diaPuesto=='':
          messagebox.showwarning('Fecha','Debe ingresar la fecha del dia a buscar')
          self.sumaOpeL.place_forget() 
          self.mostrarNoOper.place_forget()
        else:
        #validar fecha escrita
          try:
            datetime.strptime(diaPuesto, '%Y-%m')
            #######
            anio=''
            mes=''
            confi='0'
            for i in diaPuesto:
              if confi=='0':
                if i=='-':
                  confi='1'
                  continue
                anio+=i
              elif confi=='1':
                mes+=i
            if int(mes)<10:
              diaPuesto=anio+'-0'+mes
            elif int(mes)>10:
              diaPuesto=anio+'-'+mes
            #######
            self.operaciones=[]
            if self.activoSelectMes.get()=='': #activo que selecciona la persona que es opcional
              if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto,pos=False)
              elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto,pos=True)
              else:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto)
              for i in self.operaciones:
                resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
                #inserto el dato
                self.resBus.insert(0,resultado)
              if self.resBus.get(0)=='':
                self.resBus.insert(0,'No se encontraron resultados.')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()
              else:
                #muestro la suma
                self.sumaOpeMos()

            elif self.activoSelectMes.get()!='':

              activo=self.activoSelectMes.get().strip()

              if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto,activo,False)
              elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto,activo,True)
              else:
                self.operaciones=buscarOpeMes(self.IDusuario,diaPuesto,activo)

              for i in self.operaciones:
                resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
                #inserto el dato
                self.resBus.insert(0,resultado)
              #muestro la suma
              self.sumaOpeMos()
              if self.resBus.get(0)=='':
                self.resBus.insert(0,'No se encontraron resultados.')
                self.sumaOpeL.place_forget() 
                self.mostrarNoOper.place_forget()

          except Exception as e:
            a=str(e)
            if 'unconverted' in a:
              messagebox.showwarning('Ingreso dia','''La fecha no existe o es incorrecta
(no se puede agregar el dia)''')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()
            elif 'time data' in a:
              messagebox.showerror('Ingreso dia','Fecha invalida')
              self.sumaOpeL.place_forget() 
              self.mostrarNoOper.place_forget()
              self.ponerMesE.set('')
      
    elif self.activoSelectBus.get()=='ACTIVO':
      if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
        messagebox.showwarning('Positivo y Negativo',\
                                'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
        self.sumaOpeL.place_forget() 
        self.mostrarNoOper.place_forget()
      else:
        activo=self.activoSelectOp.get()
        self.operaciones=[]
        if self.activoSelectOp.get()=='':
          messagebox.showwarning('Seleccion activo','No has seleccionado un activo a buscar.')
          self.sumaOpeL.place_forget() 
          self.mostrarNoOper.place_forget()
        else:
          if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
            self.operaciones=buscarOpeActivo(self.IDusuario,activo,pos=False)
          elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
            self.operaciones=buscarOpeActivo(self.IDusuario,activo,pos=True)
          else:
            self.operaciones=buscarOpeActivo(self.IDusuario,activo)
          for i in self.operaciones:
            resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
            #inserto el dato
            self.resBus.insert(0,resultado)
          if self.resBus.get(0)=='':
            self.resBus.insert(0,'No se encontraron resultados.')
            self.sumaOpeL.place_forget() 
            self.mostrarNoOper.place_forget()
          else:
            #muestro la suma
            self.sumaOpeMos()

    elif self.activoSelectBus.get()=='TODO':
      if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
        messagebox.showwarning('Positivo y Negativo',\
                                'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
        self.sumaOpeL.place_forget() 
        self.mostrarNoOper.place_forget()
      else:
        self.operaciones=[]
        if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
          self.operaciones=buscarOpeTodo(self.IDusuario,pos=False)
        elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
          self.operaciones=buscarOpeTodo(self.IDusuario,pos=True)
        else:
          self.operaciones=buscarOpeTodo(self.IDusuario)
        for i in self.operaciones:
          resultado=f'ID: {i[0]} - Activo: {str(i[2]).upper()} - Valor: {float(i[1])} USD - Fecha: {str(i[3])}'
          #inserto el dato
          self.resBus.insert(0,resultado)
        if self.resBus.get(0)=='':
          self.resBus.insert(0,'No se encontraron resultados.')
          self.sumaOpeL.place_forget() 
          self.mostrarNoOper.place_forget()
        else:
          #muestro la suma
          self.sumaOpeMos()
    self.botonBuscar.config(state='normal')
    self.actuOpeB.place_forget()
    self.borrarOpeB.place_forget()
    try:
      self.hiloB.join()
    except:
      pass
  
  def opeSeleccionado(self,event):
    def esE(n):
      try:
        int(n)
        return True
      except:
        return False
    #self.resBus.curselection() para mirar el index y .get() para el valor
    if len(self.resBus.curselection())!=0:#por si se le unde en el cuadro y no hay nada
      #borrar seleccion anterior
      self.limpiarOpcionesActuBor()
      a=self.resBus.curselection()[0]#indice del item seleccionado
      b=self.resBus.get(a)#obtener lo que tiene el item seleccionado
      if not 'La operacion con el ID' in b and not 'No se encontraron resultados.' in b:
        id=str(b[4])
        #obtener ID
        for i in range(5,len(b)):
          if esE(b[i])==True:
            id+=b[i]
          else:
            break
        self.idSelect=int(id)

        
        #ubicaciones de los botones
        self.actuOpeB.place(x=560,y=371)
        self.borrarOpeB.place(x=640,y=371)

  def actualizarOpe(self):
    #cosas de ocultar
    self.logoLabel.place_forget() #logo

    self.borrarL.place_forget()
    self.mostrarOpeBor.place_forget()
    self.borrarOpeBor.place_forget()
    self.cancelarOpeBor.place_forget()
    
    #Mostrar cosas del apartado de actualizar
    self.actualizarL.config(text=f'¿Desea actualizar la operacion con el ID: {self.idSelect}?')
    self.actualizarL.place(x=535,y=410)

    self.activoLActu.place(x=555,y=435)
    self.selectActu.place(x=555,y=460)
    self.valorLActu.place(x=555,y=485)
    self.eValorActu.place(x=555,y=510)
    self.eFechaActu.place(x=555,y=560)
    self.fechaLActu.place(x=555,y=535)
    self.actuOpeActu.place(x=750,y=455)
    self.cancelarOpeActu.place(x=750,y=505)

    #poner valores de la operacion seleccionada
    #valores de la operacion
    valores=saberActivoValorFecha(self.idSelect)

    activo=valores[0].upper()
    valor=valores[1]
    fecha=valores[2]

    self.activoSelectActu.set(activo) #combobox
    self.striValor.set(valor) #entry valor
    self.striFecha.set(fecha) #entry fecha
    
    #guardar valores anteriores
    self.activoMessa=activo
    self.valorMessa=valor
    self.fechaMessa=fecha
  
  def actualizarOpeConfi(self):
    def esF(n):
      try:
        float(n)
        return True
      except:
        return False
    if self.activoSelectActu.get()=='':
      messagebox.showwarning('Activo','Debe seleccionar el activo.')
    elif self.striValor.get().strip()=='':
      messagebox.showwarning('Valor','Debe ingresar el valor.')
    elif self.striFecha.get().strip()=='':
      messagebox.showwarning('Fecha','Debe ingresar la fecha.')
    else:
      if esF(self.striValor.get())==False:
        messagebox.showerror('Valor','El valor debe ser un número.')
      else:
        try:
          fechaIngre=self.striFecha.get()
          datetime.strptime(fechaIngre, '%Y-%m-%d')
          #Valores anteriores
          activoA=self.activoMessa
          valorA=self.valorMessa
          fechaA=self.fechaMessa

          #Valor ingresados por el usuario
          activo=self.activoSelectActu.get()
          valor=self.striValor.get()
          fecha=self.striFecha.get()
          confi=messagebox.askokcancel('Actualizacion',\
f'''¿Confirma la actualizacion de la operación?
De:
Activo: {activoA} - Valor: {valorA} USD - Fecha: {fechaA}
A:
Activo: {activo} - Valor: {valor} USD - Fecha: {fecha}''')
          if confi==True:
            try:
              actualizarOperacion(self.idSelect,activo,valor,fecha)
              self.actuActualGanPer()
              messagebox.showinfo('Actualizacion','Se actualizó correctamente la operacion.')
              self.limpiarBuscarOpe()
            except Exception as e:
              print(e)
          else:
            messagebox.showinfo('Actualizacion','Actualizacion cancelada.')
            self.limpiarBuscarOpe()


        except:
          messagebox.showerror('Fecha','Fecha invalida.')
      
  def borrarOpe(self):
    self.logoLabel.place_forget()

    #valores de actualizar
    self.actualizarL.place_forget()
    self.activoLActu.place_forget()
    self.selectActu.place_forget()
    self.valorLActu.place_forget()
    self.eValorActu.place_forget()
    self.eFechaActu.place_forget()
    self.fechaLActu.place_forget()
    self.actuOpeActu.place_forget()
    self.cancelarOpeActu.place_forget()

    self.borrarL.config(text=f'¿Desea borrar la operacion con el ID: {self.idSelect}?')
    self.borrarL.place(x=535,y=410)
    self.mostrarOpeBor.place(x=570,y=440)
    a=buscarOperacionID(self.IDusuario,self.idSelect)
    res=f'ID: {a[0]} - Activo: {str(saberActivoID(a[1])).upper()} - Valor: {a[2]} USD - Fecha: {a[4]}'
    self.mostrarOpeBor.config(text=f'Operacion a borrar: \n{res}')
    self.borrarOpeBor.place(x=680,y=500)
    self.cancelarOpeBor.place(x=790,y=500)
  
  def borrarOpeConfi(self):

    try:
      borrarOperacion(self.idSelect)
      messagebox.showinfo('Borrar operacion',f'La operacion con el ID: {self.idSelect} se borro correctamente.')
      self.actuActualGanPer()
    except Exception as e:
      print(e)
    self.limpiarBuscarOpe()

  def cancelarConfir(self):
      self.limpiarOpcionesActuBor()

  def limpiarOpcionesActuBor(self):
    #valores de actualziar
    self.activoLActu.place_forget()
    self.selectActu.place_forget()
    self.valorLActu.place_forget()
    self.eValorActu.place_forget()
    self.eFechaActu.place_forget()
    self.fechaLActu.place_forget()
    self.actuOpeActu.place_forget()
    self.cancelarOpeActu.place_forget()
    self.actualizarL.place_forget()

    #valores de borrar
    self.borrarL.place_forget()
    self.mostrarOpeBor.place_forget()
    self.borrarOpeBor.place_forget()
    self.cancelarOpeBor.place_forget()

    #mostrar logo
    self.logoLabel.place(x=660,y=430)

  def sumaOpeMos(self):
     #suma de cada busqueda:
    if self.resBus.get(0)!='No se encontraron resultados.' and self.resBus.get(0)!='':
      if not 'La operacion' in self.resBus.get(0):
        if self.activoSelectBus.get()=='ID':
          posicion=2
        else:
          posicion=1
        cantidad=0
        suma=0
        for i in self.operaciones:
          if i==False or i==True:
            continue
          suma+=float(i[posicion])
          cantidad+=1
        suma=round(suma,2)
        if suma<0:
          self.sumaOpeL.config(text=f'Suma: {suma} USD',fg='#ff7676')
        elif suma>0:
          self.sumaOpeL.config(text=f'Suma: {suma} USD',fg='#009929')
        self.sumaOpeL.place(x=870,y=150)
        self.mostrarNoOper.place(x=840,y=370)
        self.mostrarNoOper.config(text=f'N° de operaciones: {cantidad}')

#VentanaPrincipal(1)

#tarea:
# hacer un hilo que traiga los id de las operaciones para hacer la verificacion de el cvs mas rapido, y asi puedo utilizar el executemany y que suba más rapido

#nota: hay algo con el codigo en develop que hace que haya el error en pyinstaller