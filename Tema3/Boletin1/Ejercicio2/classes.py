import threading

class CounterThread(threading.Thread):

    cuenta = 0
    lock = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.name = nombre

    def run(self):
        while True:
            with CounterThread.lock:
                if CounterThread.cuenta < 1000:
                    CounterThread.cuenta += 1
                    print(f"Hilo {self.name} aumenta la cuenta a {CounterThread.cuenta}")
                else:
                    break