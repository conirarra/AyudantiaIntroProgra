# -*- coding: utf-8 -*-
"""Libreria random.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11QxuPX2fHqMxqyupYVT5Ngpa3esJ8wl-

Pagina de libreria random [aquí](https://interactivechaos.com/es/manual/tutorial-de-python/la-libreria-random)
"""

import random

x = random.randint(0,100)

print(x)

from random import randint

x = randint(0,100)

print(x)

from random import randint

# from libreria import funcion

a = 5
b = 10

x = random.random() # -> [0,1)
y = random.randint(a, b) # -> [a,b]

print(f'{x} - {y}')