# Programa Desafio - Calculadora com operação escolhida

def calculadora_com_operacao():
    try:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        operacao = input("Informe a operação (soma, subtração, multiplicação, divisão): ").lower()

        if operacao == "soma":
            resultado = num1 + num2
            print(f"O resultado da soma de {num1} e {num2} é {resultado}")
        elif operacao == "subtração":
            resultado = num1 - num2
            print(f"O resultado da subtração de {num1} por {num2} é {resultado}")
        elif operacao == "multiplicação":
            resultado = num1 * num2
            print(f"O resultado da multiplicação de {num1} e {num2} é {resultado}")
        elif operacao == "divisão":
            if num2 == 0:
                print("Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                print(f"O resultado da divisão de {num1} por {num2} é {resultado}")
        else:
            print("Operação inválida! Por favor, escolha uma operação válida.")
    except ValueError:
        print("Valor inválido! Por favor, informe números válidos.")

# Executar a função
calculadora_com_operacao()
