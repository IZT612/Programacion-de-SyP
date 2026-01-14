import time

def sumarNumeros(numeroLimite):
    
    inicio = time.perf_counter()

    numeroInicial = 1

    resultado = 0

    while(numeroInicial != numeroLimite + 1):

        resultado += numeroInicial

        numeroInicial += 1

    fin = time.perf_counter()

    tiempo_total = fin - inicio

    print("Resultado:", resultado, ". Con un tiempo de:", tiempo_total, "segundos")