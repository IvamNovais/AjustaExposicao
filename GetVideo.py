import cv2
import AjustaExposicao
def capturaDir(inicio,fim,dir):
    # area de declaração
    video = cv2.VideoCapture(dir)
    inicio = inicio*100
    fim = 6000-fim*100
    count = 0
    imagens = []
    # remove inicio
    while count <= inicio:
        video.read()
        count += 1
    # separa as imagens
    while count<=fim:
        success,image = video.read()
        imagens.append(AjustaExposicao.acertaBrilho(image))
        count += 1
    return imagens

def capturaCamera(inicio,fim,camera):
    # area de declaração
    cam = cv2.VideoCapture(camera)
    inicio = inicio*100
    fim = 6000-fim*100
    count = 0
    imagens = []
    # remove inicio
    while count <=inicio:
        cam.read()
        count += 1
    # separa as imagens
    while count<=fim:
        _,image = cam.read()
        imagens.append(AjustaExposicao.acertaBrilho(image))
    cam.release()
    return imagens