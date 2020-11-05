from math import gcd
import binascii
from PIL import Image
from factordb.factordb import FactorDB


def File_bin():
    f = open("testjpg.jpg","rb+")
    string = ""
    line = f.read()
    string+=str(binascii.b2a_hex(line))
    string = string.replace("'", "")
    string = string[1:]
"""-----------------------RSA--------------------------"""
def sendkey(Tf):                    # 공개키 e와 개인키 d생성
    
    e = 3;  #Public 
    while e<Tf and gcd(e, Tf)!=1:
        e += 1
    
    d = 3;  #Private
    while (e*d)%Tf != 1 or d == e:
        d+=1

    return e,d
    

def test(e, d, n, plaintext):       # 암호화 진행 + 다시 복호화해 암호화가 정상적으로 진행되는지 test
    cip=encrypt(e, n, plaintext)
    cip_str = ""
    for char in cip:
        cip_str+=char[2:]
    return cip_str, decrypt(d, n, cip)


def encrypt(key, n,ptext):          #암호화
    print(ptext[1])
    cipher = []
    for char in ptext:
         cip = hex((int(char,16) ** key) % n)
         if len(cip) == 3:
             cip = cip[:2]+'0'+cip[2:]
         #print(f"{hexi} : {char} -> {cip}")
         cipher.append(cip)
    
    return cipher

def decrypt(key,n, ctext):          #복호화

    plain = []
    
    for char in ctext:
        chri = int(char[2:],16)
        pin = hex((chri ** key) % n)
        plain.append(pin[2:])
    """
    for i in plain:
        print(i,end='')
    """  
    plain_str = ''.join(plain)
    return plain_str


def RSA(plaintext):
    p = 13          # 두 소수 p, q 설정
    q = 23
    n=p*q
    Totient = (p-1)*(q-1)
    e ,d = sendkey(Totient)
    cip, res = test(e, d, n, plaintext)
    #print(res)

    if res == plaintext :       #암호화를 복호화한 평문과 원래 평문이 같은지 검사
        print("Good!")
    else :
        print("Ooo")
"""-----------------------RSA--------------------------"""

def rgb_png(rgbstring):
    rgbstr = rgbstring
    rgblist = rgbstr.split('#')
    #print(rgblist)
    size = len(rgblist)-1
    print(size)
    f = FactorDB(size)
    f.connect()
    flist = list(f.get_factor_list())
    
    if len(flist) == 1:
        fsize=flist[0] + 1
        f=FactorDB(fsize)
        f.connect()
        flist = list(f.get_factor_list())

    if len(flist) % 2 == 1:
        plus=flist[len(flist)-1]
        del flist[len(flist)-1]
        flist[len(flist)-1] = flist[len(flist)-1]*plus
    #print(flist)
    while len(flist) != 2:
        listlen = len(flist)
        for i in range(listlen//2):
            sec = listlen-1-i
            flist[i] = flist[i]*flist[sec]
	
        for j in range(listlen//2,listlen):	
            flist.pop()

#print(flist)
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

if __name__ == "__main__": 
     bintext = File_bin()
     cip = RSA(bintext)
     rgbstring = ""
     rgb_png(rgbstring)