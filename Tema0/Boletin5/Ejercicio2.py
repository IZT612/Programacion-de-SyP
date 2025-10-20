fichero = open('Tema 0/Boletín 5/ficheros/Ejercicio_2f.txt', 'w', encoding='utf8')

linea_usuario = input('Introduzca una linea que introducir al fichero: ')

while linea_usuario != 'fin':

    fichero.write(linea_usuario + '\n')

    linea_usuario = input('Introduzca una linea que introducir al fichero: ')

fichero.close()

print('Saliendo del programa')