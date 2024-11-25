from Grafo import Grafo  
import Arquivo

def main():
    num_vertices = Arquivo.carregar_num_vertices('entrada.txt')

    print(f"Número de vértices: {num_vertices}")

    grafo = Grafo(num_vertices)

    Arquivo.carregar_arestas('entrada.txt', grafo)

    grafo.imprimir_grafo() 
    print()

    grafo.grau_vertices()

    grafo.componentes_conexas()

if __name__ == "__main__":
    main()
