from bicicleta import Bicicleta

class ViajeYaIniciadoError(Exception):
    pass

class BicicletaInvalidaError(Exception):
    pass

class Reserva:
    def __init__(self, id, fecha, hora_inicio, hora_fin, bicicleta=None, estado=None):
        self.id = id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.__bicicleta = bicicleta
        self.estado = estado
        self.valida = True  # Flag para indicar si la reserva es válida
        
        # Validar la bicicleta internamente
        self._validar_bicicleta()

    def _validar_bicicleta(self):
        """Método privado para validar la bicicleta"""
        try:
            if self.__bicicleta is None:
                raise BicicletaInvalidaError("No se puede crear una reserva sin bicicleta")
            elif not self.__bicicleta.es_valida():
                raise BicicletaInvalidaError("No se puede crear una reserva con una bicicleta inválida")
        except BicicletaInvalidaError as e:
            print(f"Error al crear la reserva {self.id}: {e}")
            self.valida = False
            self.estado = "error"

    def reservar(self):
        if not self.valida:
            print(f"No se puede procesar la reserva {self.id}: reserva inválida")
            return self
            
        try:
            if self.estado == "activa":
                raise ViajeYaIniciadoError("El viaje ya ha sido iniciado")
            else:
                self.estado = "pendiente"
                print(f"Has hecho una reserva con ID {self.id}")
        except ViajeYaIniciadoError as e:
            print(f"Error en reserva {self.id}: {e}")
        
        return self

    def empezar_viaje(self):
        if not self.valida:
            print(f"No se puede iniciar el viaje {self.id}: reserva inválida")
            return self
            
        self.estado = "activa"
        print(f"Viaje iniciado a las {self.hora_inicio}")
        return self

    def terminar_viaje(self):
        if not self.valida:
            print(f"No se puede terminar el viaje {self.id}: reserva inválida")
            return self
            
        self.estado = "terminada"
        print(f"Viaje terminado a las {self.hora_fin}")
        return self

    def pagar(self):
        if not self.valida:
            print(f"No se puede procesar el pago {self.id}: reserva inválida")
            return self
            
        precio = self.__bicicleta.precio
        print(f"Pagar reserva {self.id} por ${precio}")
        return self

    def cancelar_reserva(self):
        self.estado = "cancelada"
        print(f"Reserva {self.id} cancelada")
        return self

    def get_bicicleta(self):
        return self.__bicicleta

    def set_bicicleta(self, bicicleta):
        if isinstance(bicicleta, Bicicleta):
            self.__bicicleta = bicicleta
            self._validar_bicicleta()  # Re-validar cuando se cambia la bicicleta
        else:
            print("Error: El objeto no es una instancia de Bicicleta")
            
    def es_valida(self):
        """Método para verificar si la reserva es válida"""
        return self.valida