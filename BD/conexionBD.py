import mysql.connector
import time
from datetime import datetime

def conexion():
  con = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='root',
  port='3306',
  database='adminTrading')
  cursor = con.cursor()
  cursor.close()
  return con

def buscarUsuario(nom):
  ori=nom
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
  mes=f'{fecha.tm_year}-{fecha.tm_mon}'
  cursor.execute(f"select o.id, o.valor, a.nombre_activo activo, o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario=1 and o.fecha like '{mes}%';")
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
  anioMes=f'{localT.tm_year}-{localT.tm_mon}'
  hoy=int(localT.tm_mday)-diaActualSem
  cursor.execute(f"select o.id, o.valor,a.nombre_activo activo,o.fecha from operaciones o left join activo a on o.id_activo=a.id where o.id_usuario=1 and o.fecha >= '{anioMes}-{hoy}';")
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

def actualizarOperacion(id,idActivo=False,valor=False,fecha=False):
  con=conexion()
  cursor=con.cursor()
  if idActivo!=False:
    cursor.execute(f'')
  pass

def borrarOperacion(id):
  pass
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