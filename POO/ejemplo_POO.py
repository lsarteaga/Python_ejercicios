#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:36:47 2020

@author: lsarteaga
"""
import random
class Terminal:
    def __init__(self, letra):
        self.letra = letra
        self.premios = {}
        
    def canjear_dinero(self, dinero, tarjeta):
        self.tarjeta = tarjeta
        self.tarjeta.creditos += dinero*2
    def consultar_saldo(self, tarjeta):
        print('codigo de tarjeta: ',tarjeta.codigo)
        print('tickets de tarjeta: ',tarjeta.tickets)
        print('creditos de tarjeta: ',tarjeta.creditos)
        print('premios de tarjeta: ',tarjeta.premios)

    def transferir_creditos(self, tarjeta1, tarjeta2):
        saldo = int(input('ingrese saldo a transferir: '))
        if saldo > tarjeta1.creditos:
            print('no dispone de creditos suficientes')
        else:
            tarjeta1.creditos -= saldo
            tarjeta2.creditos += saldo
            print('transaccion exitosa')
            print('se han transferido ', str(saldo), ' creditos')
    
    def transferir_tickets(self, tarjeta1, tarjeta2):
        cantidad_tickets = int(input('ingrese tickets a transferir: '))
        if cantidad_tickets > tarjeta1.tickets:
            print('no dispone de suficientes tickets')
        else:
            tarjeta1.tickets -= cantidad_tickets
            tarjeta2.tickets += cantidad_tickets
            print('transaccion exitosa')
            print('se han transferido ', str(cantidad_tickets), ' tickets')
        
    def canjear_tickets(self, tarjeta):
        for x in self.premios.values():
            if tarjeta.tickets >= x.valor and x.cantidad > 0:
                tarjeta.tickets -= x.valor
                tarjeta.premios.append(x.categoria)
                x.cantidad -= 1
                print('Premio canjeado con exito')
            else:
                print('no se puede proceder con el canje')
    def crear_premio(self, categoria, cantidad, valor):
        self.premios[categoria] = Premio(categoria, cantidad, valor, self)
        
class Juego:
    def __init__(self, nombre_juego, costo_creditos):
        self.nombre_juego = nombre_juego
        self.costo_creditos = costo_creditos

    def otorgar_tickets(self, tarjeta):
        '''
        si pongo self.tarjeta = tarjeta se crea una relacion
        si no pongo no se crea una relacion osea solo uso al objeto
        tarjeta.tickets += random.randint(1,20)
        tarjeta.creditos -= self.costo_tickets
        '''
        if self.costo_creditos > tarjeta.creditos:
            print('no dispone de creditos suficientes')
        else:
            tarjeta.tickets += random.randint(1,20)
            tarjeta.creditos -= self.costo_creditos
            
class Tarjeta:

    def __init__(self, codigo):
        self.tickets = 0
        self.creditos = 0
        self.codigo = codigo
        self.premios = []
    '''
    def crear_codigo(self):
        valor = random.randint(1,10)
        return valor
    '''
        
class Premio:
    def __init__(self, categoria, cantidad, valor, terminal):
        self.categoria = categoria
        self.cantidad = cantidad
        self.valor = valor
        self.terminal = terminal


#principal

tarjeta1 = Tarjeta(1)
tarjeta2 = Tarjeta(2)

#creacion de 3 terminales y sus respectivos premios
terminal1 = Terminal('A')
terminal1.crear_premio('Premio Mayor',3,40)
terminal2 = Terminal('B')
terminal2.crear_premio('Premio Menor',5,30)
terminal3 = Terminal('C')
terminal3.crear_premio('Recompensa',7,25)

#ingresando dinero
terminal1.canjear_dinero(25,tarjeta1)
terminal2.canjear_dinero(36,tarjeta2)
print("")
print("")
terminal1.consultar_saldo(tarjeta1)
print("")
terminal3.consultar_saldo(tarjeta2)
#creando juegos
juego1 = Juego('metro exodus', 10)
juego2 = Juego('hit man', 8)
juego3 = Juego('mortal kombat', 11)
juego4 = Juego('guitar hero', 9)


#listo para jugar

juego1.otorgar_tickets(tarjeta1)
juego2.otorgar_tickets(tarjeta2)
juego3.otorgar_tickets(tarjeta1)
juego4.otorgar_tickets(tarjeta2)

print("")
print("")
terminal1.consultar_saldo(tarjeta1)
print("")
terminal1.consultar_saldo(tarjeta2)

terminal3.transferir_tickets(tarjeta1, tarjeta2)
print("")
print("")
terminal1.consultar_saldo(tarjeta1)
print("")
terminal1.consultar_saldo(tarjeta2)


terminal3.canjear_tickets(tarjeta2)
terminal3.canjear_tickets(tarjeta1)
print("")
print("")
terminal1.consultar_saldo(tarjeta1)
print("")
terminal1.consultar_saldo(tarjeta2)

for x in terminal3.premios.values():
    print(x.categoria)
    print(x.cantidad)
    
for x in terminal2.premios.values():
    print(x.categoria)
    print(x.cantidad)
    
    