# # Bucle while para imprimir números del 1 al 10
# contador = 10  # 1. Inicialización
# while contador >= 1 and True:  # 2. Condición (corregido de ≤ a <=)
#     print(contador, end=', ')
#     contador -= 1  # 3. Actualización. ¡Es crucial para no crear un bucle infinito!
# import random
#
# # Ejemplo: Búsqueda de un número con while-else
# oportunidades = 3
# numero_secreto = random.randint(1, 10)
#
# while oportunidades > 0:
#     intento = int(input("Adivina el número (1-10): "))
#     if intento == numero_secreto:
#         print("¡Felicitaciones! ¡Has adivinado!")
#         break  # El bucle se interrumpe, el 'else' no se ejecutará
#     oportunidades -= 1
#     print("Incorrecto. El numero es ",end="")
#     print("menor." if intento > numero_secreto else "mayor.")
#     print(f"Te quedan {oportunidades} oportunidades.")
# else:
#     # Este bloque solo se ejecuta si el while termina porque 'oportunidades' llega a 0
#     print(f"Lo siento, te quedaste sin oportunidades. El número era {numero_secreto}.")

# #
# while True:
#     user_input = input("Ingrese un comando: ")
#     if user_input == "salir":
#         break
#     print(f"Usted ingresó: {user_input}")

# def do_while():
#     x = 0
#     while True:
#         print(f"x = {x}")
#         x += 1
#         if x >= 5:
#             break
# do_while()

#
# for number in range(1,10,1):
#     if number == 6:
#         break
#     print(number)
#
# print("Estoy por fuera y sigo ejecutando el programa")
#
# # Iterar sobre una lista de frutas
# fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
# for fruit in fruits:
#     print(fruit)
#     if fruit == "Naranja":
#         print("-> Naranja encontrada")
#
#
# # Iterar sobre una cadena de texto
# for caracter in "SENA":
#     print(caracter)
#
# # Iteracion Sobre Diccionarios
# persona = {"nombre": "Diego", "edad": 35, "ciudad": "Sogamoso"}
#
# # Iterar sobre las claves
# for clave in persona:
#     print(clave)
#
# # Iterar sobre los valores
# for valor in persona.values():
#     print(valor)
#
# # Iterar sobre pares clave-valor
# for clave, valor in persona.items():
#     print(f"{clave}: {valor}")
#
# # Forma moderna y recomendada con enumerate()
# paises = ["Colombia", "México", "Argentina"]
# for indice, pais in enumerate(paises[::-1], start=1):
#     print(f"Índice {indice}: {pais}")

# # Imprimir solo los números impares de una lista
# numbers = range(1, 22)
# for num in numbers:
#     if num % 3 != 0:
#         continue  # Si el número es par, salta a la siguiente iteración
#     print(num) # Esta línea solo se ejecuta para números impares
#
# # Imprimir una tabla de multiplicar del 1 al 5
# for i in range(1, 6): # Filas
#     for j in range(1, 6): # Columnas
#         # end='\t' evita el salto de línea y agrega una tabulación
#         print(f'{i} x {j} = {i * j}', end='\t')
#     print()  # Imprime un salto de línea para empezar la siguiente fila

# Estructuras complejas como lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento)