# BOJ 22857번

# 길이가 N인 S 수열이 있다. 
# 수열에서 원하는 위치에 있는 수를 골라 최대 K번 삭제할 수 있다.

# 1 2 3 4 5 6 7 8  --> 4를 지움
# 1 2 3 5 6 7 8

N, K = 8, 2
array = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]

import sys
from collections import deque
# N,k = map(int,sys.stdin.readline().rstrip().split())
# s= list(map(int,sys.stdin.readline().rstrip().split()))

# 홀짝 구분해서 홀수 앞에 짝수가 얼마나 있는지 세는 함수
def OddEven(array):
    dic = dict()
    cnt = 0
    for i in range(N):
        if array[i] % 2 == 1:
            dic[i] = cnt
            cnt = 0
        else:
            cnt += 1
    return dic, cnt

# 짝수로 이루어져 있는 연속한 부분 수열 최대 길이 구하는 함수
def EvenCount(dic, cnt):
    queue = deque(dic.keys())
    qcopy = queue.copy()
    K1 = 0
    result = 0
    result2 = 0
    c = 0
    while (K1 < K+1):
        if len(queue) != 0 :
            num = queue.popleft()
            K1 += 1
            result += dic[num]
            if (K1 == K+1) :
                result2 = max(result2, result)
                K1 -= 1
                result -= dic[qcopy[c]]
                c +=1
        else:
            result += cnt
            result2 = max(result2, result)
            break 
    return result2  

re1, cnt = OddEven(array)
print(re1,cnt)
print(EvenCount(re1,cnt))