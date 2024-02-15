def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    else:
        inventario.append(item)

# Ejemplo de uso
inventario = ['espada', 'poción', 'escudo']
nuevo_item = 'poción'
try:
    agregar_item(inventario, nuevo_item)
    print(f"'{nuevo_item}' añadido correctamente al inventario.")
except ValueError as e:
    print(f"Error: {e}")

nuevo_item = 'llave'
try:
    agregar_item(inventario, nuevo_item)
    print(f"'{nuevo_item}' añadido correctamente al inventario.")
except ValueError as e:
    print(f"Error: {e}")

print("Inventario actualizado:", inventario)
