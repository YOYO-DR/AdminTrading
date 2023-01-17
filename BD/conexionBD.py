import mysql.connector
import time
from datetime import datetime
from calendar import monthrange

def conexion():
  con = mysql.connector.connect(
  host='20.168.252.60',#'192.168.110.47',
  user='yoyo',#'user',
  password='119351',#'root',
  port='3306',
  database='admintrading',#'adminTrading',
  auth_plugin='mysql_native_password')
  cursor = con.cursor()
  cursor.close()
  return con

def buscarUsuario(nom):
  nom=nom.lower().strip()
  con=conexion()
  cur=con.cursor()
  cur.execute(f"select * from usuario where usuario='{nom}';")
  busqueda=()
  for i in cur:
    busqueda=i
  if len(busqueda)!=0:
    cur.close()
    return True
  else:
    cur.close()
    return False

def verificarUsuario(usuario,contraseña):
  con=conexion()
  cur=con.cursor()
  cur.execute(f"select * from usuario where usuario='{usuario}';")
  user=()
  for i in cur:
    user=i
  cur.execute(f"select * from usuario where contraseña='{contraseña}';")
  contra=()
  for i in cur:
    contra=i

  if len(user)!=0 and len(contra)!=0:
    cur.close()
    return True
  else:
    cur.close()
    return False

def obtenerIdUsuario(usuario):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"select * from usuario where usuario='{usuario}'")
  for i in cursor:
    idUsuario=i[0]
  con.close()
  return idUsuario

def registrar(usuario, contraseña,valorInicial):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"insert into usuario(usuario,contraseña,inicioCuenta,totalActual) values('{usuario}','{contraseña}',{valorInicial},{valorInicial});")
  con.commit()
  cursor.close()

def obtenActivos():
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"select * from activo")
  activos=['']
  for i in cursor:
    activos.append(i[1].upper())
  con.close()
  return activos

def siguienteID():
  con=conexion()
  cursor=con.cursor()
  idUltimo=0
  cursor.execute('select max(id) from operaciones;')
  for i in cursor:
    idUltimo=i[0]
  idUltimo+=1
  con.close()
  return idUltimo

def guardarValores(datos): 
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"select * from activo where nombre_activo='{datos[1]}'")
  for i in cursor:
    id_activo=i[0]
  cursor.execute(f"insert into operaciones (id_usuario, id_activo, valor, valorPorcentaje, fecha) values ({datos[0]},{id_activo}, {datos[2]}, {datos[3]}, '{datos[4]}');")
  con.commit()
  con.close()

def obtenerValorInicio(idUsuario):
  con=conexion()
  cursor=con.cursor()
  valorInicio=0
  cursor.execute(f"select * from usuario where id={idUsuario};")
  for i in cursor:
    valorInicio=i[3]
  con.close()
  return valorInicio

def sumarOperacion(operacion,idUsuario):
  con=conexion()
  cursor=con.cursor()
  valorActual=0
  cursor.execute(f"select * from usuario where id={idUsuario};")
  for i in cursor:
    valorActual=float(i[4])
  valorActual+=operacion
  cursor.execute(f"update usuario set totalActual={valorActual} where id={idUsuario};")
  con.commit()
  con.close()

def obtenerValorActual(idUsuario):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"select * from usuario where id={idUsuario}")
  valorActual=0
  for i in cursor:
    valorActual=i[4]
  con.close()
  return valorActual

def actualizarInicio(idUsuario,valor):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"update usuario set inicioCuenta={valor} where id={idUsuario};")
  con.commit()
  con.close()
  
def sumaTodasOperaciones(idUsuario):
  con=conexion()
  cursor=con.cursor()
  suma=0
  cursor.execute(f"select * from operaciones where id_usuario={idUsuario}")
  for i in cursor:
    suma+=i[3]
  con.close()
  return suma

def actualizarValorActual(idUsario):
  con=conexion()
  cursor=con.cursor()
  valor=sumaTodasOperaciones(idUsario)+obtenerValorInicio(idUsario)
  cursor.execute(f"update usuario set totalActual={valor} where id={idUsario};")
  con.commit()
  con.close()

def sumaOperMes(id):
  con=conexion()
  cursor=con.cursor()
  fecha=time.localtime()
  if fecha.tm_mon<10:
    mes=f'{fecha.tm_year}-0{fecha.tm_mon}' 
  else:
    mes=f'{fecha.tm_year}-{fecha.tm_mon}'
  cursor.execute(f"select o.id, o.valor, a.nombre_activo activo, o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like '{mes}%';")
  suma=0
  for i in cursor:
    suma+=float(i[1])
  ValorIniMes=float(obtenerValorActual(id))-suma
  por=(suma/ValorIniMes)*100
  con.close()
  return [suma,por]

