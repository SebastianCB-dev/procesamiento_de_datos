"""
Construya una función que reciba dos vectores (con 3 componentes cada uno) y retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla con tres valores flotantes.

Su solución debe tener una función de acuerdo con la siguiente especificación:

Nombre de la función: suma_vectorial    

Si lo requiere, puede agregar funciones adicionales.

"""

def suma_vectorial(vector_1: tuple, vector_2: tuple) -> tuple:
  """Función que suma dos vectores de 3 dimensiones y retorna su solución

  Args:
      vector_1 (tuple): primer vector con 3 dimensiones
      vector_2 (tuple): segundo vector con 3 dimensiones

  Returns:
      tuple: vector del resultado de la suma entre vector_1 y vector_2
  """
  return ( (vector_1[0] + vector_2[0]), (vector_1[1] + vector_2[1]), (vector_1[2] + vector_1[2]) )