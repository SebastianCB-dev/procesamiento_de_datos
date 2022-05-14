# Loc == Acceder por etiqueta
# Iloc == Acceder por posicion

import pandas as pd

numeros_jugadores = [1, 3, 29, 19, 11, 9, 10]
nombres_jugadores = ["Edouard Mendy", "Rudiger", "Kai Havertz 🐍", "Mason Mount", "Timo Werner", "Lakaka", "Capitan America"]

chelsea_fc = pd.Series(numeros_jugadores, index=nombres_jugadores, name="Jugadores Chelsea F.C.")

# chelsea_fc = chelsea_fc.sort_values() -> Ordenar por valores
chelsea_fc = chelsea_fc.sort_index() # -> Ordenar por etiqueta
#print(chelsea_fc)

# *Crear una copia es necesario para evitar alteraciones
copia = chelsea_fc.copy()
#! Asignación
# Etiqueta 500
copia['Rudiger'] = 4

# copia[0:100] = 20 -> Por posicion
print(copia)

#! Asignación loc

copia2 = nombres_jugadores.copy()
"""
  copia2.loc[500] = 180 -> Etiqueta 500
  copia2.loc[0:100] = 190 -> Etiqueta de la 0 a la 100
"""

# ! Asignación iloc

copia_3 = nombres_jugadores.copy()
"""
  copia3.iloc[500]   = 180 -> Posición 500
  copia3.iloc[0:100] = 20 -> Posición 0 a la 100
"""