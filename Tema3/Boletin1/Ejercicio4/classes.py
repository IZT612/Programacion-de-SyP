import threading

class VocalCounterThread(threading.Thread):
    def __init__(self, vocal, texto):
        super().__init__()
        self.vocal = vocal.lower()
        self.texto = texto.lower()
        self.conteo = 0

    def run(self):
        self.conteo = self.texto.count(self.vocal)
        print(f"La vocal '{self.vocal}' aparece {self.conteo} veces.")