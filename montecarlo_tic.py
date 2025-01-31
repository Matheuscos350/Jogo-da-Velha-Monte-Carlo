# -*- coding: utf-8 -*-
"""MONTECARLO-TIC

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ha3za7iZltaYcuIuLSfOYvGiVg18pWdE

# ***Você deve criar um jogo da Velha (Tic-Tac-Toe) (computador versus computador).***
Realizar a simulação de 1000 partidas, verificando qual jogador venceu mais vezes.
"""

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Verifica linhas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Verifica colunas
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def computer_move(board, player):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]

    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        print(f"Jogador atual: {current_player}")
        if current_player == 'X':
            row, col = computer_move(board, current_player)
        else:
            row, col = computer_move(board, current_player)
        board[row][col] = current_player
        current_player = 'X' if current_player == 'O' else 'O'

    print_board(board)
    if check_winner(board):
        print(f"O jogador {current_player} venceu!")
        return current_player
    else:
        print("Empate!")
        return None

def simulate_games(num_games):
    results = {'X': 0, 'O': 0, 'Empate': 0}
    for _ in range(num_games):
        winner = play_game()
        if winner:
            results[winner] += 1
        else:
            results['Empate'] += 1
    return results

if __name__ == "__main__":
    num_games = 1000
    results = simulate_games(num_games)
    print("Resultados da simulação sem SMC:")
    print(results)

"""## *Implementar SMC (Simulação Monte Carlo) no jogo anterior e realizar a mesma verificação*
Por fim, fazer uma comparação para verificar qual algoritmo tem maior eficiência.


"""

import random
import copy

def print_board(board):
    # Função para imprimir o tabuleiro formatado
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Função para verificar se algum jogador venceu
    # Verifica linhas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Verifica colunas
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    # Função para verificar se o tabuleiro está cheio (empate)
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    # Função para obter as células vazias do tabuleiro
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def computer_move(board, player):
    # Função para realizar a jogada do computador aleatoriamente
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def monte_carlo_simulation(board, player, num_simulations=100):
    # Função para simulação Monte Carlo para determinar a melhor jogada
    wins = 0
    for _ in range(num_simulations):
        temp_board = copy.deepcopy(board)  # Cria uma cópia do tabuleiro atual
        temp_player = player
        while not check_winner(temp_board) and not is_board_full(temp_board):
            # Enquanto o jogo não acabar, realiza jogadas aleatórias
            row, col = random.choice(get_empty_cells(temp_board))
            temp_board[row][col] = temp_player
            temp_player = 'X' if temp_player == 'O' else 'O'
        # Se o jogador atual venceu, incrementa o contador de vitórias
        if check_winner(temp_board) and temp_player == player:
            wins += 1
    return wins

def computer_move_monte_carlo(board, player, num_simulations=100):
    # Função para a jogada do computador usando o algoritmo Monte Carlo
    empty_cells = get_empty_cells(board)
    best_move = None
    best_score = -1
    for cell in empty_cells:
        row, col = cell
        temp_board = copy.deepcopy(board)  # Cria uma cópia do tabuleiro atual
        temp_board[row][col] = player  # Faz a jogada em uma célula vazia
        # Calcula o número de vitórias simuladas para essa jogada
        score = monte_carlo_simulation(temp_board, player, num_simulations)
        # Atualiza a melhor jogada com base no número de vitórias simuladas
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

def play_game():
    # Função principal para jogar uma partida
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Cria o tabuleiro vazio
    players = ['X', 'O']
    random.shuffle(players)  # Escolhe aleatoriamente quem começa o jogo
    current_player = players[0]

    while not check_winner(board) and not is_board_full(board):
        # Enquanto o jogo não acabar, continua jogando
        print_board(board)
        print(f"Jogador atual: {current_player}")
        if current_player == 'X':
            row, col = computer_move(board, current_player)
        else:
            row, col = computer_move_monte_carlo(board, current_player)
        board[row][col] = current_player
        current_player = 'X' if current_player == 'O' else 'O'

    print_board(board)
    if check_winner(board):
        print(f"O jogador {current_player} venceu!")
        return current_player
    else:
        print("Empate!")
        return None

def simulate_games(num_games):
    # Função para simular múltiplos jogos e contar os resultados
    results = {'X': 0, 'O': 0, 'Empate': 0}
    for _ in range(num_games):
        winner = play_game()
        if winner:
            results[winner] += 1
        else:
            results['Empate'] += 1
    return results

if __name__ == "__main__":
    num_games = 1000
    results = simulate_games(num_games)
    print("Resultados da simulação sem SMC:")
    print(results)

"""# ***Simulando ambos os códigos para mostrar qual tem o melhor resultado.***"""

num_games = 1000

# Simulação com o primeiro algoritmo (jogadas aleatórias)
results_random = simulate_games(num_games)

# Simulação com o segundo algoritmo (Monte Carlo)
results_monte_carlo = simulate_games(num_games)

