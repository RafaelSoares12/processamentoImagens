import cv2
import numpy as np

def adicao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    novaImagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            # Verifica se a coordenada (x, y) está dentro das dimensões da primeira imagem.
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                # Se estiver dentro das dimensões da primeira imagem, adiciona o valor do pixel correspondente na primeira imagem à nova imagem.
                novaImagem[x, y] += imagem1[x, y]
            
            # Verifica se a coordenada (x, y) está dentro das dimensões da segunda imagem.
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                # Se estiver dentro das dimensões da segunda imagem, adiciona o valor do pixel correspondente na segunda imagem à nova imagem.
                novaImagem[x, y] += imagem2[x, y]

    cv2.imwrite('resultadoSoma.png', novaImagem)

def subtracao(imagem01, imagem02):
    imagem1 = cv2.imread(imagem01)
    imagem2 = cv2.imread(imagem02)

    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    novaImagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            # Verifica se a coordenada (x, y) está dentro das dimensões da primeira imagem.
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                # Se estiver dentro das dimensões da primeira imagem, adiciona o valor do pixel correspondente na primeira imagem à nova imagem.
                novaImagem[x, y] += imagem1[x, y]
            
            # Verifica se a coordenada (x, y) está dentro das dimensões da segunda imagem.
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                # Se estiver dentro das dimensões da segunda imagem, subtrai o valor do pixel correspondente na segunda imagem da nova imagem.
                novaImagem[x, y] -= imagem2[x, y]

    cv2.imwrite('resultadoSubtracao.png', novaImagem)

adicao('image.png', 'imgBinaria.png')
subtracao('image.png', 'imgBinaria.png')
