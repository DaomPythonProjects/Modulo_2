def main(value=None):
    # # Definimos una variable
    # x = 10
    #
    # # Si la condición (x > 5) es verdadera, se ejecuta el código indentado
    # if x > 5:
    #     print("x es mayor que 5")
    #
    # x = 3
    #
    # if x > 5:
    #     print("x es mayor que 5")
    # else:
    #     print("x es menor o igual a 5")

    # x = 5
    #
    # if x > 5:
    #     print("x es mayor que 5")
    # elif x == 5: # Si la primera condición es falsa, prueba con esta
    #     print("x es igual a 5")
    # else: # Si ninguna de las anteriores es verdadera, ejecuta esta
    #     print("x es menor que 5"
    #
    # x = 15
    # y = 30
    #
    # # Ejemplo con 'and'
    # if x > 10 and y > 25:
    #     print("x es mayor que 10 Y y es mayor que 25")
    #
    # # Ejemplo con 'or'
    # if x > 10 or y > 35:
    #     print("x es mayor que 10 O y es mayor que 35")
    #
    # x = 15
    #
    # if not x > 20: # not (False) se convierte en True
    #     print("x no es mayor que 20")
    # Forma tradicional con 'and'
    # edad = 25
    # if edad >= 18 and edad <= 65:
    #     print("Estás en edad laboral.")
    #
    # # Forma Pythónica encadenada (más limpia y recomendada)
    # edad = 25
    # if 18 <= edad <= 65:
    #     print("Estás en edad laboral.")
    #

    # def es_casado(estado_civil):
    #     if estado_civil == "Casado":
    #         return True
    #     else:
    #         print("No tienes acceso ya que no eres casado.")
    #         return False
    #
    # def es_colombiano(nacionalidad):
    #     if nacionalidad == "Colombia":
    #         return True
    #     else:
    #         print("NO eres colombiano.")
    #         return False
    #
    # def es_mayor(edad_user):
    #     if edad_user >= 18:
    #         return True
    #     else:
    #         print("No eres mayor de edad")
    #         return False
    #
    # def es_miembro(esMiembro):
    #     if esMiembro:
    #         return True
    #     else:
    #         print("No eres miembro.")
    #         return False
    #
    # esMiembro = True
    # edad = int(input("Ingresa tu edad:"))
    # nacionalidad = "Colombia"
    # estado_civil = "Casado"
    #
    # if (es_mayor(edad) and es_miembro(esMiembro) and
    #         es_colombiano(nacionalidad) and
    #         es_casado(estado_civil)
    # ):
    #     print("Bienvenido cumples con todos los requisitos.")

    # # Forma tradicional
    # edad = 20
    # if edad >= 18:
    #     mensaje = "Es mayor de edad"
    # else:
    #     mensaje = "Es menor de edad"
    # print(mensaje)
    #
    # # Con el operador ternario
    # edad = 20
    # print("Es mayor de edad" if edad >= 18 else "Es menor de edad")


    # Imagina que evaluamos un código de estado de una petición web
    # value = 0
    # status = int(input("Ingresa el código de estado HTTP: "))
    #
    # match status:
    #     case _ if(200 <= status <= 299): # Podemos agrupar casos con el operador '|'
    #         print("La petición fue exitosa")
    #     case _ if(400 <= status <= 499): # Podemos usar 'range' para un rango de valores
    #         print("Error al cargar la pagina")
    #     case _ if(500 <= status <= 599):
    #         print("Error interno del servidor")
    #     case _: # El guion bajo (_) actúa como el caso por defecto (else)
    #         print("Código de estado no reconocido")

    # --- Sistema de Validación de Entrada a un Evento ---

    print("¡Bienvenido al sistema de validación de entradas!")

    # Pedimos los datos al usuario de forma interactiva
    try:
        edad = int(input("Por favor, introduce tu edad: "))
    except ValueError:
        print("Error: La edad debe ser un número válido.")
        exit()

    # Validamos la edad con un operador encadenado
    if not (0 < edad < 100):
        print("Por favor, introduce una edad realista.")
    elif edad < 18:
        print("Lo sentimos, este evento es solo para mayores de 18 años.")
        exit()
    else:
        tipo_entrada = input("¿Qué tipo de entrada tienes (VIP, General o Estudiante)?: ").upper()
        # Usamos match-case para gestionar el tipo de entrada de forma legible
        print(f"Edad verificada ({edad} años). Verificando entrada tipo '{tipo_entrada}'...")

        match tipo_entrada:
            case "VIP":
                mensaje_acceso = "Acceso concedido a la zona VIP. ¡Disfruta!"
            case "GENERAL":
                mensaje_acceso = "Acceso concedido a la zona general. ¡Disfruta del evento!"
            case "ESTUDIANTE":
                mensaje_acceso = "Acceso concedido. Recuerda mostrar tu carné de estudiante."
            case _:
                mensaje_acceso = "Error: El tipo de entrada no es válido."

        print(mensaje_acceso)

        # Usamos el operador ternario para un mensaje adicional
        if mensaje_acceso.startswith("Acceso"):
            mensaje_bebida = "Pasa a la barra por una bebida de cortesía." if tipo_entrada == "VIP" else "Puedes comprar bebidas en la barra."
            print(mensaje_bebida)


if __name__ == "__main__":
    main()
