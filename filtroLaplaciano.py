import cv2
import numpy as np

# Função para aplicar o filtro laplaciano
def aplicar_filtro_laplaciano(imagem, kernel, tratar_negativos=False):
    # Obter as dimensões da imagem e do kernel
    linhas, colunas = imagem.shape
    k_linhas, k_colunas = kernel.shape
    
    # Inicializar a imagem resultante com zeros
    resultado = np.zeros((linhas, colunas), dtype=np.float32)
    
    # Preencher as bordas da imagem com zeros
    imagem_preenchida = np.pad(imagem, ((2, 2), (2, 2)), mode='constant', constant_values=0)
    
    # Percorrer a imagem
    for i in range(2, linhas + 2):
        for j in range(2, colunas + 2):
            # Calcular os limites para aplicar o kernel
            r_min = i - 2
            r_max = i + 3
            c_min = j - 2
            c_max = j + 3
            
            # Aplicar o kernel à região da imagem
            patch = imagem_preenchida[r_min:r_max, c_min:c_max]
            
            # Ajustar o tamanho do patch para corresponder ao tamanho do kernel
            if patch.shape != kernel.shape:
                patch = imagem_preenchida[i - k_linhas // 2:i + k_linhas // 2 + 1, j - k_colunas // 2:j + k_colunas // 2 + 1]
                
            resultado[i - 2, j - 2] = np.sum(patch * kernel)
    
    # Tratamento de valores negativos
    if tratar_negativos:
        resultado = np.where(resultado < 0, 0, resultado)
    
    # Normalizar a imagem resultante
    resultado = np.clip(resultado, 0, 255).astype(np.uint8)
    
    return resultado

# Máscaras laplacianas
laplaciano3x3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplaciano5x5 = np.array([[-1, -1, -1, -1, -1], [-1, 1, 1, 1, -1], [-1, 1, 1, 1, -1], [-1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]])
laplaciano1Derivada3x3 = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])
laplaciano2Derivada3x3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

# Carregar imagem de exemplo
imagem = cv2.imread("imgBinaria.png", cv2.IMREAD_GRAYSCALE)

# Aplicar o filtro laplaciano com tratamento de valores negativos
resultado1 = aplicar_filtro_laplaciano(imagem, laplaciano3x3, tratar_negativos=True)
resultado2 = aplicar_filtro_laplaciano(imagem, laplaciano5x5, tratar_negativos=True)
resultado3 = aplicar_filtro_laplaciano(imagem, laplaciano1Derivada3x3, tratar_negativos=True)
resultado4 = aplicar_filtro_laplaciano(imagem, laplaciano2Derivada3x3, tratar_negativos=True)

# Exibir os resultados
cv2.imshow("Original", imagem)
cv2.imshow("Laplaciano 3x3", resultado1)
cv2.imshow("Laplaciano 5x5", resultado2)
cv2.imshow("Laplaciano 1ª Derivada 3x3", resultado3)
cv2.imshow("Laplaciano 2ª Derivada 3x3", resultado4)
cv2.waitKey(0)
cv2.destroyAllWindows()
