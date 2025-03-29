#///////////////////////////////////////////////////////////////////
#/////////////////          Jesus Gaspar          //////////////////
#///////////////////////////////////////////////////////////////////

#EJERCICIOS///////////////////////////////////////////////////////////////////////////////////////////////////

#1 Escribe un programa en Python que solicite al usuario un número entero positivo n y luego calcule la suma de todos los números naturales desde 1 hasta n utilizando un bucle while. El programa debe imprimir el resultado.

i = 1

print("-------------------Bienvenido al loop de suma de un entero-------------------")

n = int(input("\nIngresa un número positivo entero para comenzar: "))
while i < n:
    print("Suma",i,"+",n,":",i+n)
    i+=1
print("Ciclo terminado.")


#2 Escribe un programa en Python que solicite al usuario un número entero y luego imprima la tabla de multiplicar de ese número del 1 al 10 utilizando un bucle for.

print("-------------------Bienvenido al loop de multiplicación de un entero-------------------")

n = int(input("\nIngresa un número positivo entero para comenzar: "))
for i in range (1,11):
    print("La multiplicacion de",n,"y",i,"es:",n*i)
    i+=1
print("Ciclo terminado.")


#3 Escribe un programa en Python que solicite al usuario una serie de números enteros hasta que ingrese un número negativo. El programa debe utilizar un bucle while para procesar los números y al final imprimir el número mayor ingresado.

i = 0
n = 0

print("-------------------Bienvenido al loop de números positivos-------------------")

while n > -1:
    if n > i:
        i = n
    n = int(input("\nIngrese un número entero positivo o uno negativo para terminar:"))    

print("\nEl número más grande fue:",i)