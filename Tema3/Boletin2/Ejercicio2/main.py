from classes import ClientePanaderia

def main():

    clientes = [ClientePanaderia(f"Cliente-{i}") for i in range(5)]
    
    for c in clientes: c.start()
    for c in clientes: c.join()

if __name__ == "__main__":
    main()