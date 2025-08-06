import datetime
import math
from bicicleta import Bicicleta
class Reserva:
    def __init__(self, id, fecha, hora_inicio, hora_fin=None, precio=None, bicicleta=None):
        self.id = id
        self.fecha = fecha
        self.precio = precio
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.__bicicleta = bicicleta
        self.estado = "pendiente"  # pendiente, activa, terminada, cancelada
        self.precio_por_minuto = 50

    def reservar(self):
        self.estado = "activa"
        print(f"Tu reserva {self.id} está activa")
        if self.__bicicleta and hasattr(self.__bicicleta, 'disponible'):
            self.__bicicleta.disponible = False

    def empezar_viaje(self):
        self.hora_inicio = datetime.datetime.now()
        print(f"Viaje iniciado a las {self.hora_inicio.strftime('%H:%M:%S')}")

    def terminar_viaje(self):
        self.hora_fin = datetime.datetime.now()
        self.estado = "terminada"
        
        print(f"Viaje terminado a las {self.hora_fin.strftime('%H:%M:%S')}")

    def calcular_precio(self):

        duracion = self.hora_fin - self.hora_inicio
        minutos_totales = duracion.total_seconds() / 60
        
        # Redondear hacia arriba (siempre cobrar minuto completo)

        minutos_cobrados = math.ceil(minutos_totales)
        
        self.precio = minutos_cobrados * self.precio_por_minuto
        
        print(f"Duración del viaje: {minutos_totales:.2f} minutos")
        print(f"Precio calculado: ${self.precio}")
        
        return self.precio


    def pagar(self):
        # Pagar la reserva
        print(f"Pagar reserva {self.id} por ${self.precio}")
        pass

    def cancelar_reserva(self):
        self.estado = "cancelado"
        print(f"Reserva {self.id} cancelada")
        pass



