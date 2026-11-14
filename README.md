# Heurísticas de Substituição de Páginas - Sistemas Operacionais
> Simulação utilizando a linguagem Python para simplificar as operações

## Motivação do Uso de Código
A ideia é acompanhar, passo a passo e de forma interativa, a evolução da memória a cada referência de 
página. Ou seja, descobrir a cada novo acesso:

1. quando ocorre um hit (a página existe na memória)
2. quando ocorre um miss (falta de página - ela não está na memória)
3. qual página é escolhida como vítima.

## Algoritmos Implementados
| Algoritmo | Ideia central | Estado |
|---|---|---|
| FIFO | Remove a página mais antiga | Implementado |
| **Second Chance** | FIFO com bit de referência (R): página antiga com R = 1 ganha uma segunda chance | Implementado |
| LRU | Remove a página menos recentemente usada | Planejado |
| ... | ... | ... |
> Em Breve: a adicionar mais algoritmos!
