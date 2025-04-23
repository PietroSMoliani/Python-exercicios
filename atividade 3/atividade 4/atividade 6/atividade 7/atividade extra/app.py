import random

# Função para o jogo de adivinhação
def jogo_de_adivinhacao():
    numero_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número gerado entre 1 e 100.")

    # Loop até o usuário acertar o número
    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_aleatorio:
                print("O número é maior. Tente novamente.")
            elif palpite > numero_aleatorio:
                print("O número é menor. Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_aleatorio}!")
                print(f"Você acertou em {tentativas} tentativas.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Executar o jogo
jogo_de_adivinhacao()
