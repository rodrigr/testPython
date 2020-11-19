# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:01:48 2019

@author: rodri
"""

import random

## 1
def generar_bosque(n,vacio=True,limpio=False):
    bosque = list()
    
    if vacio and not(limpio):
        for i in range(n):
            bosque.append(0)
    elif limpio and not(vacio):
        for i in range(n):
            bosque.append(random.randint(0,1))
    elif not(vacio) and not(limpio):
        for i in range(n):
            bosque.append(random.randint(-1,1))
    else:
        print('alguno de los valores vacio o limpio debe ser false')
        return None   
    
    return bosque
    

bosque_vacio = generar_bosque(10)

bosque_limpio = generar_bosque(10,False,True)

bosque_quemado = generar_bosque(10,False)

## 2

def suceso_aleatorio(prob):
    rand = random.randint(0,100)
    if rand < prob*100:
        return True
    else:
        return False

def brotes(bosque,p):
    i = 0
    while i < len(bosque):
        if bosque[i] == 0 and suceso_aleatorio(p):
            bosque[i] = 1
        i += 1
    
            
brotes(bosque_vacio,0.6)

brotes(bosque_limpio,0.6)

## 3

def cuantos(bosque, tipo_celda):
    return bosque.count(tipo_celda)

## 4
    
def rayos(bosque, f):
    i = 0
    while i < len(bosque):
        if bosque[i] == 1 and suceso_aleatorio(f):
            bosque[i] = -1
        i += 1
        
bosque1 = generar_bosque(100,False,True)
        
rayos(bosque1, 0.3)

print(cuantos(bosque1,1))
print(cuantos(bosque1,-1))

## 5

b_1 = [1, 1, 1, -1, 0, 0, 0, -1, 1, 0]

b_2 = [-1, 1, 1, -1, 1, 1, 0, 0, -1, 1]

def propagacion(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            if i < len(bosque) - 1 and bosque[i + 1] == 1:
                bosque[i + 1] = -1
            if i != 0 and bosque[i - 1] == 1:
                bosque[i - 1] = -1
                for j in range(i - 1, 0,-1):
                    if bosque[j] == -1:
                        if j != 0 and bosque[j -1] == 1:
                            bosque[j - 1] = -1
                
                
propagacion(b_1)

propagacion(b_2)

## 6

def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0
            
limpieza(b_1)
            
## 7

b_3 = generar_bosque(100)

def incendio_forestal(p, f, n_rep, bosque):
    vivos_temporada = list()
    for i in range(n_rep):
        ## Primavera
        brotes(bosque, p)
        ## Rayos
        rayos(bosque, f)
        ## Propagación Incendio
        propagacion(bosque)
        ## Limpieza
        limpieza(bosque)
        ## Cantidad de arboles sobrevivientes
        vivos_temporada.append(cuantos(bosque,1))
    
    sum = 0
    
    for i in  vivos_temporada:
        sum += i
        
    ##print('sobrevivieron en promedio %s árboles con una probabilidad de caída de rayos de %s y una probabilidad de crecimiento de %s'% (sum/n_rep, f, p))
    return sum/n_rep


incendio_forestal(0.3,0.02,50,b_3)


## 8

b_4 = generar_bosque(100)

data = dict()

data['p'] = list()
data['prom'] = list()


for i in range(10):
    
    data['p'].append(i/10)
    
    data['prom'].append(incendio_forestal(i/10,0.02,100,b_4))
    


import matplotlib.pyplot as plt

plt.plot('p', 'prom', data=data, linestyle='-', marker='o')



#Hola





















