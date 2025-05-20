# Moeda Viciada - Q-Learning

## Introdução ao Projeto

Este projeto implementa uma versão simplificada do algoritmo Q-Learning para prever os resultados de uma moeda viciada. A moeda tem 60% de chance de cair cara e 40% de chance de cair coroa. O agente aprende qual é a melhor estratégia para maximizar seus acertos.

## Tecnologias Utilizadas

- Python 3.x
- NumPy
- Matplotlib

## Como Funciona

### O Problema da Moeda Viciada

Uma moeda viciada tem probabilidades diferentes para cara e coroa. Neste caso:
- 60% de chance de cair cara
- 40% de chance de cair coroa

A estratégia ótima é sempre escolher "cara", o que levaria a uma taxa de acerto de 60%.

### Q-Learning Simplificado

O algoritmo Q-Learning mantém uma tabela com dois valores:
- Q[0]: Valor esperado de escolher "cara"
- Q[1]: Valor esperado de escolher "coroa"

A cada lançamento:
1. O agente escolhe uma ação (cara ou coroa)
2. A moeda é lançada e o agente recebe recompensa (1 se acertou, 0 se errou)
3. O agente atualiza sua Q-table com base na recompensa
4. A taxa de exploração (epsilon) é reduzida

## Como Executar

```bash
python moeda.py
```

## O Que Você Verá

1. **Treinamento**: O agente treina por 1000 episódios, mostrando progresso a cada 20%
2. **Resultados**: A Q-table final e a melhor ação aprendida
3. **Gráfico**: Taxa de acerto ao longo do tempo
4. **Demonstração**: 5 lançamentos de teste mostrando o agente em ação

## Dicas para Apresentação

### Pontos a Destacar

- **Problema Simples**: A moeda é viciada (60% cara, 40% coroa)
- **Estratégia Ótima**: Sempre escolher "cara" para maximizar acertos
- **Aprendizado**: O agente começa sem conhecimento e aprende a estratégia ótima
- **Gráfico**: Mostra como a taxa de acerto converge para aproximadamente 60%

### Durante a Demonstração

- Explique que o agente escolherá "cara" na maioria das vezes
- Destaque que mesmo a estratégia ótima não garante 100% de acerto
- Mostre como os valores Q indicam a preferência do agente por "cara"

## Conceitos Aplicados

1. **Exploração vs. Exploração**: Balanceado pelo parâmetro epsilon
2. **Atualização da Q-Table**: Aprendizado incremental com base nas recompensas
3. **Convergência**: O agente converge para a estratégia ótima

## Conclusão

Este projeto demonstra como um algoritmo simples de aprendizado por reforço pode descobrir a estratégia ótima para um problema probabilístico. A simplicidade do exemplo permite focar nos conceitos fundamentais do Q-Learning.
