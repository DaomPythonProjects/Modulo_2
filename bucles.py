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

def do_while():
    x = 0
    while True:
        print(f"x = {x}")
        x += 1
        if x >= 5:
            break
do_while()


for number in range(1,10,1):
    if number == 6:
        break
    print(number)

print("Estoy por fuera y sigo ejecutando el programa")