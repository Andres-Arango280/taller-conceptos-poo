#9. Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

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


cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.00)

# Realizar retiros
cuenta.retirar(2000)
cuenta.retirar(3500)
cuenta.retirar(10000)
