from PIL import Image

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

def rgbtxt(img, filepath):
    file = open(str(filepath), 'w')
    for y in range(0, img.size[1]):
        for x in range(0, img.size[0]):
            RGBvalue = img.getpixel((x,y))
            RGBcode = '#'
            for i in range(3):
                RGBcode += format(RGBvalue[i], '02X')
            #RGBcode += '\n'
            file.write(RGBcode)
    file.close()

if __name__ == "__main__":
    img = rgbopen("test.png")
    rgbtxt(img, "result.txt")