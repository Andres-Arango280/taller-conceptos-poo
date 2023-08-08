# 11.Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def retirar(self, monto):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            print(f"Se ha retirado {monto:.2f} unidades. Nuevo balance: {self.balance:.2f}")
        else:
            print("No es posible realizar el retiro.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado una cuota de manejo del 2% ({cuota:.2f} unidades). Nuevo balance: {self.balance:.2f}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", ", ".join(self.propietarios))
        print("Balance:", self.balance)

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.00)

# Mostrar detalles de la cuenta 
cuenta.mostrar_detalles()
