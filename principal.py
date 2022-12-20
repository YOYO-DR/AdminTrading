from tkinter import *
import os

class VentanaPrincipal:
  def __init__(self):
    self.root=Tk()
    self.root.geometry('1050x600+1500+50')
    self.root.title('AdminTrading')
    
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



    #----------------------elementos del apartado de operaciones----------------------#
    #apartado de operaciones
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=50)

    #Label del titulo de operaciones
    self.tituloIngresar=Label(self.root,text='Ingresar operacion',bg='grey90',font=('Leelawadee UI Semilight',14))
    self.tituloIngresar.place(x=20,y=55)

    #----------------------elementos del apartado de calculadora----------------------#
    #apartado de calculadora
    self.operacionesC=Canvas(self.root,width=500,height=195,bg='grey90')
    self.operacionesC.place(x=10,y=255)

    #Label del titulo de calculadora
    self.tituloIngresar=Label(self.root,text='Calculadora',bg='grey90',font=('Leelawadee UI Semilight',14))
    self.tituloIngresar.place(x=20,y=260)

    #--------------------elementos del apartado de ganancias/perdidas--------------------#
    #apartado de ganancias/perdidas
    self.operacionesC=Canvas(self.root,width=500,height=130,bg='grey90')
    self.operacionesC.place(x=10,y=460)

    #Label del titulo de ganancias/perdidas
    self.tituloIngresar=Label(self.root,text='Ganancias/perdidas',bg='grey90',font=('Leelawadee UI Semilight',14))
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
    self.tituloIngresar=Label(self.root,text='Buscar operaciones',bg='grey90',font=('Leelawadee UI Semilight',14))
    self.tituloIngresar.place(x=530,y=55)

    #--------------------elementos del apartado de actualizar/borrar/logo--------------------#
    
    #apartado de actualizar/borrar/logo
    self.operacionesC=Canvas(self.root,width=510,height=180,bg='grey90')
    self.operacionesC.place(x=525,y=410)

    #logo
    self.logoVelas=PhotoImage(file=os.path.join(self.carpetaImg,'velas_japonesas.png')).subsample(3)
    Label(self.root,image=self.logoVelas,bg='grey90').place(x=660,y=430)

    """ #label acturalizar
    self.actualizarL=Label(self.root,text='¿Desea actualizar la operacion n° ?',bg='grey90',font=('Leelawadee UI Semilight',14))
    self.actualizarL.place(x=535,y=415) """
    
    #label borrar
    self.actualizarL=Label(self.root,text='¿Desea borrar la operacion n° ?',bg='grey90',font=('Leelawadee UI Semilight',14))
    self.actualizarL.place(x=535,y=415)



    self.root.mainloop()


VentanaPrincipal()