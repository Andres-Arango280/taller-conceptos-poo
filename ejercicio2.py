# 2.Cree una clase Punto que represente un punto en el plano cartesiano.


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def obtener_coordenadas(self):
        return self.x, self.y
    
    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx**2 + dy**2)**0.5


punto1 = Punto(2, 3)
punto2 = Punto(5, 7)


coordenadas_punto1 = punto1.obtener_coordenadas()
coordenadas_punto2 = punto2.obtener_coordenadas()
print("Coordenadas punto 1:", coordenadas_punto1)
print("Coordenadas punto 2:", coordenadas_punto2)

distancia_entre_puntos = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia_entre_puntos)
