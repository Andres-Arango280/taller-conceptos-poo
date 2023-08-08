#5 Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_centro_punto <= self.radio


centro_circulo = Punto(3, 4)


circulo = Circulo(centro_circulo, 5)


area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()
print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)


punto_fuera = Punto(10, 10)


if circulo.punto_pertenece(punto_fuera):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")
