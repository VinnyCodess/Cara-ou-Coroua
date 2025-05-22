# Q-Learning para Previsão de Resultados de Moeda Viciada

Este projeto implementa um agente que utiliza o algoritmo de **Q-Learning** para prever os resultados de lançamentos de uma **moeda viciada**. A moeda tem 60% de chance de cair "cara" e 40% de chance de cair "coroa". O objetivo do agente é aprender a escolher a ação (cara ou coroa) que maximize sua taxa de acerto.

## Estrutura do Projeto

O projeto é composto por duas classes principais:

- **MoedaViciada**: Simula os lançamentos da moeda viciada, retornando 1 (acerto) ou 0 (erro) com base na ação do agente e no resultado do lançamento.
- **Agente**: Implementa o algoritmo de Q-Learning, onde a Q-table é atualizada durante o treinamento com base nas recompensas obtidas.

A política do agente é **epsilon-greedy**, ou seja, em alguns casos ele escolhe uma ação aleatoriamente (exploração), enquanto em outros escolhe a melhor ação com base no valor armazenado na Q-table (exploração).

## Como Funciona

1. **Treinamento**: O agente realiza 1000 episódios de treinamento, jogando a moeda e atualizando sua Q-table com base nas recompensas recebidas.
2. **Visualização**: Ao final do treinamento, é gerado um gráfico mostrando a taxa de acerto do agente ao longo do tempo.
3. **Demonstração**: O agente é testado em 5 lançamentos, sempre escolhendo a melhor ação aprendida, e o resultado é exibido.

## Resultados Esperados

- O agente aprende a escolher sempre "cara" como ação, pois é a melhor estratégia para a moeda viciada.
- O gráfico mostra uma tendência de aumento na taxa de acerto ao longo do tempo, à medida que o agente aprende com as experiências.

## Requisitos

- **Python 3.x**
- **Bibliotecas necessárias**:
  - `numpy`
  - `matplotlib`

## Como Rodar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install numpy matplotlib
