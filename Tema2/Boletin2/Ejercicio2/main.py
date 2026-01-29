import random
import multiprocessing

# Función para generar IP aleatoria
def generar_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Proceso 1: Genera 10 direcciones IP aleatorias y las envía al Proceso 2
def proceso_1(queue):
    ips = [generar_ip() for _ in range(10)]
    for ip in ips:
        queue.put(ip)  # Envía la IP a la cola

# Proceso 2: Filtra las IPs para que solo queden las de clases A, B, C
def proceso_2(queue_in, queue_out):
    while not queue_in.empty():
        ip = queue_in.get()
        # Obtener el primer octeto para determinar la clase
        clase = int(ip.split('.')[0])
        if clase < 224:  # Clases A, B, C (primer octeto < 224)
            queue_out.put(ip)

# Proceso 3: Imprime la IP y la clase correspondiente
def proceso_3(queue):
    while not queue.empty():
        ip = queue.get()
        clase = int(ip.split('.')[0])
        if clase < 128:
            print(f"{ip} - Clase A")
        elif clase < 192:
            print(f"{ip} - Clase B")
        else:
            print(f"{ip} - Clase C")

# Función principal que organiza la ejecución de los procesos
def main():
    queue_1_2 = multiprocessing.Queue()  # Cola para enviar IPs entre Proceso 1 y Proceso 2
    queue_2_3 = multiprocessing.Queue()  # Cola para enviar IPs entre Proceso 2 y Proceso 3

    # Creamos y lanzamos los procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(queue_1_2,))
    p2 = multiprocessing.Process(target=proceso_2, args=(queue_1_2, queue_2_3))
    p3 = multiprocessing.Process(target=proceso_3, args=(queue_2_3,))

    p1.start()
    p1.join()  # Esperamos que Proceso 1 termine

    p2.start()
    p2.join()  # Esperamos que Proceso 2 termine

    p3.start()
    p3.join()  # Esperamos que Proceso 3 termine

if __name__ == "__main__":
    main()
