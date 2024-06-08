import threading
import time
import queue


class Coordenador:
    def __init__(self):
        self.lock = threading.Lock()
        self.fila = queue.Queue()

    def requisitar_acesso(self, processo_id):
        with self.lock:
            self.fila.put(processo_id)
            while self.fila.queue[0] != processo_id:
                self.lock.release()
                self.lock.acquire()
            print(f"Processo {processo_id} entrou na seção crítica")

    def liberar_acesso(self):
        with self.lock:
            processo_id = self.fila.get()
            print(f"Processo {processo_id} saiu da seção crítica")


coordenador = Coordenador()


def processo(processo_id):
    coordenador.requisitar_acesso(processo_id)
    time.sleep(1)
    coordenador.liberar_acesso()


if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=processo, args=(i + 1,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
