from Validaçoes import *
from Cadastro.cadastro_user import cadastro_usuario
import Menus.menu_inicio, Menus.menu_adm, Menus.menu_cliente, Menus.menu_feedback
import ADM.cadastrar_filme, ADM.buscar_filme, ADM.atualizar_filme, ADM.grafico, ADM.ingressos_v, ADM.remover_filme, ADM.remover_usu
from Salas.cadastro import cadastrar_sala
import Cliente.compra, Cliente.ingressos, Cliente.avaliar_filme
import Login.login_ADM, Login.login_Cliente

usuarios = []

Filmes = [{'nome_filme': 'matrix', 'genero': 'ficção científica', 'valor': '10.00','quantidade_inicial':100, 'quantidade':10}]

Salas = []
Ingressos = []
Avaliacoes = []

while True:
    Menus.menu_inicio.menu_principal()
   
    opcao = input('\n\033[1;37mDigite a opção desejada:\033[m ')
   
    if opcao == '1':
        usuario = cadastro_usuario(usuarios)
        usuarios.append(usuario)
       
       
    elif opcao == '2':
        if Login.login_ADM.login_ADM(usuarios):
            while True:
                Menus.menu_adm.menu_adm()

                opcao_adm = input('\n\033[1;37mDigite a opção desejada:\033[m')

                if opcao_adm == '1':
                    ADM.cadastrar_filme.Cadastrar_Filme(Filmes)
                
                elif opcao_adm == '2':
                    ADM.buscar_filme.buscar_filmes(Filmes)

                elif opcao_adm == '3':
                    ADM.atualizar_filme.atualizar_filme(Filmes)
                
                elif opcao_adm == '4':
                    ADM.remover_filme.remover_filme(Filmes)

                elif opcao_adm == '5':
                    pergunt = input('\n\033[1;37mDigite (\033[1;31m1\033[m\033[1;37m) para listar o total de ingressos ou (\033[1;31m2\033[m\033[1;37m) para lista apenas do filme desejado:\033[m')
                    if pergunt == '1':
                        ADM.ingressos_v.criar_arquivo_total_vendidos(Filmes)
                    elif pergunt == '2':
                        ADM.ingressos_v.listar_ingressos_vendidos(Filmes)
                
                elif opcao_adm == '6':
                    ADM.remover_usu.remover_usuario(usuarios)

                elif opcao_adm == '7':
                    ADM.grafico.mais_vendidos(Filmes)

                elif opcao_adm == '8':
                    sala = cadastrar_sala(Filmes)
                    Salas.append(sala)
                
                elif opcao_adm == '0':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

    elif opcao == '3':
        if Login.login_Cliente.login_cliente(usuarios):
            while True:
                Menus.menu_cliente.menu_cliente()

                opcao_cliente = input('\n\033[1;37mDigite a opção desejada:\033[m')

                if opcao_cliente == '1':
                    compra = Cliente.compra.compra_ingresso(Filmes,Ingressos)

                elif opcao_cliente == '2':
                    ingresso = Cliente.ingressos.listar_ingressos(Ingressos)
                    
                elif opcao_cliente == '3':
                    while True:
                        Menus.menu_feedback.menu_feedback()
                        opcao_feedback = input("Escolha uma opção: ")

                        if opcao_feedback == '1':
                            Cliente.avaliar_filme.avaliar_filme(Filmes,Ingressos,Avaliacoes)
                        elif opcao_feedback == '2':
                            Cliente.avaliar_filme.ver_avaliacoes(Avaliacoes)
                        elif opcao_feedback == '3':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
    elif opcao == '0':
        break
    else:
        print('\n\033[1;31m Opção inválida. Tente novamente\033[m')
