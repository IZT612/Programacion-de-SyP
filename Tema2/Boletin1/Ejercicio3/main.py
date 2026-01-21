from multiprocessing import Process, Queue
from functions import leerFichero, sumarNumeros

if __name__ == '__main__':

    cola = Queue()

    p1 = Process(target=leerFichero, args=(cola,))
    p2 = Process(target=sumarNumeros, args=(cola,))

    p1.start()
    p2.start()

    p1.join()

    p2.join()

    print("Se han terminado todos los procesos.")