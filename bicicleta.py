class Bicicleta:
    def init(self, id, marca, modelo, disponible, precio):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.disponible = disponible
        self.precio = precio
        self.valida = True  # Indica si la bicicleta es válida
        self._validar_precio()

    def _validar_precio(self):
        """Método privado para validar el precio"""
        try:
            if self.precio < 1:
                raise ValueError("El precio de la bicicleta no puede ser negativo.")
        except ValueError as e:
            print(f"Error al crear la bicicleta {self.id}: {e}")
            self.valida = False
            self.disponible = False  # Si no es válida, no está disponible
            self.precio = 0

    def mostrar_info(self):
        if not self.valida:
            info = f"Bicicleta {self.id}: INVÁLIDA - Precio incorrecto"
        else:
            info = f"Bicicleta {self.id}: {self.marca} {self.modelo} - ${self.precio}, Disponible: {self.disponible}"

        print(info)
        return info

    def registrar(self):
        if self.valida:
            print("Bicicleta registrada correctamente.")
            return True
        else:
            print(f"No se puede registrar la bicicleta {self.id}: bicicleta inválida.")
            return False

    def es_valida(self):
        """Método para verificar si la bicicleta es válida"""
        return self.valida