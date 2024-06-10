def remover_usuario(Usuarios):
    while True:
        usuarios_sem_compra = [usuario for usuario in Usuarios if usuario['ingressos'] == 0]

        if not usuarios_sem_compra:
            print('\n\033[1;31mNão há usuários sem compra.\033[m')
            return Usuarios

        print('\n\t\033[1;34mUSUÁRIOS SEM COMPRA:\033[m')
        for usuario in usuarios_sem_compra:
            print(f"\033[1;37mNome: {usuario['nome']}\033[m")

        resposta_remover = input('\n\033[1;37mDeseja remover algum usuário sem compra? (S/N): \033[m').lower()
        if resposta_remover == 's':
            nome = input('Digite o nome de usuário que deseja deletar: ')
            for usuario in Usuarios:
                if usuario['nome'] == nome and usuario['ingressos'] == 0:
                    Usuarios.remove(usuario)
                    print(f'\n\033[1;32mUsuário {nome} removido.\033[m')
                    break
            else:
                print('\n\033[1;31mUsuário não encontrado ou não está na lista de usuários sem compra.\033[m')
        elif resposta_remover == 'n':
            break
        else:
            print('\n\033[1;31mOpção inválida. Digite S ou N.\033[m')

    return Usuarios
