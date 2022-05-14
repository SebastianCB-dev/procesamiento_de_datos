import pandas as pd


jugadores = {
  "9": "Romelu Lukaku",
  "11": "Timo Werner",
  "10": "Capitan America",
  "1": "Edouard Mendy",
  "19": "My Boy Mason Mount",
  "29": "COBRA Havertz"
}

chelsea_fc = pd.Series(jugadores, name="Chelsea F.C. Jugadores")

print(chelsea_fc)

# !Resetear indices
chelsea_fc = chelsea_fc.reset_index(drop = True)
