def validar_edad(edad):
    while True:
        try:
            edad_validada = int(edad)
            if edad_validada < 0:
                raise ValueError("La edad no puede ser negativa.")
            return edad_validada
        except ValueError:
            print("Error: La edad debe ser un número entero mayor o igual a cero.")
            edad = input("Ingrese su edad nuevamente: ")
