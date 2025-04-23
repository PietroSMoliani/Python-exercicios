# Programa 3 - Calculadora Simples

def calculadora():
    try:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        if num2 != 0:
            divisao = num1 / num2
        else:
            divisao = "Não é possível dividir por zero."

        # Exibir resultados
        print(f"A soma de {num1} e {num2} é {soma}")
        print(f"A subtração de {num1} por {num2} é {subtracao}")
        print(f"A multiplicação de {num1} e {num2} é {multiplicacao}")
        print(f"A divisão de {num1} por {num2} é {divisao}")

    except ValueError:
        print("Valor inválido! Por favor, informe números válidos.")

# Executar a função
calculadora()
