import cv2
import os

caminho_da_imagem = 'pasta/img/imagem3.jpg'

carregaAlgoritmo = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')


imagem = cv2.imread(caminho_da_imagem)
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagem_cinza)

print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    

cv2.imshow("Formas ", imagem)
cv2.waitKey()
