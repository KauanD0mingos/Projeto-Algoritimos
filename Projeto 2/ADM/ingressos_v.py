def criar_arquivo_total_vendidos(Filmes):
    def ingressos_vendidos_total(Filmes):
        total = 0
        for filme in Filmes:
            total += (filme['quantidade_inicial'] - filme['quantidade'])
        return total

    def criar_arquivo_txt_total_vendidos(Filmes, total):
        nome_arquivo = 'total_ingressos_vendidos.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('Lista de filmes vendidos:\n\n')
            for filme in Filmes:
                ingressos_iniciais = filme['quantidade_inicial']
                ingressos_vendidos = ingressos_iniciais - filme['quantidade']
                arquivo.write(f'Filme: {filme["nome_filme"]}\n')
                arquivo.write(f'Quantidade inicial de ingressos: {ingressos_iniciais}\n')
                arquivo.write(f'Quantidade final de ingressos: {ingressos_vendidos}\n\n')  # Corrigido aqui
            arquivo.write(f'Total de ingressos vendidos: {total}')
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

    def solicitar_envio_arquivo():
        resposta = input("Deseja enviar o arquivo TXT? (s/n): ").strip().lower()
        return resposta == 's'

    total_vendidos = ingressos_vendidos_total(Filmes)
    print(f'Total de ingressos vendidos: {total_vendidos}')

    if solicitar_envio_arquivo():
        criar_arquivo_txt_total_vendidos(Filmes, total_vendidos)
    else:
        print('Arquivo não enviado')


def listar_ingressos_vendidos(Filmes):
    nome_filme = input('\n\033[1;37mDigite o nome do filme:\033[m')
    for filme in Filmes:
        if filme['nome_filme'].lower() == nome_filme.lower():
            print(f'\n\033[1;32m O filme {filme["nome_filme"]} vendeu {filme["quantidade"]} ingressos.\033[m')
            return
    print(f'\n\033[1;31m Filme {nome_filme} não encontrado.\033[m')
