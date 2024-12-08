class Asiento:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 0

    # Getters y setters
    @property
    def numero(self):
        return self.__numero

    @property
    def fila(self):
        return self.__fila

    @property
    def reservado(self):
        return self.__reservado

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

class SalaCine:
    def __init__(self):
        self.__asientos = []
        self.__precio_base = 10  # Ajustar el precio base según sea necesario

    def agregar_asiento(self, asiento):
        if asiento not in self.__asientos:
            self.__asientos.append(asiento)
        else:
            raise ValueError("Asiento ya existe")

    def reservar_asiento(self, numero, fila, edad, dia):
        asiento = self.buscar_asiento(numero, fila)
        if asiento:
            if not asiento.reservado:
                precio_base = self.__precio_base
                if dia == "miercoles":
                    precio_base *= 0.8
                if edad >= 65:
                    precio_base *= 0.7
                asiento.precio = precio_base
                asiento.reservado = True
            else:
                raise ValueError("Asiento ya está reservado")
        else:
            raise ValueError("Asiento no encontrado")

    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if asiento and asiento.reservado:
            asiento.reservado = False
        else:
            raise ValueError("Asiento no está reservado o no existe")

    def mostrar_asientos(self):
        for asiento in self.__asientos:
            print(f"Asiento {asiento.numero}, Fila {asiento.fila}, Reservado: {asiento.reservado}, Precio: {asiento.precio}")

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None

# Ejemplo de uso
sala = SalaCine()
# Agregar asientos (ejemplo)
sala.agregar_asiento(Asiento(1, 1))
sala.agregar_asiento(Asiento(2, 1))

# Reservar asiento
sala.reservar_asiento(1, 1, 70, "miercoles")

# Mostrar asientos
sala.mostrar_asientos()