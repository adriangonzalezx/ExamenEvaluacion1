def separar_personajes(lista_personajes):
    # Utilizamos listas de comprensión para separar los personajes humanos y no humanos
    humanos = [personaje for personaje in lista_personajes if personaje['tipo'] == 'humano']
    no_humanos = [personaje for personaje in lista_personajes if personaje['tipo'] != 'humano']
    
    # Ordenamos las listas por el nombre de los personajes
    humanos_ordenados = sorted(humanos, key=lambda x: x['nombre'])
    no_humanos_ordenados = sorted(no_humanos, key=lambda x: x['nombre'])
    
    return humanos_ordenados, no_humanos_ordenados

# Ejemplo de uso
personajes = [
    {'nombre': 'Mario', 'tipo': 'humano'},
    {'nombre': 'Link', 'tipo': 'humano'},
    {'nombre': 'Sonic', 'tipo': 'no humano'},
    {'nombre': 'Pikachu', 'tipo': 'no humano'},
    {'nombre': 'Samus', 'tipo': 'humano'}
]

humanos, no_humanos = separar_personajes(personajes)
print("Personajes Humanos:")
for personaje in humanos:
    print(personaje['nombre'])
print("\nPersonajes No Humanos:")
for personaje in no_humanos:
    print(personaje['nombre'])
