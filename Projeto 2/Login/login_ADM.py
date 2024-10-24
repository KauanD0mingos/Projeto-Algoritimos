import getpass

def login_ADM(usuarios):

    tentativas = 3  
    while tentativas > 0:
        nome = input('\033[1;37mDigite seu nome de usuário (ou "sair" para encerrar):\033[m ')
        if nome.lower() == 'sair':
            return None  
        
        senha = getpass.getpass('\033[1;37mDigite sua senha:\033[m ')
        
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha and usuario['perfil'] == '1':
                print(f'\n\033[1;32mSeja bem-vindo(a) ADM {usuario["nome"]}!\033[m')
                return usuarios 
            else:
                print(f'\n\033[1;31mUsuário {usuario["nome"]} não é administrador\033[m')
                break
        else:
            print('\n\033[1;31mUsuário não cadastrado ou senha incorreta!\033[m\n')
            tentativas -= 1  
    
    print('\n\033[1;31mLimite de tentativas excedido\033[m')
    return None  
