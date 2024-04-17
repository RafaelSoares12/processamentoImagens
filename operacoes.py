import cv2
import numpy as np

def adicao(imagem_01, imagem_02, nome_saida):
    # Carregar as imagens
    imagem1 = cv2.imread(imagem_01)
    imagem2 = cv2.imread(imagem_02)

    # Verificar se as imagens têm o mesmo tamanho
    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                nova_imagem[x, y] += imagem1[x, y]
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                nova_imagem[x, y] += imagem2[x, y]

    # Salvar a imagem resultante
    cv2.imwrite(nome_saida, nova_imagem)

def subtracao(imagem_01, imagem_02, nome_saida):
    # Carregar as imagens
    imagem1 = cv2.imread(imagem_01)
    imagem2 = cv2.imread(imagem_02)

    # Verificar se as imagens têm o mesmo tamanho
    largura = max(imagem1.shape[0], imagem2.shape[0])
    altura = max(imagem1.shape[1], imagem2.shape[1])

    nova_imagem = np.zeros((largura, altura, 3), dtype=np.uint8)

    for x in range(largura):
        for y in range(altura):
            if x < imagem1.shape[0] and y < imagem1.shape[1]:
                nova_imagem[x, y] += imagem1[x, y]
            if x < imagem2.shape[0] and y < imagem2.shape[1]:
                nova_imagem[x, y] -= imagem2[x, y]

    # Salvar a imagem resultante
    cv2.imwrite(nome_saida, nova_imagem)

adicao('image.png', 'imgBinaria.png', 'resultado_adicao.png')
subtracao('image.png', 'imgBinaria.png', 'resultado_subtracao.png')
