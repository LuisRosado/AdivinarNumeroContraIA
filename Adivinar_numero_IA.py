import random
import os

intentos = 0

nombre = input('Cual es tu nombre?  ')

x = random.randint(1, 20)
a = 1
b = 20
y = int()
numero = int()

print('\nHola ', nombre,
      ',competiras contra ROBOTIN, quien adivine primero un numero entre 1 y 20 gana, tienes 5 intentos para adivinar')
input('\nPresione ENTER para comenzar...')
os.system('cls')
print('ADIVINA EL NUMERO (', nombre, 'VS ROBOTIN)')

while intentos < 5:

    intentos = intentos + 1
    # Robotin
    y = random.randint(a, b)
    print('\nRobotin dice: ', y)
    if y < x:
        print('El numero es menor')
        a = y + 1
        y = random.randint(a, b)
    elif y > x:
        print('El numero es mayor')
        b = y - 1
        y = random.randint(a, b)
    elif y == x:
        break
    # Jugador
    numero = int(input("\nElige un numero: "))

    if numero < x:
        print('Tu numero es menor')
        a = numero + 1
        y = random.randint(a, b)
    elif numero > x:
        print('Tu numero es mayor')
        b = numero - 1
        y = random.randint(a, b)
    elif numero == x:
        break

if numero == x:
    os.system('cls')

    print('GANADOR\n')
    print('\nEres un Adivino?\n')
    print(nombre, 'lo lograste con este numero de intentos:', intentos)
    print('Nos vemos...')
if y == x:
    os.system('cls')
    print('\nRobotin dice: ', y)
    print('\nHa Ganado Robotin')
    print('Suerte para la proxima')

if numero != x:
    print('\nHas perdido , sera en otra oportunidad.')
    print('Suerte para la proxima')