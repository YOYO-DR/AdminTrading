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

def insertarDatos():
  cant=int(input('Cuantos datos va a insertar: '))
  con=conexion()
  cursor=con.cursor()
  for i in range(cant):
    nom=input('Dame el nombre de la persona: ')
    nom=nom.strip()
    nom=nom.lower()
    cursor.execute(f'insert into prueba(nombres) values ("{nom}")')
    con.commit()
  cursor.close()

def buscarUsuario():
  con=conexion()
  cur=con.cursor()
  nom=input('Dame un nombre a buscar:')
  nom=nom.strip(' ')
  ori=nom
  nom=nom.lower()
  cur.execute(f"select * from prueba where nombres='{nom}';")
  busqueda=()
  for i in cur:
    busqueda=i
  if len(busqueda)!=0:
    print(f'Se encontro el usuario {ori}')
  else:
    print(f'No se encontro el usuario {ori}')
  cur.close()

#insertarDatos()

def verificarUsuario(usuario,contraseña):
  con=conexion()
  cur=con.cursor()
  cur.execute(f"select * from usuario where usuario='{usuario}';")
  user=()
  for i in cur:
    user=i
  cur.execute(f"select * from usuario where contraseña='{usuario}';")
  contra=()
  for i in cur:
    contra=i
  
  if len(user)!=0 and len(contra)!=0:
    return True
  else:
    return False
  
  cur.close()