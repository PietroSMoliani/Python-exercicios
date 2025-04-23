def soma_dos_numeros():
  entrada = input("digite um número inteiro!")
  if not entrada.lstrip('-').isdigit():
    return print("este número não é válido, por favor digite um número inteiro!")
    numero = int(entrada)
    soma = sum(int(digito) for digito in str(abs(numero)))
    print(f"A soma dos digitos do numero {numero} é: {soma}")
    
    soma_dos_numeros()