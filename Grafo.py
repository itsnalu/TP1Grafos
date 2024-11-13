class Grafo:

    def __init__(self, num_vertices):
        # inicializa o grafo
        self.num_vertices = num_vertices
        self.num_arestas = 0 
        self.matriz_adj = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.dt = [float('inf')] * num_vertices  # inicializa com infinito
        self.rot = [-1] * num_vertices           # inicializa com -1
        self.tem_ciclo = None                    
        self.ciclo_negativo = 0                  

    def adicionar_aresta(self, origem, destino, peso):
        if origem < 1 or origem > self.num_vertices or destino < 1 or destino > self.num_vertices:
            print("Erro: vértice fora do intervalo")
            return
        # adiciona a aresta à matriz de valores e atualiza o contador de arestas do grafo
        self.matriz_adj[origem - 1][destino - 1] = peso
        self.matriz_adj[destino - 1][origem - 1] = peso
        self.num_arestas += 1

    def imprimir_grafo(self):

        #  imprime o número do vértice de cada coluna.
        print("   ", end="")
        for j in range(1, self.num_vertices + 1):
            print(f"{j:>4}", end="")
        print()
        
        # imprime a matriz com o número do vértice de cada linha
        for i in range(self.num_vertices):
            print(f"{i + 1:<3}", end="")
            for j in range(self.num_vertices):
                print(f"{self.matriz_adj[i][j]:>4.1f}", end="")
            print()

    @staticmethod # define um método dentro de uma classe que não precisa acessar 
    # ou modificar os atributos da classe ou da instância
    def carregar_num_vertices(arquivo):
        # número de vértices na primeira linha do arquivo.
        with open(arquivo, 'r') as f:
            num_vertices = int(f.readline().strip())
        return num_vertices

    def carregar_arestas(self, arquivo):
        # processa as arestas a partir da segunda linha do arquivo.
        with open(arquivo, 'r') as f:
            # ignora a primeira linha já que o grafo já foi inicializado
            next(f)
            for linha in f:
                origem, destino, peso = linha.split()
                self.adicionar_aresta(int(origem), int(destino), float(peso))


def main():

    num_vertices = Grafo.carregar_num_vertices('entrada.txt')
    print(f"Número de vértices: {num_vertices}")

    grafo = Grafo(num_vertices)

    grafo.carregar_arestas('entrada.txt')

    grafo.imprimir_grafo() 


if __name__ == "__main__":
    main()
