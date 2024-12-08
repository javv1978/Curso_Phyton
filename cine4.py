

# Entrega del Caso Práctico Final Curso Python Autoestudio 2da Edición 24
# Sistema de Reservas para un Cine con Tarifas Especiales 

# # Descripción: Desarrolla una aplicación en Python para gestionar las reservas de asientos 
# en una sala de cine, incluyendo un sistema de precios con descuentos en ciertos días y tarifas
#  reducidas para personas mayores. 



class Asiento:
    def __init__(self, numero, fila, precio_base):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = precio_base

    # Getters y Setters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def is_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def reservar(self, precio):
        if self.__reservado:
            raise Exception(f"El asiento {self.__fila}{self.__numero} ya está reservado.")
        self.__reservado = True
        self.__precio = precio

    def cancelar_reserva(self):
        if not self.__reservado:
            raise Exception(f"El asiento {self.__fila}{self.__numero} no está reservado.")
        self.__reservado = False
        self.__precio = 0

    def __str__(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__fila}{self.__numero} - {estado} - Precio: ${self.__precio:.2f}"


class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

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
        for asiento in self.__asientos:
            print(asiento)

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        raise Exception(f"Asiento {fila}{numero} no encontrado.")

    def __calcular_precio(self, dia, edad):
        precio = self.__precio_base
        if dia.lower() == "miércoles":
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración inicial
    precio_base = 10.0
    sala = SalaCine(precio_base)

    # Agregar asientos
    sala.agregar_asiento(1, "A")
    sala.agregar_asiento(2, "A")
    sala.agregar_asiento(3, "B")

    # Mostrar asientos
    print("Asientos disponibles:")
    sala.mostrar_asientos()

    # Reservar un asiento
    print("\nReservando asiento A1 para un adulto mayor de 65 años un miércoles:")
    sala.reservar_asiento(1, "A", "miércoles", 70)

    # Mostrar asientos otra vez
    print("\nEstado actual de los asientos:")
    sala.mostrar_asientos()

    # Cancelar reserva
    print("\nCancelando reserva del asiento A1:")
    sala.cancelar_reserva(1, "A")

    # Mostrar asientos otra vez 2
    print("\nEstado actual de los asientos:")
    sala.mostrar_asientos()
