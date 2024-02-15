def palabras_comunes(lista1, lista2):
    # Convertir las listas a conjuntos para eliminar duplicados
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Encontrar la intersección de los conjuntos para obtener las palabras comunes
    palabras_comunes = set1.intersection(set2)
    
    # Convertir el resultado de nuevo a una lista
    lista_palabras_comunes = list(palabras_comunes)
    
    return lista_palabras_comunes

# Ejemplo de uso
lista1 = ["hola", "mundo", "esto", "es", "una", "prueba"]
lista2 = ["esto", "es", "otra", "prueba", "más"]

resultado = palabras_comunes(lista1, lista2)
print("Palabras comunes:", resultado)
