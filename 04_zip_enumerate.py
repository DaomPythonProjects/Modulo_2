# # Dos listas que queremos recorrer en paralelo
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
details = ['mineral natural', 'gallina feliz', 'de oliva', 'marina', 'verde']

# # zip() las une elemento a elemento
# for product, detail in zip(shopping, details):
#     print(f'Producto: {product} ({detail})')

# new_list = list(zip(shopping, details))
# print(new_list)
# # Salida: [('Agua', 'mineral natural'), ('Huevos', 'gallina feliz'), ...]
#
# lista_claves = ['nombre', 'edad', 'región']
# lista_valores = ['Juan', 30, 'Tunja']
#
# # Usando dict() con zip()
# mi_dict = dict(zip(lista_claves, lista_valores))
# print(mi_dict) # {'nombre': 'Juan', 'edad': 30, 'región': 'Tunja'}
#
# import sys
#
# rango_largo = range(1000000)
# otro_rango = range(1000000)
#
# # zip() crea un objeto iterador muy pequeño, sin importar el tamaño de las entradas
# zipped_object = zip(rango_largo, otro_rango)
# print(f"Tamaño del objeto zip en memoria: {sys.getsizeof(zipped_object) / 1024} MB") # Salida: ej. 72 bytes
#
# # Solo si lo materializas en una lista, consume mucha memoria
# lista_zipped = list(zipped_object)
# print(f"Tamaño de la lista creada desde zip: {sys.getsizeof(lista_zipped) / 1024} MB") # Salida: >8MB

# # Tenemos datos ya zipeados
# pares = [
#     ('Agua', 'mineral'),
#     ('Huevos', 'gallina'),
#     ('Aceite', 'oliva')
# ]
#
# # Usamos zip(*) para "descomprimir"
# productos, detalles = zip(*pares)
#
# print(f"Productos: {productos}") # ('Agua', 'Huevos', 'Aceite')
# print(f"Detalles: {detalles}")   # ('mineral', 'gallina', 'oliva')
#
# from itertools import zip_longest
#
# shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
# precios = [3000, 8000, 15000] # Lista más corta
#
# # Comportamiento de zip() normal (se detiene en el tercer elemento)
# print("Con zip():")
# for item, precio in zip(shopping, precios):
#     print(f"{item}: ${precio}")
#
# print("\nCon zip_longest():")
# # Continúa hasta el final de 'shopping', rellenando los precios faltantes con 0
# for item, precio in zip_longest(shopping, precios, fillvalue=0):
#     print(f"{item}: ${precio}")

# #############################################
# #############################################

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

# Usamos enumerate para obtener tanto el índice como el producto
print("Lista de compras con su posición:")
for indice, product in enumerate(shopping):
    print(f"{indice}: {product}")

# Empezar a contar desde 1 para una lista más "humana"
for indice, product in enumerate(shopping, start=1):
    print(f"{indice}. {product}")

# Buscamos 'Sal' en la lista
for i, nombre in enumerate(shopping):
    if nombre == "Sal":
        print(f"'{nombre}' se encontró en el índice {i}.")
        break
else:
    # Este bloque solo se ejecuta si el 'break' nunca se activó
    print("'Sal' no está en la lista.")

shopping = ['Agua', 'Huevos', 'Aceite']
enumerated_object = enumerate(shopping)

# Es un objeto iterador de la clase 'enumerate'
print(type(enumerated_object))
# Salida: <class 'enumerate'>

# Podemos consumir su contenido con next()
print(next(enumerated_object)) # Salida: (0, 'Agua')
print(next(enumerated_object)) # Salida: (1, 'Huevos')

enumerated_list = [(0, 'Agua'), (1, 'Huevos'), (2, 'Aceite')]

# Extraemos solo el segundo elemento de cada tupla
original_items = [item for index, item in enumerated_list]
print(original_items) # ['Agua', 'Huevos', 'Aceite']

shopping = ['Agua', 'Huevos', 'Aceite']

index_to_item_map = {index: item for index, item in enumerate(shopping)}
print(index_to_item_map)
# Salida: {0: 'Agua', 1: 'Huevos', 2: 'Aceite'}

words = ["uno", "dos", "tres", "cuatro", "cinco"]

# Poner en mayúsculas las palabras en posiciones pares
for i, word in enumerate(words, start=1):
    if i % 2 == 0:
        print(word.upper(),end=", ")
    else:
        print(word.lower(),end=", ")