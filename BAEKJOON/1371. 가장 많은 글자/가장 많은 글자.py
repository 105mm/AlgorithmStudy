import sys
input = sys.stdin.read 



s = input().replace("\n","").replace(" ","") 



c = [0] * 26 


for i in s:
    c[ord(i)-97]+=1  
    

    
maxx = max(c) 



r = []
for i in range(len(c)): 
    

    if c[i] == maxx: 
        


        r.append(chr(i+97)) 
        
r.sort()
print(*r,sep="")


""" 텍스트를 한 번에 입력받는다. """

""" 공백과 개행 문자를 없앤다"""

""" 알파벳 26개를 담을 수 있는 배열 생성"""

""" 문자열 전체 순회하면서 알파벳을 아스키코드로 바꾸고 a로부터 위치 계산"""

"""배열 중 가장 많은 요소"""

""" 요소들의 집합 순회"""

""" 가장 많은 요소라면 아스키코드를 알파벳으로 바꿔서 r 리스트에 추가 """

""" 뽑힌 리스트를 오름차순으로 정렬 """

""" 정렬된 결과를 공백없이 붙혀서 출력 """
 
"""

줄 수가 입력에 있지 않아 끝내는 시점이 명확하지 않다.

따라서 줄 수 대신 텍스트를 한 번에 입력받을 수 있는 sys.stdin.read() 함수를 사용한다.

이후 공백과 개행 문자를 없애주고, 알파벳을 카운트한다.

 

"""