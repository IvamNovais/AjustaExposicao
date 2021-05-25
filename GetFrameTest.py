import GetFrame
import cv2

ignorarInicio = 15 #tempo em segundos que sera removido no inicio do video
tirarFim = 15 #tempo em segundos que sera removido no fim do video
# recebe o diretorio do video , o tamanho do corte inicial em segundos e o tanho do corete final em segundos
dir = 'c:\\Users\\ivamn\\Documents\\estudos\\sis 7p\\pexinho\\videos\\Basler_acA640-120uc__21379673__20201213_080543930.avi'
imagens = GetFrame.GetFrames(dir,ignorarInicio,tirarFim)
cv2.imwrite("img.jpg",imagens[1000])