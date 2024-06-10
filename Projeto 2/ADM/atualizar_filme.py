def atualizar_filme(Filmes):
    nome_filme = input('\n\033[1;37mDigite o nome do filme que deseja atualizar:\033[m ')
    
    for i, filme in enumerate(Filmes):
        if filme['nome_filme'] == nome_filme.lower():
            print('\n\033[1;32m Filme encontrado!\033[m')
            novo_nome = input('\n\033[1;37mDigite o novo nome do filme:\033[m ')
            genero = input('\033[1;37mDigite o gênero do filme:\033[m ')
            novo_valor = input('\033[1;37mDigite o valor do filme:\033[m ')
            nova_quantidade = int(input('\033[1;37mDigite a quantidade de ingressos:\033[m'))

            Filmes[i] = {'nome_filme': novo_nome, 'genero': genero, 'valor': novo_valor, 'quantidade': nova_quantidade}
            print('\n\t\033[1;32mO filme foi atualizado!\033[m')
            return Filmes
    
    print('\n\033[1;31m Filme não encontrado!\033[m')
    return Filmes
