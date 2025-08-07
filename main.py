from bicicleta import Bicicleta
from reserva import Reserva

# Crear bicicletas
bicicleta1 = Bicicleta(1, "Bicicleta 1", "Modelo 1", True, 1000)
bicicleta2 = Bicicleta(2, "Bicicleta 2", "Modelo 2", False, 2000)
bicicleta3 = Bicicleta(3, "Bicicleta 3", "Modelo 3", True, 0)  # Esto dará error internamente

# Crear reservas
reserva1 = Reserva(1, "06/08/2025", "10:00", "12:00", bicicleta1)
reserva2 = Reserva(2, "07/08/2025", "14:00", "16:00", bicicleta2)
reserva3 = Reserva(3, "07/08/2025", "10:00", "16:00", bicicleta3)

def main():
    print("Bienvenido al sistema de reservas de BIKECITY")
    print("\n")
    
    # Reserva 1
    print("Reserva 1:\n")
    bicicleta1.registrar()
    bicicleta1.mostrar_info()
    reserva1.reservar()
    reserva1.empezar_viaje()
    reserva1.terminar_viaje()
    reserva1.pagar()

    # Reserva 2
    print("\n")
    print("Reserva 2:\n")
    bicicleta2.registrar()
    bicicleta2.mostrar_info()
    reserva2.reservar()
    reserva2.empezar_viaje()
    reserva2.terminar_viaje()
    reserva2.pagar()

    # Reserva 3 
    print("\n")
    print("Reserva 3:\n")
    bicicleta3.registrar()
    bicicleta3.mostrar_info()
    reserva3.reservar()
    reserva3.empezar_viaje()
    reserva3.terminar_viaje()
    reserva3.pagar()
    reserva3.cancelar_reserva()

if __name__ == "__main__":
    main()