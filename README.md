# AdivinarNumeroContraIA
Juego básico de adivinar un numero entre 1 y 20 compitiendo contra Robotin

Este código en Python es un juego de adivinanzas en el que compites contra un "Robotin" para adivinar un número secreto entre 1 y 20. A continuación, te explico cada parte del código:

import random: Importa el módulo "random" de Python para generar números aleatorios.

import os: Importa el módulo "os" de Python, que proporciona funciones para interactuar con el sistema operativo, como borrar la pantalla en este caso.

intentos = 0: Inicializa la variable intentos para contar cuántos intentos se han realizado.

nombre = input('Cual es tu nombre? '): Solicita al usuario que ingrese su nombre y lo almacena en la variable nombre.

x = random.randint(1, 20): Genera un número secreto aleatorio entre 1 y 20 (ambos inclusive) y lo guarda en la variable x.

a = 1 y b = 20: Establece los límites inicialmente para que Robotin adivine el número secreto entre 1 y 20.

y = int(): Inicializa la variable y que será usada por Robotin para hacer sus conjeturas.

numero = int(): Inicializa la variable numero que será utilizada para almacenar la conjetura del jugador.

Imprime un mensaje de bienvenida y las reglas del juego.

while intentos < 5:: Inicia un bucle mientras el número de intentos sea menor que 5.

intentos = intentos + 1: Incrementa el contador de intentos en cada iteración.

y = random.randint(a, b): Robotin hace una conjetura aleatoria inicial entre los límites a y b y lo guarda en la variable y.

Compara la conjetura de Robotin y con el número secreto x y ajusta los límites a y b en función de la conjetura para hacer la próxima conjetura más precisa.

numero = int(input("\nElige un numero: ")): El jugador ingresa su conjetura y se almacena en la variable numero.

Compara la conjetura del jugador numero con el número secreto x y ajusta los límites a y b de manera similar a como lo hizo Robotin.

Si el jugador o Robotin adivina el número secreto, se rompe el bucle while.

Luego del bucle, se comprueba si el jugador o Robotin ha adivinado el número y se imprime el mensaje correspondiente.

os.system('cls'): Se utiliza para borrar la pantalla y ocultar el número secreto una vez que termina el juego.

En resumen, el juego permite que el jugador y Robotin adivinen un número secreto entre 1 y 20 en un máximo de 5 intentos. Si el jugador o Robotin adivinan el número, se muestra un mensaje de victoria correspondiente; de lo contrario, se muestra un mensaje de derrota.
