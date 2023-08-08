#6. Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.


class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Definir las constantes para las pintas
PIKES = "Picas"
HEARTS = "Corazones"
DIAMONDS = "Diamantes"
CLUBS = "Tréboles"

# Crear instancias de la clase Carta con diferentes valores y pintas
carta1 = Carta("As", PIKES)
carta2 = Carta("10", HEARTS)
carta3 = Carta("Reina", DIAMONDS)
carta4 = Carta("7", CLUBS)

# Mostrar las propiedades de las cartas
print(f"Carta 1: Valor = {carta1.valor}, Pinta = {carta1.pinta}")
print(f"Carta 2: Valor = {carta2.valor}, Pinta = {carta2.pinta}")
print(f"Carta 3: Valor = {carta3.valor}, Pinta = {carta3.pinta}")
print(f"Carta 4: Valor = {carta4.valor}, Pinta = {carta4.pinta}")
