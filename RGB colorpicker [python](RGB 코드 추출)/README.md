# 이미지 RGB 추출

```python
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
            RGBcode += '\n'
            file.write(RGBcode)
    file.close()

if __name__ == "__main__":
    img = rgbopen("target.png")
    rgbprint(img, 0, 5)
    rgbtxt(img, "result.txt")
```

`*필수 라이브러리: Pillow*`

이미지를 RGB 형태로 변환 후 이미지에서 RGB코드를 얻어 txt 파일에 저장합니다.



# 함수

| 함수                        | 설명                                                         |
| --------------------------- | ------------------------------------------------------------ |
| ```image = rgbopen(path)``` | rgbopen: 이미지 열기<br />path: 이미지 파일 경로 또는 파일명<br />반환값: Pillow Image.open() 관련 함수 |
| ```rgbprint(img, x, y)```   | rgbprint: 콘솔에 단일 RGB  코드 출력<br />img: rgbopen한 이미지<br />x, y: 이미지 픽셀 위치 |
| ```rgbtxt(img, filepath)``` | rgbtxt: 모든 픽셀 RGB 코드 파일로 출력<br />img: rgbopen한 이미지<br />filepath: RGB 코드를 저장할 파일 경로 또는 파일명 |



# RGB 출력 형태

rgbtxt를 사용하면 다음과 같은 형태로 RGB 코드가 저장됩니다.

![txt](txt.png)