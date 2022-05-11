# Usando imagenes rasterizadas
#? RGB (255,255,255) -> Red, Green, Blue
# Rango entre 0 y 255 para cada componente
# !Escala de grises debe tener los 3 componentes con el mismo número
"""
- Sintesis aditiva de colores -> Combinar colores
- Sintesis substractiva de colores -> Reducir luz
"""

#! EJERCICIO
"""
Escribe una función, que reciba una tupla de tres booleanos
y una matriz de tuplas que representa una imagen, donde cada 
booleana indica si se debe conservar el componente RGB respectivo
de cada pixel.
Un False nos indica que el componente debe quedar en 0, y un True que debe que
conserver su valor.
La funcion debe retornar una nueva imagen (matriz de tuplas) con el
filtro aplicado.
""" 


def aplicar_filtro_color(imagen: list, conservar: tuple) -> list:
  nueva_imagen = []
  alto = len(imagen)
  ancho = len(imagen[0])

  for i in range(alto):
    fila_nueva = []
    for j in range(ancho):
      r, g, b = imagen[i][j]
      temp = [r, g, b]
      for k in range(3):
        if not conservar[k]:
          temp[k] = 0
      nuevo_pixel = tuple(temp)
      fila_nueva.append(nuevo_pixel)
    nueva_imagen.append(fila_nueva)
  return nueva_imagen




