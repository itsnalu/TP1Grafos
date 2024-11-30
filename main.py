from Grafo import Grafo
import Arquivo
import tkinter as tk
from tkinter import messagebox, simpledialog
import sys

class GrafoApp:
    def __init__(self, master, grafo):
        self.master = master
        self.grafo = grafo
        master.title("Grafo App")
        master.configure(bg="#f0f8ff")  # Cor de fundo suave

        # Título da aplicação
        self.label = tk.Label(
            master,
            text="Escolha uma opção:",
            bg="#f0f8ff",
            font=("Arial", 14, "bold")
        )
        self.label.pack(pady=10)

        # Botões com estilos
        self.buttons = [
            ("Ordem do grafo", self.ordem),
            ("Tamanho do grafo", self.tamanho),
            ("Densidade do grafo", self.densidade),
            ("Obter vizinhos", self.obter_vizinhos),
            ("Lista de graus dos vértices", self.grau_vertices),
            ("Pontos de articulação", self.pontos_articulacao),
            ("Busca em largura", self.busca_em_largura),
            ("Componentes conexas", self.componentes_conexas),
            ("Detectar ciclo", self.detectar_ciclo),
            ("Distância e Caminho Mínimo", self.caminho_minimo),
            ("Sair", self.sair)
        ]

        # Criação de botões
        for (text, func) in self.buttons:
            button = tk.Button(
                master,
                text=text,
                command=func,
                width=30,
                height=2,
                bg="#4682b4",  # Azul claro
                fg="white",  # Texto branco
                font=("Arial", 10, "bold"),
                relief="raised"
            )
            button.pack(pady=5)

        # Área de resultados
        self.result_text = tk.Text(
            master,
            height=10,
            width=50,
            bg="#ffffff",  # Fundo branco
            fg="#000000",  # Texto preto
            font=("Courier", 10)
        )
        self.result_text.pack(pady=10)

    # Métodos (mesmo código das funções anteriores)
    def ordem(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        result = self.grafo.ordem()
        self.result_text.insert(tk.END, f"Ordem do grafo: {result}\n")

    def tamanho(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        result = self.grafo.tamanho()
        self.result_text.insert(tk.END, f"Tamanho do grafo: {result}\n")

    def densidade(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        result = self.grafo.calcular_densidade()
        self.result_text.insert(tk.END, f"Densidade do grafo: {result}\n")

    def obter_vizinhos(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        try:
            vertice = simpledialog.askinteger(
                "Obter Vizinhos",
                "Digite o vértice para obter os vizinhos:"
            )
            if vertice is None:
                self.result_text.insert(tk.END, "Operação cancelada pelo usuário.\n")
                return

            result = self.grafo.obter_vizinhos(vertice)
            self.result_text.insert(tk.END, f"Vizinhos do vértice {vertice}: {result}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Erro: {str(e)}\n")

    def grau_vertices(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        try:
            graus = []
            for i in range(self.grafo.num_vertices):
                grau = 0
                for j in range(self.grafo.num_vertices):
                    if self.grafo.matriz_adj[i][j] != 0:
                        grau += 1
                graus.append(grau)

            self.result_text.insert(tk.END, "Graus dos vértices:\n")
            for i, grau in enumerate(graus, start=1):
                self.result_text.insert(tk.END, f"Vértice {i}: Grau {grau}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Erro ao calcular os graus dos vértices: {str(e)}\n")

    def pontos_articulacao(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        result = self.grafo.ponto_articulacao()
        self.result_text.insert(tk.END, f"Número de pontos de articulação: {len(result)}\n")
        self.result_text.insert(tk.END, f"Pontos de articulação: {result}\n")

    def busca_em_largura(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        try:
            vertice_inicial = simpledialog.askinteger(
                "Busca em Largura",
                "Digite o vértice inicial para a busca em largura:"
            )
            if vertice_inicial is None:
                self.result_text.insert(tk.END, "Operação cancelada pelo usuário.\n")
                return

            sequencia, arvore, nao_arvore = self.grafo.busca_em_largura(vertice_inicial)
            self.result_text.insert(tk.END, f"Sequência de vértices visitados: {sequencia}\n")
            self.result_text.insert(tk.END, f"Arestas da árvore de busca: {arvore}\n")
            self.result_text.insert(tk.END, f"Arestas que não fazem parte da árvore de busca: {nao_arvore}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Erro: {str(e)}\n")

    def componentes_conexas(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        try:
            num_componentes = self.grafo.roy_componentes_conexas()
            self.result_text.insert(tk.END, f"O grafo possui {num_componentes} componente(s) conexa(s).\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Erro ao calcular os componentes conexos: {str(e)}\n")

    def detectar_ciclo(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        result = self.grafo.detectar_ciclo()
        self.result_text.insert(tk.END, f"Ciclo presente no grafo: {'Sim' if result else 'Não'}\n")

    def caminho_minimo(self):
        self.result_text.delete("1.0", tk.END)  # Limpa mensagens anteriores
        try:
            origem = simpledialog.askinteger(
                "Distância e Caminho Mínimo",
                "Digite o vértice de origem:"
            )
            if origem is None:
                self.result_text.insert(tk.END, "Operação cancelada pelo usuário.\n")
                return

            if self.grafo.bellman_ford(origem):
                caminhos = self.grafo.imprimir_caminhos(origem)
                self.result_text.insert(tk.END, caminhos)
            else:
                self.result_text.insert(tk.END, "Erro ao calcular caminhos mínimos: Ciclo de peso negativo detectado!\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Erro: {str(e)}\n")



    def sair(self):
        self.master.destroy()  # Fecha a janela do Tkinter
        sys.exit()  # Fecha o terminal (o script termina completamente)


def main():
    # Criação da janela principal temporária para solicitar o arquivo
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal enquanto solicita o arquivo

    # Solicita o nome do arquivo de entrada
    arquivo_entrada = simpledialog.askstring(
        "Entrada de Arquivo",
        "Digite o nome do arquivo de entrada (ex: entrada.txt):"
    )

    # Verifica se o usuário cancelou ou não inseriu o nome
    if not arquivo_entrada:
        messagebox.showerror("Erro", "Nenhum arquivo especificado. Encerrando o programa.")
        return

    try:
        # Carrega o grafo usando o arquivo especificado
        num_vertices = Arquivo.carregar_num_vertices(arquivo_entrada)
        grafo = Grafo(num_vertices)
        Arquivo.carregar_arestas(arquivo_entrada, grafo)

        # Exibe a aplicação principal
        root = tk.Tk()
        app = GrafoApp(root, grafo)
        root.mainloop()

    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


if __name__ == "__main__":
    main()
