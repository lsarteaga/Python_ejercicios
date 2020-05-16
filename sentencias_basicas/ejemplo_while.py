# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:10:57 2018

@author: lenin
"""
print("Notas de alumnos")
n = 1
while n <= 3:
    Nota = int(input("Ingrese la nota para el alumno : "))
    if Nota < 7:
        print("El alumno esta reprobado")
    else:
        print("El alumno esta aprobado")
    
    n += 1
    
print("\nPromedio de notas de alumnos")
n = 1
Aux = 0
Nota = int(input("Ingrese el número de notas que desee: "))
while n <= Nota:
    Acumulador = int(input("Ingrese la nota: "))
    Aux += Acumulador
    n += 1
print("El promedio de las notas es : ", (Aux/Nota))
print("\nSueldo de los trabajadores")
A = 0
B = 0
N = 1
Aux = 0
n = int(input("Ingrese el número de empleados: "))
while N <= n:
    print("Ingrese el sueldo del empleado ", N)
    Acumulador = int(input(": "))
    if Acumulador <= 300:
        A += 1
    else:
        B += 1
    Aux += Acumulador
    N += 1

print("Empleados con sueldos menores o iguales a 300 $$: ", A)
print("Empleados con sueldos mayores a 500 $$: ", B)
print("Total a pagar en sueldos de empleados: ", Aux)

print("\nEjercicio del resto de la división XD")
N = 1
A = 0
B = 0
n = int(input("Ingrese el número de elementos que desea analizar: "))
while N <= n:
    print("Ingrese dato ",N)
    Aux = int(input(": "))
    if Aux % 2 == 0:
        A += 1
    else:
        B += 1
    N += 1
print("Elementos pares: ", A)
print("Elementos impares: ", B)
        















