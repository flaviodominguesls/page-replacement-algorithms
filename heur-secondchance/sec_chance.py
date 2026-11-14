from queue import Queue
from page import Page

class SecondChance:
    
    def __init__(self, num_frames):
        self.memoria = Queue(num_frames)
        self.misses = 0
        self.hits = 0

    def referenciar(self, number):
        page = self.memoria.search(number)

        if page is not None:
            page.ref_bit = 1
            self.hits += 1
            return None

        self.misses += 1

        removida = None        
        if self.memoria.is_full():
            removida = self.get_vitima()

        self.memoria.enqueue(Page(number))
        return removida

    def get_vitima(self):
        while True:
            candidata = self.memoria.dequeue()

            if candidata.bit_r == 1:
                candidata.bit_r = 0
                self.memoria.enqueue(candidata)
            else:
                return candidata

    def evolucao(self):
        print("Digite o número da página a referenciar (ou 'sair' para encerrar).")
        print(f"Fila: {self.memoria}\n")

        while True:
            novaPag = input("New Page: ").strip()

            misses_before = self.misses
            removida = self.referenciar(novaPag)

            if self.misses == misses_before:
                print(f"  HIT  --> bit R da página [{novaPag}] é igual a 1")
            elif removida is None:
                print(f"  MISS --> a página [{novaPag}] acabou de ser carregada na memória")
            else:
                print(f"  MISS --> página [{removida.numero}] removida, "
                      f"página [{novaPag}] foi carregada")

            print(f"  Fila: {self.memoria}\n")

        print(f"\nMisses: {self.misses} | Acertos: {self.hits}")

if __name__ == "__main__":
    num_frames = int(input("Quant. de frames: "))
    SecondChance(num_frames).evolucao() 
