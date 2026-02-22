import random
from classes import JugadorEscape

def main():
    JugadorEscape.clave_correcta = random.randint(0, 5000)
    print(f"--- Clave secreta: {JugadorEscape.clave_correcta} ---")

    jugadores = [JugadorEscape(f"Jugador-{i}") for i in range(5)]

    for j in jugadores: j.start()
    for j in jugadores: j.join()

    print("¡Equipo completo fuera!")

if __name__ == "__main__":
    main()