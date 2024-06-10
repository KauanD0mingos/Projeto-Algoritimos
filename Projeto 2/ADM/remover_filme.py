def remover_filme(Filme):
    while True:
        nome_filme = input('\n\033[1;37mDigite o nome do filme que deseja remover:\033[m ')
        filme_encontrado = False
        for filme in Filme:
            if filme['nome_filme'] == nome_filme:
                print('\n\033[1;32m Filme encontrado!\033[m')
                perg = input('\n\033[1;37m Deseja remover? \033[1;32mS\033[m\033[1;37m/\033[m\033[1;31mN\033[m:')
                if perg.lower() == 's':
                    Filme.remove(filme)
                    filme_encontrado = True
                    print('\n\033[1;32m Filme removido com sucesso!\033[m')
                    break  
                elif perg.lower() == 'n':
                    print('\n\033[1;31m O filme não foi removido!\033[m ')
                    filme_encontrado = True
        if not filme_encontrado:
            print('\n\033[1;31m O filme não foi encontrado!\033[m')
        continuar = input('\n\033[1;37m Deseja remover outro filme? \033[1;32mS\033[m\033[1;37m/\033[m\033[1;31mN\033[m:')
        if continuar.lower() != 's':
            break
    return Filme
