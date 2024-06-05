import numpy as np 
from PIL import Image  

def dilatar(imagem, kernel):
    alturaKernel, larguraKernel = kernel.shape  
    padAltura, padLargura = alturaKernel // 2, larguraKernel // 2  

    imagemComPadding = np.pad(imagem, ((padAltura, padAltura), (padLargura, padLargura)), mode='constant', constant_values=0)
    imagemDilatada = np.zeros_like(imagem)  

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            # Seleciona a vizinhança do pixel na imagem original com padding
            vizinhanca = imagemComPadding[i:i+alturaKernel, j:j+larguraKernel]
            # Multiplica cada elemento da vizinhança pelo elemento correspondente no kernel e calcula o valor max dos elementos resultantes da multiplicação
            valorMax = np.max(vizinhanca * kernel)
            imagemDilatada[i, j] = valorMax

    return imagemDilatada  

def erodir(imagem, kernel):
    alturaKernel, larguraKernel = kernel.shape 
    padAltura, padLargura = alturaKernel // 2, larguraKernel // 2  

    imagemComPadding = np.pad(imagem, ((padAltura, padAltura), (padLargura, padLargura)), mode='constant', constant_values=255)
    imagemErodida = np.zeros_like(imagem)  

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            vizinhanca = imagemComPadding[i:i+alturaKernel, j:j+larguraKernel]
            valorMin = np.min(vizinhanca * kernel)
            imagemErodida[i, j] = valorMin

    return imagemErodida  

def carregarImagem(caminho_imagem):
    imagem = Image.open(caminho_imagem).convert('L')
    return np.array(imagem) 

def salvarImg(array_imagem, caminho_saida):

    imagem = Image.fromarray(array_imagem)  
    imagem.save(caminho_saida)  

entrada = 'imagem.jpg'
    
imagemDilatadaPath = 'imagemDilatada.jpg'
imagemErodidaPath = 'imagemErodida.jpg'
    
imagem = carregarImagem(entrada)
    
kernel = np.ones((3, 3), dtype=np.uint8)

imagemDilatada = dilatar(imagem, kernel)
imagemErodida = erodir(imagem, kernel)
    
salvarImg(imagemDilatada, imagemDilatadaPath)
salvarImg(imagemErodida, imagemErodidaPath)