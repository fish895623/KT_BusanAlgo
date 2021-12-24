# 14425번
# N에 속하는 M의 문자열은 총 몇개 인가?
import sys

n,m = map(int,input().split())
s,words = [],[]
count =0 

for i in range(n+m):
    if i <n:
        # N개의 문자열 집합 정보 (S)
        s.append(sys.stdin.readline().strip())
    else:
        # M개의 문자열 정보
        word = sys.stdin.readline().strip()
        # 입력한 문자열이 s에 포함되면 count+=1을 증가시킨다.
        if word in set(s):
            count+=1
            
print(count)
        