def sumaOperSemana(id):
  diaActualSem=int(datetime.today().weekday())+1
  con=conexion()
  cursor=con.cursor()
  localT=time.localtime()
  
  #inicioS=int(localT.tm_mday)-diaActualSem

  if diaActualSem>int(localT.tm_mday) and int(localT.tm_mon)==1:

    inicioS=int(monthrange(int(localT.tm_year)-1,12))-diaActualSem
    anioMes=f'{int(localT.tm_year)-1}-12'

  elif diaActualSem>int(localT.tm_mday) and int(localT.tm_mon)<10:

    inicioS=int(monthrange(int(localT.tm_year),int(localT.tm_mon)-1))-diaActualSem
    anioMes=f'{int(localT.tm_year)}-0{int(localT.tm_mon)-1}'

  elif diaActualSem>int(localT.tm_mday) and int(localT.tm_mon)>10:
    inicioS=int(monthrange(int(localT.tm_year),int(localT.tm_mon)-1))-diaActualSem
    anioMes=f'{int(localT.tm_year)}-{int(localT.tm_mon)-1}'
  else:
    inicioS=int(localT.tm_mday)-diaActualSem
    if int(localT.tm_mon)<10:
      anioMes=f'{localT.tm_year}-0{int(localT.tm_mon)}'
    else:
      anioMes=f'{localT.tm_year}-{int(localT.tm_mon)}'
    
  cursor.execute(f"select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha > '{anioMes}-{inicioS}';")
  suma=0
  for i in cursor:
    suma+=float(i[1])
  con.close()

  ValorIniSemana=float(obtenerValorActual(id))-suma
  por=(suma/ValorIniSemana)*100
  return [suma,por]

def buscarOperacionID(idUsuario,id=0,pos=2):
  con=conexion()
  cursor=con.cursor()
  if pos==False:
    cursor.execute(f"select * from operaciones where id_usuario={idUsuario} and id={id} and valor<0;")
  elif pos==True:
    cursor.execute(f"select * from operaciones where id_usuario={idUsuario} and id={id} and valor>0;")
  elif pos==2:
    cursor.execute(f"select * from operaciones where id_usuario={idUsuario} and id={id};")
  ope=[]
  for i in cursor:
    
    #id operacion, id activo,valor,valor en porcentaje,fecha
    ope=[i[0],i[2],i[3],i[4],i[5]]
  if len(ope)==0:
    con.close()
    return False
  else:
    con.close()
    return ope

def saberActivoID(id):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f'select * from activo where id={id}')
  valor=0
  for i in cursor:
    valor=i[1]
  con.close()
  return valor

def buscarOpeDia(id,dia,activo='',pos=2):
  con=conexion()
  cursor=con.cursor()
  if activo=='':
    if pos==True:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}" and o.valor>0')
    elif pos==False:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}" and o.valor<0')
    elif pos==2:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}"')

    ope=[]
    for i in cursor:
      ope.append(i)
    con.close()
    return ope
  elif activo!='':

    if pos==True:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}" and o.valor>0 and a.nombre_activo="{activo}"')
    elif pos==False:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}" and o.valor<0 and a.nombre_activo="{activo}"')
    elif pos==2:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha = "{dia}" and a.nombre_activo="{activo}"')

    ope=[]
    for i in cursor:
      ope.append(i)
    con.close()
    return ope

def buscarOpeMes(id,dia,activo='',pos=2):
  con=conexion()
  cursor=con.cursor()
  if activo=='':
    if pos==True:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%" and o.valor>0')
    elif pos==False:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%" and o.valor<0')
    elif pos==2:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%"')

    ope=[]
    for i in cursor:
      ope.append(i)
    con.close()
    return ope
  elif activo!='':

    if pos==True:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%" and o.valor>0 and a.nombre_activo="{activo}"')
    elif pos==False:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%" and o.valor<0 and a.nombre_activo="{activo}"')
    elif pos==2:
      cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.fecha like "{dia}%" and a.nombre_activo="{activo}"')

    ope=[]
    for i in cursor:
      ope.append(i)
    con.close()
    return ope

def buscarOpeActivo(id,activo,pos=2):
  con=conexion()
  cursor=con.cursor()
  if pos==True:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and a.nombre_activo="{activo}" and o.valor>0')
  elif pos==False:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and a.nombre_activo="{activo}" and o.valor<0')
  elif pos==2:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and a.nombre_activo="{activo}"')

  ope=[]
  for i in cursor:
    ope.append(i)
  con.close()
  return ope

def buscarOpeTodo(id,pos=2):
  con=conexion()
  cursor=con.cursor()
  if pos==True:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.valor>0')
  elif pos==False:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id} and o.valor<0')
  elif pos==2:
    cursor.execute(f'select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario={id}')
  
  ope=[]
  for i in cursor:
    ope.append(i)
  con.close()
  return ope

def saberActivoValorFecha(idOpe):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f'select a.nombre_activo,o.valor,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id={idOpe};')
  for i in cursor:
    ope=i
  nombreActivo=ope[0]
  valor=float(ope[1])
  fecha=str(ope[2])
  ope=[nombreActivo,valor,fecha]
  con.close()
  return ope

def actualizarOperacion(idOpe,activo,valor,fecha):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f'select * from activo where nombre_activo="{activo}"')
  for i in cursor:
    idActivo=i[0]

  cursor.execute(f'update operaciones set id_activo={idActivo},valor={valor},fecha="{fecha}" where id={idOpe}')
  con.commit()
  con.close()

def borrarOperacion(id):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f'delete from operaciones where id={id}')
  con.commit()
  con.close()

 # tabla operaciones:
  #create table operaciones
  # (
  # id int auto_increment, 
  # id_usuario smallint, 
  # id_activo smallint, 
  # valor dec(7,2),
  # valorPorcentaje dec(5,2),
  # fecha date, 
  # primary key(id),
  # foreign key(id_usuario) references usuario(id), 
  # foreign key(id_activo) references activo(id)
  # );
  

#insert into operaciones (id_usuario, id_activo, valor, valorPorcentaje, fecha) values (1,4,-1.03,-1.03,'2022-11-23');