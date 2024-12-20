# -*- coding: utf-8 -*-
"""Clases.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MsgIt71wfi19gCbdJ5RlFhTCBref1L4A
"""

class Perro:
  # Atributo de Clase
  especie = 'mamífero'

  def __init__(self, nombre, raza):
    print(f"Creando perro {nombre}, {raza}")

    # Atributos de Instancia
    self.nombre = nombre
    self.raza = raza

  # Métodos
  def ladra(self):
    print(f"{self.nombre}: Guau")

  def camina(self, pasos):
    print(f"{self.nombre}: Caminando {pasos} pasos")

  def dormir(self, horas):
    print(f"{self.nombre}: Durmiendo {horas} horas")

  def comer(self, comida):
    print(f"{self.nombre}: Comiendo {comida}")

mi_perro = Perro("Juanito", "Yorkshire")
mi_perro.ladra()
mi_perro.camina(10)
mi_perro.dormir(2)

tu_perro = Perro("Pedrito", "Bulldog")
tu_perro.ladra()
tu_perro.camina(100)
tu_perro.dormir(5)

nuestro_perro = Perro("Matias", "Chihuahua")
nuestro_perro.ladra()
nuestro_perro.camina(1)
nuestro_perro.dormir(24)

mi_perro.ladra()
tu_perro.ladra()
nuestro_perro.ladra()

mi_perro.comer("palomitas")
tu_perro.comer("Bistec")
nuestro_perro.comer("Papas Fritas")

print(mi_perro.especie)
print(tu_perro.especie)
print(nuestro_perro.especie)

a = open("archivo", "w")
a.read()
a.write()

with open("archivo", "w") as a:
  a.read()
  a.write()

a.close()

# r -> read (modo default)  (si archivo no existe, tira error)
# w -> write (sobreescribe) (si archivo no existe, lo crea)
# a -> append (agrega al final) (si archivo no existe, lo crea)
# x -> create (crea un archivo)

a = open("archivo.txt", "w")
frase = "Hola"
a.write(frase)
a.close()

a = open("archivo.txt", "r")
frase = "Mundo"
#a.write(frase)
a.close()

a = open("archivo.txt", "w")
frase = "!"
a.write(frase)
a.close()

b = open("archivo1.txt", "x")
b.write("Hola Mundo!")
b = open("archivo1.txt", "r")
print(b.read())
b.close()


a = open("archivo.txt", "r")
texto = a.read()
print(texto)
a.close()