class Producto:

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio

    def __str__(self):

        return(self.nombre + ': ' + str(self.precio) + '€')
    
    def __lt__(self, otroProducto):

        menor = False

        if (self.nombre < otroProducto.nombre):

            menor = True

        return menor

    def calcular(self, cantidad):

        return cantidad * self.precio

class Perecedero(Producto):

    def __init__(self, nombre, precio, dias_caducar):
        super().__init__(nombre, precio)
        self.dias_caducar = dias_caducar

    def calcular(self, cantidad):

        divisor = 1

        if self.dias_caducar == 1:

            divisor = 4

        elif self.dias_caducar == 2:

            divisor = 3

        elif self.dias_caducar == 3:

            divisor = 2

        return (super().calcular(cantidad) / divisor)
    
    def __str__(self):
        return super().__str__() + '. Días para caducar: ' + str(self.dias_caducar) 

class No_Perecedero(Producto):

    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)    
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + '. Tipo: ' + self.tipo
    
# Pruebas de los productos

# Producto No Perecedero
herramienta = No_Perecedero("Martillo", 25, "Herramienta")
print(herramienta)
print("Coste total (3 unidades):", herramienta.calcular(3))
print()

# Producto Perecedero que caduca en 1 día (precio se divide entre 4)
leche = Perecedero("Leche", 10, 1)
print(leche)
print("Coste total (4 unidades):", leche.calcular(4))
print()

# Producto Perecedero que caduca en 2 días (precio se divide entre 3)
yogurt = Perecedero("Yogurt", 6, 2)
print(yogurt)
print("Coste total (5 unidades):", yogurt.calcular(5))
print()

# Producto Perecedero que caduca en 3 días (precio se divide entre 2)
pan = Perecedero("Pan", 4, 3)
print(pan)
print("Coste total (6 unidades):", pan.calcular(6))
print()

# Producto Perecedero que tarda mucho en caducar (no varía el precio)
miel = Perecedero("Miel", 15, 30)
print(miel)
print("Coste total (2 unidades):", miel.calcular(2))