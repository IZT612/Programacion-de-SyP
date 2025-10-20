productos = {}

menu = 'Escoja una de las siguientes opciones: \n 1. Añadir producto. \n 2. Buscar ventas de un producto. \n 3. Sumar ventas a producto. \n 4. Eliminar producto. \n 5. Mostrar productos. \n Otro Nº: Salir del programa. \n \n'

def añadir_producto(producto):

    conseguido = False

    if (productos.get(producto) == None):

        productos[producto] = 0

        conseguido = True

    return conseguido

def buscar_ventas(producto):

    ventas = -1

    if (productos.get(producto)) != None:

        ventas = productos[producto]

    return ventas

def sumar_ventas(producto, ventas_mas):

    conseguido = False

    if (productos.get(producto) != None):

        productos[producto] += ventas_mas

        conseguido = True

    return conseguido

def eliminar_producto(producto):

    conseguido = False

    if (productos.get(producto) != None):

        productos.pop(producto)

        conseguido = True

    return conseguido

def mostrar_productos():

    productos_str = ''

    for producto in productos:

        productos_str += producto + ': ' + str(productos[producto]) + '\n'

    return productos_str

opcion = int(input(menu))

while (opcion >= 1 and opcion <= 5):

    if (opcion == 1):

        if(añadir_producto(input('Introduzca el nombre del producto a añadir: '))):

            print('Producto añadido correctamente.')

        else:

            print('Ya existe un producto con ese nombre.')

    elif (opcion == 2): 

        ventas = buscar_ventas(input('Introduzca el nombre del producto a buscar: '))

        if (ventas >= 0):

            print('El producto tiene', ventas, 'ventas.')

        else:

            print('No se ha podido encontrar el producto.')
    
    elif (opcion == 3):

        if(sumar_ventas(input('Introduzca el nombre del producto: '), int(input('Introduzca ahora la cantidad de ventas a sumar: ')))):

            print('Se han añadido las ventas correctamente.')

        else:

            print('No se ha encontrado el producto.')

    elif (opcion == 4): 

        if (eliminar_producto(input('Introduzca el nombre del producto a eliminar: '))):

            print('Se ha eliminado correctamente.')
        
        else:

            print('No se ha encontrado el producto.')

    elif (opcion == 5): 

        print(mostrar_productos())

    opcion = int(input(menu))

print('Programa finalizado.')

