def cadastrar_sala(filmes):
    sala = dict()

    sala['numero'] = int(input('Digite o número da sala: '))
    sala['horario'] = input('Digite o horário que a sala funcionará: ')
    sala['capacidade'] = int(input('Digite a capacidade da sala: '))

    print("Escolha um filme da lista abaixo:")
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['nome_filme']}")

    escolha = int(input('Digite o número do filme que será exibido na sala: '))

    if 1 <= escolha <= len(filmes):
        sala['filme'] = filmes[escolha - 1]['nome_filme']
        sala['quantidade'] = filmes[escolha - 1]['quantidade_inicial']
    else:
        print("Escolha inválida. Nenhum filme será adicionado à sala.")
        sala['filme'] = None
        sala['quantidade_inicial'] = 0

    return sala