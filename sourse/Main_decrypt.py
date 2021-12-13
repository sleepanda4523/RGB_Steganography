# -*- coding: utf-8 -*-
from PIL import Image

"""-------------------RGB코드 추출---------------------"""

def rgbopen(path): # 사진 RGB로 열기, 픽셀 = 0,0
    img = Image.open(str(path))
    img_RGB = img.convert("RGB")
    return img_RGB

def rgbprint(img, x,y): # RGB 코드 단일 추출
    RGBvalue = img.getpixel((x,y))
    RGBcode = '#'
    for i in range(3):
        RGBcode += format(RGBvalue[i], '02X')
    print(RGBcode)

def rgbtxt(img):
    file = ""
    print(img.size[0],img.size[1])
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            RGBvalue = img.getpixel((x,y))
            RGBcode = '#'
            for i in range(3):
                RGBcode += format(RGBvalue[i], '02X')
            #RGBcode += '\n'
            file+=RGBcode[1:]       # #빼는용도
    return file

def sendRGB(filepath):
    img = rgbopen(str(filepath))
    rgbcode = rgbtxt(img)
    return rgbcode
"""-------------------RSA 복호화---------------------"""
def decrypt(key,n, ctext):          #복호화
    plain = []
    length = 2
    cip_list = [ctext[i:i+length] for i in range(0,len(ctext),length)]
    for char in cip_list:
        chri = int(char,16)
        pin = hex((chri ** key) % n)
        plain.append(pin[2:])
  
    plain_str = ''.join(plain)
    return plain_str


if __name__ == "__main__":
    filepath = "image1.png"     #input("암호화 된 사진파일 명(확장자포함) : ")"""  
    rgbtext = sendRGB(filepath)
    edit_rgb = list(map(''.join, zip(*[iter(rgbtext)]*2)))
    rgblist = [int(i, base=16) for i in edit_rgb]
        
    with open("decrypt.png", "wb") as f:
        f.write(bytes(rgblist))
