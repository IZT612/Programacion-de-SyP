class Libro:

    def __init__(self, titulo, autor, numero_total, numero_prestados):

        self.titulo = titulo
        self.autor = autor
        self.numero_total = numero_total
        self.numero_prestados = numero_prestados

    def prestamo(self):

        conseguido = False

        if (self.numero_total - self.numero_prestados > 0):

            self.numero_prestados += 1
            conseguido = True


        return conseguido
    
    def devolucion(self):

        conseguido = False

        if (self.numero_prestados > 0):

            self.numero_prestados -= 1
            conseguido = True

        return conseguido
    
    def __str__(self):

        return 'Título: ' + self.titulo + ' | Autor: '+ self.autor + ' | Número de ejemplares en total: ' + str(self.numero_total) + ' | Número de ejemplares prestados: ' + str(self.numero_prestados)
    
    def __eq__(self, otro_libro):

        return self.titulo == otro_libro.titulo and self.autor == otro_libro.autor
    
    def __lt__(self, otro_libro):

        return self.autor < otro_libro.autor


libro1 = Libro('Mi primer libro', 'Ivan', 3, 0)
print(libro1)

if (libro1.devolucion()):

    print('Esto no deberia ocurrir porque no hay prestados')

else:

    print('No hay libros para devolver.')

libro1.prestamo()
libro1.prestamo()
libro1.prestamo()

if (libro1.prestamo()):

    print('Esto no deberia ocurrir porque se ha alcanzado el maximo')

else:

    print('No quedan libros para prestar')

if (libro1.devolucion()):

    print('Se pudo devolver')

else: 

    print('Se debería haber podido devolver...')