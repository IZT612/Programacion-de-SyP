from classes import Productor, Consumidor

def main():
    p = Productor()
    c = Consumidor()
    
    p.start()
    c.start()
    
    p.join()
    c.join()

if __name__ == "__main__":
    main()