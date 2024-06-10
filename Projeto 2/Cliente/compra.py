def compra_ingresso(Filmes, ingressos_comprados):
 
    while True:
        quantidade = input('\033[1;37mDigite a quantidade de ingressos que deseja:\033[m ')
        if quantidade.isdigit() and int(quantidade) > 0:
            quantidade = int(quantidade)
            break
        else:
            print('\n\033[1;31mVocê precisa digitar um número inteiro positivo!\033[m')
    
    compra = input('\033[1;37mDeseja comprar (S/N): \033[m').strip().lower()
    if compra == 's':
        print('\n\033[1;32mFilmes Disponíveis\033[m')
        for i, filme in enumerate(Filmes, start=1):
            print(f'\n\033[1;37m{i}º {filme["nome_filme"]} - {filme["quantidade_inicial"]} ingressos disponíveis\033[m')

        while True:
            escolha = input('\033[1;37mDigite o número do filme que deseja assistir:\033[m ')
            if escolha.isdigit() and 1 <= int(escolha) <= len(Filmes):
                escolha = int(escolha) - 1
                break
            else:
                print('\n\033[1;31mVocê precisa escolher um número da lista!\033[m')

        if Filmes[escolha]['quantidade_inicial'] < quantidade:
            print(f'\n\033[1;31mNão há ingressos suficientes para {Filmes[escolha]["nome_filme"]}!\033[m')
        else:
            Filmes[escolha]['quantidade_inicial'] -= quantidade
            print(f'\n\033[1;32mCompra realizada com sucesso para {quantidade} ingresso(s) do filme {Filmes[escolha]["nome_filme"]}!\033[m')
            ingressos_comprados.append({
                'nome_filme': Filmes[escolha]['nome_filme'],
                'quantidade': quantidade
            })

    return Filmes, ingressos_comprados