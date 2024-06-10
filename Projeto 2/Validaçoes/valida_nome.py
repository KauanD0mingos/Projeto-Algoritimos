def valida_nome(nome):
    while(True):
        if(len(nome) < 3):
            print('\t\n\033[1;31mSeu nome deve conter (3) caractere!\033[m\n ')
            nome = input('\033[1;37m Digite novamente seu nome:\033[m ')
        elif(' ' in nome):
            print('\t\n\033[1;31mSeu nome não pode conter espaço!\033[m\n ')
            nome = input('\033[1;37m Digite novamente seu nome:\033[m ')
        else:
            print('\t\n\033[1;32mSeu nome foi cadastrado!\033[m\n')
            return nome
