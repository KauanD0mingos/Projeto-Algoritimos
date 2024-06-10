def valida_senha(senha):
    while(True):
        if len(senha) < 5:
            print('\n\033[1;31mÉ recomendado conter (5) caractere na senha!\033[m\n ')
            senha = input('\033[1;37m Digite sua senha:\033[m ')
        else:
            pergunta = input('\n\033[1;37m Deseja cadastrar? \033[1;32mS\033[m\033[1;37m/\033[m\033[1;31mN\033[m:')
            if pergunta.lower() == 's':
                    print('\t\n\033[1;32mSua senha está cadastrada!\033[m\n ')
                    return senha
            
            elif pergunta.lower() == 'n':
                Nova_senha = input('\033[1;37mDigite a nova senha:\033[m ')

                if len(Nova_senha) < 5:
                    print('\t\033[1;31mÉ recomendado conter (5) caractere na senha!\033[m\n ')
                    senha = input('\033[1;37mDigite sua senha:\033[m ')

                elif Nova_senha == senha:
                    print('\t\033[1;31mSua senha não pode ser igual a aterior!\033[m\n')
                    Nova_senha = input('\033[1;37mDigite a nova senha:\033[m ')
            else:
                print('\t\033[1;31mVocê precisar confirmar com Sim ou N\033[m')  
           