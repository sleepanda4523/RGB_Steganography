from math import gcd
# from Crypto.PublicKey import RSA
# from Crypto import Random

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
         hexi = int(char,16)
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
    cip, res = test(e, d, n, plaintext)
    #print(res)

    if res == plaintext :       #암호화를 복호화한 평문과 원래 평문이 같은지 검사
        print("Good!")
    else :
        print("Ooo")
    
    fw.write(cip)
    fr.close()
    fw.close()
    