from classes import ClienteCompleto

def main():
    hilos = [ClienteCompleto(f"Cliente-{i}") for i in range(10)]
    for h in hilos: h.start()
    for h in hilos: h.join()

if __name__ == "__main__":
    main()