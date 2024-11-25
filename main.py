from Grafo import Grafo  
import Arquivo

def main():
    num_vertices = Arquivo.carregar_num_vertices('entrada.txt')
    # num_vertices = Arquivo.carregar_num_vertices('entrada_sem_ciclo.txt')

    print(f"Número de vértices: {num_vertices}")

    grafo = Grafo(num_vertices)

    Arquivo.carregar_arestas('entrada.txt', grafo)
    # Arquivo.carregar_arestas('entrada_sem_ciclo.txt', grafo)

    grafo.imprimir_grafo() 

    densidade = grafo.calcular_densidade()
    # print(f"Densidade do grafo: {densidade}")

    vizinhos = grafo.obter_vizinhos(5)
    # print(f"Vizinhos do vértice 5: {vizinhos}")

    ciclo_presente = grafo.detectar_ciclo()
    # print(f"Ciclo presente no grafo: {ciclo_presente}")



if __name__ == "__main__":
    main()
