def valida_perfil(perfil):
    while(True):
        if perfil == '1' or perfil == '2':
            if perfil == '1':
                print('\t\n\033[1;32mAcesso de Administrador Cadastrado!\033[m\n')
            elif perfil == '2':
                print('\t\n\033[1;32mAcesso de Cliente Cadastrado!\033[m\n')
            break
        else:
            print('\n\033[1;37mÉ preciso digitar (\033[1;31m1\033[m\033[1;37m) para ADM ou (\033[1;31m2\033[m\033[1;37m) para Cliente:\033[m ')
            perfil = int(input('\033[1;37mDigite novamente:\033[m '))
    return perfil
    