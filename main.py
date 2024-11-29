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
if __name__ == "__main__":
    main()
