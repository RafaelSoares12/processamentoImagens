import cv2

# Função para reflexão horizontal
def reflexao_horizontal(imagem):
    # Obtém as dimensões da imagem (altura, largura, canais de cor)
    altura, largura, _ = imagem.shape
    # Cria uma cópia da imagem para realizar a reflexão
    imagem_reflexao = imagem.copy()
    # Itera sobre as linhas da imagem
    for y in range(altura):
        # Itera sobre a metade das colunas da imagem
        for x in range(largura // 2):
            # Troca os pixels correspondentes horizontalmente
            temp = imagem_reflexao[y, x].copy()  # Pixel temporário para armazenar o valor original
            imagem_reflexao[y, x] = imagem_reflexao[y, largura - 1 - x]  # Troca o pixel atual com o correspondente na outra extremidade
            imagem_reflexao[y, largura - 1 - x] = temp  # Atualiza o pixel correspondente na outra extremidade com o valor original
    # Retorna a imagem com a reflexão horizontal aplicada
    return imagem_reflexao

# Função para reflexão vertical
def reflexao_vertical(imagem):
    # Obtém as dimensões da imagem (altura, largura, canais de cor)
    altura, largura, _ = imagem.shape
    # Cria uma cópia da imagem para realizar a reflexão
    imagem_reflexao = imagem.copy()
    # Itera sobre as colunas da imagem
    for x in range(largura):
        # Itera sobre a metade das linhas da imagem
        for y in range(altura // 2):
            # Troca os pixels correspondentes verticalmente
            temp = imagem_reflexao[y, x].copy()  # Pixel temporário para armazenar o valor original
            imagem_reflexao[y, x] = imagem_reflexao[altura - 1 - y, x]  # Troca o pixel atual com o correspondente na outra extremidade
            imagem_reflexao[altura - 1 - y, x] = temp  # Atualiza o pixel correspondente na outra extremidade com o valor original
    # Retorna a imagem com a reflexão vertical aplicada
    return imagem_reflexao

# Carregar a imagem
imagem = cv2.imread('image.png')

# Aplicar a reflexão horizontal
reflexao_horizontal_imagem = reflexao_horizontal(imagem)

# Aplicar a reflexão vertical
reflexao_vertical_imagem = reflexao_vertical(imagem)

# Mostrar as imagens resultantes
cv2.imshow('Original', imagem)
cv2.imshow('Reflexao Horizontal', reflexao_horizontal_imagem)
cv2.imshow('Reflexao Vertical', reflexao_vertical_imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
