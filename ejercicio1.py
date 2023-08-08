#1. Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


mi_auto = Vehículo(200, 15000)


print("Velocidad máxima:", mi_auto.velocidad_maxima)
print("Kilometraje:", mi_auto.kilometraje)
