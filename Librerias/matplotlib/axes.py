import matplotlib.pyplot as plt

# Data
jugador = ["Mason Mount", "Kai Havertz", "Timo Werner", "Lukaku", "Pulisic"]
goles = [20,22,15,2,7]

# Create figure
fig = plt.figure(figsize=(7,4))

# Return an ax -> Son elementos que conforman las graficas
# Array = Izquierda, Abajo, Ancho, Alto
ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.plot(jugador, goles, label="goles")

# Set labels
ax.set_xlabel("Jugadores")
ax.set_ylabel("Goles")
ax.set_title('Goles por Jugador Chelsea F.C.')

# Show legend
ax.legend()

fig.show()
# fig.savefig("Imagen.png")