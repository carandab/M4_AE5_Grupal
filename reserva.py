import datetime
from cliente import Cliente
from bicicleta import Bicicleta
class Reserva:
    def __init__(self, id, fecha, hora, precio:None, bicicleta, cliente):
        self.id = id
        self.fecha = fecha
        self.precio = precio
        self.hora = hora
        self.bicicleta = bicicleta
        self.cliente = cliente

    def asignar_cliente(self):
        pass

    def asignar_bicicleta(self):
        pass

    def empezar_viaje(self):
        pass

    def terminar_viaje(self):
        pass

    def calcular_precio(self):
        pass

    def cancelar_reserva(self):
        pass


