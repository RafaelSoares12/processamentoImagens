import cv2
import numpy as np

def aplicarFiltroSobel(imagem):
    # Converte a imagem para um array numpy
    imagem = np.array(imagem)
    
    # Define as máscaras de Sobel
    sobelX = np.array([[-1, 0, 1], 
                       [-2, 0, 2], 
                       [-1, 0, 1]])
    
    sobelY = np.array([[-1, -2, -1], 
                       [ 0,  0,  0], 
                       [ 1,  2,  1]])
    
    # Cria imagens para armazenar os gradientes nas direções x e y
    gradienteX = np.zeros(imagem.shape)
    gradienteY = np.zeros(imagem.shape)
    gradienteMagnitude = np.zeros(imagem.shape)
    
    # Define a função de convolução
    def convoluir(imagem, kernel):
        # Obtém as dimensões do kernel e da imagem
        alturaKernel, larguraKernel = kernel.shape
        alturaImagem, larguraImagem = imagem.shape
        
        # Adiciona padding à imagem para tratar os pixels nas bordas
        imagemPadded = np.pad(imagem, ((1, 1), (1, 1)), 'constant')
        
        # Cria uma nova imagem para armazenar o resultado da convolução
        novaImagem = np.zeros_like(imagem)
        
        # Percorre cada pixel da imagem
        for i in range(alturaImagem):
            for j in range(larguraImagem):
                # Seleciona a região da imagem que será multiplicada pelo kernel
                regiao = imagemPadded[i:i + alturaKernel, j:j + larguraKernel]
                
                # Calcula a soma dos produtos da região pelo kernel
                novaImagem[i, j] = np.sum(regiao * kernel)
                
        return novaImagem
    
    # Aplica as máscaras de Sobel à imagem para calcular os gradientes
    gradienteX = convoluir(imagem, sobelX)
    gradienteY = convoluir(imagem, sobelY)
    
    # Calcula a magnitude do gradiente combinando os gradientes x e y
    gradienteMagnitude = np.sqrt(gradienteX**2 + gradienteY**2)
    
    return gradienteX, gradienteY, gradienteMagnitude

imagem = cv2.imread("imgBinaria.png", cv2.IMREAD_GRAYSCALE)

# Aplicar o filtro Sobel
gradienteX, gradienteY, gradienteMagnitude = aplicarFiltroSobel(imagem)

# Exibir os resultados
cv2.imshow("Gradiente X", gradienteX.astype(np.uint8))
cv2.imshow("Gradiente Y", gradienteY.astype(np.uint8))
cv2.imshow("Gradiente Magnitude", gradienteMagnitude.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
