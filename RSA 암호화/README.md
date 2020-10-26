# 파일 바이너리 형식으로 read   
```python
import binascii

f = open("testjpg.jpg","rb+")
fw = open("binary.txt","w")
string = ""
line = f.read()
#print(line)
string+=str(binascii.b2a_hex(line))
string = string.replace("'", "")
string = string[1:]
print(string)
fw.write(string)
f.close()
fw.close()
```

> 필수 라이브러리 : binascii    


# RSA 암호화   
```python
from math import gcd
# from Crypto.PublicKey import RSA
# from Crypto import Random

def sendkey(Tf):                    # 공개키 e와 개인키 d생성
    
    e = 5;  #Public 
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
        cip_str+=char[2:]			# 16진수로 변환하면서 앞에 붙는 '0x'제거
    return cip_str, decrypt(d, n, cip)


def encrypt(key, n,ptext):          #암호화
    print(ptext[1])
    cipher = []
    for char in ptext:
         hexi = int(char,16)
         cip = hex((int(char,16) ** key) % n)
         if len(cip) == 3:				# 만약 16진수가 한자리 뿐이라면
             cip = cip[:2]+'0'+cip[2:]	# 0추가
         print(f"{hexi} : {char} -> {cip}")
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


if __name__ == "__main__":
    fr = open("./binary.txt","r")
    fw = open("crypto.txt","w")
    plaintext = fr.read()
    #print(plaintext)
    p = 13          # 두 소수 p, q 설정
    q = 23
    n=p*q
    Totient = (p-1)*(q-1)
    e ,d = sendkey(Totient)
    print(e)
    cip, res = test(e, d, n, plaintext)
    #print(res)

    if res == plaintext :       #암호화를 복호화한 평문과 원래 평문이 같은지 검사
        print("Good!")
    else :
        print("Ooo")
    
    fw.write(cip)
    fr.close()
    fw.close()
    
```    
	
## 함수 설명   
|함수|설명|
|:------------:|:-------------------------------------------------:|   
|```sendkey(Totient)```|Totient(오일러)를 가지고<br /> 공개키 e와 개인키 d생성|    
|```encrypt(key, n,ptext)```|공개키 e와 n, 평문을 가지고 암호화. return은 리스트. |
|```decrypt(key,n, ctext)```|개인키 d와 n, 암호문을 가지고 복호화. return은 문자열. |    
	   
	