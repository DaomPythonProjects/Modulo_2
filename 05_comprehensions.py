# Método tradicional para crear una lista con los cuadrados de los primeros 5 números
cuadrados_tradicional = []
for i in range(5):
    cuadrados_tradicional.append(i**2)

# Equivalente usando comprensión de listas (más corto y legible)
cuadrados_comprehension = [i**2 for i in range(5)]

print(cuadrados_tradicional)    # [0, 1, 4, 9, 16]
print(cuadrados_comprehension) # [0, 1, 4, 9, 16]

# Se pueden usar funciones dentro de la expresión
def eleva_al_2(i):
    return i**2
cuadrados_funcion = [eleva_al_2(i) for i in range(5)]

# Si no necesitas el valor, puedes usar un guion bajo (_)
unos = [1 for _ in range(5)] # [1, 1, 1, 1, 1]

# Crear una lista solo con las letras 'r' de una frase
frase = "El perro de san roque no tiene rabo"
erres = [letra for letra in frase if letra == 'r']
print(erres)  # ['r', 'r', 'r', 'r']

# Crear una nueva lista eliminando los múltiplos de 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_multiplos_3 = [n for n in nums if n % 3 != 0]
print(no_multiplos_3)  # [1, 2, 4, 5, 7, 8, 10]

numeros = [1, 2, 3, 4, 5, 6]

# Para cada número, la expresión decide qué string añadir
etiquetas = ["par" if n % 2 == 0 else "impar" for n in numeros]

print(etiquetas)
# Salida: ['impar', 'par', 'impar', 'par', 'impar', 'par']

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# El primer 'for' recorre las filas, el segundo recorre los números de cada fila
lista_plana = [num for fila in matriz for num in fila]

print(lista_plana)
# Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Esto es equivalente al siguiente bucle tradicional:
# lista_plana_tradicional = []
# for fila in matriz:
#     for num in fila:
#         lista_plana_tradicional.append(num)

numeros_con_duplicados = [1, 2, 3, 1, 2, 4, 5, 4]

# Crea un set con los cuadrados únicos
cuadrados_unicos = {n**2 for n in numeros_con_duplicados}

print(cuadrados_unicos)
# Salida: {1, 4, 9, 16, 25}

frase = "El perro de san roque no tiene rabo"

# La comprensión de set solo guardará una 'r', ya que los sets no permiten duplicados
mi_set = {letra for letra in frase if letra == "r"}
print(mi_set)  # {'r'}

product_ids = ['ABC-001', 'DEF-002', 'ABC-003', 'GHI-004', 'DEF-005']

# Obtenemos las categorías únicas (los 3 primeros caracteres)
unique_categories = {pid[:3] for pid in product_ids}

print(unique_categories)
# Salida: {'GHI', 'ABC', 'DEF'}
# Nota cómo 'ABC' y 'DEF' aparecen solo una vez.

# Set comprehension: No hay dos puntos
mi_set = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

# Dictionary comprehension: Hay un par 'clave: valor'
mi_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Un error común
empty_set_wrong = {}
print(type(empty_set_wrong)) # <class 'dict'>

# La forma correcta
empty_set_correct = set()
print(type(empty_set_correct)) # <class 'set'>

# Crear un diccionario a partir de una lista de números, con el número como clave y su cuadrado como valor
numeros = [1, 2, 3, 4]
cuadrados_dict = {num: num**2 for num in numeros}
print(cuadrados_dict) # {1: 1, 2: 4, 3: 9, 4: 16}

# Un uso muy común es combinarlo con zip para crear un diccionario
lista_claves = ['nombre', 'edad', 'región']
lista_valores = ['Juan', 30, 'Tunja']
mi_dict = {clave: valor for clave, valor in zip(lista_claves, lista_valores)}
print(mi_dict) # {'nombre': 'Juan', 'edad': 30, 'región': 'Tunja'}

# Crear un diccionario solo con los números pares y sus cuadrados
numeros = [1, 2, 3, 4, 5, 6]

# Caso 1 (if al final): Actúa como un filtro.
# Decide SI un elemento se procesa o se descarta por completo.
cuadrados_pares = {n: n**2 for n in numeros if n % 2 == 0}

print(cuadrados_pares)
# Salida: {2: 4, 4: 16, 6: 36}

# Caso 2 (if/else en la expresión): Actúa como una transformación.
# Procesa TODOS los elementos y decide QUÉ valor se le asigna a cada uno.

# Crear un diccionario que categoriza los números
numeros = [1, 2, 3, 4, 5]
categorias = {n: 'par' if n % 2 == 0 else 'impar' for n in numeros}

print(categorias)
# Salida: {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

datos_personales = {'nombre': 'Juan', 'ciudad': 'Tunja', 'profesion': 'Ingeniero'}

# Invertimos el diccionario: el valor se convierte en clave y la clave en valor
datos_invertidos = {valor: clave for clave, valor in datos_personales.items()}

print(datos_invertidos)
# Salida: {'Juan': 'nombre', 'Tunja': 'ciudad', 'Ingeniero': 'profesion'}

palabras = ['hola', 'python', 'excelente']

# La palabra es la clave, su longitud (len) es el valor
longitudes = {palabra: len(palabra) for palabra in palabras}

print(longitudes)
# Salida: {'hola': 4, 'python': 6, 'excelente': 9}