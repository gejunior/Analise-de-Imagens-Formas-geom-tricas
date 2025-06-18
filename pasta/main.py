import cv2
import numpy as np

# Carregar a imagem
# imagem = cv2.imread('pasta/img/circle.png')
imagem = cv2.imread('pasta/img/imagem2.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# # Aplicar filtro de borda
_, limiar = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
contornos, _ = cv2.findContours(limiar, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos:
    # Aproximar o contorno para reduzir número de pontos
    epsilon = 0.02 * cv2.arcLength(contorno, True)
    aproximacao = cv2.approxPolyDP(contorno, epsilon, True)

    # Detectar formas pelo número de vértices
    if len(aproximacao) == 3:
        # forma = "Triangulo"
        forma = "1"
    elif len(aproximacao) == 4:
        # forma = "Quadrado ou Retangulo"
        forma = "2"
    elif len(aproximacao) > 4:
        # forma = "Circulo ou Poligono"
        forma = "3"

    # Desenhar os contornos e nome da forma na imagem
    cv2.drawContours(imagem, [aproximacao], 0, (0, 255, 0), 3)
    x, y = aproximacao.ravel()[0], aproximacao.ravel()[1]
    cv2.putText(imagem, forma, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Mostrar o resultado
cv2.imshow("Formas Detectadas", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()