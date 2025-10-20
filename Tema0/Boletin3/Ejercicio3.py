import math

class Punto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def setXY(self, x, y):

        self.x = x
        self.y = y

    def desplaza(self, dx, dy):

        self.x += dx
        self.y += dy

    def distancia(self, punto):

        return (math.sqrt(math.pow((punto.x - self.x), 2) + math.pow((punto.y - self.y), 2)))
    

# Creación de un par de puntos para probar
p1 = Punto(2, 3)
print(p1)
p2 = Punto(5, 7)
print(p2)

# Probando los métodos de la clase
print('Distancia entre ambos:', p1.distancia(p2))
p1.desplaza(1, 1)
print('Punto 1 tras desplazarlo:', p1)
