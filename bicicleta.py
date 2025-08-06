class Bicicleta:
    def __init__(self, id, tipo, cantidad, disponible=None):
        self.id = id
        self.tipo = tipo
        self.cantidad = cantidad
        self.disponible = disponible

    def asignar_cliente(self, cliente):
        self.cliente = cliente