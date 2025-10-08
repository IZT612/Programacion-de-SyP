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

    

