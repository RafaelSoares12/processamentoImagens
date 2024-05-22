import cv2

def negativa_transformacao(imagem):
    imagem = cv2.imread(imagem)

    imagemNegativa = imagem.copy()
    
    altura, largura, _ = imagem.shape
    
    # Iterando sobre cada pixel da imagem
    for y in range(altura):
        for x in range(largura):
            # Obtendo o valor do pixel atual
            pixel = imagem[y, x]
            
            # Atribuindo o novo valor ao pixel na imagem negativa
            imagemNegativa[y, x] = 255 - pixel
    
    cv2.imwrite('imagemNegativa.png', imagemNegativa)

negativa_transformacao('imagemBinaria.png')
