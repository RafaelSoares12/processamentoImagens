from PIL import Image

def interpolacaoVizinho(imagemPath, novaLargura, novaAltura):
    
    imagem = Image.open(imagemPath)
    largura, altura = imagem.size
    
    escalaX = largura / novaLargura
    escalaY = altura / novaAltura
    
    novaImagem = Image.new("RGB", (novaLargura, novaAltura))
    
    for y in range(novaAltura):
        for x in range(novaLargura):
            originalX = int(x * escalaX)
            originalY = int(y * escalaY)
            
            # Obtém o valor do pixel mais próximo na imagem original (vizinho mais próximo).
            proxPixel = imagem.getpixel((originalX, originalY))
            
            novaImagem.putpixel((x, y), proxPixel)
    
    return novaImagem.save(imagemPath.split('.')[0] + '-redimensionada.jpg')
