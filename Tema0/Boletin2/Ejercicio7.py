contactos = {}

menu = 'Escoja una de las siguientes opciones: \n 1. Añadir contacto. \n 2. Eliminar contacto. \n 3. Modificar contacto. \n 4. Buscar contacto. \n 5. Mostrar contactos. \n Otro Nº. Finalizar programa. \n \n'

def añadir_contacto(contacto, numero):

    conseguido = False

    if contactos.get(contacto) == None:

        contactos[contacto] = numero

        conseguido = True

    return conseguido

def eliminar_contacto(contacto):

    conseguido = False

    if contactos.get(contacto) != None:

        contactos.pop(contacto)

        conseguido = True

    return conseguido
    
def modificar_contacto(contacto, nuevo_numero):

    conseguido = False

    if contactos.get(contacto) != None:

        contactos[contacto] = nuevo_numero

        conseguido = True

    return conseguido

def buscar_contacto(contacto):

    numero = -1

    if contactos.get(contacto) != None:

        numero = contactos[contacto]

    return numero

def mostrar_contactos():
    
    contactos_str = ''

    for contacto in contactos:

        contactos_str += contacto + ' ' + str((contactos[contacto])) + '\n'

    return contactos_str
    
opcion = int(input(menu))

while (opcion <= 5 and opcion >= 1):

    if(opcion == 1):

        if (añadir_contacto(input('Introduce el nombre del contacto a añadir: '), int(input('Ahora, introduzca su número: ')))):

            print('Se ha añadido correctamente.')

        else:

            print('Ya existe un contacto con ese nombre, no se ha podido añadir.')

    elif(opcion == 2):

        if (eliminar_contacto(input('Introduce el nombre del contacto a eliminar: '))):

            print('Se ha eliminado correctamente.')

        else:

            print('No se ha encontrado ese contacto.')

    elif(opcion == 3):

        if (modificar_contacto(input('Introduzca el nombre del contacto a modificar: '), int(input('Ahora el nuevo número que le quiere dar: ')))): 

            print('Se ha modificado correctamente.')

        else:

            print('No se ha encontrado el contacto.')

    elif(opcion == 4):

        numero = buscar_contacto(input('Introduzca el contacto que desea buscar: '))

        if (numero > 0):

            print('El número es', numero)

        else:

            print('No se ha podido encontrar el contacto.')

    elif(opcion == 5):

        print(mostrar_contactos())

    opcion = int(input(menu))


print('Programa finalizado')