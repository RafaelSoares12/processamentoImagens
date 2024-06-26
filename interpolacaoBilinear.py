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
                        
            # Determina os quatro pixels mais próximos na imagem original em torno das coordenadas calculadas.
            x1 = int(originalX)
            y1 = int(originalY)
            x2 = min(x1 + 1, largura - 1)
            y2 = min(y1 + 1, altura - 1)
            
            # Obtém os valores dos quatro pixels mais próximos na imagem original.
            q11 = image.getpixel((x1, y1))
            q21 = image.getpixel((x2, y1))
            q12 = image.getpixel((x1, y2))
            q22 = image.getpixel((x2, y2))
            
            # Calcula as distâncias entre as coordenadas reais e as coordenadas dos pixels.
            dx = originalX - x1
            dy = originalY - y1

            # Calcula os pesos para cada um dos quatro pixels com base na distância entre as coordenadas reais e as coordenadas dos pixels.
            # Interpola os valores de pixel na nova imagem, aplicando uma média ponderada dos valores dos pixels vizinhos na imagem original.
            pixelInterpolado = (
                int((1 - dx) * (1 - dy) * q11[0] + dx * (1 - dy) * q21[0] + (1 - dx) * dy * q12[0] + dx * dy * q22[0]),
                int((1 - dx) * (1 - dy) * q11[1] + dx * (1 - dy) * q21[1] + (1 - dx) * dy * q12[1] + dx * dy * q22[1]),
                int((1 - dx) * (1 - dy) * q11[2] + dx * (1 - dy) * q21[2] + (1 - dx) * dy * q12[2] + dx * dy * q22[2])
            )

            novaImagem.putpixel((x, y), pixelInterpolado)
    
    return novaImagem.save(imagemPath.split('.')[0] + 'interpolada.jpg')

interpolacaoBilinear('image.png', 300, 200)