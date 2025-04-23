def dolares_para_float(d):
    # Remove o símbolo "$" e converte o valor restante para float
    return float(d.replace('$', ''))

def percentual_para_float(p):
    # Remove o símbolo "%" e converte o valor restante para float e divide por 100
    return float(p.replace('%', '')) / 100

dolares = dolares_para_float(input("Quanto custou a refeição? "))
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? "))
gorjeta = dolares * percentual
print(f"Deixe ${gorjeta:.2f}")