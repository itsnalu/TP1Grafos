from Grafo import Grafo  
import Arquivo

def main():
    num_vertices = Arquivo.carregar_num_vertices('entrada.txt')
    # num_vertices = Arquivo.carregar_num_vertices('entrada_sem_ciclo.txt')

    print(f"Número de vértices: {num_vertices}")

    grafo = Grafo(num_vertices)

    Arquivo.carregar_arestas('entrada.txt', grafo)
    # Arquivo.carregar_arestas('entrada_sem_ciclo.txt', grafo)

    grafo.menu()



    print()

    ponto_articulacao = grafo.ponto_articulacao()

    print(f"Número de pontos de articulação: {len(ponto_articulacao)}")
    print(f"Pontos de articulação: {ponto_articulacao}")

    # Distância e Caminho Mínimo
    origem = 1  # Vértice inicial para o cálculo de caminhos mínimos
    print("Digite a origem: ")
    origem = int(input())
    print("\nCalculando distâncias e caminhos mínimos...")
    if(grafo.bellman_ford(origem)):
        grafo.imprimir_caminhos(origem)
    
if __name__ == "__main__":
    main()
