import numpy as np
from graph_tool.generation import random_graph
from graph_tool.draw import graph_draw
from graph_tool.topology import random_spanning_tree
from graph_tool import GraphView, Graph
import networkx as nx
import matplotlib.pyplot as plt

def sample_k(max):
    accept = False
    while not accept:
        k = np.random.randint(1,max+1)
        accept = np.random.random() < 1.0/k
    return k

def estrela(n):
    arr = np.arange(n)
    np.random.shuffle(arr)
    centro = np.random.choice(arr)

    return np.array([[centro, i] for i in arr[arr != centro]])

def linha(n):
    arr = np.arange(n)
    np.random.shuffle(arr)

    return np.array([[arr[i], arr[i + 1]] for i in range(n - 1)])

def arvore (n):
    g = random_graph(n, lambda: sample_k(40), model="probabilistic-configuration",
        edge_probs=lambda i, k: 1.0 / (1 + abs(i - k)), directed=False, n_iter=100)

    tree = random_spanning_tree(g)
    u = GraphView(g, efilt=tree)

    return u.get_edges()

def lobster (n):
    g = nx.random_lobster(n, 0.49, 0.49)

    return np.array([[edge[0], edge[1]] for edge in g.edges])
    

# selecionar aleatoriamente o centro para a estrela
#print(lobster(10))

# enbaralhar um vertor de 0 a n - 1 para o caminho

# calcular a MST de um grafo normal aleatório

# gerar árvore aleatoriamente com um centro fixo

