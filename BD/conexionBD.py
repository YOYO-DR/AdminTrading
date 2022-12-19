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
  

#insertarDatos()

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



def registrar(usuario, contraseña):
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
  