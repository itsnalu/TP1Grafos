from GrafoApp import GrafoApp
from Grafo import Grafo
import Arquivo
import tkinter as tk
from tkinter import messagebox, filedialog
import sys

def main():

    print("1 - Saida no terminal")
    print("2 - Saida por interface")
    saida = int(input("Escolha a saida desejada:"))
    
    match(saida):
        case 1:
            arquivo = input("Digite o numero do arquivo + .txt:")
            num_vertices = Arquivo.carregar_num_vertices(arquivo)

            print(f"Número de vértices: {num_vertices}")

            grafo = Grafo(num_vertices)

            Arquivo.carregar_arestas(arquivo, grafo)

            grafo.menu()

        case 2:      
            root = tk.Tk()
            root.title("Teste de Interface Tkinter")
            label = tk.Label(root, text="Tkinter está funcionando!", font=("Arial", 16))
            label.pack(pady=20)
            root.mainloop()

        case _:
            print("Opção inválida. Encerrando o programa.")
            sys.exit(1)

if __name__ == "__main__":
    main()