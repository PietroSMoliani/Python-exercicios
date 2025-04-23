# Programa - Notas de Carnaval (Modo Antigo)

def notas_de_carnaval():
    notas = []

    # Solicitar as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota {i}: "))
                if 0 <= nota <= 10:  # Validar que a nota está no intervalo de 0 a 10
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    # Descarta a maior e a menor nota
    maior_nota = max(notas)
    menor_nota = min(notas)
    notas.remove(maior_nota)
    notas.remove(menor_nota)

    # Calcular a média das 3 notas restantes
    media_notas = sum(notas) / len(notas)

    # Exibir o resultado
    print(f"\nMédia das notas (descontando a maior e a menor): {media_notas:.2f}")

# Executar a função
notas_de_carnaval()
