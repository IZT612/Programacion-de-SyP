class Empleado:

    def __init__(self, nombre):

        self.nombre = nombre

    def __str__(self):

        return('Empleado ' + self.nombre)
    

class Directivo(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return (super().__str__() + ' -> Directivo')

class Operario(Empleado):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
       return (super().__str__() + ' -> Operario')
    
class Oficial(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return (super().__str__() + ' -> Oficial')
        
class Tecnico(Operario):

    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return (super().__str__() + ' -> Tecnico') 
    

# Pruebas de las clases

# Empleado
empleado = Empleado("Ana")
print(empleado)

# Directivo
directivo = Directivo("Carlos")
print(directivo)

# Operario
operario = Operario("Luis")
print(operario)

# Oficial
oficial = Oficial("Marta")
print(oficial)

# Tecnico
tecnico = Tecnico("Pedro")
print(tecnico)