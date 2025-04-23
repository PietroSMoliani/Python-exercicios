# Programa - Notas da equipe

def notas_da_equipe():
    notas = []

    # Solicitar as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i}: "))
                if 0 <= nota <= 10:  # Validar que a nota está no intervalo de 0 a 10
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    # Calcular o maior valor, menor valor e média
    maior_nota = max(notas)
    menor_nota = min(notas)
    media_notas = sum(notas) / len(notas)

    # Exibir os resultados
    print(f"\nMaior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média das notas: {media_notas:.2f}")

# Executar a função
notas_da_equipe()
