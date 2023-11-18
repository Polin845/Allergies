import easyocr
from PIL import Image


def found(image, a):
    ans = []
    text = easyocr.Reader(["ru"]).readtext(image, detail=0, paragraph=True, text_threshold=0.8)
    for i in a:
        if i in text:
            ans.append(i)
    return ans



