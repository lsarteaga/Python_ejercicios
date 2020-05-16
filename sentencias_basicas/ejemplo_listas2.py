'''
ejercicio 9.2
Escribir un programa para eliminar los elementos repetidos de una lista
numèrica
'''
import random
lista = []
for i in range(15):
    lista.append(random.randint(1,5))

u = []
for x in lista:
    if x not in u:
        u.append(x)
print(lista)
print(u)

'''
Ejemplo. Escribir una función para ordenar una lista de palabras en forma creciente
usando como criterio la longitud de las palabras
'''
palabras = ['Formar','profesionales','investigadores' ,'de' ,'excelencia', 'creativos', 'humanistas', 'con'
'capacidad', 'de' ,'liderazgo', 'pensamiento', 'crítico' ,'y' ,'alta', 'conciencia', 'ciudadana', 'generar', 'aplicar' ,'el', 'conocimiento', 'científico',
 'transferir' ,'tecnología']
print(palabras)
for x in range(len(palabras)):
    i = len(palabras[x])
    for y in range(len(palabras)):
        u = len(palabras[y])
        if i < u:
            palabras[x],palabras[y] = palabras[y],palabras[x]
            
print(palabras)
