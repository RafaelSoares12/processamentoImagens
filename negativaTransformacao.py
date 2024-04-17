import cv2

def negativa_transformacao(img):
    # Criando uma cópia da imagem
    img_negativa = img.copy()
    
    # Obtendo a altura e largura da imagem
    altura, largura = img.shape[:2]
    
    # Iterando sobre cada pixel da imagem
    for y in range(altura):
        for x in range(largura):
            # Obtendo o valor do pixel atual
            pixel = img[y, x]
            
            # Calculando o novo valor do pixel para a transformação negativa
            novo_valor = 255 - pixel
            
            # Atribuindo o novo valor ao pixel na imagem negativa
            img_negativa[y, x] = novo_valor
    
    return img_negativa

# Carregando a imagem
img = cv2.imread('resultado_subtracao.png')

# Convertendo para escala de cinza, se necessário
if len(img.shape) > 2:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicando a transformação negativa
img_transformada = negativa_transformacao(img)

# Mostrando a imagem original e a imagem transformada
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Transformada - Negativa', img_transformada)
cv2.waitKey(0)
cv2.destroyAllWindows()
