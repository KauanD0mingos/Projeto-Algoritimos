def valida_email(email):
    while(True):
        if '@gmail.com' not in email.lower() and '@gmail.edu' not in email.lower() and '@gmail.gov' not in email.lower():
            print('\t\n\033[1;31mE-mail inválido!\033[m\n')
            email = input('\033[1;37m Digite novamente:\033[m')
        else:
             print('\t\n\033[1;32mE-mail cadastrado!\033[m\n ')
             return email
