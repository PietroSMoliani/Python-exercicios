# Programa 1 - Par ou Ímpar

def verificar_par_ou_impar():
    try:
        numero = int(input("Informe um número: "))
        if numero % 2 == 0:
            return True  # Número par
        else:
            return False  # Número ímpar
    except ValueError:
        return "Valor inválido! Por favor, informe um número inteiro."

# Executar a função
print(verificar_par_ou_impar())
