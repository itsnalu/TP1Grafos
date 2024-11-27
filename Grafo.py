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

    # TODO 1 - Representação de vértices (calcular grau dos vértices)
    def grau_vertices(self):
        graus = []
        for i in range(self.num_vertices):
            grau = 0
            for j in range(self.num_vertices):
                if self.matriz_adj[i][j] != 0:
                    grau += 1
            graus.append(grau)
        #print()
        for i in range(self.num_vertices):
            print(f"Vértice {i+1} tem grau {graus[i]}")
        print()

    # TODO 2 - Algoritmo de Roy para contar o número de componentes conexas (não é dfs)
    def roy_componentes_conexas(self):
        # Cria matriz de alcançabilidade com base na matriz de adjacência
        alcançavel = [[1 if i == j or self.matriz_adj[i][j] != 0 else 0 for j in range(self.num_vertices)] for i in range(self.num_vertices)]
        
        # Algoritmo de Floyd-Warshall para calcular a alcançabilidade
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    alcançavel[i][j] = alcançavel[i][j] or (alcançavel[i][k] and alcançavel[k][j])

        # Determina os componentes conexos
        visitados = [False] * self.num_vertices
        componentes = 0

        for i in range(self.num_vertices):
            if not visitados[i]:
                componentes += 1
                for j in range(self.num_vertices):
                    if alcançavel[i][j]:
                        visitados[j] = True

        print(f"O grafo possui {componentes} componente(s) conexa(s).")
        print()
