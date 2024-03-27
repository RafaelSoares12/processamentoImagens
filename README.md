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

interpolacaoVizinho('caminho/para/sua/imagem.jpg', 300, 200)
```

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
