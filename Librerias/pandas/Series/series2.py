import pandas as pd

numeros_jugadores = [1, 3, 29, 19, 11, 9, 10]
nombres_jugadores = ["Edouard Mendy", "Rudiger", "Kai Havertz 🐍", "Mason Mount", "Timo Werner", "Lakaka", "Capitan America"]

chelsea_fc = pd.Series(numeros_jugadores, index=nombres_jugadores, name="Jugadores Chelsea F.C.")

print( chelsea_fc )
