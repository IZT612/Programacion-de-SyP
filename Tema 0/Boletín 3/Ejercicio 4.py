class Articulo:

    IVA = 21

    def __init__(self, nombre, precio, cuantos_quedan):

        self.nombre = nombre
        self.precio = precio
        self.cuantos_quedan = cuantos_quedan

    def getPVP(self):

        return (self.precio * (1 + Articulo.IVA / 100))
    
    def getPVPDescuento(self, descuento):

        return (self.precio - (self.precio * (descuento / 100))) * (1 + Articulo.IVA / 100)
    
    def vender(self, cantidad):

        conseguido = False

        if (cantidad <= self.cuantos_quedan):
        
            self.cuantos_quedan -= cantidad
            conseguido = True

        return conseguido

    def almacenar(self, cantidad): 

        conseguido = False

        if (cantidad > 0):

            self.cuantos_quedan += cantidad
            conseguido = True

        return conseguido
    
    def __str__(self):

        return('Nombre: ' + self.nombre + ' | Precio: ' + str(self.precio) + ' | Cantidad restante: ' + str(self.cuantos_quedan))
    
    def __eq__(self, articulo2):

        return(self.nombre == articulo2.nombre)
    
    def __lt__(self, articulo2):

        return(self.nombre < articulo2.nombre)
    

    # Prueba de la clase Articulo
articulo1 = Articulo("Camiseta", 20, 100)
print(articulo1)

print(articulo1.getPVP())

print(articulo1.getPVPDescuento(10))

print(articulo1.vender(5))
print(articulo1)

print(articulo1.almacenar(20))
print(articulo1)

print(articulo1.vender(150))
print(articulo1)

# Imprimiendo el estado final del artículo
print(articulo1)
    

