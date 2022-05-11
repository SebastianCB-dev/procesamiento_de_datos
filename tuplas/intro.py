lista = [4, 7, 2, 4, 7, 9, 2, 9]

lista[2] #2

lista[2] = 99

lista.append(-1)

# Tuplas

tupla = (1, 2, 3, 4, 5) # Parentesis 

#tupla[1] = 12 # !ERROR

# Tuplas garantizan la inmutabilidad == garantía

# !Creación de tuplas

coordenada = (3, 6, 3)
coordenada2 = 3, 6, 3

valor = (1,)
valor2 = 1,

type(coordenada) # tuple

# rectangulo = ((x,y), (ancho, alto), color)
rectangulo = ((1,2), (2,2), "Rojo")

#! Tamaños especiales

tupla_vacia = ()
tupla_unitaria = (5,)
tupla_unitaria2 = 5,

type(tupla_unitaria2) # tuple

#! Acceder
tupla[0] # 1
tupla[0:2] # 1, 2
tupla[-1] # 5

# Longitud tupla
len(tupla) # 5


rectangulo = (1,2,3)
#!DESEMPEQUETADO

eje_x, eje_y, eje_z = rectangulo