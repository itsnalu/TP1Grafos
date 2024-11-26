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

    def ponto_articulacao(self):
        def dfs(v, visitado, disc, low, parent, pontos):
            visitado[v] = True
            children = 0
            disc[v] = low[v] = self.tempo
            self.tempo += 1

            for i in range(self.num_vertices):
                if self.matriz_adj[v][i] != 0:  # Se existe uma aresta
                    if not visitado[i]:  # Se o vértice i não foi visitado
                        parent[i] = v
                        children += 1
                        dfs(i, visitado, disc, low, parent, pontos)

                        low[v] = min(low[v], low[i])

                        if parent[v] == -1 and children > 1:
                            pontos.add(v)
                        if parent[v] != -1 and low[i] >= disc[v]:
                            pontos.add(v)
                    elif i != parent[v]:  # Atualizar low value para ciclo
                        low[v] = min(low[v], disc[i])

        visitado = [False] * self.num_vertices
        disc = [float('inf')] * self.num_vertices
        low = [float('inf')] * self.num_vertices
        parent = [-1] * self.num_vertices
        pontos = set()

        self.tempo = 0
        for i in range(self.num_vertices):
            if not visitado[i]:
                dfs(i, visitado, disc, low, parent, pontos)

        return [p + 1 for p in pontos]  # Retorna os pontos de articulação (1-indexados)

    def bellman_ford(self, origem):
        origem -= 1  # Ajusta para índice baseado em 0
        self.distancias = [float('inf')] * self.num_vertices
        self.predecessores = [-1] * self.num_vertices
        self.distancias[origem] = 0

        # Relaxa as arestas |V| - 1 vezes
        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if self.matriz_adj[u][v] != 0:  # Existe uma aresta
                        peso = self.matriz_adj[u][v]
                        if self.distancias[u] + peso < self.distancias[v]:
                            self.distancias[v] = self.distancias[u] + peso
                            self.predecessores[v] = u

        # Verifica ciclos negativos
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.matriz_adj[u][v] != 0:
                    peso = self.matriz_adj[u][v]
                    if self.distancias[u] + peso < self.distancias[v]:
                        print("Ciclo de peso negativo detectado!")
                        return False

        return True

    def imprimir_caminhos(self, origem):
        origem -= 1  # Ajusta para índice baseado em 0
        print(f"Caminhos mínimos a partir do vértice {origem + 1}:\n")
        for v in range(self.num_vertices):
            if self.distancias[v] == float('inf'):
                print(f"Vértice {v + 1} não é alcançável")
            else:
                caminho = []
                atual = v
                while atual != -1:  # Reconstrói o caminho até a origem
                    caminho.append(atual + 1)  # Ajusta para índice 1
                    atual = self.predecessores[atual]
                caminho.reverse()  # Reverte para obter o caminho na ordem correta
                print(f"Para {v + 1}: distância = {self.distancias[v]:.1f}, caminho = {' -> '.join(map(str, caminho))}")

    def printarDistancias(self, dist):
        print("Matrix de menores distâncias entre cada par de vértices:")
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][j] == float('inf'):
                    print("%7s" % "∞", end=" ")
                else:
                    print("%7d" % dist[i][j], end=" ")
            print()

    def floydWarshall(self):
        num_vertices = self.num_vertices
        
        # Criar uma cópia da matriz de adjacência para evitar modificações
        dist = [row[:] for row in self.matriz_adj]
        
        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    # Atualizar dist[i][j] se passar por k for mais curto
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
        

   