import mysql.connector

def conexion():
  con = mysql.connector.connect(
  host='20.168.252.60',
  user='yoyo',
  password='119351',
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

def registrar(usuario, contraseña):
  con=conexion()
  cursor=con.cursor()
  cursor.execute(f"insert into usuario(usuario,contraseña) values('{usuario}','{contraseña}');")
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