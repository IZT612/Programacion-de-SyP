from multiprocessing import Process, Pipe
from functions import leerFichero, sumarNumeros

if __name__ == '__main__':

    conn_padre, conn_hijo = Pipe()

    p1 = Process(target=leerFichero, args=(conn_hijo,))
    p2 = Process(target=sumarNumeros, args=(conn_padre,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Se han terminado todos los procesos.")
