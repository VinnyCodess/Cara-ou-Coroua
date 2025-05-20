# -*- coding: utf-8 -*-
"""
Nome do arquivo: moeda.py
Data de criação: 18/05/2025
Autor: Vinícius Gomes de Sousa
Matrícula: 01555769

Descrição:
Implementação simplificada de Q-Learning para aprender a prever resultados 
de uma moeda viciada (60% chance de cara).
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# Ambiente da moeda viciada (60% cara, 40% coroa)
class MoedaViciada:
    def __init__(self, prob_cara=0.6):
        self.prob_cara = prob_cara
    
    def jogar(self, acao):
        # Simula o lançamento da moeda
        resultado = np.random.random() < self.prob_cara  # True=cara, False=coroa
        # Retorna 1 se acertou, 0 se errou
        return 1 if (resultado and acao == 0) or (not resultado and acao == 1) else 0

# Agente Q-Learning
class Agente:
    def __init__(self):
        self.q_table = np.zeros(2)  # [valor_cara, valor_coroa]
        self.epsilon = 1.0          # Taxa de exploração inicial
        self.epsilon_min = 0.01     # Taxa mínima de exploração
        self.epsilon_decay = 0.01   # Taxa de decaimento (aumentada para convergir mais rápido)
        self.alpha = 0.1            # Taxa de aprendizado
        self.recompensas = []       # Histórico de recompensas
    
    def escolher_acao(self):
        # Política epsilon-greedy
        if np.random.random() < self.epsilon:
            return np.random.randint(0, 2)  # Exploração: escolhe aleatoriamente
        return np.argmax(self.q_table)      # Exploração: escolhe a melhor ação
    
    def atualizar(self, acao, recompensa):
        # Atualiza a Q-table
        self.q_table[acao] = (1 - self.alpha) * self.q_table[acao] + self.alpha * recompensa
        # Reduz epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * (1 - self.epsilon_decay))
        # Registra recompensa
        self.recompensas.append(recompensa)

# Função principal
def main():
    # Inicialização
    moeda = MoedaViciada()
    agente = Agente()
    episodios = 1000  # Reduzido para treinamento mais rápido
    
    print("\n=== TREINANDO AGENTE ===")
    print(f"Moeda viciada: 60% chance de cara, 40% chance de coroa")
    print(f"Episódios: {episodios}")
    
    # Treinamento
    for ep in range(episodios):
        acao = agente.escolher_acao()
        recompensa = moeda.jogar(acao)
        agente.atualizar(acao, recompensa)
        
        # Mostrar progresso
        if (ep + 1) % (episodios // 5) == 0:
            print(f"Episódio {ep + 1}/{episodios} | " 
                  f"Epsilon: {agente.epsilon:.2f} | "
                  f"Q-Table: [{agente.q_table[0]:.2f}, {agente.q_table[1]:.2f}]")
    
    # Resultados
    print("\n=== RESULTADOS ===")
    print(f"Q-Table final: [{agente.q_table[0]:.2f}, {agente.q_table[1]:.2f}]")
    melhor_acao = "Cara" if np.argmax(agente.q_table) == 0 else "Coroa"
    print(f"Melhor ação aprendida: {melhor_acao}")
    print(f"Taxa de acerto final: {np.mean(agente.recompensas[-100:]):.0%}")
    
    # Gráfico simples
    plt.figure(figsize=(10, 6))
    plt.plot(np.cumsum(agente.recompensas) / (np.arange(len(agente.recompensas)) + 1))
    plt.title('Taxa de Acerto ao Longo do Tempo')
    plt.xlabel('Tentativas')
    plt.ylabel('Taxa de Acerto')
    plt.grid(True)
    plt.savefig('resultado_moeda.png')
    plt.show()
    
    # Demonstração
    print("\n=== DEMONSTRAÇÃO ===")
    print("Testando o agente treinado em 5 lançamentos:")
    
    acertos = 0
    for i in range(5):
        # Agente sempre escolhe a melhor ação
        acao = np.argmax(agente.q_table)
        acao_nome = "Cara" if acao == 0 else "Coroa"
        
        # Lançar a moeda
        recompensa = moeda.jogar(acao)
        resultado = "Acertou!" if recompensa == 1 else "Errou!"
        acertos += recompensa
        
        # Mostrar resultado
        print(f"Lançamento {i+1}: Agente escolheu {acao_nome} → {resultado}")
        time.sleep(0.5)  # Pausa para visualização
    
    print(f"\nResultado: {acertos} acertos em 5 tentativas ({acertos/5:.0%})")
    print(f"Estratégia aprendida: Sempre escolher {melhor_acao}")

if __name__ == "__main__":
    main()
