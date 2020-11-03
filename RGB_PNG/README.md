# 필요한 모듈   
```python     
from PIL import Image
from factordb.factordb import FactorDB
```    
 
|모듈|설명|
|:------------:|:-------------------------------------------------:|   
|```Pillow```|image를 만들거나 수정하거나...이미지와 관련된 모듈|    
|```factordb-pycli```|factordb라는 소인수분해값을 저장해 출력하는 데이터베이스에 접근하는 모듈 |   

--------------------------------    
# 소스코드    
## READ AND SET   
   
```python  
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
	```      
RGB 코드가 적혀있는 txt 파일을 읽고 #을 경계로 나누어서 리스트로 저장한다.    
우리는 사진의 크기를 X x Y 형식으로 만들어야 하기 때문에 factordb를 활용해 소인수 분해한다.   
만약 소인수의 개수가 1이라면 소수라는 의미이므로 +1를 해준 뒤 다시 소인수분해를 한다.   
그 다음 소인수의 개수가 만약 홀수라면 연산이 좀 복잡해지므로 맨 뒤 값을 그 전 값과 곱해 인수들의 개수를 짝수로 맞춰준다.    

##  SET IMAGE SIZE     
```python 
while len(flist) != 2:
	listlen = len(flist)
	for i in range(listlen//2):
		sec = listlen-1-i
		print(i)
		flist[i] = flist[i]*flist[sec]
	
	for j in range(listlen//2,listlen):
		flist.pop()
		
```     

인수들의 개수가 2가 될때 까지 반복하는데,   
첫 번째 for문은 0번째 인덱스는 마지막 인덱스, 1번째 인덱스는 마지막-1 인덱스... 형식으로 곱해      
인수 개수의 절반까지의 인덱스에 위의 알고리즘으로 계산한 값을 넣는다.    
두 번째 for문은 인덱스 절반 부터 끝까지 인수들을 pop(), 삭제해준다.    
-> 이렇게 하면 결국 배열이 절반으로 계속해서 축소하게 된다.      
