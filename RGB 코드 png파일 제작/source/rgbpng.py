from PIL import Image


f = open("D:/공주대영재교육원/프젝/RGB_RSA/RGB colorpicker [python](RGB 코드 추출)/source/result.txt", "r")
rgbstr = f.read() 
rgblist = rgbstr.split('#')
print(rgblist)
size = range(rgblist)

