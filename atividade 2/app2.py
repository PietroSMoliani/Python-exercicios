# Programa 2 - Can You Drive?

def verificar_idade():
    try:
        idade = int(input("Informe sua idade: "))
        if idade < 0:
            return "Idade inválida! Informe um número positivo."
        elif idade < 18:
            return "Você é menor de idade."
        elif 18 <= idade <= 59:
            return "Você é adulto."
        else:
            return "Você é idoso."
    except ValueError:
        return "Valor inválido! Por favor, informe um número válido para a idade."

# Executar a função
print(verificar_idade())
