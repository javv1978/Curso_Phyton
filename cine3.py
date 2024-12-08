


class Asiento:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio_base = 10  # Ajusta el precio base aquí

    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def esta_reservado(self):
        return self.__reservado

    def reservar(self, dia, edad):
        if self.__reservado:
            raise Exception("Asiento ya reservado")
        self.__reservado = True
        self.__precio = self.__calcular_precio(dia, edad)

    def cancelar_reserva(self):
        if not self.__reservado:
            raise Exception("Asiento no reservado")
        self.__reservado = False

    def __calcular_precio(self, dia, edad):
        precio = self.__precio_base
        if dia.lower() == "miercoles":
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio

class SalaCine:
    def __init__(self):
        self.__asientos = []

    def agregar_asiento(self, asiento):
        if asiento in self.__asientos:
            raise Exception("Asiento ya existe")
        self.__asientos.append(asiento)

    def reservar_asiento(self, numero, fila, dia, edad):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                asiento.reservar(dia, edad)
                return
        raise Exception("Asiento no encontrado")

    def cancelar_reserva(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                asiento.cancelar_reserva()
                return
        raise Exception("Asiento no encontrado")

    def mostrar_asientos(self):
        for asiento in self.__asientos:
            print(f"Asiento {asiento.get_numero()}-{asiento.get_fila()}: {'Reservado' if asiento.esta_reservado() else 'Disponible'} - Precio: ${asiento.__precio:.2f}")

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

# Ejemplo de uso:
sala = SalaCine()
asiento1 = Asiento(1, 'A')
sala.agregar_asiento(asiento1)

sala.reservar_asiento(1, 'A', "miercoles", 70)
sala.mostrar_asientos() 