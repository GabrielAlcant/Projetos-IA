# Busca Gulosa e Busca A* em um Grafo

Este é um programa em Python que implementa as estratégias de busca gulosa pela melhor escolha e busca A* em um grafo. Ele permite encontrar o caminho de um vértice de origem a um vértice de destino, levando em consideração os valores dos vértices e os pesos das arestas.

## Funcionalidades

- Adicionar vértices ao grafo, especificando o valor heurístico para cada vértice.
- Adicionar arestas ao grafo, definindo o vértice de origem, vértice de destino e peso da aresta.
- Realizar busca gulosa pela melhor escolha, encontrando o caminho mais promissor em termos do valor heurístico dos vértices.
- Realizar busca A*, levando em consideração o valor heurístico dos vértices e o custo acumulado ao longo do caminho.

## Como usar

1. Clone o repositório para o seu ambiente local.
2. Execute o programa Python usando o comando `python **busca_grafo.py**`.
3. Siga as instruções apresentadas no terminal para adicionar vértices, arestas e realizar as buscas.
4. Insira a opção "0" para sair do programa.

## Exemplo de Uso

Aqui está um exemplo de como utilizar o programa:

1 - Adicionar vértice
2 - Adicionar aresta
3 - Realizar busca gulosa pela melhor escolha
4 - Realizar busca A*
0 - Sair

Escolha uma opção: 1
Nome do vértice: s
Valor heurístico: 7
Vértice adicionado.

Escolha uma opção: 1
Nome do vértice: t
Valor heurístico: 0
Vértice adicionado.

Escolha uma opção: 2
Vértice de origem: s
Vértice de destino: a
Peso da aresta: 2
Aresta adicionada.

Escolha uma opção: 2
Vértice de origem: a
Vértice de destino: t
Peso da aresta: 3
Aresta adicionada.

Escolha uma opção: 3
Vértice de origem: s
Vértice de destino: t
Caminho encontrado: s -> a -> t

Escolha uma opção: 4
Vértice de origem: s
Vértice de destino: t
Caminho encontrado: s -> a -> t

Escolha uma opção: 0
## Requisitos

- Python 3.x
- Biblioteca `queue` (já incluída na biblioteca padrão do Python)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorias no código ou nas funcionalidades.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).