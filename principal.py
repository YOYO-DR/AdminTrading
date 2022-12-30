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

    #---------------------------------------------------------------------------------#
    #----------------------elementos del apartado de operaciones----------------------#
    #---------------------------------------------------------------------------------#
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
    self.valorUsdS.set('0')
    self.valorUsdE=Entry(self.root,textvariable=self.valorUsdS)
    self.valorUsdE.config(font=('Leelawadee UI Semilight',11))
    self.valorUsdE.place(x=20,y=160)

    #boton de vista previa
    self.botonGuardarOpe=Button(self.root,text='Vista previa',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.verVistaP)
    self.botonGuardarOpe.place(x=20,y=187)
    self.confirmarVista=False

    #boton guardar
    self.botonGuardarOpe=Button(self.root,text='Guardar',bg='#92e27a',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.guardar,width=19)
    self.botonGuardarOpe.place(x=21,y=217)

    #boton limpiar
    self.botonLimpiarOpe=Button(self.root,text='Limpiar',bg='#ff7676',\
    font=('Leelawadee UI Semilight',9,'bold'),command=self.limpiarOpe,width=8)
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
    self.fechaHoy=Button(self.root,text='Hoy',bg='#92e27a',\
    font=('Leelawadee UI Semilight',8,'bold'),command=self.fechaHoyB)
    self.fechaHoy.place(x=365,y=110)

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
    self.activoOpciones=['CRIPTO','FOREX']
    self.selectA=ttk.Combobox(self.root,state='readonly',width=10,\
      font=('Leelawadee UI Semilight',10),textvariable=self.activoSelectCal,values=self.activoOpciones)
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
    self.ePonerMes=Entry(self.root,textvariable=self.ponerDiaE,width=11)
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
      font=('Leelawadee UI Semilight',9,'bold'),bg='#92e27a')

    #boton cancelar confirmacion
    self.cancelarOpeActu=Button(self.root,text='Cancelar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#ff7676')

    #cosas del boton borrar

    #boton borrar confirmacion
    self.borrarOpeBor=Button(self.root,text='Borrar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#92e27a',width=10)

    #boton cancelar borrado confirmacion
    self.cancelarOpeBor=Button(self.root,text='Cancelar',\
      font=('Leelawadee UI Semilight',9,'bold'),bg='#ff7676',width=10)
    
    #label muestreo de operacion
    self.mostrarOpeBor=Label(self.root,text='Operacion a borrar: \n{res}',bg='grey90',\
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


#----------------------funciones del apartado de operaciones----------------------#

  def guardar(self):
    if self.confirmarVista==True:
      try:
        guardarValores(self.valoresGuardar)
        sumarOperacion(round((float(self.valorUsdS.get())),2),self.IDusuario)
        messagebox.showinfo('Operacion','La operacion se guardo correctamente')
        actualizarValorActual(self.IDusuario)
        self.MValorActual=obtenerValorActual(self.IDusuario)
        self.tituloB.config(text=f'Inicio: {self.valorInicioMostrar}   Actual: {self.MValorActual}')
        self.limpiarOpe()
        self.ganPerValores()
      except:
        messagebox.showerror('Error','Hubo un error, vuelve a intentarlo.')
    elif self.confirmarVista==False:
      messagebox.showwarning('Vista previa','No has realizado la vista previa.')

  def verVistaP(self):
    activo=self.activoSelect.get().lower()
    try:
      valor=float(self.valorUsdS.get())

    except:
      messagebox.showwarning('Valor USD','El valor no es un número, el formato debe ser (0.0)')
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
    self.activoSelect.set('')
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
    #Label de los valores total(0 USD / 0 %)
    #USD
    valorActual=float(obtenerValorActual(self.IDusuario))
    valorInicial=float(obtenerValorInicio(self.IDusuario))
    valorUSD=valorActual-valorInicial
    #%
    valorPor=(valorUSD/valorInicial)*100
    if valorUSD>0:
      self.valorTotalActuL.config(text=f'{round(valorUSD,2)} USD / {round(valorPor,2)}%')
    elif valorUSD<0:
      self.valorTotalActuL.config(text=f'{round(valorUSD,2)} USD / {round(valorPor,2)}%',fg='#ff7676')
    
    #Label de los valores mes(0 USD / 0 %)
    #USD
    #%
    valorMes=sumaOperMes(self.IDusuario)[0]
    porMes=sumaOperMes(self.IDusuario)[1]
    if valorMes>0:
      self.valorMesActuL.config(text=f'{round(valorMes,2)} USD / {round(porMes,2)}%')
    elif valorMes<0:
      self.valorMesActuL.config(text=f'{round(valorMes,2)} USD / {round(porMes,2)}%',fg='#ff7676')

    #Label de los valores semana(0 USD / 0 %)
    #USD
    #%
    valorSemana=sumaOperSemana(self.IDusuario)[0]
    porSemana=sumaOperSemana(self.IDusuario)[1]
    if valorSemana>0:
      self.valorSemActuL.config(text=f'{round(valorSemana,2)} USD / {round(porSemana,2)}%')
    elif valorSemana<0:
      self.valorSemActuL.config(text=f'{round(valorSemana,2)} USD / {round(porSemana,2)}%',fg='#ff7676')

#--------------------funciones del apartado de buscar operaciones--------------------#

  def seleccionBus(self,event):
    if self.activoSelectBus.get()=='ID':
      self.limpiarBus('ID')
      self.limpiarOpcionesActuBor()

      self.IDDeHas.place(x=700,y=105)
      self.eIDBus.place(x=720,y=107)
      self.ePrimerIDBus.place(x=825,y=107)
      self.eSegunIDBus.place(x=910,y=107)

    elif self.activoSelectBus.get()=='DIA':
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

          elif self.IDBus.get().strip()!='' and id1=='' and id2=='':
            self.primerID.set('')
            self.segunID.set('')
            try: #verificar que sea un numero y no otro caracter
              id=int(self.IDBus.get())
              #busco la operacion
              datosOpe=buscarOperacionID(self.IDusuario,id) 
              if datosOpe==False:
                self.resBus.insert(0,f'La operacion con el ID: {id} no existe.')
              else:
                #self.resBus.insert(0,'ID: 15 | Activo: BTC | Valor: 3 USD | Fecha: 2022/12/26')
                #hago el mensaje a mostrar
                resultado=f'ID: {datosOpe[0]} - Activo: {str(saberActivoID(datosOpe[1])).upper()}'\
                +f' - Valor: {datosOpe[2]} USD - Fecha: {datosOpe[4]}'

                #inserto el dato
                self.resBus.insert(0,resultado)
                #limpio el entry del ID
                self.IDBus.set('')
            except:
              messagebox.showwarning('ID','El ID debe ser un número entero.')
          elif (id1!='' and id2=='') or (id1=='' and id2!=''):
            messagebox.showwarning('ID','Falta un ID.')
          else:
            try:
              id1=int(id1)
              id2=int(id2)
              if id1>id2:
                messagebox.showerror('ID','El primer ID no puede ser mayor al segundo.')
                self.primerID.set('')
                self.segunID.set('')
                
              else:
                if self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==0:
                  messagebox.showwarning('Positivo y Negativo',\
                    'Debe seleccionar si quiere ver operaciones negativas y/o positivas')
                else:
                  if self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==1:
                    pos=2
                  elif self.valorCheckNeg.get()==1 and self.valorCheckPos.get()==0:
                    pos=False
                  elif self.valorCheckNeg.get()==0 and self.valorCheckPos.get()==1:
                    pos=True
                    
                  for i in range(id2, id1-1,-1):
                    a=buscarOperacionID(self.IDusuario,i,pos)
                    if a!=False:
                      b=f'ID: {a[0]} - Activo: {str(saberActivoID(a[1])).upper()} - Valor: {a[2]} USD - Fecha: {a[4]}'
                      self.resBus.insert(0,b)
                  self.primerID.set('')
                  self.segunID.set('')
                  self.IDBus.set('')
            except:
              messagebox.showwarning('ID','Los ID no deben ser letras o estar vacios.')

        except:
          messagebox.showwarning('ID','El ID debe ser un número entero.')
          self.IDBus.set('')

    elif self.activoSelectBus.get()=='DIA':
      pass
    elif self.activoSelectBus.get()=='MES':
      pass
    elif self.activoSelectBus.get()=='ACTIVO':
      pass
    elif self.activoSelectBus.get()=='TODO':
      pass
    self.actuOpeB.place_forget()
    self.borrarOpeB.place_forget()
  
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
      if not 'La operacion con el ID' in b:
        id=str(b[4])
        #obtener ID
        for i in range(5,len(b)):
          if esE(b[i])==True:
            id+=b[i]
          else:
            break
        self.idSelect=id=int(id)
        #ubicaciones de los botones
        self.actuOpeB.place(x=710,y=371)
        self.borrarOpeB.place(x=790,y=371)

  def actualizarOpe(self):
    self.logoLabel.place_forget()
    
    #cosas de borrar
    self.borrarL.place_forget()
    self.mostrarOpeBor.place_forget()
    self.borrarOpeBor.place_forget()
    self.cancelarOpeBor.place_forget()

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
    
    pass

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

VentanaPrincipal(1)