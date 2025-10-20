fichero = open('Tema 0/Boletín 5/ficheros/Ejercicio_3f.txt', 'a', encoding='utf8')

nombre = input('Introduce tu nombre: ')
edad = input('Y ahora introduce tu edad: ')

fichero.write(nombre + ' ' + str(edad) + '\n')

fichero.close()