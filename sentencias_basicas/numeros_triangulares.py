'''
python
21. Los números triangulares f(n)tienen la regla de formación descrita con el
siguiente grafico para n=1, 2, 3, 4, 5, ...Escriba una función que reciba un valor de  n  y
entregue el resultado f(n)
a) Use una forma normal para la función mediante un ciclo
b) Use una forma recursiva para la función

Tn = n(n+1)/2
'''
'''
-----------------------parte 1----------------------
def triangular(n):
    t = (n*(n+1))/2
    print('El valor es: ',t)


print('Numeros triangulares')
n = int(input('Ingrese un numero: '))
triangular(n)

'''

#parte 2 funcion recursiva
def triangular(n,aux):
    print('n = ',n,' aux = ',aux)
    if n == 1:
        aux += 1
    else:
        aux = n + triangular(n-1,aux)
        print('aux al final = ',aux )
    return aux


print('Numeros triangulares')
n = int(input('Ingresa numero: '))
aux = 0
valor = triangular(n,aux)
print('resultado = ',valor)
