import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
array = list(map(int, input().split()))

# 홀짝 구분해서 홀수 앞에 짝수가 얼마나 있는지 세는 함수 (예외: 모두 짝수일 때는 무조건 하나는 빼야함)
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
print(EvenCount(re1,cnt))