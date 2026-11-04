# Usando a heurística baseada na política de acesso FIFO

## Ideia do Algoritmo

Usando uma fila por baixo, desejamos adicionar novas páginas na memória e substituí-las a mesma está cheia. Essa substituição leva em conta a página que está na memória a mais tempo, independentemente do número de ocasiões em que ela foi acessada após entrar pela primeira vez.

O fluxo dele é bem simples. Antes de mais nada, o programa pergunta quanto espaço de memória será reservado para a aplicação do algoritmo. Depois, a primeira página é solicitada e sua inserção é constatada. Seguem várias inserções (e/ou substituições) com o intuito de atender a todos os acessos solicitados, junto da configuração de memória ao longo dessa manipulação. Por fim, o sistema retorna um Hit Rate, que é mais alta quando menos substituições ocorrem, uma vez que a maioria dos dados já se encontram na memória (espaço e quantidade são inimigos aqui).

## Implementação da Estrutura de Dados - Fila

A classe Queue, cuja implementação está descrita abaixo, possui todos os métodos necessários para manipular a memória como uma FILA, ao invés da estrutura de dados padrão usada - array ou vetor.
 
```
class Queue:

        def __init__(self, length):
                self.length = length
                self.items = []

        def is_empty(self):
                return len(self.items) == 0

        def is_full(self):
                return len(self.items) == self.length

        def enqueue(self, element):
                self.items.append(element)

        def dequeue(self):
                if self.is_empty():
                        return IndexError("POP PROIBIDO: não há como remover algo de uma pilha vazia")
                return self.items.pop(0)

        def head(self):
                if self.is_empty():
                        return IndexError("PEEK PROIBIDO: não existe topo em pilha vazia")
                return self.items[0]

        def size(self):
                return len(self.items)

        def __str__(self):
                return f'Fila Atual: {list(self.items)}'
```

A partir do is_full, decidimos entre somente adicionar o novo pedaço de página na memória ou modificá-la para que a page recém acessada tenha espaço suficiente para ser guardada. A carta aqui é simular uma caminhada dos elementos, na qual toda página mais antiga sai pela cabeça (head) e entra pela cauda, evidenciando a política de acesso utilizada.

A seguir você verá os problemas que, por falta de atenção e compreensão a respeito do algoritmo, enfrentei para que a ideia fosse 100% concretizada e bem executada no código.

## Problemas Principais

1. **Ausência de IS_FULL()**:
Na primeira versão da minha implementação, eu havia esquecido de realizar a conferência de espaço e, devido a isso, acabei enfrentando problemas relacionados ao tamanho determinado para a memória (ele era simplesmente ignorado)!

2. **Falta de Verificação sobre "Clones"**:
Ao adicionar programas que já estavam usando a memória, meu fluxo de código ignorava esse fator e seguia remanejando o espaço de uso (como resultado, ele removia um programa e adicionava o mesmo programa logo em seguida, causando um Miss importuno)...

3. **Capacidade da Fila igual a Zero**
Em python, quando a capacidade de uma Queue (maxsize) é igual ou menor a 0, a estrutura de dados passa a não ter limite de tamanho, se comportando como uma fila infinita. No contexto de espaço de memória na disciplina de Sistemas Operacionais, é inadequado que esses valores sejam válidos para as operações de inserção e substituição na memória, ainda mais para o acesso no pior caso, que é O(N), uma vez que podemos adicionar infinitas páginas (porém já sabemos que NÃO existe memória infinita!!).

## Execução

Como resultado, você pode testar esse algoritmo seguindo os passos abaixo:
1. Esteja exatamente no diretório heur-fifo.
2. Digite o comando `python3 fifo-so.py`.
3. Adicione programas para ver como a memória se comporta ao longo do tempo.
4. Para encerrar a execução, não digite nada (deixe o espaço totalmente vazio) e aperte **ENTER**.
