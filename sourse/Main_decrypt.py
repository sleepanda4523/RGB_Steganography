# -*- coding: utf-8 -*-
from PIL import Image
from sys import exit
from os import system

"""-------------------RGB코드 추출---------------------"""
def rgbopen(path): # 사진 RGB로 열기, 픽셀 = 0,0
    try : 
        img = Image.open(str(path))
    except FileNotFoundError:
        print("파일이 없습니다")
        exit()
    else : 
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
    for y in range(0, img.size[1]):
        for x in range(0, img.size[0]):
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
    
    for char in ctext:
        chri = int(char,16)
        pin = hex((chri ** key) % n)
        plain.append(pin[2:])
    """
    for i in plain:
        print(i,end='')
    """  
    plain_str = ''.join(plain)
    return plain_str


if __name__ == "__main__":
    filepath = input("암호화 된 사진파일 명(확장자포함) : ")
    private, n = input("개인키와 n : ").split()
    rgbtext = sendRGB(filepath)
    ptext = decrypt(private, n, rgbtext)
    with open("decrypt.txt","wb") as file:
        file.write(ptext)
    
    file.close()
    system("pause")