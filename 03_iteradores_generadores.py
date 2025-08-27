# # Una lista es un objeto "iterable"
# # (list, set, dict, str, tuple, range, etc.)
# lista = [1, 2, 3]
#
# # Podemos obtener su iterador manualmente
# my_iter = iter(lista) # Crear el separador o marcador
#
# # Y pedir el siguiente elemento con next()
# print(next(my_iter))  # Output: 1
# print(next(my_iter))  # Output: 2
# print(next(my_iter))  # Output: 3
# # Si llamamos a next(my_iter) de nuevo, daría un error StopIteration
# # print(next(my_iter))
#
# # Funcionamiento por debajo
# mi_lista = ['a', 'b', 'c']
#
# # 1. El bucle 'for' obtiene el iterador del iterable
# iterador = mi_lista.__iter__() # O iter(mi_lista)
#
# # 2. Inicia un bucle infinito para pedir el siguiente elemento
# while True:
#     try:
#         # 3. Llama a next() en cada ciclo
#         letra = iterador.__next__() # O next(iterador)
#         print(letra)
#     except StopIteration:
#         # 4. Si next() lanza StopIteration, el bucle se rompe
#         break

# -------------------------------------------------------------
# -------------------------------------------------------------

# mi_lista = ['a', 'b', 'c']
# # Esto:
# for elemento in mi_lista:
#     print(elemento)
#
# # Es equivalente a esto:
# iterador = iter(mi_lista) # Igual a mi_lista.__iter__()
# while True:
#     try:
#         elemento = next(iterador) # Igual a iterador.__next__()
#         print(elemento)
#     except StopIteration:
#         break

# # -------------------------------------------------------------
# # -------------------------------------------------------------
#
# # Uniendo todas las piezas...
#
# class ContadorRegresivo:
#     """
#     Un iterador personalizado que cuenta hacia atrás desde un número inicial hasta 1.
#     """
#     def __init__(self, inicio, nombre):
#         self.actual = inicio
#         self.nombre = nombre
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # 1. Primero, revisamos la condición de parada.
#         # Si el número actual es menor que 1, hemos terminado.
#         if self.actual < 0:
#             raise StopIteration  # Esta es la señal para que el bucle for se detenga.
#
#         # 2. Si no nos hemos detenido, hacemos el trabajo.
#         else:
#             # Guardamos el número actual para devolverlo
#             valor_a_devolver = self.actual
#
#             # Restamos 1 para la *próxima* vez que se llame a next()
#             self.actual -= 1
#
#             # Devolvemos el número que guardamos
#             return valor_a_devolver
#
# print("Iniciando la cuenta regresiva...")
# for numero in ContadorRegresivo(7, nombre="Diego"):
#     print(numero)
# print("¡Despegue!")

# --- Salida ---
# Iniciando la cuenta regresiva...
# 5
# 4
# 3
# 2
# 1
# ¡Despegue!

# # -------------------------------------------------------------
# # -------------------------------------------------------------
#
# def contador_regresivo(inicio):
#     """
#     Un generador que cuenta hacia atrás desde un número inicial.
#     """
#     actual = inicio
#     while actual > 0:
#         yield actual
#         actual -= 1
#
# # Uso:
# for numero in contador_regresivo(5):
#     print(f"{numero}")

# Salida:
# -> La función generadora comienza ahora.
# -> Antes de yield: actual = 3
# Bucle FOR obtuvo: 3
#
# -> Después de yield: actual = 2
# -> Antes de yield: actual = 2
# Bucle FOR obtuvo: 2
#
# -> Después de yield: actual = 1
# -> Antes de yield: actual = 1
# Bucle FOR obtuvo: 1
#
# -> Después de yield: actual = 0
# -> La función generadora ha terminado.

# -------------------------------------------------------------
# -------------------------------------------------------------
#
# def leer_lineas(nombre_archivo):
#     """
#     Generador que lee un archivo línea por línea de forma eficiente.
#     """
#     with open(nombre_archivo, 'r') as f:
#         for linea in f:
#             yield linea.strip() # .strip() quita espacios y saltos de línea

# Uso (asumiendo que tienes un archivo 'mi_log.txt'):
# for linea_log in leer_lineas('mi_log.txt'):
#     if "ERROR" in linea_log:
#         print(linea_log)
#
# # -------------------------------------------------------------
# # -------------------------------------------------------------
#
# # Función generadora para la secuencia de Fibonacci
# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a  # 'produce' el valor actual y pausa la ejecución aquí
#         a, b = b, a + b # Esto se reanuda en la siguiente llamada a next()
# #
# # El bucle for consume el generador valor por valor
# print("Secuencia de Fibonacci generada:")
# for num in fibonacci(100):
#     print(num)
#
# # -------------------------------------------------------------
# # -------------------------------------------------------------

# # Lista (Ineficiente para grandes números):
# lista_cuadrados = [x*x for x in range(1000000)]
# # Generador (Eficiente):
# generador_cuadrados = (x*x for x in range(1000000))
#
# # La expresión generadora es perezosa. No se ha calculado nada aún.
# generador = (num * 10 for num in [1, 2, 3])
#
# # Los valores se generan al iterar sobre él
# for valor in generador:
#     print(valor) # Imprime 10, 20, 30
#
# # Ejemplo de un pipeline de datos
# # 1. Lee un archivo perezosamente
# lineas = leer_lineas('mi_log.txt')
# # 2. Filtra solo las líneas de error perezosamente
# lineas_error = (linea for linea in lineas if "ERROR" in linea)
# # 3. Extrae el mensaje de error perezosamente
# mensajes = (linea.split(": ")[2] for linea in lineas_error)
#
# # Ningún trabajo se ha realizado hasta que el bucle for lo pide
# for msg in mensajes:
#     print(msg)
#
# import sys
#
# # --- Opción 1: Lista (Comprensión de listas) ---
# # Creamos una lista en memoria con un millón de números.
# lista_cuadrados = [x*x for x in range(10000000)]
# print(f"Tamaño de la LISTA en memoria: {sys.getsizeof(lista_cuadrados)} bytes")
#
# # --- Opción 2: Generador (Expresión generadora) ---
# # Creamos un objeto generador. ¡Ojo, no calcula nada todavía!
# generador_cuadrados = (x*x for x in range(10000000))
# print(f"Tamaño del GENERADOR en memoria: {sys.getsizeof(generador_cuadrados)} bytes")
#
# # El generador es un objeto muy pequeño.
# # Solo cuando lo consumimos (ej. con sum()), calcula los valores uno por uno.
# # suma = sum(generador_cuadrados) # Esto seguiría siendo eficiente