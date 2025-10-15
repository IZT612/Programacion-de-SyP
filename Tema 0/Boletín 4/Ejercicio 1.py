class Animal:

    def __init__(self, nombre, numero_patas):

        self.nombre = nombre
        self.numero_patas = numero_patas

    def habla(self):

        return('')
    
    def __str__(self):

        return ('Me llamo ' + self.nombre + ', tengo ' + str(self.numero_patas) + ' patas y sueno así: ' + self.habla())
    

class Gato(Animal):

    def __init__(self, nombre, numero_patas):

        super().__init__(nombre, numero_patas)

    def habla(self):

        return('Miau')  

    def __str__(self):

        return('Soy un gato. ' + super().__str__())

class Perro(Animal):

    def __init__(self, nombre, numero_patas):

        super().__init__(nombre, numero_patas)

    def habla(self):

        return('Guau')

    def __str__(self):

        return('Soy un perro. ' + super().__str__())

# Pruebas

gato = Gato('Michi', 4)
print(gato)
print(gato.habla())

print()
perro = Perro('Firulais', 4)
print(perro)
print(perro.habla())

