import math

#! Tuplas como valores de retorno

def calcular_area_y_perimetro(rectangulo: tuple) -> tuple:
  dimension = rectangulo[1]
  ancho, alto = dimension

  area = ancho * alto
  perimetro = (ancho + alto) * 2

  return (area, perimetro)

rectangulo = ((1,2), (2,3), "Rojo")
area, perimetro = calcular_area_y_perimetro(rectangulo)

#! Tuplas como parámetros

def calcular_distancia(punto_1: tuple, punto_2: tuple) -> float:
  delta_x = abs(punto_1[0] - punto_2[0])
  delta_y = abs(punto_1[1] - punto_2[1])
  distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
  return distancia

p1 = (1, 2)
p2 = (4, 6)

calcular_distancia(p1, p2)