


#  para mostrar los asientos, realizar reservas y cancelar reservas.
# Ventanas secundarias para introducir datos.

import tkinter as tk
from tkinter import messagebox

# para guardar y cargar el estado de los asientos.ç
import pickle     


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
        return [str(asiento) for asiento in self.__asientos]

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

    def guardar_estado(self, archivo):
        with open(archivo, "wb") as f:
            pickle.dump(self.__asientos, f)

    def cargar_estado(self, archivo):
        try:
            with open(archivo, "rb") as f:
                self.__asientos = pickle.load(f)
        except FileNotFoundError:
            pass  # Si el archivo no existe, no hace nada.


class CineApp:
    def __init__(self, root, sala):
        self.sala = sala
        self.root = root
        self.root.title("Sistema de Reservas de Cine")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.lbl_info = tk.Label(self.frame, text="Bienvenido al Cine")
        self.lbl_info.grid(row=0, column=0, columnspan=2)

        self.btn_mostrar = tk.Button(self.frame, text="Mostrar Asientos", command=self.mostrar_asientos)
        self.btn_mostrar.grid(row=1, column=0, pady=5)

        self.btn_guardar = tk.Button(self.frame, text="Guardar Estado", command=self.guardar_estado)
        self.btn_guardar.grid(row=1, column=1, pady=5)

        self.btn_reservar = tk.Button(self.frame, text="Reservar Asiento", command=self.reservar_asiento)
        self.btn_reservar.grid(row=2, column=0, pady=5)

        self.btn_cancelar = tk.Button(self.frame, text="Cancelar Reserva", command=self.cancelar_reserva)
        self.btn_cancelar.grid(row=2, column=1, pady=5)

    def mostrar_asientos(self):
        asientos = self.sala.mostrar_asientos()
        messagebox.showinfo("Asientos", "\n".join(asientos))

    def guardar_estado(self):
        self.sala.guardar_estado("cine.pkl")
        messagebox.showinfo("Guardar", "Estado guardado exitosamente.")

    def reservar_asiento(self):
        def realizar_reserva():
            try:
                fila = entry_fila.get()
                numero = int(entry_numero.get())
                dia = entry_dia.get()
                edad = int(entry_edad.get())
                self.sala.reservar_asiento(numero, fila, dia, edad)
                messagebox.showinfo("Reservar", f"¡Asiento {fila}{numero} reservado!")
                reserva_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        reserva_win = tk.Toplevel(self.root)
        reserva_win.title("Reservar Asiento")

        tk.Label(reserva_win, text="Fila:").grid(row=0, column=0, padx=5, pady=5)
        entry_fila = tk.Entry(reserva_win)
        entry_fila.grid(row=0, column=1)

        tk.Label(reserva_win, text="Número:").grid(row=1, column=0, padx=5, pady=5)
        entry_numero = tk.Entry(reserva_win)
        entry_numero.grid(row=1, column=1)

        tk.Label(reserva_win, text="Día:").grid(row=2, column=0, padx=5, pady=5)
        entry_dia = tk.Entry(reserva_win)
        entry_dia.grid(row=2, column=1)

        tk.Label(reserva_win, text="Edad:").grid(row=3, column=0, padx=5, pady=5)
        entry_edad = tk.Entry(reserva_win)
        entry_edad.grid(row=3, column=1)

        btn_confirmar = tk.Button(reserva_win, text="Reservar", command=realizar_reserva)
        btn_confirmar.grid(row=4, column=0, columnspan=2, pady=10)

    def cancelar_reserva(self):
        def realizar_cancelacion():
            try:
                fila = entry_fila.get()
                numero = int(entry_numero.get())
                self.sala.cancelar_reserva(numero, fila)
                messagebox.showinfo("Cancelar", f"Reserva del asiento {fila}{numero} cancelada.")
                cancel_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        cancel_win = tk.Toplevel(self.root)
        cancel_win.title("Cancelar Reserva")

        tk.Label(cancel_win, text="Fila:").grid(row=0, column=0, padx=5, pady=5)
        entry_fila = tk.Entry(cancel_win)
        entry_fila.grid(row=0, column=1)

        tk.Label(cancel_win, text="Número:").grid(row=1, column=0, padx=5, pady=5)
        entry_numero = tk.Entry(cancel_win)
        entry_numero.grid(row=1, column=1)

        btn_confirmar = tk.Button(cancel_win, text="Cancelar", command=realizar_cancelacion)
        btn_confirmar.grid(row=2, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    precio_base = 10.0
    sala = SalaCine(precio_base)
    sala.cargar_estado("cine.pkl")

    # Agregar algunos asientos para la prueba
    for fila in "ABC":
        for num in range(1, 6):
            try:
                sala.agregar_asiento(num, fila)
            except:
                pass

    root = tk.Tk()
    app = CineApp(root, sala)
    root.mainloop()
