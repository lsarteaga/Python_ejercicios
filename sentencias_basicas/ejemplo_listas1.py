'''
Suponga que está disponible la siguiente lista de los URLs de diferentes sitios Web que
han sido visitados
lista=['www.espol.edu.ec','www.google.com','www.sri.gob.ec','www.fiec.esp
ol.edu.ec','www.uess.edu.ec','www.FIEC.espol.edu.ec','www.fict.espol.edu.
ec','www.fcnm.espol.edu.ec','www.ucsg.edu.ec','www.Stanford.edu','www.har
vard.edu','www.stanford.edu','www.UCSG.edu.ec','www.google.com.ec','www.f
acebook.com','www.opensource.org','www.educacionbc.edu.mx']
Los URLs se pueden repetir y algunos corresponden a universidades del Ecuador y de
otros países.
Los URLs no diferencian entre mayúsculas y minúsculas. Por ejemplo. www,espol.edu.ec y
www.ESPOL.edu.ec representan el mismo sitio Web.
Escriba un programa que dada la lista indicada realice lo siguiente
a. Muestre numerados los nombres o siglas de las universidades que aparecen en la lista
(sin repetir)
b. Muestre la cantidad y el número y los nombres o siglas de las universidades del
Ecuador que aparecen en la lista (sin repetir)
c. Dado el nombre de un usuario y el nombre o sigla de la universidad, imprima la
identificación del correo del usuario con el formato del siguiente ejemplo:
juan_perez@espol.edu.ec
'''
lista=['www.espol.edu.ec','www.google.com','www.sri.gob.ec','www.fiec.espol.edu.ec','www.uess.edu.ec','www.FIEC.espol.edu.ec',
'www.fict.espol.edu.ec','www.fcnm.espol.edu.ec','www.ucsg.edu.ec','www.Stanford.edu','www.harvard.edu','www.stanford.edu',
'www.UCSG.edu.ec','www.google.com.ec','www.facebook.com','www.opensource.org','www.educacionbc.edu.mx']

universidades = []
universidades_ecuador = []
for x in range(len(lista)):
    lista[x] = lista[x].lower()
for x in lista:
    url = x.split('.')
    if 'edu' in url and url[1] not in universidades and url[2] not in universidades:
        universidades.append(url[1])
        if 'ec' in url:
            universidades_ecuador.append(url[1])

for x in range(len(universidades)):
    print(x+1,universidades[x],sep=' ')
aux = 0
for x in universidades_ecuador:
    print(x)
    aux += 1
print('cantidad de universidades del ecuador: ',aux)
print("")
usuario = input('Ingrese nombre de usuario: ')
universidad = input('Ingrese universidad: ')

for x in lista:
    url = x.split('.')
    if universidad in url:
        correo = usuario+'@'
        for y in range(1,len(url)):#puedo decir desde donde va el conteo
            correo += str(url[y]) + '.'
print(correo[:-1])#rebanado de strings
