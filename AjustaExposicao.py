from skimage.filters import threshold_yen
from skimage.exposure import rescale_intensity
import cv2

def Expo(img):
    yen_threshold = threshold_yen(img)
    bright = rescale_intensity(img, (0, yen_threshold), (0, 255))
    return bright
def acertaBrilho (image):
    img = image
    yen_threshold = threshold_yen(img) 
    a = cv2.addWeighted(img,(yen_threshold/100),img,0,0)
    b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    saida = cv2.threshold(b,210,255,cv2.THRESH_BINARY)[1]
    return saida