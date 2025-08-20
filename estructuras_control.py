def main():
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

    def es_casado(estado_civil):
        if estado_civil == "Casado":
            return True
        else:
            print("No tienes acceso ya que no eres casado.")
            return False

    def es_colombiano(nacionalidad):
        if nacionalidad == "Colombia":
            return True
        else:
            print("NO eres colombiano.")
            return False

    def es_mayor(edad_user):
        if edad_user >= 18:
            return True
        else:
            print("No eres mayor de edad")
            return False

    def es_miembro(esMiembro):
        if esMiembro:
            return True
        else:
            print("No eres miembro.")
            return False

    esMiembro = True
    edad = int(input("Ingresa tu edad:"))
    nacionalidad = "Colombia"
    estado_civil = "Casado"

    if (es_mayor(edad) and es_miembro(esMiembro) and
            es_colombiano(nacionalidad) and
            es_casado(estado_civil)
    ):
        print("Bienvenido cumples con todos los requisitos.")


if __name__ == "__main__":
    main()
