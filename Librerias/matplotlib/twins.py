# Twins = 2 Graficas mezcladas con diferente eje Y

import matplotlib.pyplot as plt

jugador = ["Mason Mount", "Kai Havertz", "Timo Werner", "Lukaku", "Pulisic"]
goles = [20,22,15,2,7]
asistencias = [3,3,2,1,0]


fig = plt.figure(figsize=(7,4))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# Graficar linea con color rojo = r
ax.plot(jugador, goles, "r", label="goles")
ax.set_xlabel("Jugadores", color="green")
ax.set_ylabel("Goles", color="red")
ax.set_title("Goles vs Asistencias Chelsea F.C.")


# Segunda grafica en la misma
ax2 = ax.twinx()
ax2.plot(jugador, asistencias, "b", label="asistencias")
ax2.set_ylabel("Asistencias", color="blue")



