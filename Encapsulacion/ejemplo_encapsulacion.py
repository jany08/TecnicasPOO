class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: ${cantidad}")
        else:
            print("Cantidad inválida para depósito.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(200)
print("Saldo actual:", cuenta.obtener_saldo())
