class Jogadores:
    # A linha abaixo cria uma lista vazia
    lista_jogadores = []

    # def __init__(self, jogadores):
    #     self.lista_jogadores = jogadores

    # aqui adiciona o jogador no final da lista
    def adicionar_jogador(self, nome_jogador):
        self.lista_jogadores.append(nome_jogador)
        # exemplo para fazer a interpolacao de uma string
        print(f"Jogador: {nome_jogador} adicionado")

    def listar_jogadores(self):
        print(self.lista_jogadores)

    # aqui remove um jogador especifico da lista
    def remover_jogador(self, nome_jogador):
        self.lista_jogadores.remove(nome_jogador)
        print(f"Jogador: {nome_jogador} removido")

    # aqui é um exemplo de pilha, LIFO, sempre remove o ultimo elemento
    def remover_ultimo_jogador(self):
        removido = self.lista_jogadores.pop()
        print("Jogador Removido: ", removido)
    
    # aqui um exemplo de fila, FIFO, sempre remove o primeiro elemennto
    def remover_primeiro_jogador(self):
        removido = self.lista_jogadores.pop(0)
        print("Jogador Removido: ", removido)

        
