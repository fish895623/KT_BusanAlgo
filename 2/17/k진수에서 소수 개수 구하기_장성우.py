"""
https://programmers.co.kr/learn/courses/30/lessons/92335


양의 정수 n이 주어진다.
이 숫자를 k 진수로 바꾸었을 때 변환된 수 안에 조건에 맞는 소수가 몇개인가?

10진수 -> 소수로 변환 하기

0P0 처럼 소수 양쪽에 0이 있는경우
P0처럼 소수 오른쪽
=> 앞에서 부터 읽으면서 0을 만나면 find_prime진행

단 각 자짓수에 0을 포함하지 않는 소수이다.


"""
from collections import deque 

# 소수인지 판별 소수 : 1 소수아님 : 0
def isPrime(num):
    if num == 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1


def solution(n, k):
    answer = 0

    # 진수 변환
    result = deque([])

    while (n >= k):
        result.appendleft(n % k)
        n //= k
    result.appendleft(n)

    data = []
    while result:
        d = str(result.popleft())

        if d == "0" and len(data) != 0:
            # 소수인지 판별
            
            answer += isPrime(int("".join(data)))
            data = []
        else:
            data.append(d)


    answer += isPrime(int("".join(data)))

    return answer



n = [437674, 110011]
k = [3, 10]

for i in range(2):
    print(solution(n[i], k[i]))
