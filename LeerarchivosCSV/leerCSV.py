import csv,re,os
#funcion para acomodar la fecha para que este bien en la base de datos

def fechaA(fecha):
  dia=''
  mes=''
  anio=''
  confi='0'
  for i in fecha:
    if confi=='0':
      if i=='/':
        confi='1'
        continue
      else:
        dia+=i
    elif confi=='1':
      if i=='/':
        confi='2'
        continue
      else:
        mes+=i
    elif confi=='2':
      if i=='/':
        confi='3'
        continue
      else:
        anio+=i
  if int(dia)<10:
    dia='0'+str(dia)
  if int(mes)<10:
    mes='0'+str(mes)
  fechaC=anio+'/'+mes+'/'+dia
  return fechaC

def leerArchivoCSV(file):
  #Abrir archivo
  try:
    reader = csv.reader(file)
    archivo=[]
    for row in reader:
      archivo.append(row)
  except:
    return False
  if not 'Libertex' in archivo[0][0]:
    return 'No es de Libertex'

  id=''
  activo=''
  fecha=''
  valor=''
  confi='0'
  ope=[]
  for i in range(5,len(archivo)-3):

    try:
      p=archivo[i][0]
    except Exception as e:
      if 'list index out of range' in e.args[0]:
        p=archivo[i-1][0]
      else:
        break

    for a in p:
      if confi=='0':
        if a =="\t": #primera tabulacion donde va el nombre normal de divisa, lo salto. Eje: gold\t
          confi='1'
          continue
      elif confi=='1':
        if a =="-": #freno cuando encuntre el '-' donde inicia el id de la operacion
          confi='2'
          continue
        activo+=a #voy formando el nombre de la divisa
      elif confi=='2':
        if a =="\t": #salto la segunda tabulacion donde marca que tipo de operacion fue. EJe: \tSell
          confi='3'
          continue
        id+=a

      elif confi=='3':
        if a =="\t": #salto la tabulacion despues del tipo de operacion (sell - buy). EJe: Sell\t
          confi='4'
          continue
      elif confi=='4':
        if a ==" ": #freno para solo escribir la fecha y no la hora
          confi='5'
          continue
        fecha+=a #voy formando la fecha
      elif confi=='5':
        if a =="\t": #salto la tabulacion despues de la hora. EJe: 18:43\t
          confi='6'
          continue
      elif confi=='6':
        if a =="\t": #salto la tabulacion despues del precio de apertura. EJe: 1.05342\t
          confi='7'
          continue
      elif confi=='7':
        if a =="\t": #salto la tabulacion despues de la fecha de cierre. EJe: 5/1/2023 20:10\t
          confi='8'
          continue
      elif confi=='8':
        if a =="\t": #salto la tabulacion despues del precio de cierre. EJe: 1.05476\t
          confi='9'
          continue
      elif confi=='9':
        if a =="\t": #salto la tabulacion despues del monto. EJe: 10\t
          confi='10'
          continue
      elif confi=='10':
        if a =="\t": #salto la tabulacion despues del multiplicador. EJe: x100\t
          confi='11'
          continue
      elif confi=='11':
        if a =="\t":
          confi='12'
          continue
      elif confi=='12':
        patron=re.compile('[A-Za-z]')
        if re.search(patron,a) : #me detengo ya que es el final
          confi='13'
          continue
        valor+=a #voy formando el valor de la operacion


      else:
        #print(f"N°: {i} - ID: {id} - Activo: '{activo.lower()}' - Fecha: '{fecha}' - Valor: '{valor}'")
        if not valor=='-':

          operacion={
            'No':i-5,
            'id':id,
            'activo': activo,
            'fecha':fechaA(fecha),
            'valor':valor
        }
          ope.append(operacion)
        id=''
        activo=''
        fecha=''
        valor=''
        confi='0'
        continue
  return ope

