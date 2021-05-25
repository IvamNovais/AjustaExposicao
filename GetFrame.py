import cv2
import AjustaExposicao

def GetFrames(dir, inicio, fim):
  try:
    video = cv2.VideoCapture(dir)
  except:
    print(f'erro ao carregar')
    return False
  inicio = inicio*100
  fim = 6000-fim*100
  count = 1
  print("removendo inicio...")
  while count <=inicio:
    video.read()
    count += 1
  imagens = []
  print("separando as imagens...")
  while count<=fim:
    success,image = video.read()
    print(count)
    try:
      imagens.append(AjustaExposicao.acertaBrilho(image))
    except:
      print(f'ocorreu um erro na imagem {count}')
    count += 1
  return imagens