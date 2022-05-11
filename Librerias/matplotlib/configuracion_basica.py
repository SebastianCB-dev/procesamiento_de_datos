import matplotlib.pyplot as plt

# Datos a graficar
jugador = ["Mason Mount", "Kai Havertz", "Timo Werner", "Lukaku", "Pulisic"]
goles = [20,22,15,2,7]

# Crear figura y setear tamaño
plt.figure(figsize=(7,4))

# Dibujar grafica
plt.plot(jugador, goles, label="goles")

# Label eje x
plt.xlabel("Jugadores")

# Label eje y
plt.ylabel("Goles")

# Titulo grafica
plt.title("Goles de jugadores Chelsea F.C.")

# Mostrar leyenda
plt.legend()
