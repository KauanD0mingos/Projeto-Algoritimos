def avaliar_filme(Filmes, ingressos_comprados, Comentarios):
    filmes_disponiveis = []
    for filme in Filmes:
        for ingresso in ingressos_comprados:
            if filme['nome_filme'] == ingresso['nome_filme'] and ingresso['quantidade'] > 0:
                filmes_disponiveis.append(filme['nome_filme'])
                break

    if not filmes_disponiveis:
        print('\n\033[1;31mVocê não possui ingressos para nenhum filme. Não é possível deixar feedback\033[m')
        return

    print('\n\033[1;32mFilmes Disponíveis para Avaliação:\033[m')
    for i, filme in enumerate(filmes_disponiveis):
        print(f'{i + 1}º {filme}')

    escolha = input('\n\033[1;37mDigite o número do filme que deseja avaliar:\033[m ')
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(filmes_disponiveis):
            escolha = escolha - 1
        else:
            print('\n\033[1;31mVocê precisa escolher um número da lista!\033[m')
            return
    else:
        print('\n\033[1;31mVocê precisa escolher um número da lista!\033[m')
        return

    avaliacao = input('\n\033[1;37mDe 1 a 5, qual seria sua avaliação para este filme?\033[m ')
    if avaliacao.isdigit():
        avaliacao = int(avaliacao)
        if 1 <= avaliacao <= 5:
            # A avaliação é válida, podemos prosseguir
            comentario = input('\033[1;37mDeixe um comentário (opcional):\033[m ')
            if not comentario:
                comentario = None

            avaliacao_filme = {
                'nome_filme': filmes_disponiveis[escolha],
                'avaliacao': avaliacao,
                'comentario': comentario or None
            }

            Comentarios.append(avaliacao_filme)

            print('\n\033[1;32mObrigado pelo seu feedback!\033[m')
            return avaliacao_filme
        else:
            print('\n\033[1;31mPor favor, insira uma avaliação válida (de 1 a 5):\033[m')
            return
    else:
        print('\n\033[1;31mPor favor, insira uma avaliação válida (de 1 a 5):\033[m')
        return


def ver_avaliacoes(avaliacoes):
    print('\033[1;30m-\033[m' * 30)
    print('\033[1;34m    Avaliações dos Filmes\033[m')
    print('\033[1;30m-\033[m' * 30, '\n')

    if not avaliacoes:
        print('\n\033[1;31mNenhuma avaliação disponível no momento\033[m')
    else:
        for i, avaliacao in enumerate(avaliacoes):
            print(f'\n\033[1;37mAvaliação {i + 1}:\033[m')
            print(f'\n\033[1;37mFilme: {avaliacao["nome_filme"]}\033[m')
            print(f'Avaliação: {avaliacao["avaliacao"]}')
            if avaliacao['comentario']:
                print(f'\n\033[1;37mComentário: {avaliacao["comentario"]}\033[m')
            print()

