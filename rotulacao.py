from PIL import Image 
from collections import deque

def rotulacao(caminhoImagem):
    imagem = Image.open(caminhoImagem).convert("RGB")
    largura, altura = imagem.size
    
    imagemRotulada = Image.new("RGB", (largura, altura))
    
    pixelsImagem = imagem.load()
    pixelsImagemRotulada = imagemRotulada.load()
    
    for x in range(largura): 
        for y in range(altura):  
            if pixelsImagemRotulada[x, y] == (0, 0, 0) and pixelsImagem[x, y] == (255, 255, 255):
                queue = deque([(x, y)])  
                while queue:
                    px, py = queue.popleft()  
                    pixelsImagemRotulada[px, py] = (255, 0, 0) 
    
    imagemRotulada.save('imagemRotulada.png')

rotulacao('caminhoImagem.png')
