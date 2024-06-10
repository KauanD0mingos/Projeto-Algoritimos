def buscar_filmes(filmes):
    nome_filme = input('\n\033[1;37mDigite o nome do filme que deseja buscar:\033[m ')
    resultados = [filme for filme in filmes if nome_filme.lower() in filme['nome_filme'].lower()]
    
    if resultados:
        print('\n\033[1;32mFilmes encontrados:\033[m')
        for filme in resultados:
            print(f"Nome: {filme['nome_filme']}, Genêro: {filme['genero']}")
    else:
        print('\n\033[1;31mNenhum filme encontrado com esse nome.\033[m')
