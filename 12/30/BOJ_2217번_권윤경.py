# 맞은 풀이 (오름차순으로 정렬하면 큰 수 부터 정렬 되니, 인덱스+1을 하면 현재숫자 + 현재숫자보다 큰 수의 갯수를 바로 나타낼 수 있음)
import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)
result = 0
for i in range(len(s)):
    if result < s[i] * (i+1):
        result = s[i] * (i+1)
print(result)


'''
# 틀린 풀이 (시간초과뜸 --> 오름차순 정렬 하지 않고 내림차순으로 진행하고 리스트 슬라이스(O(b-a)를 사용해서 시간복잡도가 증가한 것 같다.)
import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort()
result = 0
for i in range(len(s)):
    if result < s[i] * len(s[i:]):
        result = s[i] * len(s[i:])
print(result)
'''