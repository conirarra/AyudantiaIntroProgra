# -*- coding: utf-8 -*-
"""Preparacion Solemne 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/117Y6FdKC5Mx6JRCNIvg51HWS6vLihWvn
"""

i = 0
a = 2
b = 8

while i<a:
  while b>0:
    b=b-1
  i=i+1

"""¿Cuál es el último valor que toma b?
*   0
*   5
*   2
*   6


"""

print("Hola Mundo")
print("Hola") # Hola Mundo

""" Hola Mundo
"""

print("""'Esto es un comentario'""")

lista = input("Ingrese frase:")
lista = lista.split()
ma = lista[0]
for i in range(1,len(lista)):
  if len(lista[i]) > len(ma):
    ma = lista[i]
print(f"{ma}")

"""¿ Cuantas veces cambiará el valor de la variable ma, si la frase ingresada es "Buenos dias a todos los presentes"?


"""

import random

lista = []
valor_min = 10
valor_max = 0

for i in range(4):
  lista.append(random.randint(valor_max, valor_min))

for numero in lista:
  if (numero < valor_min):
    valor_min = numero
  if (numero > valor_max):
    valor_max = numero


print(f"{valor_min},{valor_max}")