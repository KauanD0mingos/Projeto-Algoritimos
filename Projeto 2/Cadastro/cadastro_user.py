def cadastro_usuario(Usuario):
    from Validaçoes import valida_senha,valida_email,valida_nome,valida_perfil
    usuario = dict()

    usuario['nome'] = valida_nome.valida_nome(input('\033[1;37m Digite seu nome:\033[m '))
    usuario['senha'] = valida_senha.valida_senha(input('\033[1;37m Digite sua senha:\033[m '))
    usuario['email'] = valida_email.valida_email(input('\033[1;37m Digite seu E-mail no formato\033[m(\033[1;31m @gmail.com\033[m):\033[m'))
    usuario['perfil'] = valida_perfil.valida_perfil(input('\033[1;37mDigite (\033[1;31m1\033[m\033[1;37m) para ADM ou (\033[1;31m2\033[m\033[1;37m) para Cliente:\033[m '))
    usuario['ingresso'] = 0
    return usuario




        

