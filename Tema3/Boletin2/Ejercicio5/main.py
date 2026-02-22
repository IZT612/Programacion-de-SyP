from classes import Estudiante

def main():
    estudiantes = [Estudiante(f"Estudiante-{i}") for i in range(4)]
    for e in estudiantes: e.start()
    for e in estudiantes: e.join()

if __name__ == "__main__":
    main()