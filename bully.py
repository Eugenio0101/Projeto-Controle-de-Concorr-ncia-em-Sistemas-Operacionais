import threading
import time
import random


class Processo:
    def __init__(self, processo_id, coord=False):
        self.processo_id = processo_id
        self.coordenador = coord
        self.ativo = True

    def iniciar_eleicao(self, processos):
        print(f"Processo {self.processo_id} iniciou uma eleição")
        candidatos = [p for p in processos if p.processo_id >
                      self.processo_id and p.ativo]
        if not candidatos:
            self.coordenador = True
            print(f"Processo {self.processo_id} foi eleito como coordenador")
        else:
            vencedor = max(candidatos, key=lambda p: p.processo_id)
            vencedor.iniciar_eleicao(processos)


def simular_processos():
    processos = [Processo(i) for i in range(1, 6)]
    coordenador_inicial = random.choice(processos)
    coordenador_inicial.coordenador = True
    print(f"Processo {
          coordenador_inicial.processo_id} é o coordenador inicial")

    time.sleep(2)
    coordenador_inicial.ativo = False
    print(f"Processo {coordenador_inicial.processo_id} falhou")

    for p in processos:
        if p.ativo:
            p.iniciar_eleicao(processos)
            p.iniciar_eleicao(processos)
            p.iniciar_eleicao(processos)
            break


if __name__ == "__main__":
    simular_processos()
