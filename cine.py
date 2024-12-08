


# Sistema de Reservas para un Cine con Tarifas Especiales 

class Asiento:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0.0

    @property
    def numero(self):
        return self.__numero

    @property
    def fila(self):
        return self.__fila

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, estado):
        self.__reservado = estado

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio


class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

    def agregar_asiento(self, numero, fila):
        if not any(a.numero == numero and a.fila == fila for a in self.__asientos):
            self.__asientos.append(Asiento(numero, fila))
        else:
            raise ValueError(f"El asiento {numero}-{fila} ya está registrado.")

    def reservar_asiento(self, numero, fila, dia, edad):
        asiento = self.buscar_asiento(numero, fila)
        if asiento and not asiento.reservado:
            asiento.precio = self.__calcular_precio(dia, edad)
            asiento.reservado = True
        else:
            raise ValueError(f"El asiento {numero}-{fila} no está disponible.")

    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if asiento and asiento.reservado:
            asiento.reservado = False
            asiento.precio = 0.0
        else:
            raise ValueError(f"El asiento {numero}-{fila} no está reservado.")

    def mostrar_asientos(self):
        for asiento in self.__asientos:
            estado = 'Reservado' if asiento.reservado else 'Disponible'
            print(f"Asiento {asiento.numero}-{asiento.fila}: {estado}, Precio: {asiento.precio:.2f}€")

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None

    def __calcular_precio(self, dia, edad):
        precio = self.__precio_base
        if dia.lower() == 'miércoles':
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio


# Ejemplo de uso
cine = SalaCine(precio_base=10.0)
cine.agregar_asiento(1, 'A')
cine.agregar_asiento(2, 'A')
cine.agregar_asiento(3, 'B')

# Reservar y mostrar asientos
cine.reservar_asiento(1, 'A', 'miércoles', 70)
cine.reservar_asiento(2, 'A', 'viernes', 30)
cine.mostrar_asientos()

# Cancelar una reserva
cine.cancelar_reserva(1, 'A')
cine.mostrar_asientos()
