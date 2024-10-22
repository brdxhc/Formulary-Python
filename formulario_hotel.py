from validaciones import validar_edad

class FormularioHotel:
    def __init__(self):
        self.datos_personales = {}

    def solicitar_nombre(self, ):
        self.datos_personales["nombre"] = input("Ingrese su nombre: ")

    def solicitar_edad(self):
        self.datos_personales["edad"] = validar_edad(input("Ingrese su edad: "))

    def verificar_edad(self):
        if self.datos_personales["edad"] >= 18:
            print("Usted es mayor de edad.")
        else:
            print("Usted es menor de edad.")

    def solicitar_actualizaciones_correo(self):
        respuesta = input("¿Desea recibir actualizaciones por correo electrónico? (s/n): ")

        while respuesta.lower() != "s" and respuesta.lower() != "n":
            print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")
            respuesta = input("¿Desea recibir actualizaciones por correo electrónico? (s/n): ")

        if respuesta.lower() == "s":
            self.datos_personales["correo"] = input("Ingrese su dirección de correo electrónico: ")
            print(f"Se ha registrado el correo electrónico {self.datos_personales['correo']} para recibir actualizaciones.")
        else:
            print("Ha decidido no recibir actualizaciones por correo electrónico.")

    def guardar_datos(self):
        try:
            with open("datos/datos.txt", "w") as archivo:
                for key, value in self.datos_personales.items():
                    archivo.write(f"{key.capitalize()}: {value}\n")
            print("Los datos se han guardado exitosamente.")
        except IOError:
            print("Error al guardar los datos.")

    def mostrar_datos_guardados(self):#muestra los datos guardados
        try:
            with open("archivo.txt", "r", encoding="utf-8") as archivo:
    
                print("Datos guardados:")
                print(archivo.read())
        except IOError:
            print("Error al mostrar los datos guardados.")


def main():
    formulario = FormularioHotel()

    formulario.solicitar_nombre()
    formulario.solicitar_edad()
    formulario.verificar_edad()
    formulario.solicitar_actualizaciones_correo()
    formulario.guardar_datos()
    formulario.mostrar_datos_guardados()


if __name__ == "__main__":
    main()
