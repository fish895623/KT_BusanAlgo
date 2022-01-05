"""
https://www.acmicpc.net/problem/22857

"""

"""
첫번째 풀이과정

#1 92퍼에서 틀렸다고 나옴 어디선가 

1) +와 -가 연속적으로 있는것은 더하기 (+는 +1 , -는 -1)
2) 만약 첫번째 연속적으로 있는 데이터가 -인경우 없앤다.


"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))




data_result = []

even = 0
odd = 0

for i in data:
    # 들어온 데이터가 짝수인 경우
    if i%2==0:
        if odd != 0:
            data_result.append(odd)
            odd = 0

        even +=1

    # 들어온 데이터가 홀수인 경우
    if i%2!=0:
        if even != 0:
            data_result.append(even)
            even = 0

        odd -=1

# 이거 처리안해줘서 92퍼에서 멈췄었다.
if odd != 0:
    data_result.append(odd)
elif even != 0:
    data_result.append(even)

minus_s = []
plus_s = []

result = []
try:
    # 첫번째 데이터가 0보다 작은경우 첫 데이터 없애기
    if data_result[0] < 0:
        data_result.pop(0)
except:
    pass

for data_result_num in data_result:
    if data_result_num < 0:
        minus_s.append(data_result_num)
    else:
        plus_s.append(data_result_num)

    while True:

        if abs(sum(minus_s)) > k:
            minus_s.pop(0)

            if len(plus_s) !=0:
                plus_s.pop(0)

        if abs(sum(minus_s)) <= k:
            break

    result.append(sum(plus_s))

if len(result) == 0:
    print("0")
else:
    print(max(result))



