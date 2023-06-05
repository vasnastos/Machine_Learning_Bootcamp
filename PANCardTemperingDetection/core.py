from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests,os


class Data:
    def __init__(self):
        self.image=Image.open(os.path.join('','image','original.jpg'))
        self.tampered=Image.open(os.path.join('','image','tampered.jpg'))

        print(f'{self.image.format=}')
        print(f'{self.tampered.format=}')

        print(f'{self.image.size=}')
        print(f'{self.tampered.size=}')


if __name__=='__main__':
    data=Data()