class CuentaCorriente:

    def __init__(self, DNI, saldo, nombre = ''):

        self.DNI = DNI
        self.nombre = nombre
        self.saldo = saldo

    def sacar_dinero(self, cantidad):

        conseguido = False

        if (cantidad <= self.saldo and cantidad > 0):

            self.saldo -= cantidad
            conseguido = True

        return conseguido
    
    def ingresar_dinero(self, cantidad):

        conseguido = False

        if (cantidad > 0):

            self.saldo += cantidad
            conseguido = True

        return conseguido

    def __str__(self):

        return 'DNI:', self.DNI, '             Nombre:', self.nombre, '             Saldo:', self.saldo
    
    def __eq__(self, otra_cuenta):

        return self.DNI == otra_cuenta.DNI

    def __lt__(self, otra_cuenta):

        return self.saldo < otra_cuenta.saldo
    
cuenta1 = CuentaCorriente('nolose', 2731, 'Ivan')

print('Veamos el sueldo de mi cuenta:', cuenta1.saldo)

cuenta1.ingresar_dinero(100)

print('Ahora veamos mi dinero tras ingresar 100€:', cuenta1.saldo)

cuenta1.sacar_dinero(50)

print('Ahora veamos el saldo tras quitar 50€:', cuenta1.saldo)

print('Voy a mostrar ahora todos los datos de mi cuenta:\n', cuenta1)

cuenta2 = CuentaCorriente('nolose', 5000)

print('Ahora echemosle un vistazo a esta otra:\n', cuenta2)

print('Veamos si las cuentas son iguales o no:')

print(cuenta1.__eq__(cuenta2))

print('Y por último, veamos si mi cuenta tiene menos dinero que la nueva:')
print(cuenta1.__lt__(cuenta2))