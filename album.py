# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:17:40 2019

@author: rodri
"""

# importando paquetes necesarios

import random

import numpy as np

# pruebas

x = random.random()

a = np.arange(10)

len(a)

a[:3]

random.shuffle(a)

np.mean(a)

random.randint(1, 10)

miSet = set()

miSet.add(1)
miSet.add(2)
miSet.update([1,4,5])
miSet.add(1)

#Primera simplificación

##1


figu = random.randint(1,6)

print("tu figurita es la número: % s" % (figu))

##2 

def comprar_figus():
    figu = random.randint(1,6)
    print("tu figurita es la número: % s" % (figu))
    return figu

def completar_album():
    album = set()
    figus_compradas = 0
    album_lleno = False
    while not(album_lleno):
        nueva_figu = comprar_figus()
        album.add(nueva_figu)
        album_lleno = len(album) == 6
        figus_compradas += 1
    print("compraste % s figuritas" % (figus_compradas))
    
completar_album()

##3
def comprar_figusII(n):
    figu = random.randint(1,n)
    print("tu figurita es la número: % s" % (figu))
    return figu

def completar_albumII(n):
    album = set()
    figus_compradas = 0
    album_lleno = False
    while not(album_lleno):
        nueva_figu = comprar_figusII(n)
        album.add(nueva_figu)
        album_lleno = len(album) == n
        figus_compradas += 1
    print("compraste % s figuritas" % (figus_compradas))
    
completar_albumII(350) 






