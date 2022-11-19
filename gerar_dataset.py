import numpy as np
from gerar_arvores import estrela, arvore, linha, lobster

def gerar_arvores (qtdInstancias, qtdVerticesPossiveis):
    i = 0
    X = []
    Y = []
    tipos = ['1', '2', '3', '4']
    while i < qtdInstancias:
        n = np.random.choice(qtdVerticesPossiveis, 1)[0]
        tipo = np.random.choice(tipos, 1)[0]
        
        try:
            if tipo == '1':
                X.append(estrela(n))
            elif tipo == '2':
                X.append(linha(n))
            elif tipo == '3':
                X.append(arvore(n))
            else:
                X.append(lobster(n))

            Y.append(tipo)

            i += 1
            print(i)
        except Exception as e:
            pass

    return (X, Y)

qtdInstanciasTreino = 60000
qtdInstanciasTeste = 10000
tamanhosArvore = [10, 20, 30, 40, 50, 60]

X_treino, Y_treino = gerar_arvores(qtdInstanciasTreino, tamanhosArvore)
X_teste, Y_teste = gerar_arvores(qtdInstanciasTeste, tamanhosArvore)

#print(X_treino[:10])
#print(Y_treino[:10])

np.savez("arvores_treino.npz", X=np.array(X_treino, dtype=object), Y=np.array(Y_treino, dtype=object))
np.savez("arvores_teste.npz", X=np.array(X_teste, dtype=object), Y=np.array(Y_teste, dtype=object))
