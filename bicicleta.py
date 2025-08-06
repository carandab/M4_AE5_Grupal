class Bicicleta:
    def __init__(self, id, marca, modelo, disponible, precio):
        try:
            if precio < 0:
                raise ValueError("El precio de la bicicleta no puede ser negativo.")

            self.id = id
            self.marca = marca
            self.modelo = modelo
            self.disponible = disponible
            self.precio = precio

        except ValueError as e:
            print(f"Error al crear la bicicleta: {e}")
            raise  

    def mostrar_info(self):
        return f"Bicicleta {self.id}: {self.marca} {self.modelo} - ${self.precio}, Disponible: {self.disponible}"

    def registrar(self):
        print("Bicicleta registrada correctamente.")

