import numpy as np
import wisardpkg as wp
from codificadores_t2 import filtrar_vazio, preordem_codificador, lista_aresta_codificador, node2vec_codificador, struct2vec_codificador
import time
#from graph_tool.draw import graph_draw
#from graph_tool import Graph

def wisard(i):
    return wp.Wisard(i)

def clusWisard(i):
    return wp.ClusWisard(i, 0.1, 6000, 100)

def accuracy(y_pred, y_target):
  return np.where(np.array(y_pred) == np.array(y_target), 1, 0).sum()/len(y_target)

def executar_testes(X_treino, Y_treino, X_teste, Y_teste, codificador, kc):
  X_treino_kernel = [kc.transform(a) for a in codificador(X_treino)]

  modelK = wp.Wisard(22)
  modelK.train(X_treino_kernel, Y_treino)

  X_teste_kernel = [kc.transform(a) for a in codificador(X_teste)]
  pred = modelK.classify(X_teste_kernel)

  print(accuracy(pred, Y_teste))

def rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, codificador, kc, buildModel, nome):
    X_treino_kernel = [kc.transform(a) for a in codificador(X_treino)]
    X_teste_kernel = [kc.transform(a) for a in codificador(X_teste)]
    rodadas = 3
    with open("{}.csv".format(nome), 'w') as file:
      melhorAcc = 0
      melhorPred = None
      for i in range(2, 65):
          soma = 0
          soma_treino = 0
          soma_predicao = 0
          
          for j in range(rodadas):
              print("Testando a {0}-tupla pela {1}ª vez".format(i, j + 1))
              model = buildModel(i)
              
              start = time.time()
              model.train(X_treino_kernel, Y_treino)
              soma_treino += (time.time() - start)
              
              start = time.time()
              pred = model.classify(X_teste_kernel)
              soma_predicao += (time.time() - start)

              acc = accuracy(pred, Y_teste)
              soma += acc

              if acc > melhorAcc:
                melhorAcc = acc
                melhorPred = pred
          file.write("{},{},{},{}\n".format(i, soma / rodadas, soma_treino / rodadas, soma_predicao / rodadas))

      for y in melhorPred:
        file.write("{}\n".format(y))

data = np.load('arvores_treino.npz', allow_pickle=True)
X_treino, Y_treino = filtrar_vazio(data['X'], data['Y'])

data = np.load('arvores_teste.npz', allow_pickle=True)
X_teste, Y_teste = filtrar_vazio(data['X'], data['Y'])

kc_edge_list = wp.KernelCanvas(2, 1000, bitsPerKernel=10)
kc_preorder = wp.KernelCanvas(1, 1000, bitsPerKernel=10)
kc_node2vec = wp.KernelCanvas(10, 100, bitsPerKernel=10)

rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, lista_aresta_codificador, kc_edge_list, wisard, 'wisard_edge_list_7000')
rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, lista_aresta_codificador, kc_edge_list, wisard, 'cluswisard_edge_list_7000')

rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, preordem_codificador, kc_preorder, wisard, 'wisard_pre_ordem_7000')
rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, preordem_codificador, kc_preorder, wisard, 'cluswisard_pre_ordem_7000')


rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, node2vec_codificador, kc_node2vec, wisard, 'wisard_node2vec_7000')
rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, node2vec_codificador, kc_node2vec, wisard, 'cluswisard_node2vec_7000')

rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, struct2vec_codificador, kc_node2vec, wisard, 'wisard_struct2vec')
rodarExperimentos(X_treino, Y_treino, X_teste, Y_teste, struct2vec_codificador, kc_node2vec, wisard, 'cluswisard_struct2vec')