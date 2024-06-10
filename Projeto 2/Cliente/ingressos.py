def listar_ingressos(ingressos_comprados):
    if not ingressos_comprados:
        print('\n\033[1;31mVocê ainda não comprou nenhum ingresso\033[m')
        return
    else:
        print('\n\033[1;34mIngressos Comprados:\033[m')
        for i, ingresso in enumerate(ingressos_comprados, 1):
            print(f'\n\033[1;37m{i}º Filme: {ingresso["nome_filme"]}, Quantidade: {ingresso["quantidade"]}\033[m')

    pergunta = input('\n\033[1;37mDeseja enviar o arquivo TXT?\033[m ')

    if pergunta.lower() == 's':
        with open("ingressos_comprados.txt", "a", encoding="UTF-8") as f:
            for ingresso in ingressos_comprados:
                f.write(f"Nome do filme: {ingresso['nome_filme']}, Quantidade: {ingresso['quantidade']}\n")
        print('\n\033[1;32mArquivo TXT enviado com sucesso\033[m')
    return
