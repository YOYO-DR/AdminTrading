import csv,re
with open('operaciones.csv', newline='') as File:  
  reader = csv.reader(File)
  ope=[]
  for row in reader:
    ope.append(row)

print('\n',ope[3])

print('\nNombre divisa')
id=''
activo=''
fecha=''
valor=''
confi='0'
print(len(ope))
for i in range(5,len(ope)-4):
  p=ope[i][0]
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
      print(f"N°: {i} - ID: {id} - Activo: '{activo.lower()}' - Fecha: '{fecha}' - Valor: '{valor}'")
      id=''
      activo=''
      fecha=''
      valor=''
      confi='0'
      continue
    
  

