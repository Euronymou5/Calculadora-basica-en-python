def sumar():
  print(' ')
  print('Sumar')
  numero = int(input('Que numero quieres sumar por otro numero: '))
  suma = int(input('Ingresa numero a sumar: '))
  suma = print(numero + suma)

def restar():
  print(' ')
  print('Restar')
  numero = int(input('Que numero quieres restar por otro numero: '))
  restar = int(input('Ingresa numero a restar: '))
  restar = print(numero - restar)

def multi():
  print(' ')
  print('Multiplicar')
  numero = int(input('Que numero quieres multiplicar por otro numero: '))
  multiplicar = int(input('Ingresa numero a multiplicar: '))
  multiplicar = print(numero * multiplicar)

def divir():
  print(' ')
  print('Division')
  numero = int(input('Ingresa que numero quieres divir por otro numero: '))
  divir = int(input('Ingresa numero a divir: '))
  divir = print(numero / divir)

def divison2():
  print(' ')
  print('Division sin flotante')
  numero = int(input('Ingresa que numero a divir sin flotante: '))
  divir = int(input('Ingresa numero a divir sin flotante: '))
  divir = print(numero // divir)

def potencia():
  print(' ')
  print('Calcular Potencias')
  numero = int(input('Ingresa el numero: '))
  potencia = int(input('Ingresa el segundo numero: '))
  potencia = print(numero ** potencia)

def menu():
  print('[1] Sumar')
  print('[2] Restar')
  print('[3] Multiplicar')
  print('[4] Division Clasica')
  print('[5] Division sin flotante')
  print('[6] Calcular Potencias')

menu()
elegir = int(input('Seleccione una opcion: '))
if elegir == 1:
  sumar()
elif elegir == 2:
  restar()
elif elegir == 3:
  multi()
elif elegir == 4:
  divir()
elif elegir == 5:
  divison2()
elif elegir == 6:
  potencia()
else: 
  print('Error opcion invalida.')
