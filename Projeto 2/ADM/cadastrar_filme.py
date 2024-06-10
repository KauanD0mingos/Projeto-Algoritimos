def Cadastrar_Filme(Filmes):
    while True:
        Nome_filme = input('\n\033[1;37mDigite o nome do filme:\033[m ')
        Genero = input('\033[1;37mDigite o gênero do filme:\033[m ')
        Valor = float(input('\033[1;37mDigite o valor do filme:\033[m '))
        if Valor < 0:
            print('\n\t\033[1;31mDigite um número válido!\033[m')
            Valor = float(input('\033[1;37mDigite o valor do filme:\033[m '))
        Quantidade = int(input('\033[1;37mDigite a quantidade de ingressos:\033[m'))
        if Quantidade < 0:
            print('\n\t\033[1;31mDigite um número válido!\033[m')
            Quantidade = int(input('\033[1;37mDigite a quantidade de ingressos:\033[m'))

        filme = {'nome_filme':Nome_filme,'genero':Genero,'valor':Valor,'quantidade_inicial':Quantidade,'quantidade':0}
        Filmes.append(filme)
        print('\n\033[1;32m Filme cadastrado com sucesso!\033[m')
        
        return Filmes
