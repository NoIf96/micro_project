from PIL import Image
import argparse

IMG = 'a.png'
WIDHT = 80
HEIGHT = 80
OUTPUT = IMG[:-4] + '.txt'

ascii_char = list("bdegiklmnosuvwx@#$%&*  ")

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    lenght = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)  #灰度值公式
    unit = (256.0+1)/lenght
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    image = Image.open(IMG)
    image = image.resize((WIDHT, HEIGHT), Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDHT):
            txt += get_char(*image.getpixel((j, i)))
        txt += "\n"
    print(txt)

    with open(OUTPUT, 'w') as f:
        f.write(txt)

