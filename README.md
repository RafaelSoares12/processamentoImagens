# Processamento de Imagens

## Descrição
Este repositório contém os trabalhos práticos da disciplina de Processamento de Imagens do curso de Ciência da Computação da Universidade Federal do Tocantins.

## Instalação
Antes de executar qualquer código deste repositório, certifique-se de instalar o Pillow, que é utilizado para manipulação de imagens em Python. Você pode instalar o Pillow usando o seguinte comando:

```bash
pip install Pillow
```

# Trabalhos

## Trabalho Prático 01
### Função de Interpolação por Vizinho
A função `interpolacaoVizinho` recebe o caminho da imagem, a nova largura e a nova altura desejadas como entrada e retorna a imagem redimensionada usando interpolação por vizinho mais próximo.

Exemplo de uso:

```python
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
            
            proxPixel = imagem.getpixel((originalX, originalY))
            
            novaImagem.putpixel((x, y), proxPixel)
    
    nomeRedimensionada = imagemPath.split('.')[0] + '_redimensionada.jpg'
    return novaImagem.save(nomeRedimensionada)

# Chamando a função
interpolacaoVizinho('caminho/para/sua/imagem.jpg', 300, 200)
```

### Função de Interpolação Bilinear
A função `interpolacaoBilinear` recebe o caminho da imagem, a nova largura e a nova altura desejadas como entrada e retorna a imagem interpolada.

Exemplo de uso:

```python
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
    
    return novaImagem.save(imagemPath.split('.')[0] + '_interpolada.jpg')

# Chamando a função
interpolacaoBilinear('caminho/para/sua/imagem.jpg', 300, 200)
```

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
