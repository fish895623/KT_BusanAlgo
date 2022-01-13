import sys
input=sys.stdin.readline
S = int(input())
result = 0
cnt = 0
for i in range(1,S):
     result += i
     cnt +=1
     if result + i >= S:
         print(cnt)
         break