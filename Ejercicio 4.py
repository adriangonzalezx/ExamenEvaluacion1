from queue import PriorityQueue

# Definir las misiones con sus niveles de dificultad
misiones = [
    ("Rescatar a la princesa", 5),
    ("Recoger 10 monedas de oro", 3),
    ("Derrotar al jefe final", 8),
    ("Explorar la cueva oscura", 4),
    ("Encontrar el tesoro perdido", 6)
]

# Crear una cola de prioridad
cola_misiones = PriorityQueue()

# Agregar las misiones a la cola de prioridad
for mision in misiones:
    cola_misiones.put((mision[1], mision[0]))  # Invertimos el orden para que el primer elemento sea la prioridad

# Mostrar las misiones sin mostrar los niveles de dificultad
print("Misiones por prioridad:")
while not cola_misiones.empty():
    mision = cola_misiones.get()
    print(" -", mision[1])  # Excluimos el nivel de dificultad en la impresión
