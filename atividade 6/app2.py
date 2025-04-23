numero = input("Digite um número para somarmos seus dígitos: ")


if numero.isdigit():
    soma = 0

    for digito in numero:
        soma += int(digito)
    print("A soma dos dígitos é:", soma)
else:
    print("Erro você precisa digitar um número inteiro.")