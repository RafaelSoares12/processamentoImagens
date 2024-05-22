import cv2

def reflexaoHorizontal(imagem):
    imagem = cv2.imread(imagem)
    altura, largura, _ = imagem.shape
    imagemReflexao = imagem.copy()

    for y in range(altura):
        for x in range(largura // 2):
            temp = imagemReflexao[y, x].copy()  # Pixel temporário para armazenar o valor original
            imagemReflexao[y, x] = imagemReflexao[y, largura - 1 - x]  # Troca o pixel atual com o correspondente na outra extremidade
            imagemReflexao[y, largura - 1 - x] = temp  # Atualiza o pixel correspondente na outra extremidade com o valor original

    cv2.imwrite('imagemReflexaoHorizontal.png', imagemReflexao)

def reflexaoVertical(imagem):
    imagem = cv2.imread(imagem)
    altura, largura, _ = imagem.shape
    imagemReflexao = imagem.copy()

    for x in range(largura):
        for y in range(altura // 2):
            temp = imagemReflexao[y, x].copy()  # Pixel temporário para armazenar o valor original
            imagemReflexao[y, x] = imagemReflexao[altura - 1 - y, x]  # Troca o pixel atual com o correspondente na outra extremidade
            imagemReflexao[altura - 1 - y, x] = temp  # Atualiza o pixel correspondente na outra extremidade com o valor original
    
    cv2.imwrite('imagemReflexaoVertical.png', imagemReflexao)

reflexaoHorizontal('image.png')
reflexaoVertical('image.png')