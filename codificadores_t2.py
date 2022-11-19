import networkx as nx
import numpy as np

def filtrar_vazio(X, Y):
    X_filtrado = []
    Y_filtrado = []

    for index, a in enumerate(X):
        if len(a) > 0:
            X_filtrado.append(a)
            Y_filtrado.append(Y[index])

    return (np.array(X_filtrado, dtype=object), np.array(Y_filtrado, dtype=object))

def lista_aresta_codificador(X):
    return X

def preorder (edges):
  G = nx.Graph()
  G.add_edges_from([(e[0], e[1]) for e in edges])
  return [[v] for v in nx.dfs_preorder_nodes(G, source=0)]

def preordem_codificador (X):
    return [preorder(a) for a in X]
