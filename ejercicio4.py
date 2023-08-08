# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, punto1, punto2):
        self.esquina_superior_izquierda = punto1
        self.esquina_inferior_derecha = punto2

    def calcular_perímetro(self):
        ancho = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        alto = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        alto = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.esquina_inferior_derecha.x - self.esquina_superior_izquierda.x)
        alto = abs(self.esquina_inferior_derecha.y - self.esquina_superior_izquierda.y)
        return ancho == alto


punto1 = Punto(2, 3)
punto2 = Punto(6, 5)


rectangulo = Rectángulo(punto1, punto2)


perimetro = rectangulo.calcular_perímetro()
area = rectangulo.calcular_area()
print("Perímetro:", perimetro)
print("Área:", area)


if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
