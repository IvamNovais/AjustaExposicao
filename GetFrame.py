import GetVideo

def GetFrames(dir, inicio, fim):
  try:
    imagens = GetVideo.capturaDir(inicio,fim,dir)
  except:
    print(f'erro ao carregar')
    return False
  return imagens