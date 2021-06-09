import cv2
def capturaDir(inicio,fim,dir):
    # area de declaração
    video = cv2.VideoCapture(dir)
    inicio = inicio*100
    fim = 6000-fim*100
    count = 0
    imagens = []
    # remove inicio
    print("removendo inicio...")
    while count <= inicio:
        video.read()
        count += 1
    # separa as imagens
    print("separando as imagens...")
    while count<=fim:
        success,image = video.read()
        print(count)
        imagens.append(image)
        count += 1
    return imagens

def capturaCamera(inicio,fim):
    # area de declaração
    cam = cv2.VideoCapture(0)
    inicio = inicio*100
    fim = 6000-fim*100
    count = 0
    imagens = []
    # remove inicio
    print("removendo inicio...")
    while count <=inicio:
        cam.read()
        count += 1
    # separa as imagens
    while count<=fim:
        _,frame = cam.read()
        imagens.append(frame)
    cam.release()
    return imagens
