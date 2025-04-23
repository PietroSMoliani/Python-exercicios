# Programa - Lista de Convidados para a Festa

def lista_de_convidados():
    convidados = []

    # Solicitar nomes dos convidados
    while True:
        nome = input("Digite o nome de um convidado (ou digite 'fim' para encerrar): ")
        
        if nome.lower() == 'fim':
            break
        else:
            convidados.append(nome)

    # Remover duplicados (usando set) e ordenar os nomes
    convidados_unicos = sorted(set(convidados))

    # Exibir a lista final
    print("\nLista final de convidados (sem duplicatas e ordenada):")
    for convidado in convidados_unicos:
        print(convidado)

# Executar a função
lista_de_convidados()
