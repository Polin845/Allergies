import easyocr
from PIL import Image


def func_easyocr(image):
    text = easyocr.Reader(["ru"]).readtext(image, detail=0, paragraph=True, text_threshold=0.8)
    return text


i = Image.open('examples/photo_4.jpg')
string = str(func_easyocr(i))
print(string)



