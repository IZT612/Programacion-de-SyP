from classes import Filosofo

def main():
    filosofos = [Filosofo(i) for i in range(5)]
    for f in filosofos: f.start()

    for f in filosofos: f.join()

if __name__ == "__main__":
    main()