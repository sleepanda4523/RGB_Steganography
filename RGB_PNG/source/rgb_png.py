from PIL import Image
from factordb.factordb import FactorDB

f = open("./result.txt", "r")
rgbstr = f.read() 
rgblist = rgbstr.split('#')
#print(rgblist)
size = len(rgblist)-1
print(size)
f = FactorDB(size)
f.connect()
flist = list(f.get_factor_list())


if len(flist) == 1:
	fsize=flist[0] + 1;
	f=FactorDB(fsize)
	f.connect()
	flist = list(f.get_factor_list())


if len(flist) % 2 == 1:
	plus=flist[len(flist)-1]
	del flist[len(flist)-1]
	flist[len(flist)-1] = flist[len(flist)-1]*plus
print(flist)
while len(flist) != 2:
	listlen = len(flist)
	for i in range(listlen//2):
		sec = listlen-1-i
		print(i)
		flist[i] = flist[i]*flist[sec]
	
	for j in range(listlen//2,listlen):
		flist.pop()

print(flist)
image1 = Image.new("RGB",(flist[0],flist[1]))
img1 = image1.load()
(width, height) = image1.size


idx = 1
for i in range(0,width):
	for j in range(0,height):
		rgbcode = rgblist[idx]
		rgb1 = rgbcode[0:2]
		rgb2 = rgbcode[2:4]
		rgb3 = rgbcode[4:]		
		img1[i,j] = (int(rgb1,16), int(rgb2,16),int(rgb3,16))
		idx+=1


image1.save("image1.png")
