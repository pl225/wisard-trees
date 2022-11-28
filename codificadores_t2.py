import networkx as nx
import numpy as np
from parser_node2vec import main as parse_node2vec
from args import Args
from parser_struct2vec import main as parse_struct2vec

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

def node2vec_codificador (X):
    return [parse_node2vec(Args(x)) for x in X]

def struct2vec_codificador (X):
    return [parse_struct2vec(Args(x)) for x in X]