# Liberías
import matplotlib.pyplot as plt

jugador = ["Mason Mount", "Kai Havertz", "Timo Werner", "Lukaku", "Pulisic"]
goles = [20,22,15,2,7]
asistencias = [3,3,2,1,0]

# Crear figura
fig = plt.figure(figsize=(7,4))

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(jugador, goles, label="goles")
ax.plot(jugador, asistencias, label="asistencias")

ax.set_xlabel("Jugadores")
ax.set_ylabel("Valores")
ax.set_title("Asistencias vs Goles Jugadores Chelsea F.C.")
ax.legend()


