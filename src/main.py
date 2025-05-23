
from jogadores import Jogadores

def menu():
    print("\n---")
    print("1 - Adicionar Jogador")
    print("2 - Remover Jogador")
    print("3 - Mostrar lista de Jogadores")
    print("4 - Sair")
    return input("Escolha uma opção: ")

lista_jogadores = Jogadores()

while True:
    opcao = menu()
    if opcao=='1':
        nome = input("Digite o nome do jogador: ")
        lista_jogadores.adicionar_jogador(nome)
    elif opcao=='2':
        nome = input("Digite o nome do jogador a ser removido: ")
        lista_jogadores.remover_jogador(nome)
    elif opcao=='3':
        lista_jogadores.listar_jogadores()
    elif opcao == '4':
        print("Sistema encerrado. Obrigado por utilizar!")
        break
    else:
        print("Opção inválida. Tente novamente.")


# lista_jogadores = Jogadores()
# lista_jogadores.adicionar_jogador("Granger")
# lista_jogadores.adicionar_jogador("Argus")
# lista_jogadores.adicionar_jogadores(["Granger", "Argus", "Freddin"])
# lista_jogadores.remover_jogador("Granger")
# lista_jogadores.listar_jogadores()
# lista_jogadores.remover_ultimo_jogador()
# lista_jogadores.remover_primeiro_jogador()
# lista_jogadores.remover_primeiro_jogador()
# lista_jogadores.conta_jogadores()