print("Resultados da simulação com jogadas aleatórias:")
print(results_random)

print("\nResultados da simulação com Monte Carlo:")
print(results_monte_carlo)

"""# ***Sugestão do Professor para melhoria***
# **Adicionar um grafico de linha de tendencia mostrando se X venceu quantas vezes seguidas ou quantos O venceu seguidas X X X O O X X**
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def simulate_games(num_games):
    # Simulação de resultados aleatórios (exemplo)
    return [random.choice(['X', 'O', 'Empate']) for _ in range(num_games)]

def count_consecutive_wins(results):
    x_streak = 0
    o_streak = 0
    x_streaks = []
    o_streaks = []

    for result in results:
        if result == 'X':
            x_streak += 1
            o_streak = 0
        elif result == 'O':
            o_streak += 1
            x_streak = 0
        else:  # Empate
            x_streak = 0
            o_streak = 0
        x_streaks.append(x_streak)
        o_streaks.append(o_streak)

    return x_streaks, o_streaks

def plot_scatter_streaks(x_streaks, o_streaks):
    games = range(len(x_streaks))

    plt.figure(figsize=(14, 7))
    plt.scatter(games, x_streaks, label='Vitórias consecutivas de X', c='blue')
    plt.scatter(games, o_streaks, label='Vitórias consecutivas de O', c='red')

    # Adicionando a linha de tendência para X
    z_X = np.polyfit(games, x_streaks, 1)
    p_X = np.poly1d(z_X)
    plt.plot(games, p_X(games), color='blue', linestyle='dashed')

    # Adicionando a linha de tendência para O
    z_O = np.polyfit(games, o_streaks, 1)
    p_O = np.poly1d(z_O)
    plt.plot(games, p_O(games), color='red', linestyle='dashed')

    plt.xlabel('Número do Jogo')
    plt.ylabel('Vitórias Consecutivas')
    plt.title('Tendência de Vitórias Consecutivas de X e O')
    plt.legend()
    plt.show()

# Número de jogos a simular
num_games = 1000
# Simulação com jogadas aleatórias
results_random = simulate_games(num_games)

# Contar vitórias consecutivas
x_streaks_random, o_streaks_random = count_consecutive_wins(results_random)

# Plotar os resultados da simulação aleatória
print("Resultados da simulação com jogadas aleatórias:")
print(results_random)
plot_scatter_streaks(x_streaks_random, o_streaks_random)

# Suponha que 'simulate_games' com Monte Carlo retorne uma lista similar
results_monte_carlo = simulate_games(num_games)

# Contar vitórias consecutivas
x_streaks_monte_carlo, o_streaks_monte_carlo = count_consecutive_wins(results_monte_carlo)

# Plotar os resultados da simulação Monte Carlo
print("\nResultados da simulação com Monte Carlo:")
print(results_monte_carlo)
plot_scatter_streaks(x_streaks_monte_carlo, o_streaks_monte_carlo)

def simulate_games(num_games):
    # Simulação de resultados aleatórios (exemplo)
    return [random.choice(['X', 'O', 'Empate']) for _ in range(num_games)]

def count_consecutive_wins(results):
    x_streak = 0
    o_streak = 0
    x_streaks = []
    o_streaks = []

    for result in results:
        if result == 'X':
            x_streak += 1
            o_streak = 0
        elif result == 'O':
            o_streak += 1
            x_streak = 0
        else:  # Empate
            x_streak = 0
            o_streak = 0
        x_streaks.append(x_streak)
        o_streaks.append(o_streak)

    return x_streaks, o_streaks

def plot_streaks(x_streaks, o_streaks):
    plt.figure(figsize=(14, 7))
    plt.plot(x_streaks, label='Vitórias consecutivas de X')
    plt.plot(o_streaks, label='Vitórias consecutivas de O', linestyle='--')
    plt.xlabel('Número do Jogo')
    plt.ylabel('Vitórias Consecutivas')
    plt.title('Tendência de Vitórias Consecutivas de X e O')
    plt.legend()
    plt.show()

# Número de jogos a simular
num_games = 1000

# Simulação com jogadas aleatórias
results_random = simulate_games(num_games)

# Contar vitórias consecutivas
x_streaks_random, o_streaks_random = count_consecutive_wins(results_random)

# Plotar os resultados da simulação aleatória
print("Resultados da simulação com jogadas aleatórias:")
print(results_random)
plot_streaks(x_streaks_random, o_streaks_random)

# Suponha que 'simulate_games' com Monte Carlo retorne uma lista similar
results_monte_carlo = simulate_games(num_games)

# Contar vitórias consecutivas
x_streaks_monte_carlo, o_streaks_monte_carlo = count_consecutive_wins(results_monte_carlo)

# Plotar os resultados da simulação Monte Carlo
print("\nResultados da simulação com Monte Carlo:")
print(results_monte_carlo)
plot_streaks(x_streaks_monte_carlo, o_streaks_monte_carlo)