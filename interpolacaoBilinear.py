from PIL import Image

def interpolacaoBilinear(imagemPath, novaLargura, novaAltura):

    image = Image.open(imagemPath)
    
    largura, altura = image.size
    
    escalaX = largura / novaLargura
    escalaY = altura / novaAltura
    
    novaImagem = Image.new("RGB", (novaLargura, novaAltura))
    
    for y in range(novaAltura):
        for x in range(novaLargura):
            originalX = x * escalaX
            originalY = y * escalaY
            
            x1 = int(originalX)
            y1 = int(originalY)
            x2 = min(x1 + 1, largura - 1)
            y2 = min(y1 + 1, altura - 1)
            
            q11 = image.getpixel((x1, y1))
            q21 = image.getpixel((x2, y1))
            q12 = image.getpixel((x1, y2))
            q22 = image.getpixel((x2, y2))
            
            dx = originalX - x1
            dy = originalY - y1
            pixelInterpolado = (
                int((1 - dx) * (1 - dy) * q11[0] + dx * (1 - dy) * q21[0] + (1 - dx) * dy * q12[0] + dx * dy * q22[0]),
                int((1 - dx) * (1 - dy) * q11[1] + dx * (1 - dy) * q21[1] + (1 - dx) * dy * q12[1] + dx * dy * q22[1]),
                int((1 - dx) * (1 - dy) * q11[2] + dx * (1 - dy) * q21[2] + (1 - dx) * dy * q12[2] + dx * dy * q22[2])
            )
            
            novaImagem.putpixel((x, y), pixelInterpolado)
    
    return novaImagem.save(imagemPath.split('.')[0] + 'interpolada.jpg')

#  de uso
interpolacaoBilinear('36-atencao-area-de-teste.jpg', 300, 200)
