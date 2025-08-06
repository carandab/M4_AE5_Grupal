class Cliente:
    def __init__(self, id, nombre, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"
    
    def hacer_reserva(self):
        pass