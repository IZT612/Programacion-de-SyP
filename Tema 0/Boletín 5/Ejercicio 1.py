fichero = open('Tema 0/Boletín 5/ficheros/Ejercicio_1f.txt', 'w', encoding='utf8')

personas = [('Juan', 22, 1.77), ('Luis', 21, 1.80), ('Pedro', 20, 1.73)]

for persona in personas:

    fichero.write(persona[0] + ' ' + str(persona[1]) + ' ' + str(persona[2]) + '\n')

fichero.close()

fichero = open('Tema 0/Boletín 5/ficheros/Ejercicio_1f.txt', 'rt')

cantidad = 0

edades = 0
alturas = 0

print('Todos los nombres')
print()

for linea in fichero.readlines():

    print(linea.split(' ')[0])
    cantidad += 1
    edades += int(linea.split(' ')[1])
    alturas += float(linea.split(' ')[2])

fichero.close()

print()
print('La edad media es:', (edades / cantidad))
print('La altura media es:', (alturas / cantidad))