import numpy as np
import wisardpkg as wp
from codificadores_t2 import filtrar_vazio, preordem_codificador, lista_aresta_codificador
#from graph_tool.draw import graph_draw
#from graph_tool import Graph

def accuracy(y_pred, y_target):
  return np.where(np.array(y_pred) == np.array(y_target), 1, 0).sum()/len(y_target)

def edge_list_code(X_treino, Y_treino, X_teste, Y_teste, codificador):
  kc = wp.KernelCanvas(2, 100, bitsPerKernel=10)

  X_treino_kernel = [kc.transform(a) for a in codificador(X_treino)]

  modelK = wp.Wisard(22)
  modelK.train(X_treino_kernel, Y_treino)

  X_teste_kernel = [kc.transform(a) for a in codificador(X_teste)]
  pred = modelK.classify(X_teste_kernel)

  print(accuracy(pred, Y_teste))

def preorder_code(X_treino, Y_treino, X_teste, Y_teste, codificador):
  kc = wp.KernelCanvas(1, 30, bitsPerKernel=10)

  X_treino_kernel = [kc.transform(a) for a in codificador(X_treino)]

  modelK = wp.Wisard(22)
  modelK.train(X_treino_kernel, Y_treino)

  X_teste_kernel = [kc.transform(a) for a in codificador(X_teste)]
  pred = modelK.classify(X_teste_kernel)

  print(accuracy(pred, Y_teste))

data = np.load('arvores_treino.npz', allow_pickle=True)
X_treino, Y_treino = filtrar_vazio(data['X'], data['Y'])

data = np.load('arvores_teste.npz', allow_pickle=True)
X_teste, Y_teste = filtrar_vazio(data['X'], data['Y'])

#print(X_treino[0], Y_treino[0])

#edge_list_code(X_treino, Y_treino, X_teste, Y_teste, lista_aresta_codificador)
preorder_code(X_treino, Y_treino, X_teste, Y_teste, preordem_codificador)