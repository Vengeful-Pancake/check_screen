from PIL import Image
from pytesseract import pytesseract
import pyautogui

check = "Dungeon Clear"

def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'images\sample.png')

def readimg():
    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Define path to image
    path_to_image = 'images/sample.png'

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)

    return text

def logic(text, check):
    x = check.split()
    y = text.split()
    
    w = 0
    o = 0

    for i in range(len(x)):
        o+=1

        for a in range(len(y)):
            cw = x[i] == y[a]
            if cw:
                w += 1
    return w, o

def autoclick():
    return

screenshot()
text = readimg()
x, y = logic(text, check)
autoclick()

print(text)
print(x)
print(y)