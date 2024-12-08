


# Entrega del Caso Práctico Final Curso Python Autoestudio 2da Edición 24
# Sistema de Reservas para un Cine con Tarifas Especiales 

# # Descripción: Desarrolla una aplicación en Python para gestionar las reservas de asientos 
# en una sala de cine, incluyendo un sistema de precios con descuentos en ciertos días y tarifas
#  reducidas para personas mayores. 




# Clase que representa un asiento en el cine.
class Asiento:                                   
    def __init__(self, numero, fila, precio_base):
        self.__numero = numero                    # Número de asiento
        self.__fila = fila                        # Fila del asiento.
        self.__reservado = False                  # Estado de la reserva (por defecto, no reservado).
        self.__precio = precio_base               # Precio base del asiento.

 #  # Métodos para obtener información del asiento.
 #  Getters y Setters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    # Para reservar el asiento.
    def reservar(self, precio):
        if self.__reservado:
            raise Exception(f"El asiento {self.__fila}{self.__numero} ya está reservado.")
        self.__reservado = True
        self.__precio = precio

    # Para cancelar una reserva.
    def cancelar_reserva(self):
        if not self.__reservado:
            raise Exception(f"El asiento {self.__fila}{self.__numero} no está reservado.")
        self.__reservado = False
        self.__precio = 0

    # Para mostrar información del asiento.
    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__fila}{self.__numero} - {estado} - Precio: ${self.__precio:.2f}"


 # Clase que representa la sala del cine y los asientos.
class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []                         # Lista de asientos en la sala.
        self.__precio_base = precio_base             # Precio base de los asientos.

    def agregar_asiento(self, numero, fila):
        if any(asiento.get_numero() == numero and asiento.get_fila() == fila for asiento in self.__asientos):
            raise Exception(f"El asiento {fila}{numero} ya está registrado.")
        self.__asientos.append(Asiento(numero, fila, self.__precio_base))

    def reservar_asiento(self, numero, fila, dia, edad):
        asiento = self.buscar_asiento(numero, fila)
        precio = self.__calcular_precio(dia, edad)
        asiento.reservar(precio)

    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        asiento.cancelar_reserva()

    def mostrar_asientos(self):
        return [str(asiento) for asiento in self.__asientos]

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        raise Exception(f"Asiento {fila}{numero} no encontrado.")

# descuento a personas mayores de 65
    def __calcular_precio(self, dia, edad):
        precio = self.__precio_base
        if dia.lower() == "miércoles":
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio

# Funcion Menu de opciones. 
def menu():
    print("\n--- Menú de Opciones ---")
    print("1. Mostrar asientos")
    print("2. Reservar asiento")
    print("3. Cancelar reserva")
    print("4. Salir")

# Función principal para ejecutar el programa.
def main():
    precio_base = 10.0
    sala = SalaCine(precio_base)

   # Agrega asientos predeterminados a la sala (por ejemplo, filas A, B, C con 5 asientos cada una).
    for fila in "ABC":
        for num in range(1, 6):
            try:
                sala.agregar_asiento(num, fila)
            except:
                pass

# Bucle principal para interactuar con el usuario repetir hasta seleccionar una opcion del 1 al 4
    while True:          
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\nEstado actual de los asientos:")
            for asiento in sala.mostrar_asientos():
                print(asiento)

        elif opcion == "2":
            try:
                fila = input("Ingrese la fila del asiento: ").upper()
                numero = int(input("Ingrese el número del asiento: "))
                dia = input("Ingrese el día (por ejemplo, lunes, miércoles, etc.): ").lower()
                edad = int(input("Ingrese la edad del espectador: "))
                sala.reservar_asiento(numero, fila, dia, edad)
                print(f"\n¡Asiento {fila}{numero} reservado con éxito!")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "3":
            try:
                fila = input("Ingrese la fila del asiento: ").upper()
                numero = int(input("Ingrese el número del asiento: "))
                sala.cancelar_reserva(numero, fila)
                print(f"\nReserva del asiento {fila}{numero} cancelada con éxito.")
            except Exception as e:
                print(f"\nError: {e}")

        elif opcion == "4":
            print("¡Gracias por usar el sistema de reservas de cine!")
            break

        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
