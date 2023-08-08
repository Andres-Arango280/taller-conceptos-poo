#8.Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("123456789", ["Juan", "María"], 5000.00)

# Mostrar los atributos de la cuenta
print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Balance:", cuenta.balance)
