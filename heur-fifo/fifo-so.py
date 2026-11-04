from queueclass import Queue

VERDE, VERMELHO, RESET = '\033[92m', '\033[91m', '\033[0m'

memory_cap = int(input("What´s your memory capacity? "))

print('\n...')

initial_text = input("Type a new page... \n")
if initial_text is None:
    print("--> Sem Páginas Para Guardar.")

rate = {'miss': 1, 'hit': 0}

q1 = Queue(memory_cap)
q1.enqueue(initial_text)
print(f'{VERMELHO}{q1.__str__()} - MISS{RESET}')

continues = True
while (continues):
    newProcess = input("One more page? ")
    if newProcess:
        if newProcess not in q1.items:
            if q1.is_full():
                q1.dequeue()
            q1.enqueue(newProcess)
            print(f'{VERMELHO}{q1.__str__()} - MISS{RESET}')
            rate['miss'] += 1
        else:
            print(f'{VERDE}{q1.__str__()} - HIT{RESET}')
            rate['hit'] += 1
    else:
        continues = False
        print('...\n')
        
        hits = rate['hit']
        misses = rate['miss']
        hit_rate = hits / (hits + misses)
        print(f"HIT RATE = {hits} / ({hits} + {misses}) = {hit_rate:.2f}")
