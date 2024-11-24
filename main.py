from Grafo import Grafo  
import Arquivo

def main():
    num_vertices = Arquivo.carregar_num_vertices('entrada.txt')

    print(f"Número de vértices: {num_vertices}")

    grafo = Grafo(num_vertices)

    Arquivo.carregar_arestas('entrada.txt', grafo)

    grafo.menu()

if __name__ == "__main__":
    main()
